import {
  CREATE_PROJECT_SUCCESS,
  CREATE_PROJECT_FAIL,
  GET_PROJECT_LIST,
  UNDO_FLAG,
  SEARCH_PROJECT_LIST,
  POST_PROJECT_ROLE,
  POST_PROJECT_ROLE_FAIL,
} from "../actions/actionTypes";

const initialState = {
  project_id: null,
  ProjectLists: [],
};

export default function (state = initialState, action) {
  const { type, payload } = action;
  console.log(payload);
  switch (type) {
    // sucess load in
    case CREATE_PROJECT_SUCCESS:
      return {
        ...state,
        flag: "create success",
      };
    case UNDO_FLAG:
      return {
        ...state,
        flag: "disappear",
      };
    case CREATE_PROJECT_FAIL:
      return { ...state };
    case GET_PROJECT_LIST:
      return { ...state, ProjectLists: payload.projects };

    case SEARCH_PROJECT_LIST:
      return {
        ...state,
        ProjectLists: payload.projects,
        flag: "search project",
      };

    case POST_PROJECT_ROLE:
      return {
        ...state,
        role: payload,
      };
    case POST_PROJECT_ROLE_FAIL:
      return {
        ...state,
        role: "Create role fail",
      };

    default:
      return state;
  }
}
