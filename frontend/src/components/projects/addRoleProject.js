import React, { useState } from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import M from "materialize-css";
import RoleList from "./roleList";
import AddRole from "./addRole";

const AddRoleProject = ({ setAlert, registerColla }) => {
  const [formData, setFormData] = useState({
    amount: 0,
    education: "",
    skills: "",
    experience: "",
  });

  const { amount, education, skills, experience } = formData;


  const onChange = (e) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const onSubmit = (e) => {
    e.preventDefault();
  };

  // const { auth } = this.props;
  // if (!auth.uid) return <Redirect to="/signin" />;
  return (
    <div className="container">
      <div class="card blue-grey darken-1" style={{ marginTop: "20px" }}>
        <div class="card-content white-text">
          <span class="card-title">Project Title</span>
          <p>project description</p>
        </div>
        <div class="card-action">
          <a href="#">project topic</a>
        </div>
      </div>
      <div>
        <form onSubmit={(e) => onSubmit(e)}>
          <div>
            <label className="left">Please enter the role amount</label>
            <input
              type="number"
              placeholder="Name"
              name="amount"
              // onChange 响应到value里
              value={amount}
              // change happens put the value into different states
              onChange={(e) => onChange(e)}
              min="0"
              required
            />
          </div>
          <div>
            <label className="left">
              Please select your highest education level
            </label>
            <select
              className="browser-default"
              value={education}
              onChange={(e) => onChange(e)}
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
            <label className="left">Please choose your current job/major</label>
            <select
              className="browser-default"
              value={skills}
              onChange={(e) => onChange(e)}
              name="skills"
            >
              <option value="" disabled>
                Choose your option
              </option>
              []
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
              value={experience}
              onChange={(e) => onChange(e)}
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
};

export default AddRoleProject;
