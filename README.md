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
    7. `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs`
    8. `pip install psycopg2-binary`, Enables us to use SQL with in Python
    9. `pip install Flask-SQLAlchemy==2.1`, Enables us to use SQL with in Python

1. Git clone react-starter from the github repository this will download the respository on your local device.

   - `git clone https://github.com/NJIT-CS490-SP21/project2-sjr52.git`

2. In order to run the app, type the following commands in the terminal and make sure you are in the react-starter directory:
   - `python app.py`
   - `npm run start`

## Info about the functionality of the game

    1.) running the `python app.py` and `npm run start` commands in two different terminals. Click on the preview button and load two or more webpages at that end point url.
    2.) Once the webpage is loaded you will see a username input form, login with different usernames on each of webpages you have opened.
    3.) After you have logged in the game, board should appear where you can start playing. Player X or the user that has entered first will start the game with his marker being "X"
    4.) After the user has placed his marker he will be blocked from clicking on another box until it's opponent makes the move. The marker placed by player X will be visible on the player O's board. The second user to enter the game will be Player O with the marker "O"
    5.) if more than two users enter the game, everyone onwards from the second user will be spectators and will only be able to view the live game updates and will not be able to play.
    6.) At the end of the game depending on the moves made by each player the output of win/draw/lose will be generated.
    7.) The winner will get +1 added to its starting score of 100 and the loser will get -1 added to its starting score of 100.
    8.) The scores can be shown/hidden by clicking the leaderboard button. if the button is clicked once it will show the leaderboard table and if the same button is clicked again it will hide the leader board.
    9.) enjoy the game!!!

## Getting the Database set-up

    1.) Install PostGreSQL: `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs`, Enter yes if any prompts show up.
    2.) Initializing the PSQL database: `sudo service postgresql initdb`, Make sure to do this in current working directory
    3.) Starting the PSQL: `sudo service postgresql start`
    4.) Creating a Superuser: `sudo -u postgres createuser --superuser $USER`
    5.) Creating a Database: `sudo -u postgres createdb $USER`
    6.) To Check if the user and database was created do `\du` for the user check and do `\l` for database check.

## Creating a new database on Heroku

    1.) Login to Heroku: `heroku login -i`
    2.) Create a new Heroku app: `heroku create`
    3.) Creating a database linked to the Heroku app: `heroku addons:create heroku-postgresql:hobby-dev`
    4.) Type `heroku config`, copy the value that DATABASE_URL is set to.
    5.) create a .env file in your work space that will store the Database_Url and export it to your python file.
        - type this in your .env file: export DATABASE_URL='copy-paste-value-in-here'

          example. DATABASE_URL='postgres://lkmlrinuazynlb:b94acaa351c0ecdaa7d60ce75f7ccaf40c2af646281bd5b1a2787c2eb5114be4@ec2-54-164-238-108.compute-1.amazonaws.com:5432/d1ef9avoe3r77f'

    6.) Now in the terminal run `python`, this will open up an interactive session.
    7.) type the following commands to see a demo of how to store info into the database
        >> `from app import db`
        >> `import models`
        >> `db.create_all()`
        >> `User1 = models.Person(username='ABC', score=100)`
        >> `User2 = models.Person(username='XYZ', score=100)`
        >> `db.session.add(User1)`
        >> `db.session.add(User2)`
        >> `db.session.commit()`

    8.) In order to see if the information was stored correctly do:
        >> `models.Person.query.all()`, this will show you the users that are stored in the db.

    9.) To check if the following was written in our Heroku Database which is lined with the app:
        - type `heroku pg:psql` in the terminal
        - `\d` this will show list all the tables and we should see the person table there as well
        - Now lets use SQL query to display the stored data:
            - `SELECT * FROM person;`

## Unsolved Problems:

    - Problem.) One of the problems which I have discovered and that still exist is that whenever I try to open the app using the heroku url on multiple devices and login in, the first player(x) is overwritten by the new user that has just logged in. When in the correct manner the user should be added after the existing player and being placed as the player with marker "O" or just a spectator.
      Possible Solution.) I tried to solve the problem and till some extent I was able to find a way that would solve this issue. So it turned out that if there is some time difference of about 5-10 seconds between each user that joins in it over writes the old user with the new user, But if we tell all users to fill out the username and click the submit button in the gap of around 1-2 seconds then the app works as it should.
      Possible Solution.) If I was given more time, I would try to locate and solve the problem on my own that way I can improve my problem-solving skills and If I still was not able to debug the problem then I would ask one of the TA's or my friends to help me solve the problem.


    - Problem.) When using the app via heroku I have often seen a delay occuring between the server and the client. I have also seen this happening when I run the app in the cloud9, often leading to a confusion when tracing the outputs provided by the server.
      Possible Solution.) I think that in order to solve this problem I would ask the TA's or someone with networking background.

    - Problem.) Sometimes it takes a while for the leaderboard to update and sometimes it updates instantly it also happens with the board sometimes where it just stops working and then starts working again.
      Possible Solution.) I truly do not know how to fix this because it mainly depends on how much time it is taking the server to send the request and get the updated data, also this only happens on heroku, on cloud9 it works fine.

    - If I had more time, I really wanted to implement a search ability so that we could search for a specific user.

## Technical Issues:

    -  Problem.) One technical issue which I encountered was when I had to block a player after their turn was over so that the player was not able to click another box until the next player made it's move, which acted as a trigger to unblock the blocked player and allowing it to make the next move.
       Solution.) In order to solve this, I stored the username into the Session Storage after receiving it from the input form. Along with this I implemented the UseState function to keep track of the next symbol to be marked. This allowed me to define a condition so that I was able to solve the above problem.

    - Problem.) Another technical issue I faced was that for some reason I was unable to change the state of the symbol to that was suppose to be marked next.
      Solution.) To solve this issue I used conditional statements checking the last symbol that was used and setting the next symbol.

    - Problem.) Another problem which I had was that for some reason in my app.py file whenever I tried to person from models.py file it kept giving me an error.
      Solution.) I spent 8 hours trying to solve this problem, checked slack, created and deleted database multiple times and also looked at the stackover-flow solutions but nothing seemed to work. I then read the documentation and saw this line `if __name__ == "__main__` which solved the problem.
