import axios from "axios";
import router from "@/router";

export default {
  state: {
    isAuthenticated: false,
    token: null,
    user: null,
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
      // 跳转到受保护的页面
      router.push("/");
    },
    logout({ commit }) {
      commit("setIsAuthenticated", false);
      commit("setToken", null);
      commit("setUser", null);
      localStorage.removeItem("vuexState");
      router.push("/");
    },
  },
  getters: {
    isAuthenticated: (state) => state.isAuthenticated,
    token: (state) => state.token,
	user: (state) => state.user,
  },
};
