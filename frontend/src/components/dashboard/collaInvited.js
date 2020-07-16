import React, { useState } from "react";
import M from "materialize-css";
import { Redirect } from "react-router-dom";
import { Link } from "react-router-dom";
import axios from "axios";
import { acceptInvitation, declineInvitation } from "../../actions/projects";
import { connect } from "react-redux";

class CollaInvited extends React.Component {
  constructor() {
    super();
  }

  state = {
    myProjects: [],
  };

  async componentDidMount() {
    // Auto initialize all the materailize css!
    M.AutoInit();
    const a = localStorage.getItem("token");

    const config = {
      headers: {
        "Content-Type": "application/json;charset=UTF-8",
        "Access-Control-Allow-Origin": "*",
        "AUTH-KEY": a,
      },
    };

    const res = await axios.get("/collaborator/invitations", config);
    console.log("invited", res.data);
    this.setState({ myProjects: res.data.invitations });
  }

  async accept(acceptUrl) {
    this.props.acceptInvitation(acceptUrl);
  }

  async decline(declineUrl) {
    this.props.declineInvitation(declineUrl);
  }

  render() {
    const category_list = [
      "All other",
      "A web based application",
      "A desktop application",
      "A mobile application",

      "A library for other project to reference",

      "A modification to existing platform",
      "A research oriented project",
    ];
    if (!this.props.isAuthenticated) {
      return <Redirect to="/login" />;
    }
    return (
      <div>
        <header>
          <div className="navbar-fixed" style={{ position: "fixed" }}>
            <Link data-target="nav-mobile" className="sidenav-trigger">
              <i className="material-icons">menu</i>
            </Link>
          </div>
          <div>
            <ul
              id="nav-mobile"
              className="sidenav sidenav-fixed"
              style={{ position: "fixed" }}
            >
              <li className="bold">
                <Link className="waves-effect waves-teal" to="./colladash">
                  My Projects
                </Link>
              </li>
              <li className="bold">
                <Link className="waves-effect waves-teal" to="./crecommend">
                  Recommend Projects
                </Link>
              </li>

              <li className="bold">
                <Link className="waves-effect waves-teal" to="./invited">
                  Invited Projects
                </Link>
              </li>

              <li className="bold">
                <Link className="waves-effect waves-teal" to="./cinfo">
                  My Info
                </Link>
              </li>

              <div className="logo">
                <h3>Logo</h3>
              </div>
            </ul>
          </div>
        </header>

        <main>
          <div className="container">
            <div className="row">
              <div className="col s12 l12 dashboard">
                <div className="card grey lighten-3">
                  <div className="card-content posts">
                    <nav className="pink darken-1">
                      <div className="nav-wrapper">
                        <h4 className="left event-title">EVENTS</h4>
                        <form className="search-field right">
                          <div className="input-field">
                            <input id="search" type="search" required />
                            <label
                              className="label-icon search-icon"
                              for="search"
                            >
                              <i className="material-icons">search</i>
                            </label>
                            <i className="material-icons close-icon">close</i>
                          </div>
                        </form>
                      </div>
                    </nav>
                    {}
                    <div>
                      Total:{" "}
                      {this.state.myProjects && this.state.myProjects.length}{" "}
                      invitations
                    </div>
                    {this.state.myProjects &&
                      this.state.myProjects.map((each, index) => {
                        const url = "/projects/" + each.projectID;
                        const url1 = "/dreamer/" + each.Invitor;
                        return (
                          <div key={index}>
                            <br></br>
                            <div>
                              <Link to={url}>Project {each.Project_title}</Link>
                              :<br></br>
                              <Link to={url1}>{each.Invitor_name}</Link> leaves
                              his message{" "}
                              {each.Role_information.general_enquiry} and wants
                              you to join his group and role infomation as
                              below: <br></br>
                              {each.Role_information.title} needs{" "}
                              {each.Role_information.amount} people who have{" "}
                              {each.Role_information.skill} skill, and
                              experience at least{" "}
                              {each.Role_information.experience} years with{" "}
                              {each.Role_information.education === "Other"
                                ? "any"
                                : each.Role_information.education}{" "}
                              degree
                            </div>

                            <div>
                              <button
                                className="btn-small"
                                onClick={(e) => {
                                  const acceptUrl =
                                    "/project/" +
                                    each.projectID +
                                    "/role/" +
                                    each.Role_information.id +
                                    "/invitation/" +
                                    each.InvitationID +
                                    "/accept";

                                  this.accept(acceptUrl);
                                }}
                                style={{ marginRight: "10px" }}
                              >
                                accept
                              </button>
                              <button
                                className="btn-small"
                                onClick={(e) => {
                                  const declineUrl =
                                    "/project/" +
                                    each.projectID +
                                    "/role/" +
                                    each.Role_information.id +
                                    "/invitation/" +
                                    each.InvitationID +
                                    "/decline";
                                  this.decline(declineUrl);
                                }}
                              >
                                decline
                              </button>

                              <span className="right">
                                status: {each.Invitation_status}
                              </span>
                            </div>
                          </div>
                        );
                      })}
                  </div>
                </div>
              </div>
            </div>
          </div>
        </main>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
});

export default connect(mapStateToProps, {
  acceptInvitation,
  declineInvitation,
})(CollaInvited);