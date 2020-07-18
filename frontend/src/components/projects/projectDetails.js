import React, { Component } from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import { Modal, Button } from "react-materialize";
import ReactApp from "../../com/ReactApp";
import M from "materialize-css";
import { Link } from "react-router-dom";
import axios from "axios";
import { applyRole } from "../../actions/projects";
import GetApplications from "./getApplications";
import { setAlert } from "../../actions/alert";
class ProjectDetails extends Component {
  constructor() {
    super();
  }

  state = {
    roles: [],
    description: "",
    category: 0,
    title: "",
    owner: null,
    general_text: "",
    follow: true,
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
  async handleFollow(e) {
    const a = localStorage.getItem("token");
    const config = {
      headers: {
        "Content-Type": "application/json;charset=UTF-8",
        "Access-Control-Allow-Origin": "*",
        "AUTH-KEY": a,
      },
    };

    const id = this.props.match.params.id;
    // get target element name
    const followUrl = "/project/" + id + "/follow";
    const unfollowUrl = "/project/" + id + "/unfollow";
    this.setState({ follow: !this.state.follow });
    if (this.state.follow) {
      const res = await axios.get(followUrl, config);
      console.log(res);
      this.props.setAlert(res.data.message);
    } else {
      const res = await axios.get(unfollowUrl, config);
      this.props.setAlert(res.data.message);
    }
  }

  handleonChange = (e) => {
    // get target element name
    this.setState({ [e.target.name]: e.target.value });
  };

  handleonSubmit = (e, rid) => {
    e.preventDefault();
    const { general_text } = this.state;
    const pid = this.props.match.params.id;
    this.props.applyRole({ general_text, pid, rid });
  };

  renderOwner(rid) {
    const pid = this.props.match.params.id;
    const url = "/project/" + pid + "/role/" + rid;
    const url1 = "/project/" + pid + "/role/" + rid + "/applications";
    return (
      <div>
        <Link to={url} style={{ marginRight: "10px" }}>
          <button className="btn-small">
            <i className="material-icons icon left">star</i>
            change
          </button>
        </Link>
        <Modal
          trigger={
            <Button className="btn-small">
              <i className="material-icons icon left">done_all</i>
              application
            </Button>
          }
        >
          <GetApplications url_1={url1} rid={rid} pid={pid} />
        </Modal>
      </div>
    );
  }

  renderUser(rid) {
    return (
      <Modal
        trigger={
          <Button className="blue-grey darken-1 waves-light btn-small right">
            <i className="material-icons icon left">done_all</i>
            apply
          </Button>
        }
      >
        <form className="col s12" onSubmit={(e) => this.handleonSubmit(e, rid)}>
          <div className="input-field ">
            <input
              placeholder="Say HI"
              type="text"
              name="general_text"
              onChange={(e) => this.handleonChange(e)}
              required
            />
            <label htmlFor="title">Send the apply message!</label>
          </div>
          <input
            type="submit"
            className="btn-small left"
            value="send"
            style={{ marginTop: "38px" }}
          />
        </form>
      </Modal>
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
      <div className="collection-item">
        {this.state.roles.map((a, key) => {
          return (
            <p key={key} style={{ fontFamily: "Ubuntu" }}>
              <span style={{ fontFamily: "Cherry Swash" }}>ROLE</span>: Project{" "}
              {a.title} needs {a.amount} people who have {skill_list[a.skill]}{" "}
              skill, and experience at least {a.experience} years with{" "}
              {education_list[a.education] === "Other"
                ? "any"
                : education_list[a.education]}{" "}
              degree
              {this.state.owner === this.props.id
                ? this.renderOwner(a.id)
                : this.renderUser(a.id)}
            </p>
          );
        })}
      </div>
    );
  }
  render() {
    const url = "https://source.unsplash.com/collection/45/1600*900";
    const pid = this.props.match.params.id;
    return (
      <div>
        <div className="container">
          <div className="row">
            <div className="col s12 m12 l12">
              <div className="card">
                <div className="card-image">
                  <img src={url} width="650" />
                  <span className="card-title">{this.state.title}</span>
                  <a className="btn-floating halfway-fab waves-effect waves-light red">
                    <i className="material-icons">add</i>
                  </a>
                </div>
                <div
                  className="card-content"
                  style={{ fontFamily: "Cherry Swash" }}
                >
                  <p>{this.state.description}</p>

                  <button
                    className="blue-grey darken-1 waves-light btn-small right"
                    style={{ position: "relative", top: "-10px" }}
                    onClick={(e) => this.handleFollow(e)}
                  >
                    <i className="material-icons icon left">favorite</i>
                    {this.state.follow ? "follow" : "unfollow"}
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div className="collection">
            {this.state.roles.length > 0
              ? this.renderRole()
              : "The project owner has not add any roles yet"}
          </div>

          <ReactApp id={pid} />
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  id: state.auth.id,
  applySuccess: state.project.payload,
});

export default connect(mapStateToProps, { applyRole, setAlert })(
  ProjectDetails
);
