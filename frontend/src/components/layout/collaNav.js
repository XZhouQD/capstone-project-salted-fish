import React from "react";
import { Link } from "react-router-dom";

const CollaNav = () => {
  return (
    <nav className="darken-2 nav-wrapper grey navbar-css">
      <Link to="/" className="brand-logo avatar">
        FindColla
      </Link>

      <ul className="right hide-on-med-and-down">
        <li>
          <Link to="/projects" className="avatar">
            Projects
          </Link>
        </li>
        <li>
          <Link to="/signout" className="avatar">
            Sign out
          </Link>
        </li>
        <li>
          <Link to="/dashboard" className="avatar">
            profile
          </Link>
        </li>
      </ul>
    </nav>
  );
};

export default CollaNav;
