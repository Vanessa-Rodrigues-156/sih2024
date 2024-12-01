<template>
  <div class="header">
    <!-- <h1>Cyber Khabar</h1> -->
    <h2><i class="fas fa-newspaper"></i> CyberKhabar</h2>
  </div>
  <div id="app">
    <Homepage />
  </div>
</template>

<script>
import Homepage from "./components/homepage.vue";

export default {
  components: {
    Homepage,
  },
};
</script>

<style>
body {
  margin: 0;
  padding: 0%;
  font-family: Arial, sans-serif;
  background-color: #1d1f27;
  color: #ffffff;
}
</style>
