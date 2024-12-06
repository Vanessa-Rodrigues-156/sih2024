import { createRouter, createWebHistory } from 'vue-router';
import NewsPage from '../components/NewsPage.vue';  // Your main page
import DataBreachPage from '../components/DataBreachPage.vue';  // The page for a specific news item

const routes = [
  { path: '/', component: NewsPage },
  { path: '/news/:id', component: DataBreachPage, props: true },  // Dynamic route for specific news
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
