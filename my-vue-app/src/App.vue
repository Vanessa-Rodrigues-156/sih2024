<template>
  <div id="app">
    <header class="app-header">
      <h1>Cybersecurity News Portal</h1>
    </header>
    <NewsPage />
    <footer class="app-footer">
      <p>&copy; 2024 Cybersecurity News. All rights reserved.</p>
    </footer>
  </div>
</template>

<script>
import NewsPage from "./components/NewsPage.vue";

export default {
  name: "App",
  components: {
    NewsPage,
  },
};
</script>

<style>
/* Global Styles */
#app {
  font-family: Arial, sans-serif;
  color: #333;
  text-align: center;
  line-height: 1.6;
  margin: 0;
  padding: 0;
}

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
