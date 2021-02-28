import React from 'react';
import { App } from './App.js';
import { Box_Comp } from './Square.js';
import './Board.css';
import { useState, useRef, useEffect } from 'react';
import io from 'socket.io-client';
import { User_Login } from './Login.js';
// import socket from 'socket.io-client';


const socket = io();

export function Board(props){
    
    const [board, setBoard] = useState(Array(9).fill(null)); //Track Board Status
    const [symbl, setSymbl] = useState("X"); //Track next Move Status
    const [username, setUsername] = useState([]); //Track  Players Joined
    const User_Input_Ref = useRef(null); //Take username as input
    const [IsLoggedIn, setIsLoggedIn] = useState(false); //Check if User logged in or not
    
    
    function FormData() {
        
      if(User_Input_Ref != null){
        setIsLoggedIn(prevIsLoggedIn => !prevIsLoggedIn)  //Displaying game if user logged in
        console.log(username);
        let Curr_User = User_Input_Ref.current.value;     //Current username
                    sessionStorage.setItem('LoggedInUser', Curr_User);
        username.push(Curr_User);                       //storing the user name in username array
        socket.emit('User_List_Update', {User_Name: Curr_User}) //sending the user name in an object to server
        console.log(username);           //printing out the entire username array
          
      }
        
    }
    
    function Listen_Click(idx){            //checking if the user clicked a box
       console.log(username, idx);
       if(sessionStorage.getItem("LoggedInUser") === username[1] || sessionStorage.getItem("LoggedInUser") === username[0]) {
        const Update_Array = Array(...board);   // checking if the clicked index was empty
        if(Update_Array[idx] == null){
            // updating the board
            if(symbl === "X" && sessionStorage.getItem("LoggedInUser") === username[0]){
                Update_Array[idx] = symbl;      //if it was empty then assiging the symbol
                setBoard(Update_Array);// if the symbl was x change to o
                setSymbl("O");
                socket.emit('Board_Info', {Index: idx, Value: symbl});   //sending the index and val of the marked box
                socket.emit('Curr_Symbl', 'O');   //sending the index and val of the marked box
                //Check_Winner(Update_Array, username[0], "X");
            }
            if ( symbl === "O" && sessionStorage.getItem("LoggedInUser") === username[1] ){
                Update_Array[idx] = symbl;      //if it was empty then assiging the symbol
                setBoard(Update_Array);//else vice versa
                setSymbl("X");
                socket.emit('Board_Info', {Index: idx, Value: symbl});   //sending the index and val of the marked box
                socket.emit('Curr_Symbl', 'X');   //sending the index and val of the marked box
                //Check_Winner(Update_Array, username[1], "O");
            }
            
        }
       }
    }
    
    function Check_Winner(Win_Check_Arr,Winner_Name_Arr){
        const Winning_Pattern = [
            [0, 1, 2,],
            [3, 4, 5,],
            [6, 7, 8,],
            [0, 3, 6,],
            [1, 4, 7,],
            [2, 5, 8,],
            [0, 4, 8,],
            [2, 4, 6,]
        ]
        
        for(let Idx_Check=0; Idx_Check < Winning_Pattern.length; Idx_Check++){
            let winning_row = Winning_Pattern[Idx_Check]
            let box_1 = winning_row[0]
            let box_2 = winning_row[1]
            let box_3 = winning_row[2]

            
            if(Win_Check_Arr[box_1] == 'X' && Win_Check_Arr[box_2] == 'X' && Win_Check_Arr[box_3] == 'X'){
                return alert("Player X : " + Winner_Name_Arr[0] + " is the Winner!!!");
                //alert(Win_Check_User + " You are the Winner!!!")
            }
            
            else if(Win_Check_Arr[box_1] == 'O' && Win_Check_Arr[box_2] == 'O' && Win_Check_Arr[box_3] == 'O'){
                return alert("Player O : " + Winner_Name_Arr[1] + " is the Winner!!!");
                //alert(Win_Check_User + " You are the Winner!!!")
            }
            else{
                continue;
            }
        
        }
        return
    }
    
    
    function Create_NewGame(){
        const Reset_Board=Array(9).fill(null);
        const Reset_Symbl="X";
        setBoard(Array(9).fill(null));
        setSymbl("X");
        socket.emit('Play_Again', {reset_Board: Reset_Board, reset_Symbl: Reset_Symbl});   //sending the index and val of the marked box
    }
    
    
    useEffect(() => {
        
        socket.on('Play_Again', (Clean_Moves) => {
            setBoard(Clean_Moves.reset_Board);
            setSymbl(Clean_Moves.reset_Symbl);
        });
        
        socket.on('Curr_Symbl', (symbol)=> {
            setSymbl(symbol);      //listening for new users and updating the username array
        });
        
        socket.on('User_List_Update', (New_User)=> {
            setUsername(New_User);      //listening for new users and updating the username array
        });
        
        socket.on('Board_Info', data => {   //listening for other player to make their move and updating the board
            console.log(data);
            
            const Store_Reciv_Data  = board => board.map((board_val, board_idx) => {    
                if(board_idx == data.Index){
                    return data.Value;
                }
                else{
                   return board_val
               }
            });
            setBoard(Store_Reciv_Data);
        
        });
        Check_Winner(board,username); 
        
    },[]);
    
    
    const Update_Board = Array(9).fill(null);
    for (let i = 0; i < 9; i++){
        Update_Board.push(<Box_Comp box_value={board[i]} box_index={i} Listen_Click={Listen_Click}/>)
    }
    const Playing_Players = Array();
    const Spectator_Players = Array();
    
    for (let i = 0; i < username.length; i++){
        if(i == 0){Playing_Players.push(<table classname ="Player_X_Stlye"><tr><td>Player_X: {username[i]}</td></tr></table>)}
        else if(i == 1){Playing_Players.push(<table classname ="Player_O_Style"><tr><td>Player_O: {username[i]}</td></tr></table>)}
        else{Spectator_Players.push(<table classname = "Spectator_Stlye"><tr><td>Spectator: {username[i]}</td></tr></table>)}
        
    }
    
    
    return(
            <div className="wrapper">
                {IsLoggedIn ?  <div class = "board"> 
                                    {Update_Board} 
                                    <p>Next move: {symbl}</p>
                                    {Playing_Players}
                                    {Spectator_Players}
                                    <button type="reset" onClick={Create_NewGame}>Play Again!</button>
                               </div>                   
                               : 
                               <div className="Input_Form"> 
                                    <h1>Enter your Username:</h1> 
                                    <input type='text' ref={User_Input_Ref} />
                                    <button type="Submit" onClick={FormData}> Submit </button>
                                </div>
                
                }
            </div>
            
    );
}

export default Board




            // else if(IsWinner == false){
            //         for (let i = 0; i < Win_Check_Arr.length; i++) {
            //             if ((Win_Check_Arr[i] != null) && ((Win_Check_Arr[i] == "X") || (Win_Check_Arr[i] == "O"))) {
            //                 alert(" It's a Draw!!!");
            //             }
            //             else{
            //                 continue
            //             }
            //         }
            //     }