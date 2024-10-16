// src/router.js
import { createRouter, createWebHistory } from 'vue-router';
import HomePage from './views/HomePage.vue';
import LogIn from './views/LogIn.vue';
import SignUp from './views/SignUp.vue';

// 定义路由
const routes = [
  {
    path: '/',
    name: 'HomePage',
    component: HomePage,
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn,
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp,
  }
];

// 创建路由实例并传递 `routes` 配置
const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;