import React, { useState } from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import { postProjectRole } from "../../actions/projects";

const AddRoleProject = ({ postProjectRole }) => {
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

  return (
    <div>
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
                        <div>
                          <label className="left">roles title</label>
                          <input
                            type="text"
                            placeholder="enter one number"
                            onChange={(e) => handleTitleChange(idx, e)}
                            min="0"
                            required
                          />
                        </div>

                        <div>
                          <label className="left">roles amount</label>
                          <input
                            type="number"
                            placeholder="enter one number"
                            onChange={(e) => handleAmountChange(idx, e)}
                            min="0"
                            required
                          />
                        </div>

                        <div style={{ marginBottom: "10px" }}>
                          <label className="left">roles skills</label>
                          <select
                            className="browser-default"
                            onChange={(e) => handleSkillChange(idx, e)}
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

                        <div>
                          <label className="left">roles experience</label>
                          <input
                            type="number"
                            placeholder="enter one number"
                            onChange={(e) => handleExperienceChange(idx, e)}
                            min="0"
                            required
                          />
                        </div>

                        <div style={{ marginBottom: "10px" }}>
                          <label className="left">roles education level</label>
                          <select
                            className="browser-default"
                            onChange={(e) => handleEducationChange(idx, e)}
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
                          <label className="left">roles general_enquiry</label>
                          <input
                            type="text"
                            placeholder="input your wish"
                            onChange={(e) => handleEnquiryChange(idx, e)}
                            min="0"
                            required
                          />
                        </div>
                      </div>
                    </div>
                  );
                })}

                <br></br>
                <input
                  type="submit"
                  className="btn btn-primary"
                  value="Register"
                />
              </form>
            </div>
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
