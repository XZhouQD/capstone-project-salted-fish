import React, { Component } from "react";
import axios from "axios";

export default class CommentForm extends Component {
  constructor(props) {
    super(props);
    this.state = {
      loading: false,
      error: "",

      comment: {
        message: ""
      }
    };

    // bind context to methods
    this.handleFieldChange = this.handleFieldChange.bind(this);
    this.onSubmit = this.onSubmit.bind(this);
  }

  /**
   * Handle form input field changes & update the state
   */
  handleFieldChange = event => {
    const { value, name } = event.target;

    this.setState({
      ...this.state,
      comment: {
        ...this.state.comment,
        [name]: value
      }
    });
  };

  /**
   * Form submit handler
   */
  async onSubmit(e) {
    // prevent default form submission
    e.preventDefault();

    if (!this.isFormValid()) {
      this.setState({ error: "All fields are required." });
      return;
    }

    // loading status and clear error
    this.setState({ error: "", loading: true });

    // persist the comments on server
    let { comment } = this.state;
    console.log(comment)
    const a = localStorage.getItem("token");
    const config = {
    headers: {
      "Content-Type": "application/json;charset=UTF-8",
      "Access-Control-Allow-Origin": "*",
      "AUTH-KEY": a,
    }}
    const parent_id = 0
    const discuss_content = comment.message
    const body = JSON.stringify({
      "parent_id":parent_id,
      "discuss_content":discuss_content
    });
    console.log(body)
    const res = await axios.post("/project/16/discussion",body,config)
console.log(res.data)
    this.props.addComment(comment);
    this.setState({
      loading: false,
      comment: { ...comment, message: discuss_content}
    });
   
      
  }

  /**
   * Simple validation
   */
  isFormValid() {
    return this.state.comment.name !== "" && this.state.comment.message !== "";
  }


  render() {
    return (
      <React.Fragment>
        <div className='comment-input'>
        <div className='input-field'>
        <form method="post" onSubmit={this.onSubmit}>
          <div className="comment-field-input">
            <textarea
              onChange={this.handleFieldChange}
              value={this.state.comment.message}
              className="materialize-textarea"
              placeholder="Your Comment"
              name="message"
              rows="5"
            />
          </div>
          

         

          <div className="">
            <button disabled={this.state.loading} className="btn-small blue-grey lighten-1 right" style={{marginBottom:"10px"}}>
              Comment &#10148;
            </button>
          </div>
        </form>
        </div>
        </div>
        
      </React.Fragment>
    );
  }
}
