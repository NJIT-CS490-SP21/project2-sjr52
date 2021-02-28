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

Current_Players = []





@app.route('/', defaults={"filename": "index.html"})
@app.route('/<path:filename>')
def index(filename):
    return send_from_directory('./build', filename)




@socketio.on('User_List_Update')
def Update_User_List(data): 
    global Current_Players

    
    print("The Data Recieved is ================================================:" + str(data))
    Current_Players.append(data['User_Name'])
    
    
    print("Current_Players list ================================================:" + str(Current_Players))
    
    
    socketio.emit('User_List_Update',  Current_Players, broadcast=True, include_self=False)
    

@socketio.on('connect')
def on_connect():
    print('User connected!')

# When a client disconnects from this Socket connection, this function is run
@socketio.on('disconnect')
def on_disconnect():
    Current_Players.clear()
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

@socketio.on("Play_Again")
def Create_NewGame(data): # data is whatever arg you pass in your emit call on client
    print(str(data))
    # This emits the 'chat' event from the server to all clients except for
    # the client that emmitted the event that triggered this function
    socketio.emit('Play_Again',  data, broadcast=True, include_self=False)
    
# Note that we don't call app.run anymore. We call socketio.run with app arg
socketio.run(
    app,
    host=os.getenv('IP', '0.0.0.0'),
    port=8081 if os.getenv('C9_PORT') else int(os.getenv('PORT', 8081)),
)













