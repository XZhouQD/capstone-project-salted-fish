import React, { Component } from 'react'
import CommentInput from './CommentInput'
import CommentList from './CommentList'
import M from "materialize-css";

class CommentApp extends Component {
    constructor () {
        super()
        this.state = {
            comments: []
        }
    }

    componentDidMount() {
        // Auto initialize all the materailize css!
        M.AutoInit();
    }

    handleSubmitComment (comment) {
        if (!comment) return
        if (!comment.content) return alert('Please enter your comments')
        this.state.comments.push(comment)
        this.setState({
            comments: this.state.comments
        })
    }

    render() {
        return (
            <div>
                <CommentInput onSubmit={this.handleSubmitComment.bind(this)} />
                <br/>
                <br/>
                <CommentList comments={this.state.comments}/>
            </div>
        )
    }
}

export default CommentApp