import React from "react";
import { Link } from "react-router-dom";

const Test = () => {
  return (
    <div>
      <div class="row">
        <div class="col s12">
          <p>s12</p>
        </div>
        <img src="/background.jpg" alt="abs" />
        <div class="col s2 offset-s2 m4 l2 offset-l2 red">
          <p>s12 m4</p>
        </div>
        <div class="col s4 m4 l8 blue">
          <p>s12 m4</p>
        </div>
        <div class="col s4 m4 l2 yellow">
          <p>s12 m4</p>
        </div>
      </div>
    </div>
  );
};

export default Test;
