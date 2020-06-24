import React, { Component } from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
// Import Materialize
import M from "materialize-css";
import ProjectRole from "./projectRoles";

class CreateProject extends Component {
  constructor(props) {
    super(props);
    this.handleonChange = this.handleonChange.bind(this);
    this.handleonSubmit = this.handleonSubmit.bind(this);
  }

  state = {
    title: "",
    topic: "",
    content: "",
  };

  componentDidMount() {
    // Auto initialize all the materailize css!
    M.AutoInit();
  }

  handleonChange = (e) => {
    // get target element name
    this.setState({ [e.target.name]: e.target.value });
  };

  handleonSubmit = (e) => {
    e.preventDefault();
    console.log(this.state);
  };

  render() {
    // const { auth } = this.props;
    // if (!auth.uid) return <Redirect to="/signin" />;
    return (
      <div className="container" style={{ marginTop: "50px" }}>
        <div className="card z-depth-6">
          <div className="row" style={{ paddingTop: "20px" }}>
            <form className="col s12" onSubmit={(e) => this.handleonSubmit(e)}>
              <div className="row">
                <div className="input-field col s12">
                  <input
                    placeholder="Your project's title"
                    type="text"
                    className="validate"
                    name="title"
                    onChange={(e) => this.handleonChange(e)}
                  />
                  <label htmlFor="title">Project Title</label>
                </div>
              </div>

              <div className="row">
                <div className="input-field col s12">
                  <input
                    placeholder="Your project's catagory"
                    type="text"
                    className="validate"
                    name="topic"
                    onChange={(e) => this.handleonChange(e)}
                  />
                  <label htmlFor="title">Project Topic</label>
                </div>
              </div>

              <div className="row">
                <div className="input-field col s12">
                  <textarea
                    placeholder="Describe your project details"
                    className="materialize-textarea"
                    length="140"
                    name="content"
                    onChange={(e) => this.handleonChange(e)}
                  ></textarea>
                  <label for="description">Describe your project!</label>
                </div>
              </div>

              <input
                type="submit"
                className="btn"
                value="Register"
                style={{ marginBottom: "20px" }}
              />
            </form>
          </div>
        </div>
      </div>
    );
  }
}

export default CreateProject;
