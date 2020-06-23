import {
  REGISTER_SUCCESS,
  REGISTER_FAIL,
  USER_LOADED,
  AUTH_ERROR,
  LOGIN_SUCCESS,
  LOGIN_FAIL,
} from "../actions/actionTypes";

const initialState = {
  // get token from localstorage localStorage.getItem()
  token: null,
  isAuthenticated: null,
  loading: true,
  user: null,
};

export default function (state = initialState, action) {
  const { type, payload } = action;
  switch (type) {
    // sucess load in
    case USER_LOADED:
      return {
        ...state,
        isAuthenticated: true,
        loading: false,
        user: payload,
      };

    case REGISTER_SUCCESS:
      return { ...state, ...payload, isAuthenticated: false, loading: false };

    case LOGIN_SUCCESS:
      // set token to local storage
      localStorage.setItem("token", payload.token);
      console.log(payload.token);
      return { ...state, ...payload, isAuthenticated: true, loading: false };

    case REGISTER_FAIL:
    case LOGIN_FAIL:
    case AUTH_ERROR:
      localStorage.removeItem("token");
      return { ...state, token: null, isAuthenticated: false, loading: false };

    default:
      return state;
  }
}
