import { createApp } from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import { loadFonts } from './plugins/webfontloader'
import router from './router'
import store from './store'; 

loadFonts()
//localStorage.removeItem('vuexState'); // 删除键为 'vuexState' 的数据

const app = createApp(App)
  .use(vuetify)
  .use(router)
  .use(store)

router.isReady().then(() => {
    app.mount('#app')
})
