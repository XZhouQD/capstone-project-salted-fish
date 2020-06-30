import React, { useState } from "react";

class DreamerDash extends React.Component {
  constructor() {
    super();
    this.handleOnclick2 = this.handleOnclick2.bind(this);
  }
  state = {
    colla: ["zhuzhu", "yomi", "yaso", "pig"],
    intereted: [],
    user: [],
  };

  handleOnclick(name) {
    var set = new Set([...this.state.intereted, name]);
    var newArr = Array.from(set);
    this.setState({ intereted: newArr });
  }

  handleOnclick2() {
    fetch("https://jsonplaceholder.typicode.com/todos/1")
      .then((response) => response.json())
      .then((json) => this.setState({ user: [...this.state.user, json] }));
  }

  render() {
    return (
      <div className="container">
        <div className="row">
          <div className="col s12 m8 l8 cards-container">
            {/* my projects */}
            <div className="card blue-grey darken-1">
              <div className="card-content white-text">
                <span className="card-title">
                  the project which you created----link to project details
                </span>
                <p>
                  I am a very simple card. I am good at containing small bits of
                  information. I am convenient because I require little markup
                  to use effectively.
                </p>
              </div>
              <div className="card-action"></div>
            </div>
          </div>
          <div className="col s12 m4 l4 cards-container">
            {/* my projects */}
            <div className="card blue-grey darken-1">
              <div className="card-content white-text">
                <span className="card-title">recommend user</span>
                <p>
                  I am a very simple card. I am good at containing small bits of
                  information. I am convenient because I require little markup
                  to use effectively.
                </p>
              </div>
              <div class="card-action"></div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default DreamerDash;
