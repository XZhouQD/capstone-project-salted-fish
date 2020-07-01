import React, { Component } from "react";
import { connect } from "react-redux";
import { getProject, searchProject } from "../../actions/projects";
import M from "materialize-css";
import EachProject from "./eachProject";

class ProjectList extends Component {
  constructor(props) {
    super(props);
    this.handleonChange = this.handleonChange.bind(this);
    this.handleonSubmit = this.handleonSubmit.bind(this);
  }

  state = {
    description: "",
    category: "",
    order_by: "",
    sorting: "",
  };

  componentWillMount() {
    this.props.getProject();
  }

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
    const { description, category, order_by, sorting } = this.state;
    console.log(this.state);
    this.props.searchProject({ description, category, order_by, sorting });
  };

  render() {
    return (
      <div>
        <div className="container">
          <div className="row">
            <div className="col s12">
              <form
                className="col s12"
                onSubmit={(e) => this.handleonSubmit(e)}
              >
                <div style={{ marginBottom: "10px", marginTop: "20px" }}>
                  <input
                    type="text"
                    placeholder="TYPE THE DESCRIPTION FOR YOUR PROJECT"
                    name="description"
                    onChange={(e) => this.handleonChange(e)}
                  />
                </div>

                <div style={{ marginBottom: "10px" }}>
                  <label className="left">
                    SELECT THE CATEGORY FOR YOUR PROJECT
                  </label>
                  <select
                    className="browser-default"
                    onChange={(e) => this.handleonChange(e)}
                    name="category"
                  >
                    <option value="">Choose your option</option>
                    <option value="1">All other</option>
                    <option value="2">A web based application</option>
                    <option value="3">A desktop application</option>
                    <option value="4">A mobile application</option>
                    <option value="5">
                      A library for other project to reference
                    </option>
                    <option value="6">
                      A modification to existing platform
                    </option>
                    <option value="7">A research oriented project</option>
                  </select>
                </div>

                <div style={{ marginBottom: "10px" }}>
                  <label className="left">SORTING ORDER</label>
                  <select
                    className="browser-default"
                    onChange={(e) => this.handleonChange(e)}
                    name="order_by"
                  >
                    <option value="">Choose your option</option>
                    <option value="last_update">last_update</option>
                    <option value="project_title">project_title</option>
                  </select>
                </div>

                <div style={{ marginBottom: "10px" }}>
                  <label className="left">ASCENDING/DESCENDING</label>
                  <select
                    className="browser-default"
                    onChange={(e) => this.handleonChange(e)}
                    name="sorting"
                    required
                  >
                    <option value="">Choose your option</option>
                    <option value="ASC">ASC</option>
                    <option value="DESC">DESC</option>
                  </select>
                </div>
                <input
                  type="submit"
                  className="btn btn-primary"
                  value="Search"
                />
              </form>
            </div>
          </div>

          {this.props.ProjectLists.map((each, index) => {
            return (
              <EachProject
                title={each.title}
                category={each.category}
                description={each.description}
              />
            );
          })}
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
  ProjectLists: state.project.ProjectLists,
});

export default connect(mapStateToProps, { getProject, searchProject })(
  ProjectList
);
