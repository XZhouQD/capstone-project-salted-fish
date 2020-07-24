import React from "react";
import CollaNav from "./collaNav";
import DreamerNav from "./dreamerNav";
import { connect } from "react-redux";
import adminDash from "../dashboard/adminDash";

const AfterAuthNarvbar = (props) => {
  const { isDreamerOrCollaOrAdmin } = props;
  if (isDreamerOrCollaOrAdmin === "Dreamer") {
    return (
      <div>
        <DreamerNav />
      </div>
    );
  } else if (isDreamerOrCollaOrAdmin === "Collaborator") {
    return (
      <div>
        <CollaNav />
      </div>
    );
  } else {
    // admin
    return(
        <div>
          <adminDash />
        </div>
    );
  }
};

const mapStateToProps = (state) => ({
  isDreamerOrCollaOrAdmin: state.auth.role,
});

export default connect(mapStateToProps, null)(AfterAuthNarvbar);
