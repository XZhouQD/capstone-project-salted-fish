import {
  CREATE_PROJECT_SUCCESS,
  CREATE_PROJECT_FAIL,
} from "../actions/actionTypes";

const initialState = {};

export default function (state = initialState, action) {
  const { type, payload } = action;
  switch (type) {
    // sucess load in
    case CREATE_PROJECT_SUCCESS:
      return {
        ...state,
        flag: "create success",
      };

    case CREATE_PROJECT_FAIL:
      return { ...state };

    default:
      return state;
  }
}
