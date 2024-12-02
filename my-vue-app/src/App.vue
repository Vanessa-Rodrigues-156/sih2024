<template>
  <div id="app">
    <nav>
      <router-link to="/">Data Breach</router-link> |
      <router-link to="/report">Report</router-link>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script>
import DataBreachPage from "./views/DataBreachPage.vue";
import reportpg from "./views/reportpage.vue";
export default {
  name: "App",
  components: {
    DataBreachPage,
    reportpg,
  },
};
</script>

<style>
/* Global Styles */
body {
  margin: 0;
  padding: 0;
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
