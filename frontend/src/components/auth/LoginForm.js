import React, { useState } from "react";
import { connect } from "react-redux";
import { setAlert } from "../../actions/alert";
import { loginUser } from "../../actions/auth";
import { Redirect } from "react-router-dom";

const LoginForm = (props) => {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  console.log(props);
  const { role, loginUser, isAuthenticated } = props;
  const { email, password } = formData;

  const onChange = (e) => {
    // get target element name
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const onSubmit = (e) => {
    e.preventDefault();
    console.log(email, password, role);
    loginUser(email, password, role);
    console.log("success");
  };

  if (isAuthenticated) {
    return <Redirect to="/dashboard" />;
  }

  return (
    <form onSubmit={(e) => onSubmit(e)}>
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
          type="password"
          placeholder="Password"
          name="password"
          minLength="8"
          value={password}
          onChange={(e) => onChange(e)}
          required
        />
      </div>
      <p>{role}</p>
      <input type="submit" className="btn btn-primary" value="Sign in" />
    </form>
  );
};

const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
});

export default connect(mapStateToProps, { loginUser })(LoginForm);
