# Flask and create-react-app

## Setting Up Project
    ## Installing Packages And Libraries
    1. `npm install`
    2. `pip install flask-socketio`

1. Git clone react-starter from the github repository this will download the respository on your local device.
    - `git clone https://github.com/NJIT-CS490-SP21/project2-sjr52.git`

2. In the terminal we will install the above mentioned packages by typing the following command in the terminal:
    - `npm install`
    - `pip install flask-socketio`
    - 
3. In order to run the app, type the following commands in the terminal:
    - `python app.py`
    - `npm run start`

##Unsolved Problems:
    - One of the problems which I have discovered and that still exist is that whenever I try to open the app on multiple devices and login in, the first player(x) is overwritten by the new user that has just logged in. When in the correct manner the user should be added after the existing player and being placed as the player with marker "O" or just a spectator.
        - If I was given more time, I would try to locate and solve the problem on my own that way I can improve my problem-solving skills and If I still was not able to debug the problem then I would ask one of the TA's or my friends to help me solve the problem.
    
    - When using the app via heroku I have often seen a delay occuring between the server and the client. I have also seen this happening when I run the app in the cloud9, often leading to a confusion when tracing the outputs provided by the server.
        - I think that in order to solve this problem I would ask the TA's or someone with networking background.
        

##Technical Issues:
    - One technical issue which I encountered was when I had to block a player after their turn was over so that the player was not able to click another box until the next player made it's move, which acted as a trigger to unblock the blocked player and allowing it to make the next move.
        - In order to solve this, I stored the username into the Session Storage after receiving it from the input form. Along with this I implemented the UseState function to keep track of the next symbol to be marked. This allowed me to define a condition so that I was able to solve the above problem.
    
    -Another technical issue I faced was that for some reason I was unable to change the state of the symbol to that was suppose to be marked next.
        - To solve this issue I used conditional statments checking the last symbol that was used and setting the next symbol.