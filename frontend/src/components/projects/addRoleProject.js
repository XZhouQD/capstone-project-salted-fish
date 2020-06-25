import React, { Component } from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";

class AddRoleProject extends Component {
  state = {
    phone_no: "",
    education: "",
    skills: "",
    experience: "",
  };

  onChange = (e) => {
    this.setState({ [e.target.name]: e.target.value });
  };

  onSubmit = (e) => {
    e.preventDefault();
  };
  render() {
    // const { auth } = this.props;
    // if (!auth.uid) return <Redirect to="/signin" />;
    return (
      <div className="container">
        <div class="card blue-grey darken-1">
          <div class="card-content white-text">
            <span class="card-title">Project Title</span>
            <p>
              I am a very simple card. I am good at containing small bits of
              information. I am convenient because I require little markup to
              use effectively. project title
            </p>
          </div>
          <div class="card-action">
            <a href="#">project topic</a>
          </div>
        </div>
        <div class="card blue-grey">
          <form onSubmit={(e) => this.onSubmit(e)}>
            <div>
              <label className="left">
                Please select your highest education level
              </label>
              <select
                className="browser-default"
                onChange={(e) => this.onChange(e)}
                name="education"
              >
                <option value="" disabled>
                  Choose your option
                </option>
                <option value="1">Other</option>
                <option value="2">Bachelor</option>
                <option value="3">Master</option>
                <option value="4">Phd</option>
              </select>
            </div>

            <div>
              <label className="left">
                Please choose your current job/major
              </label>
              <select
                className="browser-default"
                onChange={(e) => this.onChange(e)}
                name="skills"
              >
                <option value="" disabled>
                  Choose your option
                </option>
                <option value="1">UI designer</option>
                <option value="2">Backend engineer</option>
                <option value="3">Frontend engineer</option>
                <option value="4">AI engineer</option>
                <option value="5">Big data development engineer</option>
                <option value="6">Data analysis engineer </option>
              </select>
            </div>
            <div>
              <label className="left">
                How long have you been working in your feild
              </label>
              <select
                className="browser-default"
                onChange={(e) => this.onChange(e)}
                name="experience"
              >
                <option value="" disabled>
                  Choose your option
                </option>
                <option value="1">0 - 3 years</option>
                <option value="2">3 - 6 years</option>
                <option value="3">6 - 9 years</option>
                <option value="4">10+ years</option>
              </select>
            </div>
            <br></br>
            <input type="submit" className="btn btn-primary" value="Register" />
          </form>
        </div>
      </div>
    );
  }
}

export default AddRoleProject;
