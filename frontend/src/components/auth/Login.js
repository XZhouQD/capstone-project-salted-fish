import React, { useState } from "react";
import { Link } from "react-router-dom";
import LoginForm from "./LoginForm";

class Login extends React.Component {
  state = {
    role: "",
    email: "",
    password: "",
  };

  render() {
    return (
      <div className="container">
        <div className="valign-wrapper" style={{ marginTop: "50px" }}>
          <div className="row center">
            <div className="col s12  card-panel z-depth-6">
              <h5 className="avatar">Sign Into Your Account</h5>
              <div>
                Are you a{" "}
                <button
                  className="btn-small lighten-1 z-depth-0 avatar"
                  onClick={() => this.setState({ role: "Dreamer" })}
                  style={{ padding: "0px 0px 0px 0px" }}
                >
                  dreamer
                </button>
                <span> or </span>
                <button
                  className="btn-small lighten-1 z-depth-0 avatar"
                  onClick={() => this.setState({ role: "Collaborator" })}
                  style={{ padding: "0px 0px 0px 0px" }}
                >
                  collaborator
                </button>
              </div>
              <br />
              <LoginForm role={this.state.role} />
              <p>
                Don't have an account? <Link to="./register">Sign up</Link>
              </p>
              <button
                className="btn-small  z-depth-0 avatar right small"
                onClick={() => this.setState({ role: "Admin" })}
                style={{ padding: "0px 0px 0px 0px" }}
              >
                admin
              </button>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Login;
