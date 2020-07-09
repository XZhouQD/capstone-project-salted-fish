import React, { Component } from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import CommentApp from "../comments/CommentApp";
import M from "materialize-css";
import { Link } from "react-router-dom";
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
    owner: null,
  };

  async componentDidMount() {
    M.AutoInit();
    const res = await axios.get("/project/" + this.props.match.params.id);
    console.log(res.data);
    this.setState({
      owner: res.data.owner,
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

  renderOwner(rid) {
    const pid = this.props.match.params.id;
    const url = "/projects/" + pid + "/role/" + rid;

    return (
      <div
        class="input-field col s4 m4 l4"
        style={{ position: "relative", top: "10px" }}
      >
        <Link to={url}>
          <button
            className="blue-grey darken-1 waves-light btn-small right"
            onClick={() => {
              this.handlebuttona();
            }}
          >
            <i className="material-icons icon left">star</i>
            change
          </button>
        </Link>
      </div>
    );
  }

  renderUser() {
    return (
      <div
        class="input-field col s4 m4 l4"
        style={{ position: "relative", top: "10px" }}
      >
        <button
          className="blue-grey darken-1 waves-light btn-small right"
          onClick={() => {
            this.handlebuttona();
          }}
        >
          <i className="material-icons icon left">done_all</i>
          {this.state.apply ? "apply" : "unapply"}
        </button>
      </div>
    );
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
        <div style={{ fontFamily: "Cherry Swash" }}>Roles Description</div>
        {this.state.roles.map((a, key) => {
          return (
            <div class="row">
              <div value={key} key={key} style={{ fontFamily: "Ubuntu" }}>
                <p>
                  <span style={{ fontFamily: "Cherry Swash" }}>ROLE</span>:{" "}
                  Project {a.title} needs {a.amount} people who have{" "}
                  {skill_list[a.skill]} skill, and experience at least{" "}
                  {a.experience} years with{" "}
                  {education_list[a.education] === "Other"
                    ? "any"
                    : education_list[a.education]}{" "}
                  degree
                </p>
              </div>
              {this.state.owner === this.props.id
                ? this.renderOwner(a.id)
                : this.renderUser()}
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
                <div
                  class="card-content"
                  style={{ fontFamily: "Cherry Swash" }}
                >
                  <p>{this.state.description}</p>
                  <button
                    className="blue-grey darken-1 waves-light btn-small right"
                    onClick={() => {
                      this.handlebutton();
                    }}
                    style={{ position: "relative", top: "-10px" }}
                  >
                    <i className="material-icons icon left">favorite</i>
                    {this.state.follow ? "follow" : "unfollow"}
                  </button>
                </div>
              </div>
            </div>
          </div>
          <ul class="collection with-header">
            {this.state.roles.length > 0 ? (
              this.renderRole()
            ) : (
              <li class="collection-header">
                <h4>The project owner has not add any roles yet</h4>
              </li>
            )}
          </ul>
          <div className="row">comment section</div>
          <CommentApp />
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  id: state.auth.id,
});

export default connect(mapStateToProps, null)(ProjectDetails);
