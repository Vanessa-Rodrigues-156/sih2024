import { createRouter, createWebHistory } from 'vue-router'
import HomePage from '../components/HomePage.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: HomePage
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../components/AboutPage.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
