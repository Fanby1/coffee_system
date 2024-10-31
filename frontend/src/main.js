import { createApp } from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import { loadFonts } from "./plugins/webfontloader";
import router from "./router";
import store from "./store";

loadFonts();
//localStorage.removeItem('vuexState'); // 删除键为 'vuexState' 的数据

createApp(App)
.use(router)
.use(store)
.use(vuetify)
.mount("#app");
