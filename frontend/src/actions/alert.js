import { SET_ALERT, REMOVE_ALERT } from "./actionTypes";
import uuid from "uuid";

export const setAlert = (msg, alertType) => (dispatch) => {
  // only id
  const id = uuid.v4();
  dispatch({
    type: SET_ALERT,
    payload: { msg, alertType, id },
  });
};
