import React, { Component } from 'react'
import Comment from './Comment'
import M from "materialize-css";

class CommentList extends Component {
    static defaultProps = {
        comments: []
    }

    componentDidMount() {
        // Auto initialize all the materailize css!
        M.AutoInit();
    }

    render() {
        return (
            <div>
                {this.props.comments.map((comment, i) =>
                    <Comment comment={comment} key={i} />
                )}
            </div>
        )
    }
}

export default CommentList