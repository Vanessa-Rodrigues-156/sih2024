<template>
  <div id="app">
    <nav>
      <router-link to="/">Data Breach</router-link> |
      <router-link to="/report">Report</router-link>
    </nav>
    <router-view></router-view>
    <!-- Main Landing Page 1 Component -->
    <LandingPage1 />
  </div>
</template>

<script>
// Import the LandingPage1 component
import LandingPage1 from './components/LandingPage1.vue';

import DataBreachPage from "./views/DataBreachPage.vue";
import reportpg from "./views/reportpage.vue";
export default {
  name: 'App',
  components: {
    LandingPage1, // Register LandingPage1 component
  },
};
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
