import React, { Component } from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import M from "materialize-css";

class ProjectDetails extends Component {
    componentDidMount() {
        // Auto initialize all the materailize css!
        M.AutoInit();
    }

    render() {
        // const { auth } = this.props;
        // if (!auth.uid) return <Redirect to="/signin" />;
        return (
            <div>
                <div className="container">
                    <br/>
                    <div className="divider"></div>
                    <div className="section">
                        <h5>Project title</h5>
                        <p>related topics provided by the owner</p>
                    </div>
                    <div className="divider"></div>
                    <div className="section">
                        <h5>Descriptions</h5>
                        <p>This is the whole descriptions provided by the owner</p>
                    </div>
                    <div className="divider"></div>
                    <div className="section">
                        <h5>Roles Required</h5>
                        <table className="striped responsive-table">
                            <thead>
                            <tr>
                                <th>Role</th>
                                <th>Experience</th>
                                <th>Comment</th>
                                <th></th>
                            </tr>
                            </thead>

                            <tbody>
                            <tr>
                                <td>Skill_A</td>
                                <td>1 year</td>
                                <td>NA</td>
                                <td><a className="blue-grey darken-1 waves-effect waves-light btn">apply</a></td>
                            </tr>
                            <tr>
                                <td>Skill_B</td>
                                <td>2 year</td>
                                <td>NA</td>
                                <td><a className="blue-grey darken-1 waves-effect waves-light btn">apply</a></td>
                            </tr>
                            <tr>
                                <td>Skill_C</td>
                                <td>3 year</td>
                                <td>NA</td>
                                <td><a className="blue-grey darken-1 waves-effect waves-light btn">apply</a></td>
                            </tr>
                            </tbody>
                        </table>
                        <br/><br/>
                        <a className="blue-grey darken-1 waves-effect waves-light btn right"><i
                            className="material-icons left">favorite</i>follow</a>
                    </div>
                </div>
            </div>

        );
    }
}
export default ProjectDetails;
