/* eslint-disable */
import React from "react";
import { App } from "./App.js";
import { Board } from "./Board.js";
import io from "socket.io-client";

// Creating a Box Component with class box(used for styling), that calls the Listen_Click function whenever the user clicks the box. The user click function will recieve and index value so that it knows which box was clicked.

export function Box_Comp(props) {
  return (
    <div className="box" onClick={() => props.Listen_Click(props.box_index)}>
      {props.box_value}
    </div>
  );
}

export default Box_Comp;
