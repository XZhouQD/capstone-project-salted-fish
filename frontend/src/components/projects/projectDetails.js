import React, { Component } from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import CommentApp from "../comments/CommentApp";
import M from "materialize-css";

import axios from "axios";

class ProjectDetails extends Component {
  constructor() {
    super();
    this.handlebutton = this.handlebutton.bind(this);
  }

  state = {
    roles: [],
    follow: true,
    apply: true,
    description: "",
    category: 0,
    title: "",
  };

  async componentDidMount() {
    M.AutoInit();
    const res = await axios.get("/project/" + this.props.match.params.id);
    console.log(res.data);
    this.setState({
      roles: res.data.roles,
      category: res.data.category,
      title: res.data.title,
      description: res.data.description,
    });
  }

  handlebutton() {
    this.setState({ follow: !this.state.follow });
  }

  handlebuttona() {
    this.setState({ apply: !this.state.apply });
  }

  renderRole() {
    const skill_list = [
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
    ];

    const education_list = ["Other", "Bachelor", "Master", "Phd"];
    return (
      <div>
        <div>Needed roles table</div>
        {this.state.roles.map((a, key) => {
          return (
            <div class="row">
              <div class="input-field col s8 m4 l8" value={key} key={key}>
                {a.title} {a.amount}people {education_list[a.education]}{" "}
                {skill_list[a.skill]} {a.experience}years
              </div>

              <div class="input-field col s4 m4 l4">
                <button
                  className="blue-grey darken-1 waves-light btn-small right"
                  onClick={() => {
                    this.handlebuttona();
                  }}
                >
                  <i className="material-icons left">favorite</i>
                  {this.state.apply ? "apply" : "unapply"}
                </button>
              </div>
            </div>
          );
        })}
      </div>
    );
  }
  render() {
    // const { auth } = this.props;
    // if (!auth.uid) return <Redirect to="/signin" />;
    return (
      <div>
        <div className="container">
          <div class="row">
            <div class="col s12 m12 l12">
              <div class="card">
                <div class="card-image">
                  <img src="https://source.unsplash.com/collection/12" />
                  <span class="card-title">{this.state.title}</span>
                  <a class="btn-floating halfway-fab waves-effect waves-light red">
                    <i class="material-icons">add</i>
                  </a>
                </div>
                <div class="card-content">
                  <p>{this.state.description}</p>
                  <button
                    className="blue-grey darken-1 waves-light btn-small right"
                    onClick={() => {
                      this.handlebutton();
                    }}
                  >
                    <i className="material-icons left">favorite</i>
                    {this.state.follow ? "follow" : "unfollow"}
                  </button>
                </div>
              </div>
            </div>
          </div>

          {this.state.roles.length > 0
            ? this.renderRole()
            : "The project owner has not add any roles yet"}

          <div className="row">comment section</div>
          <CommentApp />
        </div>
      </div>
    );
  }
}
export default ProjectDetails;
