import React from "react";
import { Link } from "react-router-dom";

import background1 from "./img1.jpeg";
import background2 from "./img2.jpeg";
import { Parallax } from "react-parallax";

const HomePage = () => {
  return (
    <div>
      <div class="parallax-container">
        <Parallax bgImage={background1} bgImageAlt="the cat" strength={800}>
          <div style={{ height: "500px" }} />
        </Parallax>
      </div>

      <section className="center">
        <h1>Connect Your Dream</h1>
        <p>Find your dream collaborator and get help from others</p>
        <div>
          <Link
            to="register"
            className="btn waves-effect waves-light blue-grey lighten-1"
            style={{ margin: "5px" }}
          >
            Sign Up
          </Link>
          <Link
            to="login"
            className="btn waves-effect waves-light blue-grey lighten-1"
            style={{ margin: "10px" }}
          >
            Login
          </Link>
        </div>
      </section>

      <div class="parallax-container">
        <Parallax bgImage={background2} bgImageAlt="the cat" strength={1000}>
          <div style={{ height: "500px" }} />
        </Parallax>
      </div>

      <div class="container">
        <div class="row">
          <div class="col s12 m4">
            <div class="icon-block">
              <h2 class="center brown-text">
                <i class="material-icons">flash_on</i>
              </h2>
              <h5 class="center">Speeds up development</h5>

              <p class="light">
                We did most of the heavy lifting for you to provide a default
                stylings that incorporate our custom components. Additionally,
                we refined animations and transitions to provide a smoother
                experience for developers.
              </p>
            </div>
          </div>

          <div class="col s12 m4">
            <div class="icon-block">
              <h2 class="center brown-text">
                <i class="material-icons">group</i>
              </h2>
              <h5 class="center">User Experience Focused</h5>

              <p class="light">
                By utilizing elements and principles of Material Design, we were
                able to create a framework that incorporates components and
                animations that provide more feedback to users. Additionally, a
                single underlying responsive system across all platforms allow
                for a more unified user experience.
              </p>
            </div>
          </div>

          <div class="col s12 m4">
            <div class="icon-block">
              <h2 class="center brown-text">
                <i class="material-icons">settings</i>
              </h2>
              <h5 class="center">Easy to work with</h5>

              <p class="light">
                We have provided detailed documentation as well as specific code
                examples to help new users get started. We are also always open
                to feedback and can answer any questions a user may have about
                Materialize.
              </p>
            </div>
          </div>
        </div>
      </div>

      <div class="footer-copyright right">
        <div class="container">© 2014 Copyright Salted-Fish-team</div>
      </div>
    </div>
  );
};

export default HomePage;
