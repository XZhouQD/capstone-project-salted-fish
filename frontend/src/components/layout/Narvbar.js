import React from "react";
import { Link } from "react-router-dom";
import BeforeAuthNarvbar from "./BeforeAuthNarvbar";
import AfterAuthNarvbar from "./AfterAuthNarvbar";
import { connect } from "react-redux";

const Narvbar = (props) => {
  const { auth, profile } = props;

  return <div>{0 ? <AfterAuthNarvbar /> : <BeforeAuthNarvbar />}</div>;
};

export default Narvbar;
