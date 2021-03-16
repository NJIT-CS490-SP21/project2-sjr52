# pylint: disable= E1101, C0413, R0903, W0603, W1508

'''This file is a server that helps with the communication between multiple users and database'''
import os
from dotenv import load_dotenv, find_dotenv
from flask import Flask, send_from_directory, json, session # pylint: disable=unused-import
from flask_socketio import SocketIO
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

load_dotenv(find_dotenv())

APP = Flask(__name__, static_folder='./build/static')

APP.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')

APP.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

DB = SQLAlchemy(APP)

# import models
import models
if __name__ == '__main__':
    DB.create_all()

CORS = CORS(APP, resources={r"/*": {"origins": "*"}})

SOCKETIO = SocketIO(APP,
                    cors_allowed_origins="*",
                    json=json,
                    manage_session=False)

CURRENT_PLAYERS = []


@APP.route('/', defaults={"filename": "index.html"})
@APP.route('/<path:filename>')
def index(filename):
    '''This function just builds the file'''
    return send_from_directory('./build', filename)


@SOCKETIO.on('User_List_Update')
def update_user_list(data):
    '''This function updates the user list based on players that join'''
    global CURRENT_PLAYERS
    print("The Data Recieved is:"+ str(data))
    CURRENT_PLAYERS.append(data['User_Name'])
    print("CURRENT_PLAYERS list:"+ str(CURRENT_PLAYERS))
    SOCKETIO.emit('User_List_Update', CURRENT_PLAYERS, broadcast=True,include_self=False)


@SOCKETIO.on('connect')
def on_connect():
    '''This function just gets the pre-stored list of users from database'''
    print('User connected!')

    old_users_list = models.Person.query.all()
    old_user_names = {}
    for user_name in old_users_list:
        old_user_names[user_name.username] = user_name.score
    print(old_user_names)


# When a client disconnects from this Socket connection, this function is run
@SOCKETIO.on('disconnect')
def on_disconnect():
    '''This function clears the joined players list on disconnect'''
    global CURRENT_PLAYERS
    CURRENT_PLAYERS.clear()
    print('User disconnected!')


@SOCKETIO.on('Curr_Symbl')
def curr_symbl(
        symbol):  # data is whatever arg you pass in your emit call on client
    '''This function sends the current symbol to all users'''
    print(str(symbol))
    # This emits the 'chat' event from the server to all clients except for
    # the client that emmitted the event that triggered this function
    SOCKETIO.emit('Curr_Symbl', symbol, broadcast=True, include_self=False)


@SOCKETIO.on('DB_UserCheck')
def user_db_check(check_username):
    '''This function checks for user in database'''
    joined_user = check_username
    
    #add_user(joined_user)  #Changed HERE************  
    
    user_in_db = True
    print(
        str("================The Data recieved from user joined is: " +
            joined_user))

    check_userindb = models.Person.query.all()
    for user_names in check_userindb:
        if check_username != user_names.username:
            user_in_db = False
        else:
            continue

    if user_in_db:
        store_new_user = models.Person(username=joined_user, score=100)
        DB.session.add(store_new_user)
        DB.session.commit()

    initial_user_db = []
    initial_score_db = []

    added_new_user = DB.session.query(models.Person).order_by(
        models.Person.score.desc()).all()
    for updated_db_users in added_new_user:
        print(updated_db_users.username + " => " + str(updated_db_users.score))
        initial_user_db.append(updated_db_users.username)
        initial_score_db.append(updated_db_users.score)

    SOCKETIO.emit('Old_DB_Users', initial_user_db)
    SOCKETIO.emit('Old_DB_Scores', initial_score_db)


@SOCKETIO.on('Game_Result_Winner')
def game_result_winner(data):
    '''This function updates the DB based on the winner or loser'''
    print(
        str("The Result of the game is: Winner:  " + data["Winner"] +
            ", Loser: " + data["Loser"]))
    winner_name = data["Winner"]
    loser_name = data["Loser"]

    update_winner_score = DB.session.query(
        models.Person).filter_by(username=winner_name).first()
    update_loser_score = DB.session.query(
        models.Person).filter_by(username=loser_name).first()

    update_winner_score.score += 1
    update_loser_score.score -= 1

    DB.session.commit()

    updated_user_db = []
    updated_score_db = []

    # all_people = models.Person.query.all()
    all_people = DB.session.query(models.Person).order_by(
        models.Person.score.desc()).all()
    print("*****************************************************")
    for people in all_people:
        print(people.username + " => " + str(people.score))
        updated_user_db.append(people.username)
        updated_score_db.append(people.score)
    print("*****************************************************")

    SOCKETIO.emit('Updated_DB_Users', updated_user_db)
    SOCKETIO.emit('Updated_DB_Scores', updated_score_db)

# When a client emits the event 'chat' to the server, this function is run
# 'chat' is a custom event name that we just decided
@SOCKETIO.on('Board_Info')
def on_chat(data):  # data is whatever arg you pass in your emit call on client
    '''This function listens for updated board and lets other users know'''
    print(str(data))
    # This emits the 'chat' event from the server to all clients except for
    # the client that emmitted the event that triggered this function
    SOCKETIO.emit('Board_Info', data, broadcast=True, include_self=False)


@SOCKETIO.on("Play_Again")
def create_newgame(
        data):  # data is whatever arg you pass in your emit call on client
    '''This function listens for play_again and informs the connected users'''
    print(str(data))
    # This emits the 'chat' event from the server to all clients except for
    # the client that emmitted the event that triggered this function
    SOCKETIO.emit('Play_Again', data, broadcast=True, include_self=False)


@SOCKETIO.on("Game_Over")
def game_over(data):
    '''This function listens for game over'''
    print(str(data["Game_Over"]))
    SOCKETIO.emit('Game_Over', data, broadcast=True, include_self=False)

def Set_Score_NewUser(username):
    new_user = models.Person(username=username, score=100)
    DB.session.add(new_user)
    DB.session.commit()
    all_people = models.Person.query.all()
    user_info = {}
    for person in all_people:
        user_info[person.username] = 100
    return user_info

def IsUserIN_DB(username):
    if username =="Sunny":
        new_user = models.Person(username=username, score=100)
        DB.session.add(new_user)
        DB.session.commit()
    
    all_people = models.Person.query.all()
    user_text = ""
    for person in all_people:
        if person.username == username:
            user_text = "User Is In DB"
        else:
            user_text = "User Not Is In DB"
    return user_text
    





if __name__ == "__main__":
    # Note that we don't call APP.run anymore. We call SOCKETIO.run with APP arg
    SOCKETIO.run(
        APP,
        host=os.getenv('IP', '0.0.0.0'),
        port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
    )
