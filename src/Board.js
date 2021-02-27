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
    
    const [board, setBoard] = useState(Array(9).fill(null)); //array called board and function called setBoard to update the board array.
    const [symbl, setSymbl] = useState("X");
    const [username, setUsername] = useState([]);
    const User_Input_Ref = useRef(null);
    const [DisplayGame, setDisplayGame] = useState(true);
    const [CurrPlayer, setPlayer] = useState([]);
    const [IsLoggedIn, setIsLoggedIn] = useState(false);
    
    
    
    function FormData() {
        
      if(User_Input_Ref != null){
        setIsLoggedIn(prevIsLoggedIn => !prevIsLoggedIn)
        const Orig_User_Arr = Array(...username);
        Orig_User_Arr.push(User_Input_Ref.current.value);
        console.log(Orig_User_Arr);
        setUsername(Orig_User_Arr);
      }
        
    }
    
    function Listen_Click(idx){
        const Update_Array = Array(...board);
        if(Update_Array[idx] == null){
            Update_Array[idx] = symbl;
            setBoard(Update_Array);
            if(symbl === "X"){
                setSymbl("O");
            }
            else{
                setSymbl("X");
            }
        }
        socket.emit('Board_Info', {Index: idx, Value: symbl}); 
    }
    
    useEffect(() => {
        socket.on('Board_Info', data => {
            console.log(data);
            
            const Store_Reciv_Data  = prevBoard => prevBoard.map((board_val, board_idx) => {
                if(board_idx == data.Index){
                    return data.Value;
                }
                else{
                   return board_val
               }
            });
            
            setBoard(Store_Reciv_Data);
        });
    },[]);
    
    
    const Update_Board = Array(9).fill(null);
    for (let i = 0; i < 9; i++){
        Update_Board.push(<Box_Comp box_value={board[i]} box_index={i} Listen_Click={Listen_Click}/>)
    }
    
    return(
        <div class="wrapper">
            {IsLoggedIn ?  <div class = "board"> {Update_Board} </div> : <div class="Input_Form"> 
                                                                         <h1>Enter your Username:</h1> 
                                                                         <input type='text' ref={User_Input_Ref} />
                                                                         <button type="Submit" onClick={FormData}> Submit </button>
                                                                         </div>
                
            }
            </div>
            
            
            
            
            
            // <div class="Input_Form">
            //     <h1>Enter your Username:</h1>
            //     <input type='text' ref={User_Input_Ref} />
            //     <button type="Submit" onClick={FormData}> Submit </button>
            // </div>
            
            
            // <div class = "board">
            //     {Update_Board}
            // </div>
    )
}

export default Board;