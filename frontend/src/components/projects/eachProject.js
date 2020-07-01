import React, { Component } from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import M from "materialize-css";

class EachProject extends Component {
  render() {
    var categoryList = [
      "All other",
      "A web based application",
      "A desktop application",
      "A mobile application",
      "A library for other project to reference",
      "A modification to existing platform",
      "A research oriented project",
    ];
    return (
      <div className="row">
        <div className="col s12 m12 l12 xl12">
          <div className="card panel-up">
            <div className="card-image waves-effect waves-block waves-light"></div>
            <div className="card-content">
              <span className="card-title activator grey-text text-darken-4">
                {this.props.title}
                <i className="material-icons right">more_vert</i>
              </span>
              <p className="truncate">
                project category: {categoryList[this.props.category]}
              </p>
              <p className="truncate">
                project description: {this.props.description}
              </p>
            </div>
            <div className="card-action">
              <a
                className="waves-effect waves-light btn-small blue-grey darken-1"
                style={{ marginRight: "10px" }}
              >
                follow
              </a>
              <a
                className="waves-effect waves-light btn-small blue-grey darken-1"
                style={{ marginRight: "10px" }}
              >
                Apply
              </a>
              <a
                className="waves-effect waves-light btn-small blue-grey darken-1"
                style={{ marginRight: "10px" }}
              >
                More info
              </a>
            </div>
            <div className="card-reveal">
              <span className="card-title grey-text text-darken-4">
                Project 2 descriptions
                <i className="material-icons right">close</i>
              </span>
              <p>
                Here is some more information about this project that is only
                revealed once clicked on.
              </p>
            </div>
          </div>
        </div>
      </div>
    );
  }
}
export default EachProject;
