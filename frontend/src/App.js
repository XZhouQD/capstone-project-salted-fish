import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import HomePage from "./components/layout/HomePage";
import Narvbar from "./components/layout/Narvbar";
import Login from "./components/auth/Login";
import Register from "./components/auth/Register";
import Test from "./components/layout/test";
import Dashboard from "./components/dashboard/Dashboard";
import createProject from "./components/projects/createProject";
import Alert from "./components/layout/alert";

function App() {
  return (
    <Router>
      <Narvbar />
      <Route exact path="/" component={HomePage} />
      <Alert />
      <Switch>
        <Route exact path="/dashboard" component={Dashboard} />
        <Route exact path="/test" component={Test} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/register" component={Register} />
        <Route exact path="/create" component={createProject} />
      </Switch>
    </Router>
  );
}

export default App;
