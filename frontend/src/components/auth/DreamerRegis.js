import React, { useState } from "react";
import { connect } from "react-redux";
import { setAlert } from "../../actions/alert";
import { registerDreamer } from "../../actions/auth";
import { Redirect } from "react-router-dom";
import M from "materialize-css";


const DreamerRegis = ({ setAlert, registerDreamer, flag }) => {
  function componentDidMount() {
    // Auto initialize all the materailize css!
    M.AutoInit();
  }
  componentDidMount();

  const [formData, setFormData] = useState({
    name: "",
    email: "",
    password: "",
    repeat_password: "",
    phone_no: "",
  });

  const { name, email, password, repeat_password, phone_no } = formData;

  const onChange = (e) => {
    // get target element name
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const onSubmit = (e) => {
    e.preventDefault();
    if (password !== repeat_password) {
      setAlert("Password does not match");
    } else {
      registerDreamer({ name, email, phone_no, password, repeat_password });
    }
  };
  console.log(flag);
  if (flag === "register success") {
    return <Redirect to="/login" />;
  }
  return (
    <div>
      <form onSubmit={(e) => onSubmit(e)}>
        <div className="input-field">
          <input
            type="text"
            // placeholder="Name"
            name="name"
            // onChange 响应到value里
            value={name}
            // change happens put the value into different states
            onChange={(e) => onChange(e)}
            required
            id="name"
          />
          <label for="name">Name</label>
        </div>
        <div className="input-field">
          <input
            type="email"
            // placeholder="Email Address"
            name="email"
            value={email}
            onChange={(e) => onChange(e)}
            required
            id="email_address"
          />
          <label for="email_address">Email Address</label>
        </div>
        <div className="input-field">
          <input
            type="text"
            // placeholder="Phone Number"
            name="phone_no"
            minLength="8"
            value={phone_no}
            onChange={(e) => onChange(e)}
            id="phone_number"
          />
          <label for="phone_number">Phone Number</label>
        </div>
        <div className="input-field">
          <input
            type="password"
            // placeholder="Password"
            name="password"
            minLength="8"
            value={password}
            onChange={(e) => onChange(e)}
            required
            id="password"
          />
          <label for="password">Password</label>
        </div>

        <div className="input-field">
          <input
            type="password"
            // placeholder="Confirm Password"
            name="repeat_password"
            minLength="6"
            value={repeat_password}
            onChange={(e) => onChange(e)}
            required
            id="confirm_password"
          />
          <label for="confirm_password">Confirm Password</label>
        </div>
        <input type="submit" className="btn blue-grey lighten-1" value="Register"
               style={{ marginBottom: "10px" }}/>
      </form>
    </div>
  );
};

const mapStateToProps = (state) => ({
  flag: state.auth.flag,
});

export default connect(mapStateToProps, { setAlert, registerDreamer })(
  DreamerRegis
);
