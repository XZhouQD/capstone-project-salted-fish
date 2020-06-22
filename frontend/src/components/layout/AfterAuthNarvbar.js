import React from "react";
import CollaNav from "./collaNav";
import DreamerNav from "./dreamerNav";

const AfterAuthNarvbar = () => {
  return (
    // check dreamer or collaborator
    <div>{1 ? <DreamerNav /> : <CollaNav />}</div>
  );
};

export default AfterAuthNarvbar;
