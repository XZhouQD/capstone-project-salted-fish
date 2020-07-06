import React, { useState } from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import { postProjectRole } from "../../actions/projects";

const AddRoleProject = ({ postProjectRole }) => {
  const [flag, setFlag] = useState(0);
  function handleFlag(e) {
    const Flag = 1;
    setFlag(Flag);
  }

  const [fields, setFields] = useState([
    {
      title: "",
      amount: 0,
      skill: 0,
      experience: 0,
      education: 0,
      general_enquiry: "",
    },
  ]);

  function handleEnquiryChange(i, event) {
    const values = [...fields];
    values[i].general_enquiry = event.target.value;
    setFields(values);
  }

  function handleTitleChange(i, event) {
    const values = [...fields];
    values[i].title = event.target.value;
    setFields(values);
  }

  function handleAmountChange(i, event) {
    const values = [...fields];
    values[i].amount = event.target.value;
    setFields(values);
  }

  function handleEducationChange(i, event) {
    const values = [...fields];
    values[i].education = event.target.value;
    setFields(values);
  }

  function handleExperienceChange(i, event) {
    const values = [...fields];
    values[i].experience = event.target.value;
    setFields(values);
  }

  function handleSkillChange(i, event) {
    const values = [...fields];
    values[i].skill = event.target.value;
    setFields(values);
  }

  function handleAdd(e) {
    e.preventDefault();
    const {
      title,
      amount,
      skill,
      experience,
      education,
      general_enquiry,
    } = fields[fields.length - 1];

    console.log();
    postProjectRole({
      title,
      amount,
      skill,
      experience,
      education,
      general_enquiry,
    });

    const values = [...fields];
    values.push({
      title: "",
      amount: 0,
      skill: 0,
      experience: 0,
      education: 0,
      general_enquiry: "",
    });
    console.log(values);
    setFields(values);
  }

  // const onSubmit = (e) => {
  //   e.preventDefault();
  //   var skillsArr = [];
  //   var experienceArr = [];

  //   for (var i of fields) {
  //     skillsArr.push(i.skill);
  //     experienceArr.push(i.experience);
  //   }

  //   var skills = skillsArr.join(",");
  //   var experience = experienceArr.join(",");
  //   // post project
  // };

  if (flag === 1) {
    return <Redirect to="/dashboard" />;
  }

  return (
    <div className="container">
      <div className="valign-wrapper" style={{ marginTop: "50px" }}>
        <div className="row center">
          this is your {fields.length} roles
          <div className="col s12 m10 l12 card-panel z-depth-6">
            <form onSubmit={(e) => handleAdd(e)}>
              {fields.map((field, idx) => {
                return (
                  <div>
                    <div key={`${field}-${idx}`}>
                      <div className="row">
                        <div className="col l4">
                          <label className="left">Role's Title</label>
                          <input
                            type="text"
                            placeholder="enter roles title of your project"
                            onChange={(e) => handleTitleChange(idx, e)}
                            min="0"
                            required
                          />
                        </div>

                        <div className="col l4">
                          <label className="left">Role's Amount</label>
                          <input
                            type="number"
                            placeholder="enter roles amount of your project"
                            onChange={(e) => handleAmountChange(idx, e)}
                            min="0"
                            required
                          />
                        </div>

                        <div className="col l4">
                          <label className="left">Role's General_enquiry</label>
                          <input
                            type="text"
                            placeholder="enter the basic skills you wish your collabortors have"
                            onChange={(e) => handleEnquiryChange(idx, e)}
                            min="0"
                            required
                          />
                        </div>
                      </div>
                      <div className="row">
                        <div className="col l4">
                          <label className="left">Role's education level</label>
                          <select
                            className="browser-default"
                            onChange={(e) => handleEducationChange(idx, e)}
                            placeholder="enter the role's education level of your project"
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

                        <div className="col l4">
                          <label className="left">Role's Skills</label>
                          <select
                            className="browser-default"
                            onChange={(e) => handleSkillChange(idx, e)}
                            placeholder="enter the role's skills of your project"
                          >
                            <option value="" disabled>
                              Choose your option
                            </option>
                            {[
                              "Web Development",
                              "Java",
                              "Python",
                              "PHP",
                              "Script Language",
                              "Database Management",
                              "Computer Vision",
                              "Security Engineering",
                              "Testing",
                              "Algorithm Design",
                              "Operating System",
                              "Data Science",
                              "Human Computer Interaction",
                              "Deep Learning/Neural Network",
                              "Distribution System",
                            ].map((ele, index) => {
                              return (
                                <option value={index} key={index}>
                                  {ele}
                                </option>
                              );
                            })}
                          </select>
                        </div>

                        <div className="col l4">
                          <label className="left">Role's Experience</label>
                          <input
                            type="number"
                            placeholder="enter the minimal skill experience of your role"
                            onChange={(e) => handleExperienceChange(idx, e)}
                            min="0"
                            required
                          />
                        </div>
                      </div>
                    </div>
                  </div>
                );
              })}

              <br></br>
              <input
                type="submit"
                className="btn btn-primary"
                value="ADD ONE ROLE"
                style={{ marginBottom: "10px" }}
              />

              <button
                className="btn-small right"
                style={{ marginTop: "20px" }}
                onClick={(e) => handleFlag(e)}
              >
                FINISH
              </button>
            </form>
          </div>
        </div>
      </div>
    </div>
  );
};

const mapStateToProps = (state) => ({
  flag: state.auth.flag,
});

export default connect(null, { postProjectRole })(AddRoleProject);
