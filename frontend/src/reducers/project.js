import {
  CREATE_PROJECT_SUCCESS,
  CREATE_PROJECT_FAIL,
} from "../actions/actionTypes";

const initialState = {
  project_id: null,
};

export default function (state = initialState, action) {
  const { type, payload } = action;
  console.log(payload);
  switch (type) {
    // sucess load in
    case CREATE_PROJECT_SUCCESS:
      return {
        ...state,
        project_id: payload,
      };

    case CREATE_PROJECT_FAIL:
      return { ...state };

    default:
      return state;
  }
}
