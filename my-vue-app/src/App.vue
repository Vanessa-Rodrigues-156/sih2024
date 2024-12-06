<template>
  <div id="app">
    <DataBreachPage />
  </div>
</template>

<script>
import DataBreachPage from "./components/DataBreachPage.vue";

export default {
  name: "App",
  components: {
    DataBreachPage,
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
</style>