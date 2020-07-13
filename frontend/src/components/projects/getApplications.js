import React from "react";
import { Link } from "react-router-dom";
import M from "materialize-css";

import axios from "axios";

class GetApplication extends React.Component {
  state = {
    a: [],
  };

  async componentWillMount() {
    const a = localStorage.getItem("token");
    console.log(this.props.url_1);
    console.log(a);
    const res = await axios.get(this.props.url_1, {
      headers: {
        "AUTH-KEY": a,
      },
    });

    this.setState({ a: res.data.applications });
  }
  render() {
    return (
      <div>
        {this.state.a.map((each, index) => {
          return (
            <div key={index}>
              {each.name} want to have this role and say {each.general_text}
            </div>
          );
        })}
      </div>
    );
  }
}

export default GetApplication;
