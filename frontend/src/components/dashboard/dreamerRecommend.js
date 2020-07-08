import React, { useState } from "react";
import M from "materialize-css";
import { Redirect } from "react-router-dom";
import { Link } from "react-router-dom";
import axios from "axios";

class DreamerRecommend extends React.Component {
  constructor() {
    super();
  }

  state = {
    drecommend: [],
  };

  async componentDidMount() {
    M.AutoInit();
    const a = localStorage.getItem("token");

    const config = {
      headers: {
        "Content-Type": "application/json;charset=UTF-8",
        "Access-Control-Allow-Origin": "*",
        "AUTH-KEY": a,
      },
    };

    const res = await axios.get("/dreamer/recommendation", config);
    console.log(res.data);
    var b = res.data.project_role_collaborator;

    this.setState({ drecommend: res.data.project_role_collaborator });
  }

  render() {
    const url =
      "https://source.unsplash.com/collection/" +
      Math.floor(Math.random() * 100) +
      "/800x600";

    return (
      <div>
        <header>
          <div className="navbar-fixed" style={{ position: "fixed" }}>
            <Link
              data-target="nav-mobile"
              className="sidenav-trigger"
              style={{ zIndex: 1 }}
            >
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
                <Link className="waves-effect waves-teal" to="./dashboard">
                  My Projects
                </Link>
              </li>
              <li className="bold">
                <Link className="waves-effect waves-teal" to="./drecommend">
                  Recommend Collaborators
                </Link>
              </li>

              <li className="bold">
                <Link className="waves-effect waves-teal" to="./drecommend">
                  Followed collaborators
                </Link>
              </li>

              <li className="bold">
                <Link className="waves-effect waves-teal" to="./drecommend">
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
                        <h4 className="left event-title">RECOMMENDATION</h4>
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

                    <div className="col s12 m12 l12">
                      <div className="card horizontal small">
                        <div className="card-stacked">
                          <div
                            className="card-content"
                            style={{ overflowY: "scroll" }}
                          >
                            <p>11111</p>

                            <div className="collection card-content">
                              <a href="#!" className="collection-item">
                                白菜
                              </a>
                              <a href="#!" className="collection-item active">
                                青菜
                              </a>
                              <a href="#!" className="collection-item">
                                萝卜
                              </a>
                              <a href="#!" className="collection-item">
                                土豆
                              </a>
                            </div>
                            <div className="collection card-content">
                              <a href="#!" className="collection-item">
                                白菜
                              </a>
                              <a href="#!" className="collection-item active">
                                青菜
                              </a>
                              <a href="#!" className="collection-item">
                                萝卜
                              </a>
                              <a href="#!" className="collection-item">
                                土豆
                              </a>
                            </div>
                          </div>
                        </div>

                        <div className="card-image right">
                          <img src={url} />
                        </div>
                      </div>
                    </div>
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

export default DreamerRecommend;
