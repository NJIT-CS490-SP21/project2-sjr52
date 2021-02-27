import React from 'react';
import { App } from './App.js';
import { Box_Comp } from './Square.js';
import './Board.css';
import { useState, useRef, useEffect } from 'react';
import io from 'socket.io-client';
// import socket from 'socket.io-client';


const socket = io();

export function Board(props){
    
    const [board, setBoard] = useState(Array(9).fill(null)); //array called board and function called setBoard to update the board array.
    const [symbl, setSymbl] = useState("X");
    
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
        
        <div class = "board">
            {Update_Board}
        </div>
            
    )
}

export default Board;