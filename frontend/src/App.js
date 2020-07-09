import React from "react";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";
import HomePage from "./components/layout/HomePage";
import Narvbar from "./components/layout/Narvbar";
import Login from "./components/auth/Login";
import Register from "./components/auth/Register";
import Dashboard from "./components/dashboard/Dashboard";
import CreateProject from "./components/projects/createProject";
import Alert from "./components/layout/alert";
import AdminDash from "./components/dashboard/adminDash";
import AddRoleProject from "./components/projects/addRoleProject";
import ProjectList from "./components/projects/projectList";
import DreamerRecommend from "./components/dashboard/dreamerRecommend";
import projectDetails from "./components/projects/projectDetails";
import DreamerCollasCard from "./components/dashboard/dreamerCollasCard";
import ChangeRoleDetails from "./components/projects/changeRoleDetails";

function App() {
  return (
    <Router>
      <Narvbar />
      <Route exact path="/" component={HomePage} />
      <Alert />
      <Switch>
        <Route exact path="/dashboard" component={Dashboard} />
        <Route exact path="/drecommend" component={DreamerRecommend} />
        <Route exact path="/login" component={Login} />
        <Route exact path="/register" component={Register} />
        <Route exact path="/create" component={CreateProject} />
        <Route exact path="/project/:id/role" component={AddRoleProject} />
        <Route exact path="/projects" component={ProjectList} />
        <Route exact path="/admindash" component={AdminDash} />
        <Route
          exact
          path="/projects/:pid/role/:rid"
          component={ChangeRoleDetails}
        />
        <Route exact path="/projects/:id" component={projectDetails} />
        <Route exact path="/collaborators/:id" component={DreamerCollasCard} />
      </Switch>
    </Router>
  );
}

export default App;
