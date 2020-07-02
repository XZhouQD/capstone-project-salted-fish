import axios from "axios";
import { setAlert } from "./alert";
import {
  CREATE_PROJECT_FAIL,
  CREATE_PROJECT_SUCCESS,
  GET_PROJECT_LIST,
  UNDO_FLAG,
  SEARCH_PROJECT_LIST,
  POST_PROJECT_ROLE,
  POST_PROJECT_ROLE_FAIL,
} from "./actionTypes";

// createProject
export const createProject = ({ title, category, description }) => async (
  dispatch
) => {
  const a = localStorage.getItem("token");

  const config = {
    headers: {
      "Content-Type": "application/json;charset=UTF-8",
      "Access-Control-Allow-Origin": "*",
      "AUTH-KEY": a,
    },
  };
  category = Number(category) - 1;
  console.log(category, typeof category);
  const body = JSON.stringify({
    title,
    category,
    description,
  });

  try {
    const res = await axios.post("/project", body, config);
    console.log(res.data);

    dispatch(setAlert(res.data.message));

    dispatch({
      type: CREATE_PROJECT_SUCCESS,
      payload: res.data.project_id,
    });

    setTimeout(() => dispatch({ type: UNDO_FLAG }), 100);
  } catch (err) {
    // error -> dispatch setAlert to reducers
    const errors = err.response.data.message;
    dispatch(setAlert(errors));

    dispatch({
      type: CREATE_PROJECT_FAIL,
    });
  }
};

// getProject list
export const getProject = () => async (dispatch) => {
  try {
    const res = await axios.get("/projects");
    console.log(res.data);

    dispatch({
      type: GET_PROJECT_LIST,
      payload: res.data,
    });
  } catch (err) {
    // error -> dispatch setAlert to reducers
    const errors = err.response.data.message;
    console.log(errors);
  }
};

// search
export const searchProject = ({
  description,
  category,
  order_by,
  sorting,
}) => async (dispatch) => {
  category = Number(category) - 1;
  try {
    const res = await axios.get(
      "/projects?description=" +
        description +
        "&category=" +
        category +
        "&order_by=" +
        order_by +
        "&sorting=" +
        sorting
    );
    console.log(res.data);

    dispatch(setAlert(res.data.message));
    dispatch({
      type: SEARCH_PROJECT_LIST,
      payload: res.data,
    });
  } catch (err) {
    // error -> dispatch setAlert to reducers
    console.log(err.response);
    const errors = err.response.data.message;
    dispatch(setAlert(errors));
  }
};

// postProjectRole list
export const postProjectRole = ({
  title,
  amount,
  skill,
  experience,
  education,
  general_enquiry,
}) => async (dispatch) => {
  const a = localStorage.getItem("token");

  const config = {
    headers: {
      "Content-Type": "application/json;charset=UTF-8",
      "Access-Control-Allow-Origin": "*",
      "AUTH-KEY": a,
    },
  };

  amount = Number(amount);
  skill = Number(skill);
  experience = Number(experience);
  education = Number(education);

  const body = JSON.stringify({
    title,
    amount,
    skill,
    experience,
    education,
    general_enquiry,
  });
  console.log(body);

  try {
    // need to change
    const id = 3;
    const res = await axios.post("/project/" + id + "/role", body, config);
    console.log(res.data);

    dispatch(setAlert(res.data.message));

    dispatch({
      type: POST_PROJECT_ROLE,
      payload: res.data,
    });
  } catch (err) {
    // error -> dispatch setAlert to reducers
    const errors = err.response.data.message;
    dispatch(setAlert(errors));

    dispatch({
      type: POST_PROJECT_ROLE_FAIL,
    });
  }
};
