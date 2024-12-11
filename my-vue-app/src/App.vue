<template>
  <div id="app" class="bright-theme">
    <!-- Navigation Bar -->
    <header>
      <h1>CyberKhabar</h1>
      <nav class="navbar">
       <button @click="currentSection = 'newsPage'">News Portal</button>
          <button @click="currentSection = 'incidentForm'">Report Incident</button>
          <button @click="currentSection = 'map'">Cyber Map</button>
            <button @click="currentSection = 'landingPage1'">Cyber Statistics</button>
           <button @click="currentSection = 'landingPage'">Insights & Info</button>
      
      </nav>
    </header>

    <!-- Section Rendering -->
    <main>
      <section v-if="currentSection === 'landingPage1'">
        <LandingPage1 />
      </section>
      <section v-if="currentSection === 'map'">
        <CybersecurityMap />
      </section>
      <section v-if="currentSection === 'newsPage'">
        <NewsPage />
      </section>
      <section v-if="currentSection === 'landingPage'">
        <LandingPage />
      </section>
      <section v-if="currentSection === 'incidentForm'">
        <IncidentReportForm />
      </section>
    </main>

    <!-- Footer -->
    <footer>
      <p>&copy; 2024 CybersKhabar. Empowering a secure digital India.</p>
    </footer>
  </div>
</template>

<script>
import LandingPage1 from './components/LandingPage1.vue';
import CybersecurityMap from './components/CybersecurityMap.vue';
import NewsPage from './components/NewsPage.vue';
import LandingPage from './components/LandingPage.vue';
import IncidentReportForm from './components/IncidentReportForm.vue';

export default {
  name: 'App',
  components: {
    LandingPage1,
    CybersecurityMap,
    NewsPage,
    LandingPage,
    IncidentReportForm,
  },
  data() {
    return {
      currentSection: 'newsPage', // Default section
    };
  },
};
</script>

<style scoped>
/* General Styles */
.bright-theme {
  background-color: #101320;
  color: #ffffff;
  font-family: "Roboto", sans-serif;
}

header {
  background-color: #1a1a3d;
  padding: 10px 0;
  text-align: center;
  color: #0ff;
  box-shadow: 0 0 10px #0ff;
}

.navbar {
  display: flex;
  justify-content: center;
  gap: 10px;
  margin-top: 10px;
}

.navbar button {
  padding: 10px 15px;
  border: 1px solid #0ff;
  background-color: #101320;
  color: #ffffff;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

.navbar button:hover {
  background-color: #1a1a3d;
}

main {
  padding: 20px;
}

/* Footer */
footer {
  background-color: #1a1a3d;
  text-align: center;
  padding: 10px 0;
  color: #0ff;
  box-shadow: 0 -5px 10px #0ff;
  margin-top: 20px;
}
</style>