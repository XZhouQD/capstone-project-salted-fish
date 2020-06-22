import React from "react";
import CollaDash from "./collaDash";
import DreamerDash from "./dreamerDash";
import { connect } from "react-redux";

class Dashboard extends React.Component {
  render() {
    return <div>{1 ? <DreamerDash /> : <CollaDash />}</div>;
  }
}

export default Dashboard;
