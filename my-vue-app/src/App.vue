<template>
  <div id="app">
    <!-- Main Landing Page 1 Component -->
    <LandingPage1 />
  </div>
</template>

<script>
// Import the LandingPage1 component
import LandingPage1 from './components/LandingPage1.vue';

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
  color: #fff;
  background-color: #101320;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
  padding: 20px;
}
</style>
