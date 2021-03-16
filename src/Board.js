/* eslint-disable */
import React from "react";
import { App } from "./App.js";
import { Box_Comp } from "./Square.js";
import "./Board.css";
import { useState, useRef, useEffect } from "react";
import io from "socket.io-client";

const socket = io();

export function Board(props) {
  const [board, setBoard] = useState(Array(9).fill(null));
  const [symbl, setSymbl] = useState("X");
  const [username, setUsername] = useState([]);
  const User_Input_Ref = useRef(null);
  const [IsLoggedIn, setIsLoggedIn] = useState(false);
  const [IsLeaderBoard, setIsLeaderBoard] = useState(false);
  const [Orig_User, SetOrig_User] = useState([]);
  const [Orig_Score, SetOrig_Score] = useState([]);
  const [IsWinner, setWinner] = useState(false);
  const [IsGameOver, setIsGameOver] = useState(false);

  React.useEffect(() => {
    Check_Winner(board, username);
  }, [board]);

  function FormData() {
    if (User_Input_Ref != null) {
      setIsLoggedIn((prevIsLoggedIn) => !prevIsLoggedIn);
      console.log(username);
      let Curr_User = User_Input_Ref.current.value;
      sessionStorage.setItem("LoggedInUser", Curr_User);
      setUsername((prev_user) => [...prev_user, Curr_User]);
      socket.emit("User_List_Update", { User_Name: Curr_User });
      socket.emit("DB_UserCheck", Curr_User);
      console.log(username);
    }
  }

  function Listen_Click(idx) {
    console.log(username, idx);
    if (
      sessionStorage.getItem("LoggedInUser") === username[1] ||
      sessionStorage.getItem("LoggedInUser") === username[0]
    ) {
      const Update_Array = Array(...board);
      if (Update_Array[idx] == null && !IsGameOver) {
        if (
          symbl === "X" &&
          sessionStorage.getItem("LoggedInUser") === username[0]
        ) {
          Update_Array[idx] = symbl;
          setBoard(Update_Array);
          setSymbl("O");
          socket.emit("Board_Info", { Index: idx, Value: symbl });
          socket.emit("Curr_Symbl", "O");
        }
        if (
          symbl === "O" &&
          sessionStorage.getItem("LoggedInUser") === username[1]
        ) {
          Update_Array[idx] = symbl;
          setBoard(Update_Array);
          setSymbl("X");
          socket.emit("Board_Info", { Index: idx, Value: symbl });
          socket.emit("Curr_Symbl", "X");
        }
      }
    }
  }

  function Leader_Board() {
    setIsLeaderBoard((prevLeaderBoard) => !prevLeaderBoard);
  }

  function Check_Winner(Win_Check_Arr, Winner_Name_Arr) {
    const Winning_Pattern = [
      [0, 1, 2],
      [3, 4, 5],
      [6, 7, 8],
      [0, 3, 6],
      [1, 4, 7],
      [2, 5, 8],
      [0, 4, 8],
      [2, 4, 6],
    ];
    let isDraw = true;

    for (let Idx_Check = 0; Idx_Check < Winning_Pattern.length; Idx_Check++) {
      let winning_row = Winning_Pattern[Idx_Check];
      let box_1 = winning_row[0];
      let box_2 = winning_row[1];
      let box_3 = winning_row[2];

      if (
        Win_Check_Arr[box_1] == "X" &&
        Win_Check_Arr[box_2] == "X" &&
        Win_Check_Arr[box_3] == "X"
      ) {
        document.getElementById("Display_Winner").innerHTML =
          "Winner: " + Winner_Name_Arr[0] + "!!!";

        if (
          sessionStorage.getItem("LoggedInUser") === username[0] &&
          !IsWinner
        ) {
          setWinner(true);
          console.log(
            "Winner is: " +
              Winner_Name_Arr[0] +
              " Loser is: " +
              Winner_Name_Arr[1]
          );
          socket.emit("Game_Result_Winner", {
            Winner: Winner_Name_Arr[0],
            Loser: Winner_Name_Arr[1],
          });
          socket.emit("Game_Over", { Game_Over: true });
        }

        isDraw = false;
      } else if (
        Win_Check_Arr[box_1] == "O" &&
        Win_Check_Arr[box_2] == "O" &&
        Win_Check_Arr[box_3] == "O"
      ) {
        document.getElementById("Display_Winner").innerHTML =
          "Winner: " + Winner_Name_Arr[1] + "!!!";

        if (
          sessionStorage.getItem("LoggedInUser") === username[1] &&
          !IsWinner
        ) {
          setWinner(true);
          console.log(
            "Winner is: " +
              Winner_Name_Arr[1] +
              "Loser is: " +
              Winner_Name_Arr[0]
          );
          socket.emit("Game_Result_Winner", {
            Winner: Winner_Name_Arr[1],
            Loser: Winner_Name_Arr[0],
          });
          socket.emit("Game_Over", { Game_Over: true });
        }

        isDraw = false;
      } else {
        continue;
      }
    }

    let Game_Over = true;

    if (isDraw) {
      for (let i = 0; i < Win_Check_Arr.length; i++) {
        if (Win_Check_Arr[i] === null) {
          Game_Over = false;
          break;
        }
      }

      if (Game_Over) {
        document.getElementById("Display_Winner").innerHTML =
          "Game Result: DRAW!!!";

        if (sessionStorage.getItem("LoggedInUser") === username[0]) {
          console.log("The Game is: Draw");
        }
      }
    }

    return;
  }

  function Create_NewGame() {
    if (
      sessionStorage.getItem("LoggedInUser") === username[1] ||
      sessionStorage.getItem("LoggedInUser") === username[0]
    ) {
      const Reset_Board = Array(9).fill(null);
      const Reset_Symbl = "X";
      setBoard(Array(9).fill(null));
      setSymbl("X");
      setIsGameOver(false);
      socket.emit("Play_Again", {
        reset_Board: Reset_Board,
        reset_Symbl: Reset_Symbl,
      });
      document.getElementById("Display_Winner").innerHTML = "In Progress";
    }
  }

  useEffect(() => {
    socket.on("Play_Again", (Clean_Moves) => {
      setBoard(Clean_Moves.reset_Board);
      setSymbl(Clean_Moves.reset_Symbl);
      document.getElementById("Display_Winner").innerHTML = "In Progress";
    });

    socket.on("Curr_Symbl", (symbol) => {
      setSymbl(symbol);
    });

    socket.on("User_List_Update", (New_User) => {
      console.log(New_User);

      setUsername((prevUser) => [...New_User]); //Changed Here
    });

    socket.on("Old_DB_Users", (Initial_User_DB) => {
      SetOrig_User((prevOrig_User) => (prevOrig_User = Initial_User_DB));
    });

    socket.on("Old_DB_Scores", (Initial_Score_DB) => {
      SetOrig_Score((prevOrig_Score) => (prevOrig_Score = Initial_Score_DB));
    });

    socket.on("Updated_DB_Users", (Updated_User_DB) => {
      SetOrig_User((prevOrig_User) => (prevOrig_User = Updated_User_DB));
    });

    socket.on("Updated_DB_Scores", (Updated_Score_DB) => {
      SetOrig_Score((prevOrig_Score) => (prevOrig_Score = Updated_Score_DB));
    });

    socket.on("Game_Over", (Game_Over) => {
      setIsGameOver(Game_Over["Game_Over"]);
    });

    socket.on("Board_Info", (data) => {
      console.log(data);

      const Store_Reciv_Data = (board) =>
        board.map((board_val, board_idx) => {
          if (board_idx == data.Index) {
            return data.Value;
          } else {
            return board_val;
          }
        });
      setBoard(Store_Reciv_Data);
    });
  }, []);

  const Update_Board = Array(9).fill(null);
  for (let i = 0; i < 9; i++) {
    Update_Board.push(
      <Box_Comp
        box_value={board[i]}
        box_index={i}
        Listen_Click={Listen_Click}
      />
    );
  }

  const Playing_Players = Array();
  const Spectator_Players = Array();

  for (let i = 0; i < username.length; i++) {
    if (i == 0) {
      Playing_Players.push(
        <ul>
          <li id="Player_X_Style"> Player - X : {username[i]}</li>
        </ul>
      );
    } else if (i == 1) {
      Playing_Players.push(
        <ul>
          <li id="Player_O_Style"> Player - O : {username[i]}</li>
        </ul>
      );
    } else {
      Spectator_Players.push(
        <ul>
          <li id="Spectator_Style">Spectator - : {username[i]}</li>
        </ul>
      );
    }
  }

  const Leader_Board_Arr = Array();
  for (let val = 0; val < Orig_User.length; val++) {
    if (sessionStorage.getItem("LoggedInUser") == Orig_User[val]) {
      Leader_Board_Arr.push(
        <tr id="Curr_User_Data">
          <td> {Orig_User[val]} </td>
          <td> {Orig_Score[val]} </td>
        </tr>
      );
    } else {
      Leader_Board_Arr.push(
        <tr>
          <td> {Orig_User[val]} </td>
          <td> {Orig_Score[val]} </td>
        </tr>
      );
    }
  }

  return (
    <div className="wrapper">
      {IsLoggedIn ? (
        <div id="Main_Board">
          <h1 id="Game_Name">Tic Tac Toe Game!</h1>
          <img
            id="BG_IMG_Board"
            src="https://res.cloudinary.com/ddsomtotk/image/upload/v1615102367/Game_Pic_mxugms.jpg"
            alt="Background_Image"
          />
          <h2 id="Display_Winner"></h2>
          <div className="board">
            {Update_Board}
            <p>Next Turn : {symbl}</p>

            <button
              className="btn"
              type="reset"
              onClick={Create_NewGame}
              id="replay"
            >
              Play Again!
            </button>
            <button className="btn" onClick={Leader_Board} id="LB_Btn">
              Leader Board
            </button>
          </div>
          <div id="Playing">
            <h2>Currently Playing:</h2>
            {Playing_Players}
          </div>
          <div id="Watching">
            <h2>Currently Watching:</h2>
            {Spectator_Players}
          </div>
          {IsLeaderBoard ? (
            <div id="Table_Wrapper">
              <table>
                <caption>LeaderBoard</caption>
                <thead>
                  <tr>
                    <th>UserName</th>
                    <th>Ranking Score</th>
                  </tr>
                </thead>
                <tbody>{Leader_Board_Arr}</tbody>
              </table>
            </div>
          ) : null}
        </div>
      ) : (
        <div>
          <img
            id="BG_IMG_Form"
            src="https://res.cloudinary.com/ddsomtotk/image/upload/v1615102276/Pro2_Pic2_tbwb1l.webp"
            alt="Background_Image"
          />
          <div className="Input_Form">
            <h1 id="Form_Header1">
              <u>User Log-In Form</u>
            </h1>
            <h3 id="Form_Header3">Enter your Username:</h3>
            <input id="Form_Input" type="text" ref={User_Input_Ref} />
            <button id="Form_Btn" type="Submit" onClick={FormData}>
              {" "}
              Submit{" "}
            </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Board;
