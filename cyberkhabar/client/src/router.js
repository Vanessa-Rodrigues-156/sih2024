import { createRouter, createWebHistory } from "vue-router";
import CyberKhabar from "./views/HomePage.vue";
import Authentication from "./views/Authentication.vue";
import ReportPage from "./views/ReportPage.vue";

const routes = [
  { path: "/home", component: CyberKhabar },
  { path: "/", component: Authentication },
  // {path :`/news/${news.id}`, component :ReportPage, props: true},
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;