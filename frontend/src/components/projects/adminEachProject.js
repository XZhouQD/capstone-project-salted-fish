import React, { Component } from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import M from "materialize-css";

class HideButton extends Component {
    constructor () {
        super()
        this.state = { isHide: false }
    }

    handleClickOnLikeButton () {
        this.setState({
            isHide: !this.state.isHide
        })
    }

    render () {
        const hideButton = <a
            className="waves-effect waves-light btn-small"
            style={{ marginRight: "5px" }}
        >
            hide
        </a>
        const unhideButton = <a
            className="waves-effect waves-light btn-small grey"
            style={{ marginRight: "5px" }}
        >
            reveal
        </a>

        return (
            <div className="card-action" onClick={this.handleClickOnLikeButton.bind(this)}>
                {this.state.isHide ? unhideButton : hideButton}
            </div>
        )
    }
}

class AdminEachProject extends Component {
<<<<<<< HEAD
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
      <div
        className="card panel-up"
        style={{ width: "20em", marginLeft: "20px", marginRight: "10px" }}
      >
        <div className="card-image waves-effect waves-block waves-light"></div>
        <div className="card-content">
=======

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
            <div
                className="card panel-up"
                style={{ width: "20em", marginLeft: "20px", marginRight: "10px" }}
            >
                <div className="card-image waves-effect waves-block waves-light"></div>
                <div className="card-content">
>>>>>>> origin
          <span className="card-title activator grey-text text-darken-4">
            {this.props.title}
            <i className="material-icons right">more_vert</i>
          </span>
<<<<<<< HEAD
          <p className="truncate">
            Category: {categoryList[this.props.category]}
          </p>
          <p className="truncate">Description: {this.props.description}</p>
        </div>
        <div className="card-action">
          <a
            className="waves-effect waves-light btn-small"
            style={{ marginRight: "5px" }}
          >
            hide
          </a>
        </div>
        <div className="card-reveal">
=======
                    <p className="truncate">
                        Category: {categoryList[this.props.category]}
                    </p>
                    <p className="truncate">Description: {this.props.description}</p>
                </div>
                    <HideButton />
                <div className="card-reveal">
>>>>>>> origin
          <span className="card-title grey-text text-darken-4">
            {this.props.title}
            <i className="material-icons right">close</i>
          </span>
          <p>Description: {this.props.description}</p>
        </div>
      </div>
    );
  }
}
export default AdminEachProject;
