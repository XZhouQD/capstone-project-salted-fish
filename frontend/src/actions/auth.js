import axios from "axios";
import { setAlert } from "./alert";
import {
  REGISTER_SUCCESS,
  REGISTER_FAIL,
  USER_LOADED,
  AUTH_ERROR,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
} from "./actionTypes";
import setToken from "../utils/setToken";

// get the user back by token;
export const loadUser = () => async (dispatch) => {
  if (localStorage.token) {
    setToken(localStorage.token);
  }

  try {
    // change this api
    const res = await axios.get("./api/auth");
    dispatch({
      type: USER_LOADED,
      payload: res.data,
    });
  } catch (err) {
    dispatch({
      type: AUTH_ERROR,
    });
  }
};

// register user
export const registerDreamer = ({
  name,
  email,
  password,
  repeat_password,
  phone_no,
}) => async (dispatch) => {
  const config = {
    headers: {
      "Content-Type": "application/json;charset=UTF-8",
      "Access-Control-Allow-Origin": "*",
    },
  };

  const body = JSON.stringify({
    name,
    email,
    password,
    repeat_password,
    phone_no,
  });
  console.log(body);

  try {
    const res = await axios.post("/dreamer/register", body, config);
    console.log(res.data);

    dispatch(setAlert(res.data.message));

    dispatch({
      type: REGISTER_SUCCESS,
      payload: res.data,
    });
  } catch (err) {
    // error -> dispatch setAlert to reducers
    console.log(err.response.data);
    const errors = err.response.data.message;
    dispatch(setAlert(errors));

    dispatch({
      type: REGISTER_FAIL,
    });
  }
};

// register Colla
export const registerColla = ({
  name,
  email,
  phone_no,
  password,
  repeat_password,
  education,
  skills,
  experience,
}) => async (dispatch) => {
  const config = {
    headers: {
      "Content-Type": "application/json;charset=UTF-8",
      "Access-Control-Allow-Origin": "*",
    },
  };

  // change to defalult type
  education = Number(education);

  const body = JSON.stringify({
    name,
    email,
    phone_no,
    password,
    repeat_password,
    education,
    skills,
    experience,
  });
  console.log(body);

  try {
    const res = await axios.post("/collaborator/register", body, config);
    console.log(res.data);

    dispatch(setAlert(res.data.message));

    // good register
    dispatch({
      type: REGISTER_SUCCESS,
      payload: res.data,
    });
  } catch (err) {
    console.log(err.response.data);
    const errors = err.response.data.message;

    // error -> dispatch setAlert to reducers
    dispatch(setAlert(errors));
    // bad register
    dispatch({
      type: REGISTER_FAIL,
    });
  }
};

// login user
export const loginUser = (email, password, role) => async (dispatch) => {
  const config = {
    headers: {
      "Content-Type": "application/json;charset=UTF-8",
      "Access-Control-Allow-Origin": "*",
    },
  };

  const body = JSON.stringify({
    password,
    email,
    role,
  });
  console.log(body);

  try {
    const res = await axios.post("/login", body, config);
    console.log(res.data);

    dispatch({
      type: LOGIN_SUCCESS,
      payload: res.data,
    });
  } catch (err) {
    // error -> dispatch setAlert to reducers
    console.log(err.response.data);
    const errors = err.response.data.message;
    dispatch(setAlert(errors));

    dispatch({
      type: LOGIN_FAIL,
    });
  }
};
