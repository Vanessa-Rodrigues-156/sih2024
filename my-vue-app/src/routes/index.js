import { createRouter, createWebHistory } from 'vue-router'
import DataBreachPage from '../components/DataBreachPage.vue'
import ReportPage from '../components/ReportPage.vue'

const routes = [
  {
    path: '/',
    name: 'DataBreach',
    component: DataBreachPage
  },
  {
    path: '/report',
    name: 'Report',
    component: ReportPage
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
