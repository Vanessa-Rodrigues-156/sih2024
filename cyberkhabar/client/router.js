import Vue from 'vue';
import Router from 'vue-router';
import Authentication from './views/Authentication.vue';
import LandingPage from './views/LandingPage.vue'; // The main landing page after login

Vue.use(Router);

const routes = [
  {
    path: '/',
    name: 'home',
    component: Authentication, // Authentication component (for login/signup)
  },
  {
    path: '/landing',
    name: 'landing',
    component: LandingPage, // The main landing page after successful login
  }
];

const router = new Router({
  routes
});

export default router;
