import React from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import { changeProjectRole } from "../../actions/projects";
import M from "materialize-css";

class ChangeRoleDetails extends React.Component {
  constructor(props) {
    super(props);
    this.handleSkillChange = this.handleSkillChange.bind(this);
  }

  state = {
    title: "",
    amount: 0,
    skill: "",
    experience: 0,
    education: 0,
    general_enquiry: "",
  };

  componentDidMount() {
    M.AutoInit();
  }
  handleonChange = (e) => {
    // get target element name
    this.setState({ [e.target.name]: e.target.value });
  };

  handleonSubmit = (e) => {
    e.preventDefault();
    const pid = this.props.match.params.pid;
    const rid = this.props.match.params.rid;

    const {
      title,
      amount,
      skill,
      experience,
      education,
      general_enquiry,
    } = this.state;
    console.log(this.state);

    this.props.changeProjectRole({
      title,
      amount,
      skill,
      experience,
      education,
      general_enquiry,
      pid,
      rid,
    });
  };

  handleSkillChange(event) {
    var options = event.target.options;
    var value = [];
    for (var i = 0, l = options.length; i < l; i++) {
      if (options[i].selected) {
        value.push(options[i].value);
      }
    }

    // console.log(values[0].skill);
    value = value.join(",");
    console.log(value);
    this.setState({ skill: value });
  }

  render() {
    const url = "/projects/" + this.props.match.params.pid;
    if (this.props.hasChange) {
      return <Redirect to={url} />;
    }
    return (
      <div className="container">
        <div className="valign-wrapper" style={{ marginTop: "50px" }}>
          <div className="row center">
            <div className="col s12 m10 l12 card-panel z-depth-6">
              <form onSubmit={(e) => this.handleonSubmit(e)}>
                <div className="row">
                  <div className="col l4">
                    <label className="left">Role's Title</label>
                    <input
                      type="text"
                      placeholder="enter roles title of your project"
                      name="title"
                      onChange={(e) => this.handleonChange(e)}
                      min="0"
                      required
                    />
                  </div>

                  <div className="col l4">
                    <label className="left">Role's Amount</label>
                    <input
                      type="number"
                      placeholder="enter roles amount of your project"
                      name="amount"
                      onChange={(e) => this.handleonChange(e)}
                      min="0"
                      required
                    />
                  </div>

                  <div className="col l4">
                    <label className="left">Role's General_enquiry</label>
                    <input
                      type="text"
                      placeholder="enter the basic skills you wish your collabortors have"
                      name=""
                      onChange={(e) => this.handleonChange(e)}
                      min="0"
                      required
                      name="general_enquiry"
                    />
                  </div>
                </div>
                <div className="row">
                  <div className="col l4">
                    <label className="left">Role's education level</label>
                    <select
                      className="browser-default"
                      name={this.state.education}
                      onChange={(e) => this.handleonChange(e)}
                      placeholder="enter the role's education level of your project"
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

                  <div className="input-field col l4">
                    <select
                      multiple
                      onChange={(e) => this.handleSkillChange(e)}
                      placeholder="role's skills of your project"
                    >
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
                          <option value={index + 1} key={index}>
                            {ele}
                          </option>
                        );
                      })}
                    </select>
                    <label className="left">Role's Skills</label>
                  </div>

                  <div className="col l4">
                    <label className="left">Role's Experience</label>
                    <input
                      type="number"
                      placeholder="enter the minimal skill experience of your role"
                      onChange={(e) => this.handleonChange(e)}
                      min="0"
                      required
                      name="experience"
                    />
                  </div>
                </div>

                <input
                  type="submit"
                  className="btn btn-primary"
                  value="Change"
                  style={{ marginBottom: "10px" }}
                />
              </form>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  hasChange: state.project.hasChange,
});

export default connect(mapStateToProps, { changeProjectRole })(
  ChangeRoleDetails
);
