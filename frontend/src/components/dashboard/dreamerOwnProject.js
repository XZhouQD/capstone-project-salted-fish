import React from "react";
import { Link } from "react-router-dom";

class DreamerOwnProject extends React.Component {
  render() {
    const url =
      "https://source.unsplash.com/collection/" +
      Math.floor(Math.random() * 100);

    const projectDetails = "/projects/" + this.props.id;
    return (
      <div class="card medium event-card">
        <div class="card-image">
          <img src={url} alt="banner" />
        </div>
        <div class="card-content">
          <div class="card-title">
            <b>{this.props.title}</b>
          </div>
          <div class="left">
            <p>
              <Link to={projectDetails}>View Details</Link>
            </p>
            <p>create project time: {this.props.create_time.split(" ")[0]}</p>
          </div>
          <div class="right-align">
            <button class="waves-effect waves-light btn">
              <i class="material-icons left">add</i>Join
            </button>
            <p>
              <b>category:</b> {this.props.category}
            </p>
          </div>
        </div>
      </div>
    );
  }
}

export default DreamerOwnProject;
