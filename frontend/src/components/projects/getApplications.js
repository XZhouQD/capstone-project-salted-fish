import React from "react";
import { Link } from "react-router-dom";
import axios from "axios";

class GetApplication extends React.Component {
  state = {
    a: [],
  };

  async componentWillMount() {
    const a = localStorage.getItem("token");

    const res = await axios.get(this.props.url_1, {
      headers: {
        "AUTH-KEY": a,
      },
    });

    this.setState({ a: res.data.applications });
    console.log(this.state.a);
  }
  render() {
    return (
      <div>
        {this.state.a.map((each, index) => {
          const url =
            "/project/" +
            this.props.pid +
            "/role/" +
            this.props.rid +
            "/collaborators/" +
            each.id +
            "/applications";
          return (
            <div key={index} style={{ fontFamily: "Ubuntu" }}>
              <Link to={url} style={{ marginRight: "10px" }}>
                {each.name}
              </Link>
              want to apply for this role and leaves his messgae：
              {each.general_text}
            </div>
          );
        })}
      </div>
    );
  }
}

export default GetApplication;
