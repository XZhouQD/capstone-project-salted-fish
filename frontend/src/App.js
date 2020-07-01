import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import HomePage from "./components/layout/HomePage";
import Narvbar from "./components/layout/Narvbar";
import Login from "./components/auth/Login";
import Register from "./components/auth/Register";
import Dashboard from "./components/dashboard/Dashboard";
import CreateProject from "./components/projects/createProject";
import Alert from "./components/layout/alert";
import AddRoleProject from "./components/projects/addRoleProject";
import ProjectList from "./components/projects/projectList";
import ProjectDetails from "./components/projects/projectDetails";

function App() {
  return (
    <Router>
      <Narvbar />
      <Route exact path="/" component={HomePage} />
      <Alert />
      <Switch>
        <Route exact path="/dashboard" component={Dashboard} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/register" component={Register} />
        <Route exact path="/create" component={CreateProject} />
        <Route exact path="/project/:id/role" component={AddRoleProject} />
        <Route exact path="/projects" component={ProjectList} />
        <Route
          exact
          path="/projects/project_detail"
          component={ProjectDetails}
        />
      </Switch>
    </Router>
  );
}

export default App;
