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
                    Project 2<i className="material-icons right">more_vert</i>
                  </span>
                  <p className="truncate">
                    This is a brief project description. It is sliced from the
                    whole project description. Only some of the information will
                    be shown before the user click it.
                  </p>
                </div>
                <div className="card-action">
                  <a className="waves-effect waves-light btn-small">follow</a>
                  <a className="waves-effect waves-light btn-small">Apply</a>
                  <a className="waves-effect waves-light btn-small">
                    More info
                  </a>
                </div>
                <div className="card-reveal">
                  <span className="card-title grey-text text-darken-4">
                    Project 2 descriptions
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
