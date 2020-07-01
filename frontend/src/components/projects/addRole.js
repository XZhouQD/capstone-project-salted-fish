import React, { Component } from 'react'

class AddRole extends Component {
    state={
        title: null,
        amount: null,
        experience: null,
        education: null,
        general_enquiry: null
    }

    handleChange = (e) => {
        this.setState({
            [e.target.id]: e.target.value
        })
    }

    handleSubmit = (e) =>{
        e.preventDefault();
        this.props.addRole({title: this.state.title, amount: this.state.amount, experience: this.state.experience,
        education: this.state.education, general_enquiry: this.state.general_enquiry});
    }

    render() {
        return(
        <div>
            <div className="divider"></div>
            <form onSubmit={this.handleSubmit}>
                <table className="responsive-table">
                    <thead>
                    <tr>
                        <th>Title</th>
                        <th>Amount</th>
                        <th>Experience</th>
                        <th>Education</th>
                        <th>General enquiry</th>
                        <th></th>
                    </tr>
                    </thead>
                    <tbody>
                    <tr>
                        <td>
                            <div className="input-field" >
                                <select
                                    onChange={this.handleChange} required
                                    name="skills" id="title"
                                >
                                    <option value="" disabled>
                                        Choose your option
                                    </option>
                                    <option value="1">UI designer</option>
                                    <option value="2">Backend engineer</option>
                                    <option value="3">Frontend engineer</option>
                                    <option value="4">AI engineer</option>
                                    <option value="5">Big data development engineer</option>
                                    <option value="6">Data analysis engineer</option>
                                </select>
                            </div>
                        </td>
                        <td>
                            <div className="input-field">
                                <input onChange={this.handleChange} required
                                       name="amount" id="amount"
                                       placeholder="Input Amount"/>
                            </div>
                        </td>
                        <td>
                            <div className="input-field">
                                <input onChange={this.handleChange} required
                                       name="experience" id="experience"
                                       placeholder="Input Years"/>
                            </div>
                        </td>

                        <td>
                            <div className="input-field">
                                <select
                                    onChange={this.handleChange} required
                                    name="education" id="education"
                                >
                                    <option value="" disabled>
                                        Choose your option
                                    </option>
                                    <option value="1">Other</option>
                                    <option value="2">Bachelor</option>
                                    <option value="3">Master</option>
                                    <option value="4">Phd</option>
                                </select>
                            </div>
                        </td>
                        <td>
                            <div className="input-field">
                                <input onChange={this.handleChange}
                                       name="education" id="general_enquiry"
                                       placeholder="General enquiry"/>
                            </div>
                        </td>
                        <td>
                            <button className="btn-small waves-effect waves-light blue-grey darken-1 right">
                                <i className="material-icons">add</i>
                            </button>
                        </td>
                    </tr>
                    </tbody>
                </table>
            </form>
            {/*<form onSubmit={this.handleSubmit}>*/}
            {/*    <label htmlFor="title">Title: </label>*/}
            {/*    <div className="input-field" id="title"  >*/}
            {/*        <select*/}
            {/*            onChange={this.handleChange}*/}
            {/*            name="skills" id="title"*/}
            {/*        >*/}
            {/*            <option value="" disabled>*/}
            {/*                Choose your option*/}
            {/*            </option>*/}
            {/*            <option value="1">UI designer</option>*/}
            {/*            <option value="2">Backend engineer</option>*/}
            {/*            <option value="3">Frontend engineer</option>*/}
            {/*            <option value="4">AI engineer</option>*/}
            {/*            <option value="5">Big data development engineer</option>*/}
            {/*            <option value="6">Data analysis engineer</option>*/}
            {/*        </select>*/}
            {/*    </div>*/}
            {/*    <div className="input-field">*/}
            {/*        <input onChange={this.handleChange}*/}
            {/*               name="amount" id="amount"*/}
            {/*               placeholder="Input Amount"/>*/}
            {/*    </div>*/}
            {/*    <div className="input-field">*/}
            {/*        <input onChange={this.handleChange}*/}
            {/*               name="experience" id="experience"*/}
            {/*               placeholder="Input Years"/>*/}
            {/*    </div>*/}
            {/*    <div className="input-field">*/}
            {/*        <select*/}
            {/*            onChange={this.handleChange}*/}
            {/*            name="education" id="education"*/}
            {/*        >*/}
            {/*            <option value="" disabled>*/}
            {/*                Choose your option*/}
            {/*            </option>*/}
            {/*            <option value="1">Other</option>*/}
            {/*            <option value="2">Bachelor</option>*/}
            {/*            <option value="3">Master</option>*/}
            {/*            <option value="4">Phd</option>*/}
            {/*        </select>*/}
            {/*    </div>*/}
            {/*    <div className="input-field">*/}
            {/*        <input onChange={this.handleChange}*/}
            {/*               name="education" id="general_enquiry"*/}
            {/*               placeholder="General enquiry"/>*/}
            {/*    </div>*/}
            {/*    <button>add</button>*/}
            {/*</form>*/}
        </div>
        )
    }
}

export default AddRole;