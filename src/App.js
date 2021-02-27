import React from 'react';
import { Box_Comp } from './Square.js';
import logo from './logo.svg';
import './App.css';
import './Board.css';
import { useState, useRef, useEffect } from 'react';
import { Board } from './Board.js';
import io from 'socket.io-client';
import { User_Login } from './Login.js';

    
    
function App(){
    
    return(
        <Board />
    );
    
}

export default App;