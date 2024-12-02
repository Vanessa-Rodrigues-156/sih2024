<template>
  <div id="app">
    <nav>
      <router-link to="/">Landing Page 1</router-link> |
      <router-link to="/data-breach">Data Breach</router-link> |
      <router-link to="/incident-report">Incident Report</router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
/* eslint-disable */
// Import the LandingPage1 component
import { createRouter, createWebHistory } from 'vue-router'
import LandingPage1 from './views/LandingPage1.vue'
import DataBreachPage from './views/DataBreachPage.vue'
import IncidentReportPage from './views/IncidentReportForm.vue'

export default {
  name: 'App',
  components: {
    LandingPage1, // Register LandingPage1 component
    DataBreachPage,
    IncidentReportPage
  },
};

const router = createRouter({
  history: createWebHistory(),
  routes: [
    {
      path: '/',
      name: 'LandingPage1',
      component: LandingPage1
    },
    {
      path: '/data-breach',
      name: 'DataBreachPage',
      component: DataBreachPage
    },
    {
      path: '/incident-report',
      name: 'IncidentReportPage',
      component: IncidentReportPage
    }
  ]
})

</script>

<style>
/* Global Styles */
#app {
  font-family: Arial, sans-serif;
  background-color: #121212;
  color: #fff;
}
#app {
  text-align: center;
}
nav {
  padding: 30px;
}
nav a {
  font-weight: bold;
  color: #fff;
  text-decoration: none;
  margin: 0 10px;
}
nav a.router-link-active {
  color: #42b983;
}
</style>
