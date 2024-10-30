// src/router.js
import { createRouter, createWebHistory } from "vue-router";
import store from "@/store";
import HomePage from "./views/HomePage.vue";
import LogIn from "./views/LogIn.vue";
import SignUp from "./views/SignUp.vue";
import AdminPage from "./views/AdminPage.vue";

// 定义路由
const routes = [
  {
    path: "/",
    name: "HomePage",
    component: HomePage,
  },
  {
    path: "/admin-page",
    name: "AdminPage",
    component: AdminPage,
	meta: { requiresAuth: true, userType: "管理员" },
  },
  {
    path: "/log-in",
    name: "LogIn",
    component: LogIn,
  },
  {
    path: "/sign-up",
    name: "SignUp",
    component: SignUp,
  },
];

// 创建路由实例并传递 `routes` 配置
const router = createRouter({
  history: createWebHistory(),
  routes,
});

router.beforeEach((to, from, next) => {
  const isAuthenticated = store.getters.isAuthenticated;
  const user = store.getters.user;

  if (to.matched.some((record) => record.meta.requiresAuth)) {
    if (!isAuthenticated) {
      next({ name: "LogIn" });
    } else if (to.meta.userType && to.meta.userType !== user.type) {
      next({ name: "HomePage" }); // 或者跳转到其他页面
    } else {
      next();
    }
  } else {
    next();
  }
});

export default router;