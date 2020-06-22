import React, { useState } from "react";
import { Link } from "react-router-dom";
import Register from "./Register";

const Login = () => {
  const [formData, setFormData] = useState({
    email: "",
    password: "",
  });

  const { email, password } = formData;

  const onChange = (e) => {
    // get target element name
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const onSubmit = (e) => {
    e.preventDefault();
    console.log("login success");
  };

  return (
    <div className="container">
      <div className="valign-wrapper" style={{ marginTop: "50px" }}>
        <div className="row center">
          <div className="col s12  card-panel z-depth-6">
            <h5 className="avatar">Sign Into Your Account</h5>
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
                  minLength="6"
                  value={password}
                  onChange={(e) => onChange(e)}
                  required
                />
              </div>

              <input
                type="submit"
                className="btn btn-primary"
                value="Sign in"
              />
            </form>
            <p>
              Don't have an account? <Link to="./register">Sign up</Link>
            </p>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;
