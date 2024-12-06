<template>
  <div class="landing-page">
    <!-- Header Section -->
    
    <!-- Main Section -->
    <main class="main-content">
      <h1 class="main-title blinking-text">Cyber Incident Monitor</h1>
      <p class="status">Real-time Monitoring</p>
      <!-- Grid Container for Sections (One row with 4 sections) -->
      <div class="grid-container">
        <!-- Geographic Distribution Section -->
        <section class="grid-item geographic-distribution" @click="zoomSection">
          <h2>Geographic Distribution</h2>
          <ul>
            <li><strong>New Delhi:</strong> 1.2K incidents</li>
            <li><strong>Mumbai:</strong> 1K incidents</li>
            <li><strong>Bengaluru:</strong> 900 incidents</li>
            <li><strong>Chennai:</strong> 800 incidents</li>
            <li><strong>Hyderabad:</strong> 650 incidents</li>
          </ul>
        </section>
        <!-- Incident Types Section -->
        <section class="grid-item incident-types" @click="zoomSection">
          <h2>Incident Types</h2>
          <ul>
            <li><strong>Malware:</strong> 1.2K</li>
            <li><strong>Phishing:</strong> 1K</li>
            <li><strong>DDoS:</strong> 800</li>
            <li><strong>Data Breach:</strong> 650</li>
            <li><strong>Ransomware:</strong> 450</li>
          </ul>
        </section>
        <!-- Affected Sectors Section -->
        <section class="grid-item affected-sectors" @click="zoomSection">
          <h2>Affected Sectors</h2>
          <ul>
            <li><strong>Government:</strong> 1.5K</li>
            <li><strong>Finance:</strong> 1.2K</li>
            <li><strong>Healthcare:</strong> 1K</li>
            <li><strong>Education:</strong> 800</li>
            <li><strong>Critical Infrastructure:</strong> 650</li>
          </ul>
        </section>
        <!-- Recent Incidents Section -->
        <section class="grid-item recent-incidents" @click="zoomSection">
          <h2>Recent Incidents</h2>
          <ul>
            <li><strong>Ransomware Attack:</strong> Government Sector (2h ago)</li>
            <li><strong>Phishing Campaign:</strong> Finance Sector (4h ago)</li>
            <li><strong>DDoS Attack:</strong> Critical Infrastructure (8h ago)</li>
            <li><strong>Data Breach:</strong> Healthcare Sector (12h ago)</li>
          </ul>
        </section>
      </div>
    </main>
  </div>
</template>
<script>
export default {
  name: "LandingPage1",
  methods: {
    zoomSection(event) {
      const section = event.currentTarget;
      section.classList.add("zoom");
      setTimeout(() => section.classList.remove("zoom"), 300); // Reset zoom after animation
    },
  },
};
</script>
<style scoped>
/* General Styles */
.landing-page {
  background-color: #101320;
  color: #cce7ff;
  font-family: "Roboto", sans-serif;
  padding: 20px;
  display: flex;
  flex-direction: column;
  align-items: center;
  min-height: 100vh;
  transition: background-color 0.3s ease;
  position: relative;
}
/* Header Styles */

/* Main Content */
.main-content {
  width: 100%;
  text-align: center;
}
.main-title {
  font-size: 32px;
  font-weight: bold;
  text-align: center;
  color: #0ff;
  animation: blink 1.5s infinite alternate;
  transition: color 0.3s ease;
}
@keyframes blink {
  0% {
    color: #0ff;
  }
  50% {
    color: #ff00ff;
  }
  100% {
    color: #00ccff;
  }
}
.status {
  font-size: 14px;
  margin-top: 5px;
  text-align: center;
  color: #cce7ff;
  transition: color 0.3s ease;
}
/* Grid Layout for Four Sections in One Row */
.grid-container {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  grid-gap: 20px;
  max-width: 1200px;
  margin-top: 30px;
  animation: fadeIn 2s ease-out;
}
.grid-item {
  background-color: #1a1a3d;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 15px rgba(0, 255, 255, 0.5);
  min-height: 250px;
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  animation: fadeInUp 1s ease-out;
}
@keyframes fadeIn {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
@keyframes fadeInUp {
  0% {
    opacity: 0;
    transform: translateY(50px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}
/* Remove Hover Glow Effect */
.grid-item:hover {
  transform: none; /* No zooming effect */
  box-shadow: none; /* No glowing effect */
  background-color: #2a2a6c; /* Subtle background color change */
}
/* Zoom Effect */
.zoom {
  transform: scale(1.1);
  box-shadow: 0 0 25px #00ccff;
}
/* Section Titles */
.grid-item h2 {
  color: #0ff;
  text-align: center;
  margin-bottom: 10px;
  font-size: 20px;
  font-weight: bold;
  transition: color 0.3s ease;
}
.grid-item:hover h2 {
  color: #00ccff;
}
/* List Style */
.grid-item ul {
  list-style: none;
  padding-left: 0;
  color: #cce7ff;
}
.grid-item li {
  font-size: 16px;
  margin-bottom: 8px;
  display: flex;
  justify-content: space-between;
}
.grid-item a {
  color: white;
  text-decoration: none;
}
.grid-item a:hover {
  text-decoration: underline;
}
/* User Avatar */
.user-avatar img {
  border-radius: 50%;
  object-fit: cover;
  width: 32px;
  height: 32px;
  transition: transform 0.3s ease;
}
.user-avatar img:hover {
  transform: scale(1.1);
}
/* Responsive Design */
@media (max-width: 1200px) {
  .grid-container {
    grid-template-columns: repeat(2, 1fr);
  }
}
@media (max-width: 768px) {
  .grid-container {
    grid-template-columns: 1fr;
  }
}
</style>