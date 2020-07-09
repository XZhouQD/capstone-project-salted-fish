import React, { Component } from 'react'
import M from "materialize-css";

class Comment extends Component {

    componentDidMount() {
        // Auto initialize all the materailize css!
        M.AutoInit();
    }

    render () {
        return (
            <ul className="collection">
                <li className="collection-item avatar">
                    <i className="material-icons circle">person</i>
                    <span className="title blue-text">{this.props.comment.username} </span>
                    <p>{this.props.comment.content}</p>
                </li>
            </ul>
        )
    }
}

export default Comment