# Tic Tac Toe 

The repository below has the code to build a basic real time networking multiplayer tic tac toe game.

## Setting Up Project
    ## Installing Packages And Libraries
    1. `npm install`
    2. `pip install flask-socketio`
    3. `sudo pip install flask` or `pip install flask`
    4. `pip install flask-socketio`
    5. `pip install flask-cors`
    6. `npm install -g heroku`
    

1. Git clone react-starter from the github repository this will download the respository on your local device.
    - `git clone https://github.com/NJIT-CS490-SP21/project2-sjr52.git`

2. In order to run the app, type the following commands in the terminal and make sure you are in the react-starter directory:
    - `python app.py`
    - `npm run start`

## Info about the functionality of the game
    1.) running the `python app.py` and `npm run start` commands in two different terminals. Click on the preview button and load two or more webpages at that end point url.
    2.) Once the webpage is loaded you will see a username input form, login with different usernames on each of webpages you have opened.
    3.) After you have logged in the game board should appear where you can start playing. Player X or the user that has entered first will start the game with his marker being "X"
    4.) After the user has placed his marker he will be blocked from clicking on another box until it's opponent makes the move. The marker placed by player X will be visible on the player O's board. The second user to enter the game area will be Player O with the marker "O"
    5.) if more than two users enter the game, everyone onwards from the second user will be spectators and will only be able to view the live game updates and will not be able to play.
    6.) At the end of the game depending on the moves made by each player the output of win/draw/lose will be generated.
    7.) enjoy the game!!!
    
    
## Unsolved Problems:
    - Problem.) One of the problems which I have discovered and that still exist is that whenever I try to open the app on multiple devices and login in, the first player(x) is overwritten by the new user that has just logged in. When in the correct manner the user should be added after the existing player and being placed as the player with marker "O" or just a spectator.
      Solution.) If I was given more time, I would try to locate and solve the problem on my own that way I can improve my problem-solving skills and If I still was not able to debug the problem then I would ask one of the TA's or my friends to help me solve the problem.
    
    - Problem.) When using the app via heroku I have often seen a delay occuring between the server and the client. I have also seen this happening when I run the app in the cloud9, often leading to a confusion when tracing the outputs provided by the server.
      Solution.) I think that in order to solve this problem I would ask the TA's or someone with networking background.
        

## Technical Issues:
    -  Problem.) One technical issue which I encountered was when I had to block a player after their turn was over so that the player was not able to click another box until the next player made it's move, which acted as a trigger to unblock the blocked player and allowing it to make the next move.
       Solution.) In order to solve this, I stored the username into the Session Storage after receiving it from the input form. Along with this I implemented the UseState function to keep track of the next symbol to be marked. This allowed me to define a condition so that I was able to solve the above problem.
    
    - Problem.) Another technical issue I faced was that for some reason I was unable to change the state of the symbol to that was suppose to be marked next.
      Solution.) To solve this issue I used conditional statments checking the last symbol that was used and setting the next symbol.