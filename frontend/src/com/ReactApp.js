import React, { Component } from "react";
import CommentList from "./ReactCommentList";
import CommentForm from "./ReactCommentForm";
import M from "materialize-css";
import axios from "axios";

class ReactApp extends Component {
  constructor(props) {
    super(props);

    this.state = {
      comments: [],
      loading: false
    };

    this.addComment = this.addComment.bind(this);
  }

  async componentDidMount() {
    // loading
    M.AutoInit();
    const a = localStorage.getItem("token");
    this.setState({ loading: true });
    const config = {
      headers: {
        "Content-Type": "application/json;charset=UTF-8",
        "Access-Control-Allow-Origin": "*",
        "AUTH-KEY": a,
      }}


    const res = await axios.get("/project/16/discussions",config);
    console.log(res)
    this.setState({
      comments: res.data,
      loading: false
    });
  
  }

  /**
   * Add new comment
   * @param {Object} comment
   */
  addComment(comment) {
    console.log(comment)
    this.setState({
      loading: false,
      comments: [comment, ...this.state.comments]
    });
  }

  render() {

    return (
      <div className="App container light shadow">
        <div className="row">
          <div className="col-4  pt-3 border-right">
            <h6>Say something about React</h6>
            <CommentForm addComment={this.addComment} />
          </div>
          <div className="col-8  pt-3 bg-white">
            <CommentList
              loading={this.state.loading}
              comments={this.state.comments}
            />
          </div>
        </div>
      </div>
    );
  }
}

export default ReactApp ;
