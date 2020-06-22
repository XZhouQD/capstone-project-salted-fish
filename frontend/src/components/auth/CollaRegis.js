import React from "react";

const CollaRegis = () => {
  return (
    <div>
      <form action="create-profile.html">
        <div>
          <input type="text" placeholder="Name" name="name" required />
        </div>
        <div>
          <input type="email" placeholder="Email Address" name="email" />
        </div>
        <div>
          <input
            type="password"
            placeholder="Password"
            name="password"
            minLength="6"
          />
        </div>

        <div>
          <input
            type="password"
            placeholder="Confirm Password"
            name="password2"
            minLength="6"
          />
        </div>
        <div>
          <label className="left">
            Please select your highest education level
          </label>
          <select className="browser-default">
            <option value="" disabled selected>
              Choose your option
            </option>
            <option value="1">primary</option>
            <option value="2">senior</option>
            <option value="3">Bachelor</option>
            <option value="4">Master</option>
            <option value="5">PHD</option>
          </select>
        </div>
        <div>
          <label className="left">Please choose your current job/major</label>
          <select className="browser-default">
            <option value="" disabled selected>
              Choose your option
            </option>
            <option value="1">UI designer</option>
            <option value="2">Backend engineer</option>
            <option value="3">Frontend engineer</option>
            <option value="4">AI engineer</option>
            <option value="5">Big data development engineer</option>
            <option value="5">Data analysis engineer </option>
          </select>
        </div>
        <div>
          <label className="left">
            How long have you been working in your feild
          </label>
          <select className="browser-default">
            <option value="" disabled selected>
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

export default CollaRegis;
