import React, { Component } from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
// Import Materialize
import M from "materialize-css";
import { createProject } from "../../actions/projects";

class CreateProject extends Component {
  constructor(props) {
    super(props);
    this.handleonChange = this.handleonChange.bind(this);
    this.handleonSubmit = this.handleonSubmit.bind(this);
  }

  state = {
    title: "",
    category: "",
    description: "",
  };

  componentDidMount() {
    // Auto initialize all the materailize css!
    M.AutoInit();
  }

  handleonChange = (e) => {
    // get target element name
    this.setState({ [e.target.name]: e.target.value });
  };

  handleonSubmit = (e) => {
    e.preventDefault();
    const { title, category, description } = this.state;
    this.props.createProject({ title, category, description });
  };

  render() {
    const { isAuthenticated } = this.props;
    if (!isAuthenticated) return <Redirect to="/login" />;

    console.log(this.props.isAuthenticated);

    return (
      <div className="container" style={{ marginTop: "50px" }}>
        <div className="card z-depth-6">
          <div className="row" style={{ paddingTop: "20px" }}>
            <form className="col s12" onSubmit={(e) => this.handleonSubmit(e)}>
              <div className="row">
                <div className="input-field col s12">
                  <input
                    placeholder="enter your project's title"
                    type="text"
                    className="validate"
                    name="title"
                    onChange={(e) => this.handleonChange(e)}
                    required
                  />
                  <label htmlFor="title">Project Title</label>
                </div>
              </div>

              <div className="row">
                <div className="input-field col s12">
                  <input
                    placeholder="please use comma to seperate different topics(optional) example: Machine Learning,Data Analysis"
                    type="text"
                    className="validate"
                    name="category"
                    onChange={(e) => this.handleonChange(e)}
                  />
                  <label htmlFor="title">Project Topic</label>
                </div>
              </div>

              <div className="row">
                <div className="input-field col s12">
                  <textarea
                    placeholder="describe your project details not more than 140 words"
                    className="materialize-textarea"
                    length="140"
                    name="description"
                    onChange={(e) => this.handleonChange(e)}
                    required
                  ></textarea>
                  <label for="description">Describe your project!</label>
                </div>
              </div>
              <div className="row">
                <input
                  type="submit"
                  className="btn right"
                  value="Create"
                  style={{ marginRight: "20px" }}
                />
              </div>
            </form>
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
});

export default connect(mapStateToProps, { createProject })(CreateProject);
