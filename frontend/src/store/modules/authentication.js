import axios from "axios";
import router from "@/router";

export default {
  state: {
    isAuthenticated: false,
    token: null,
    user: null,
    type: null,
  },
  mutations: {
    setIsAuthenticated(state, isAuthenticated) {
      state.isAuthenticated = isAuthenticated;
    },
    setToken(state, token) {
      state.token = token;
    },
    setUser(state, user) {
      state.user = user;
    },
    setType(state, type) {
      state.type = type;
    },
  },
  actions: {
    async login({ commit }, values) {
      const response = await axios.post("api/login", values);
      const token = response.data.token;
      const user = response.data.user;

      if (response.data.message === "Login failed") {
        alert("登录失败");
        return;
      }

      commit("setIsAuthenticated", true);
      commit("setToken", token);
      commit("setUser", user);
      commit("setType", values.type);
      // 跳转到受保护的页面
      if (values.type === "顾客") {
        router.push("/");
      } else {
        router.push("/admin-page");
      }
    },
    logout({ commit }) {
      commit("setIsAuthenticated", false);
      commit("setToken", null);
      commit("setUser", null);
      commit("setType", null);
      localStorage.removeItem("vuexState");
      router.push("/");
    },
  },
  getters: {
    isAuthenticated: (state) => state.isAuthenticated,
    token: (state) => state.token,
    user: (state) => state.user,
    type: (state) => state.type,
  },
};
