import React, { Component } from 'react'
import M from "materialize-css";

class CommentInput extends Component {
    constructor () {
        super()
        this.state = {
            username: '',
            content: ''
        }
    }

    handleUsernameChange (event) {
        this.setState({
            username: event.target.value
        })
    }

    handleContentChange (event) {
        this.setState({
            content: event.target.value
        })
    }

    handleSubmit () {
        if (this.props.onSubmit) {
            const { username, content } = this.state
            this.props.onSubmit({username, content})
        }
        this.setState({ content: '' })
    }

    componentDidMount() {
        // Auto initialize all the materailize css!
        M.AutoInit();
    }

    render () {
        return (
            <div className='comment-input'>
                <div className='input-field'>
                    <div
                        className='comment-field-input'>
                        <input placeholder="Username" type="text"
                            value={this.state.username}
                        onChange={this.handleUsernameChange.bind(this)}/>
                    </div>
                </div>
                <div className='input-field'>
                    <div className='comment-field-input'>
                        <textarea
                            className="materialize-textarea"
                            placeholder="Comments" type="text"
                            value={this.state.content}
                            onChange={this.handleContentChange.bind(this)} />
                    </div>
                </div>
                <div className='comment-field-button'>
                    <button className="btn waves-effect waves-light blue-grey darken-1 right" type="submit"
                        onClick={this.handleSubmit.bind(this)}>
                        submit
                    </button>
                </div>
            </div>
        )
    }
}

export default CommentInput