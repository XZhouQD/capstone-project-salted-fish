import React from "react";


const RoleList = ({roles, deleteRole}) => {
    return (
        <div className="role-list">
            {
                roles.map(role => {
                    return (
                        <div className="ninja" key={role.id}>
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
                                    <td>{ role.title }</td>
                                    <td>{ role.amount }</td>
                                    <td>{ role.experience }</td>
                                    <td>{ role.education }</td>
                                    <td>{ role.general_enquiry }</td>
                                    <td><button onClick={() => {deleteRole(role.id)}}
                                                className="btn-small waves-effect waves-light blue-grey darken-1 right">
                                        <i className="material-icons">remove</i>
                                    </button></td>
                                </tr>
                                </tbody>
                            </table>
                        </div>
                    )
                })
            }
        </div>
    );
}

export default RoleList;