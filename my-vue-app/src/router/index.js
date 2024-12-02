import { createRouter, createWebHistory } from 'vue-router'
import Dashboard from '../views/LandingPage1.vue'
import ReportingForm from '../views/IncidentReportForm.vue'
import Reports from '../views/reportpage.vue'

const routes = [
  {
    path: '/',
    redirect: '/dashboard'
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard
  },
  {
    path: '/reporting-form',
    name: 'ReportingForm',
    component: ReportingForm
  },
  {
    path: '/reports',
    name: 'Reports',
    component: Reports
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
