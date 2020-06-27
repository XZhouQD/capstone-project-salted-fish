import React, { Component } from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import M from "materialize-css";

class ProjectList extends Component {
  componentDidMount() {
    // Auto initialize all the materailize css!
    M.AutoInit();
  }

  render() {
    // const { auth } = this.props;
    // if (!auth.uid) return <Redirect to="/signin" />;
    return (
      <div>
        <div className="container">
          <div className="row">
            <div className="col s12">
              <div className="row">
                <div className="input-field col s12">
                  <i className="material-icons prefix">search</i>
                  <input type="text" id="search-projects" />
                  <label for="search-projects">search</label>
                </div>
              </div>
            </div>
          </div>

          <div className="row">
            <div className="col s12 m12 l12 xl12">
              <div className="card">
                <div className="card-image waves-effect waves-block waves-light"></div>
                <div className="card-content">
                  <span className="card-title activator grey-text text-darken-4">
                    Project 1<i className="material-icons right">more_vert</i>
                  </span>
                  <p className="truncate">Project first sentence</p>
                </div>
                <div className="card-action">
                  <i class="material-icons icon">mode_edit</i>
                  topic
                </div>
                <div className="card-reveal">
                  <span className="card-title grey-text text-darken-4">
                    Project 1 descriptions
                    <i className="material-icons right">close</i>
                  </span>
                  <p>
                    Here is some more information about this project that is
                    only revealed once clicked on.
                  </p>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
export default ProjectList;
