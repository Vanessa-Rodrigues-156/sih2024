<template>
  <div class="header">
    <h1>Cyber Khabar</h1>
  </div>
  <div id="app">
    <HelloWorld />
  </div>
</template>

<script>
import HelloWorld from "./components/homepage.vue";

export default {
  components: {
    HelloWorld,
  },
};
</script>

<style>
.header{
color: #ffffff;
font-size: 20px;
padding: 0%;
margin: 0%;
}
body {
  margin: 0;
  padding: 0%;
  font-family: Arial, sans-serif;
  background-color: #1d1f27;
  color: #ffffff;
  overflow-y: hidden;
}
</style>
