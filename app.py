import os
from flask import Flask, send_from_directory, json, session
from flask_socketio import SocketIO
from flask_cors import CORS


app = Flask(__name__, static_folder='./build/static')

cors = CORS(app, resources={r"/*": {"origins": "*"}})

socketio = SocketIO(
    app,
    cors_allowed_origins="*",
    json=json,
    manage_session=False
)

Player_X = ""
Player_O = ""
Spectators = ""
Current_Players = []
User_List_Size=0




@app.route('/', defaults={"filename": "index.html"})
@app.route('/<path:filename>')
def index(filename):
    return send_from_directory('./build', filename)




@socketio.on('User_List_Update')
def Update_User_List(data): 
    global User_List_Size
    global Current_Players
    global Player_X
    global Player_O
    global Spectators
    
    print("The Data Recieved is ================================================:" + str(data))
    User_List_Size+=1
    Current_Players.append(data['User_Name'])
    
    
    print("Current_Players list ================================================:" + str(Current_Players))
    
    
    socketio.emit('User_List_Update',  Current_Players, broadcast=True, include_self=False)
    
    # Player_X = str(Current_Players[0])
    # Player_O = str(Current_Players[1])
    # Spectators = str(Current_Players[2:])
    
    # print("The Game Players are : X -> " + Player_X + " , O -> " + Player_O)
    # print("The Spectators are :" + Spectators)
    
    

# @socketio.on('Game_Players_Info')
# def Game_Info(): # data is whatever arg you pass in your emit call on client
#     data = [Player_X, Player_O, Spectators]
#     socketio.emit('Game_Players_Info',  data, broadcast=True, include_self=False)






@socketio.on('connect')
def on_connect():
    print('User connected!')

# When a client disconnects from this Socket connection, this function is run
@socketio.on('disconnect')
def on_disconnect():
    Current_Players = [];
    print('User disconnected!')
    
    
@socketio.on('Curr_Symbl')
def Curr_Symbl(Symbol): # data is whatever arg you pass in your emit call on client
    print(str(Symbol))
    # This emits the 'chat' event from the server to all clients except for
    # the client that emmitted the event that triggered this function
    socketio.emit('Curr_Symbl',  Symbol, broadcast=True, include_self=False)

# When a client emits the event 'chat' to the server, this function is run
# 'chat' is a custom event name that we just decided
@socketio.on('Board_Info')
def on_chat(data): # data is whatever arg you pass in your emit call on client
    print(str(data))
    # This emits the 'chat' event from the server to all clients except for
    # the client that emmitted the event that triggered this function
    socketio.emit('Board_Info',  data, broadcast=True, include_self=False)


    
# Note that we don't call app.run anymore. We call socketio.run with app arg
socketio.run(
    app,
    host=os.getenv('IP', '0.0.0.0'),
    port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
)


















# @socketio.on('User_List_Update')
# def Update_User_List(data): 
#     global User_List_Size
#     global Current_Players
#     global Player_X
#     global Player_O
    
#     print("The Data Recieved is :" + str(data))
#     User_List_Size+=1
#     Current_Players.append(data['User_Name'])
#     socketio.emit('User_List_Update',  data, broadcast=True, include_self=False)
    
#     Player_X = str(Current_Players[0])
#     Player_O = str(Current_Players[1])
    
#     size=len(Current_Players)
#     for i in range(size):
#         if(i < 2):
#             print("Players are: ")
#             print(Current_Players[i])
#         elif(i >= 2):
#             print("Spectators are: ")
#             print(Current_Players[i])











# import os
# from flask import Flask, send_from_directory, json, session
# from flask_socketio import SocketIO
# from flask_cors import CORS


# app = Flask(__name__, static_folder='./build/static')

# cors = CORS(app, resources={r"/*": {"origins": "*"}})

# socketio = SocketIO(
#     app,
#     cors_allowed_origins="*",
#     json=json,
#     manage_session=False
# )

# Player_X = ""
# Player_O = ""
# Current_Session = []
# Current_Players = []


# @app.route('/', defaults={"filename": "index.html"})
# @app.route('/<path:filename>')
# def index(filename):
#     return send_from_directory('./build', filename)

# @socketio.on('connect')
# def on_connect():
#     print('User connected!')

# # When a client disconnects from this Socket connection, this function is run
# @socketio.on('disconnect')
# def on_disconnect():
#     print('User disconnected!')
    
    
# @socketio.on('User_List_Update')
# def Users_List(data):
#     print('User disconnected!')
    
    

# @socketio.on('Players_LoggedIn')
# def player_loggeddata(data): 
#     print("The Players Who have Logged In:" + str(data))
#     Current_Session.append(data['name'])
#     print("The total players in current session are: " + Current_Session)
    
#     if(len(Current_Session) == 1):
#         Player_X = Current_Session[0]
#         Current_Players.append(Player_X)
#         socketio.emit('Curr_Players',  Current_Players, broadcast=True, include_self=False)
        
#     elif(len(Current_Session) == 2):
#         Player_O = Current_Session[1]
#         Current_Players.append(Player_O)
#         socketio.emit('Curr_Players',  Current_Players, broadcast=True, include_self=False)
        
        
#     elif(len(Current_Session) > 2 ):
#         Current_Spectators = Current_Session[2:]
#         socketio.emit('Curr_Spectators',  Current_Spectators, broadcast=True, include_self=False)
    
    


# # When a client emits the event 'chat' to the server, this function is run
# # 'chat' is a custom event name that we just decided
# @socketio.on('Board_Info')
# def on_chat(data): # data is whatever arg you pass in your emit call on client
#     print(str(data))
#     # This emits the 'chat' event from the server to all clients except for
#     # the client that emmitted the event that triggered this function
#     socketio.emit('Board_Info',  data, broadcast=True, include_self=False)

# # Note that we don't call app.run anymore. We call socketio.run with app arg
# socketio.run(
#     app,
#     host=os.getenv('IP', '0.0.0.0'),
#     port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
# )