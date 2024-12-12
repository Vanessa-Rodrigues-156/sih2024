import { createRouter, createWebHistory } from "vue-router";
import CyberKhabar from "./views/HomePage.vue";
import Authentication from "./views/Authentication.vue";

const routes = [
  { path: "/home", component: CyberKhabar },
  { path: "/", component: Authentication },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;