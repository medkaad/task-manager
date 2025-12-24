import { createRouter, createWebHistory } from "vue-router";

import Login from "../views/Login.vue";
import DashboardLayout from "../layouts/DashboardLayout.vue";
import Dashboard from "../views/Dashboard.vue";
import Projects from "../views/Projects.vue";
import ProjectDetail from "../views/ProjectDetail.vue";

const routes = [
  { path: "/login", component: Login },

  {
    path: "/",
    component: DashboardLayout,
    children: [
      { path: "dashboard", component: Dashboard },
      { path: "projects", component: Projects },
      { path: "projects/:id", component: ProjectDetail, props: true }
    ]
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

// 🔒 Guard
router.beforeEach((to, from, next) => {
  const token = localStorage.getItem("access_token");
  if (to.path !== "/login" && !token) {
    next("/login");
  } else {
    next();
  }
});

export default router;
