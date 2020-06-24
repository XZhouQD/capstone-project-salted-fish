import React from "react";

const ProjectRole = (props) => {
  return (
    <div className="row">
      <div className="input-field col s8 m8 l8">
        <select name="role">
          <option value="" disabled selected>
            Choose your collaborator roles
          </option>
          <option value="1">UI designer</option>
          <option value="2">Backend engineer</option>
          <option value="3">Frontend engineer</option>
          <option value="4">AI engineer</option>
          <option value="5">Big data development engineer</option>
          <option value="6">Data analysis engineer </option>
        </select>
        <label>Different Roles</label>
      </div>
      <div className="input-field col s4 m4 l4">
        <input
          placeholder="How many roles do you want"
          id="organizer"
          type="text"
          className="validate"
          min="0"
        />
        <label for="organizer">Roles number</label>
      </div>
    </div>
  );
};

export default ProjectRole;
