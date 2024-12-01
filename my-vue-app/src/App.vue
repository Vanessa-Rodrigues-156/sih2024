<template>
  <div id="app">
    <header class="app-header">
      <h1>Cybersecurity News Portal</h1>
    </header>
    <LandingPage />
    <footer class="app-footer">
      <p>&copy; 2024 Cyber Khabar. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
import LandingPage from "./components/LandingPage.vue";

export default {
  name: "App",
  components: {
    LandingPage,
  },
};
</script>

<style scoped>
/* Header Styles */
.app-header {
  background: #007bff;
  color: white;
  padding: 10px 20px;
}

.app-header h1 {
  margin: 0;
  font-size: 24px;
}

/* Footer Styles */
.app-footer {
  background: #f8f9fa;
  color: #555;
  padding: 10px 20px;
  border-top: 1px solid #ddd;
  margin-top: 20px;
}
</style>
