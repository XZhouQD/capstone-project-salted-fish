import React, { Component } from "react";
import { connect } from "react-redux";
import { getProject, searchProject } from "../../actions/projects";
import M from "materialize-css";
import EachProject from "./eachProject";
import { Link } from "react-router-dom";

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

  renderProject() {
    return (
      <div className="flexLayout">
        {this.props.ProjectLists.map((each, index) => {
          return (
            <EachProject
              title={each.title}
              category={each.category}
              description={each.description}
              key={index}
              id={each.id}
            />
          );
        })}
      </div>
    );
  }
  renderLoading() {
    return <div>loading....</div>;
  }
  render() {
    return (
      <div>
        <div className="container">
          <div className="row">
            <div>
              <form onSubmit={(e) => this.handleonSubmit(e)}>
                <div className="input-field col s12 l3">
                  <input
                    type="text"
                    name="description"
                    onChange={(e) => this.handleonChange(e)}
                    id="type_description"
                  />
                  <label for="type_description">Search by description</label>
                </div>

                <div
                  style={{ marginBottom: "10px" }}
                  className="input-field col s12 l3"
                >
                  <select
                    onChange={(e) => this.handleonChange(e)}
                    name="category"
                  >
                    <option value="" disabled selected>
                      Choose your option
                    </option>
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
                  <label className="left">SELECT CATEGORY</label>
                </div>

                <div
                  style={{ marginBottom: "10px" }}
                  className="input-field col s12 l3"
                >
                  <select
                    onChange={(e) => this.handleonChange(e)}
                    name="order_by"
                  >
                    <option value="">Choose your option</option>
                    <option value="last_update">last_update</option>
                    <option value="project_title">project_title</option>
                  </select>
                  <label className="left">SORTING ORDER</label>
                </div>

                <div
                  style={{ marginBottom: "10px" }}
                  className="input-field col s12 l3"
                >
                  <select
                    onChange={(e) => this.handleonChange(e)}
                    name="sorting"
                    required
                  >
                    <option value="">Choose your option</option>
                    <option value="ASC">ASC</option>
                    <option value="DESC">DESC</option>
                  </select>
                  <label className="left">ASCENDING/DESCENDING</label>
                </div>
                <div className="right">
                  {this.props.role === "Collaborator" ? (
                    <Link to="/collaproject">
                      <button
                        className="btn-small blue-grey darken-1"
                        style={{ marginRight: "10px" }}
                      >
                        match
                      </button>
                    </Link>
                  ) : (
                    ""
                  )}
                  <input
                    type="submit"
                    className="btn btn-small blue-grey darken-1"
                    value="Search"
                  />
                </div>
              </form>
            </div>
          </div>
          {this.props.ProjectLists.length === 0
            ? this.renderLoading()
            : this.renderProject()}
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
  role: state.auth.role,
  ProjectLists: state.project.ProjectLists,
});

export default connect(mapStateToProps, { getProject, searchProject })(
  ProjectList
);
