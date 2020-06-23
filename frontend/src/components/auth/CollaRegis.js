import React, { useState } from "react";
import { connect } from "react-redux";
import { setAlert } from "../../actions/alert";
import { registerColla } from "../../actions/auth";

const CollaRegis = ({ setAlert, registerColla }) => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    repeat_password: "",
    phone_no: "",
    education: "",
    skills: "",
    experience: "",
  });

  const {
    name,
    email,
    password,
    repeat_password,
    phone_no,
    education,
    skills,
    experience,
  } = formData;

  const onChange = (e) => {
    // get target element name
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const onSubmit = (e) => {
    e.preventDefault();

    if (password !== repeat_password) {
      setAlert("Password does not match");
    } else {
      registerColla({
        name,
        email,
        phone_no,
        password,
        repeat_password,
        education,
        skills,
        experience,
      });
    }
  };

  return (
    <div>
      <form onSubmit={(e) => onSubmit(e)}>
        <div>
          <input
            type="text"
            placeholder="Name"
            name="name"
            value={name}
            onChange={(e) => onChange(e)}
            required
          />
        </div>
        <div>
          <input
            type="email"
            placeholder="Email Address"
            name="email"
            value={email}
            onChange={(e) => onChange(e)}
            required
          />
        </div>
        <div>
          <input
            type="text"
            placeholder="Phone Number"
            name="phone_no"
            minLength="6"
            value={phone_no}
            onChange={(e) => onChange(e)}
          />
        </div>
        <div>
          <input
            type="password"
            placeholder="Password"
            name="password"
            minLength="8"
            value={password}
            onChange={(e) => onChange(e)}
            required
          />
        </div>

        <div>
          <input
            type="password"
            placeholder="Confirm Password"
            name="repeat_password"
            minLength="8"
            value={repeat_password}
            onChange={(e) => onChange(e)}
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
  );
};

export default connect(null, { setAlert, registerColla })(CollaRegis);
