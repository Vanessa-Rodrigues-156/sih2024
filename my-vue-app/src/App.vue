<template>
  <div id="app">
    <h1 style="text-align: center; margin: 20px;">Cybersecurity Map of India</h1>
    <!-- Cybersecurity Map Component -->
    <CybersecurityMap />
    <!-- Incident Report Form Component -->
    <IncidentReportForm />
  </div>
</template>

<script>
import CybersecurityMap from './components/CybersecurityMap.vue';
import IncidentReportForm from './components/IncidentReportForm.vue';

export default {
  name: 'App',
  components: {
    CybersecurityMap,
    IncidentReportForm,
  },
};
</script>

<style>
body {
  margin: 0;
  font-family: 'Arial', sans-serif;
  background-color: #101320;
  color: #ffffff;
}

h1 {
  color: #0ff;
}

#app {
  max-width: 1200px;
  margin: auto;
  padding: 20px;
}
</style>
