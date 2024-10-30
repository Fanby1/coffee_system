import { createStore } from "vuex";
import { persistState } from "./plugins/persisState";
import authentication from "./modules/authentication";
import shop from "./modules/shop";

const store = createStore({
  modules: {
    shop, authentication
  },
  plugins: [persistState], // 加载持久化插件
});

export default store;