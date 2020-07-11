import React, { Component } from "react";
import { connect } from "react-redux";
import { getCollaProject } from "../../actions/projects";
import M from "materialize-css";
import CollaEachProject from "../projects/collaEachProject";

class CollaProjectList extends Component {

    constructor(props) {
        super(props);
        this.handleonChange = this.handleonChange.bind(this);
        this.handleonSubmit = this.handleonSubmit.bind(this);
    }

    componentWillMount() {
        this.props.getCollaProject();
        console.log("TEST",this.props.ProjectLists)
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
                <div className="container" style={{marginTop: "20px"}}>
                    <div className="flexLayout">
                        <h1>TEST!</h1>
                        {this.props.ProjectLists.map((each, index) => {
                            return (
                                <CollaEachProject
                                    title={each.title}
                                    category={each.category}
                                    description={each.description}
                                />
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
    ProjectLists: state.project.CollarLists,
});

export default connect(mapStateToProps, { getCollaProject })(
    CollaProjectList
);
