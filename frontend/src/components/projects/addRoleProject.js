import React, { Component } from "react";
import { connect } from "react-redux";
import { Redirect } from "react-router-dom";
import M from "materialize-css";
import RoleList from "./roleList";
import AddRole from "./addRole";

class AddRoleProject extends Component {
  // state = {
  //   roles : [
  //       { title: '1', amount: 1, experience: '1', education: 1, general_enquiry :'blah', id: 1 },
  //     { title: '1', amount: 1, experience: '1', education: 1, general_enquiry :'blah', id: 2 }
  //     ]
  // }
  state = {
    roles : [
      { title: '1', amount: '1', experience: '1', education: '1', general_enquiry: '1', id: 0}
    ]
  }

   addRole = (role) => {
     let last_pos = this.state.roles.length;
     let last_id = this.state.roles[last_pos-1].id;
     role.id = last_id + 1;
     let roles = [...this.state.roles, role];
     this.setState({
       roles: roles
     })
   }

   deleteRole = (id) => {
    console.log(id);
     let roles = this.state.roles.filter(role => {
       return role.id !== id
     });
     this.setState({
       roles: roles
     });
   }

  componentDidMount() {
    // Auto initialize all the materailize css!
    M.AutoInit();
  }

  onChange = (e) => {
    this.setState({ [e.target.id]: e.target.value });
  };

  onSubmit = (e) => {
    e.preventDefault();
  };
  render() {
    // const { auth } = this.props;
    // if (!auth.uid) return <Redirect to="/signin" />;
    return (
        <div className="container">
          <div className="card blue-grey darken-1">
            <div className="card-content white-text">
              <span className="card-title">Project Title</span>
              <p>
                I am a very simple card. I am good at containing small bits of
                information. I am convenient because I require little markup to
                use effectively. project title
              </p>
            </div>
          </div>

          <div className="test">
              <RoleList roles={this.state.roles} deleteRole={this.deleteRole} />
              <AddRole addRole={this.addRole}/>
          </div>

          <br/>
        </div>
    );
  }
}

export default AddRoleProject;
