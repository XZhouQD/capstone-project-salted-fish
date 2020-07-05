import React, { Component } from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import M from "materialize-css";

import axios from "axios";

class ProjectDetails extends Component {
  constructor() {
    super();
    this.handlebutton = this.handlebutton.bind(this);
  }

  state = {
    role: [],
    follow: true,
    apply: true,
  };

  async componentDidMount() {
    M.AutoInit();
    const res = await axios.get("/project/" + this.props.match.params.id);
    console.log(res.data);
  }

  handlebutton() {
    this.setState({ follow: !this.state.follow });
  }

  handlebuttona() {
    this.setState({ apply: !this.state.apply });
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
                  <span class="card-title">卡片标题</span>
                  <a class="btn-floating halfway-fab waves-effect waves-light red">
                    <i class="material-icons">add</i>
                  </a>
                </div>
                <div class="card-content">
                  <p>
                    我是一个很简单的卡片。我很擅长于包含少量的信息。我很方便，因为我只需要一个小标记就可以有效地使用。
                  </p>
                  <button
                    className="blue-grey darken-1 waves-light btn-small right"
                    onClick={() => {
                      this.handlebutton();
                    }}
                    style={{ paddingBottom: "10px" }}
                  >
                    <i className="material-icons left">favorite</i>
                    {this.state.follow ? "follow" : "unfollow"}
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div class="row">
            <div class="input-field col s8 m4 l8">
              <select multiple>
                <option value="" disabled selected>
                  Choose your option
                </option>
                <option value="1">选项 1</option>
                <option value="2">选项 2</option>
                <option value="3">选项 3</option>
              </select>
              <label>Materialize多选下拉列表</label>
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
          <div className="row">comment section</div>
        </div>
      </div>
    );
  }
}
export default ProjectDetails;
