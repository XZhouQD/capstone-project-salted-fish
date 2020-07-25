import React, { Component } from "react";
import { connect } from "react-redux";
import { getProject, searchProject } from "../../actions/projects";
import M from "materialize-css";
import AdminEachProject from "../projects/adminEachProject";

class AdminDash extends Component {


  constructor(props) {
    super(props);
    this.handleonChange = this.handleonChange.bind(this);
    this.handleonSubmit = this.handleonSubmit.bind(this);
  }

  componentWillMount() {
    this.props.getProject();
  }

  componentDidMount() {
    // Auto initialize all the materailize css!
    M.AutoInit();
  }

  handleonChange = (e) => {
    // get target element name
    this.setState({ [e.target.name]: e.target.value });
  };

  handleonSubmit = (e) => {
    e.preventDefault();
    const { description, category, order_by, sorting } = this.state;
    console.log(this.state);
    this.props.searchProject({ description, category, order_by, sorting });
  };

  render() {
    return (
      <div>
        <div className="container" style={{ marginTop: "20px" }}>
          <div className="flexLayout">
            {this.props.ProjectLists.map((each, index) => {
              console.log(each)
              return (
                  <div>
                    <AdminEachProject
                        title={each.title}
                        category={each.category}
                        description={each.description}
                        isHidden={each.is_hidden}
                        id={each.id}
                    />
                  </div>

              );
            })}
          </div>
        </div>
      </div>
    );
  }
}

const mapStateToProps = (state) => ({
  isAuthenticated: state.auth.isAuthenticated,
  ProjectLists: state.project.ProjectLists,
});

export default connect(mapStateToProps, { getProject, searchProject })(
  AdminDash
);
