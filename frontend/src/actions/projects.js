import axios from "axios";
import { setAlert } from "./alert";
import { CREATE_PROJECT_FAIL, CREATE_PROJECT_SUCCESS } from "./actionTypes";

// register user
export const createProject = ({ title, category, description }) => async (
  dispatch
) => {
  const a = localStorage.getItem("token");
  console.log(a);
  const config = {
    headers: {
      "Content-Type": "application/json;charset=UTF-8",
      "Access-Control-Allow-Origin": "*",
      "AUTH-KEY": a,
    },
  };

  const body = JSON.stringify({
    title,
    category,
    description,
  });
  console.log(body);
  console.log("this is project");
  try {
    const res = await axios.post("/project", body, config);
    console.log(res.data);

    dispatch(setAlert(res.data.message));

    dispatch({
      type: CREATE_PROJECT_SUCCESS,
      payload: res.data.id,
    });
  } catch (err) {
    // error -> dispatch setAlert to reducers
    const errors = err.response.data.message;
    dispatch(setAlert(errors));

    dispatch({
      type: CREATE_PROJECT_FAIL,
    });
  }
};
