import React, { useState } from "react";
import M from "materialize-css";
import { Redirect } from "react-router-dom";
import { Link } from "react-router-dom";
import axios from "axios";
import DreamerOwnProject from "./dreamerOwnProject";

class DreamerDash extends React.Component {
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

    const res = await axios.get("/dreamer/my_projects", config);
    console.log(res.data);
    this.setState({ myProjects: res.data.projects });
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
    return (
      <div>
        <header>
          <div class="navbar-fixed" style={{ position: "fixed" }}>
            <a href="#" data-target="nav-mobile" class="sidenav-trigger">
              <i class="material-icons">menu</i>
            </a>
          </div>
          <div>
            <ul
              id="nav-mobile"
              class="sidenav sidenav-fixed"
              style={{ position: "fixed" }}
            >
              <li class="bold">
                <Link class="waves-effect waves-teal" to="./dashboard">
                  My Projects
                </Link>
              </li>
              <li class="bold">
                <a href="#" class="waves-effect waves-teal">
                  <Link class="waves-effect waves-teal" to="./drecommend">
                    Recommend Collaborators
                  </Link>
                </a>
              </li>

              <li class="bold">
                <a href="#" class="waves-effect waves-teal">
                  <Link class="waves-effect waves-teal" to="./drecommend">
                    Followed collaborators
                  </Link>
                </a>
              </li>

              <li class="bold">
                <a href="#" class="waves-effect waves-teal">
                  <Link class="waves-effect waves-teal" to="./drecommend">
                    My Info
                  </Link>
                </a>
              </li>

              <div class="logo">
                <h3>Logo</h3>
              </div>
            </ul>
          </div>
        </header>

        <main>
          <div class="container">
            <div class="row">
              <div class="col s12 l12 dashboard">
                <div class="card grey lighten-3">
                  <div class="card-content posts">
                    <nav class="pink darken-1">
                      <div class="nav-wrapper">
                        <h4 class="left event-title">EVENTS</h4>
                        <form class="search-field right">
                          <div class="input-field">
                            <input id="search" type="search" required />
                            <label class="label-icon search-icon" for="search">
                              <i class="material-icons">search</i>
                            </label>
                            <i class="material-icons close-icon">close</i>
                          </div>
                        </form>
                      </div>
                    </nav>
                    {this.state.myProjects.length > 0
                      ? this.state.myProjects.map((each, index) => {
                          return (
                            <DreamerOwnProject
                              key={index}
                              title={each.title}
                              description={each.description}
                              category={category_list[each.category]}
                              id={each.id}
                            />
                          );
                        })
                      : "loading"}
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

export default DreamerDash;
