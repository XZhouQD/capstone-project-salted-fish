import React, { useState } from "react";
import M from "materialize-css";

class DreamerDash extends React.Component {
  constructor() {
    super();
  }
  componentDidMount() {
    // Auto initialize all the materailize css!
    M.AutoInit();
  }

  render() {
    return (
      <div>
        <header>
          <div class="navbar-fixed" style={{ position: "fixed" }}>
            <a href="#" data-target="nav-mobile" class="sidenav-trigger">
              <i class="material-icons">menu</i>
            </a>
          </div>
          <div>
            <ul id="nav-mobile" class="sidenav sidenav-fixed">
              <li class="bold">
                <a href="#" class="waves-effect waves-teal">
                  Dashboard
                </a>
              </li>
              <li class="bold">
                <a href="#" class="waves-effect waves-teal">
                  My Events
                </a>
              </li>
              <li class="bold">
                <a href="#" class="waves-effect waves-teal">
                  Joined Events
                </a>
              </li>
              <li class="bold">
                <a href="#" class="waves-effect waves-teal">
                  My Schedule
                </a>
              </li>
              <li class="bold">
                <a
                  class="waves-effect waves-teal modal-trigger"
                  href="#calendar"
                >
                  Calendar
                </a>
              </li>
              <li class="bold">
                <a
                  class="waves-effect waves-teal modal-trigger"
                  href="#event-today"
                >
                  Events Today
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
                    <nav class="red darken-1">
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

                    <div class="card medium event-card">
                      <div class="card-image">
                        <img
                          src="https://images.pexels.com/photos/1081912/pexels-photo-1081912.jpeg?cs=srgb&dl=agriculture-bird-s-eye-view-colors-1081912.jpg&fm=jpg"
                          alt="banner"
                        />
                      </div>
                      <div class="card-content">
                        <div class="card-title">
                          <b>Event Title</b>
                        </div>
                        <div class="left">
                          <p>01/10/2019 - USA</p>
                          <p>
                            <a href="#">View Details</a>
                          </p>
                        </div>
                        <div class="right-align">
                          <button class="waves-effect waves-light btn">
                            <i class="material-icons left">add</i>Join
                          </button>
                          <p>
                            <b>Capacity: </b> 3/100
                          </p>
                        </div>
                      </div>
                    </div>
                    <div class="card medium event-card">
                      <div class="card-image">
                        <img
                          src="https://images.pexels.com/photos/1853371/pexels-photo-1853371.jpeg?cs=srgb&dl=adventure-cliff-daylight-1853371.jpg&fm=jpg"
                          alt="banner"
                        />
                      </div>
                      <div class="card-content">
                        <div class="card-title">
                          <b>Event Title</b>
                        </div>
                        <div class="left">
                          <p>01/10/2019 - USA</p>
                          <p>
                            <a href="#">View Details</a>
                          </p>
                        </div>
                        <div class="right-align">
                          <button class="waves-effect waves-light btn">
                            <i class="material-icons left">add</i>Join
                          </button>
                          <p>
                            <b>Capacity: </b> 3/100
                          </p>
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

export default DreamerDash;
