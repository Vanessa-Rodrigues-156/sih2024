<template>
  <div class="container">
  <!-- Header -->
    <header class="header">
      <nav class="navbar">
        <!-- Logo -->
        <div class="logo">Cyber Khabar</div> 
        <!-- Navigation Links -->
        <div class="nav-items">
          <input
            type="text"
            placeholder="🔍 Search for reports, insights..."
            class="search-bar"
          />
          <div class="nav-links">
            <a href="#" class="nav-link">Home</a>
            <a href="#" class="nav-link">Report</a>
            <a href="#" class="nav-link">Insights</a>
            <a href="#" class="nav-link">Sources</a>
            <a href="#" class="nav-link">Contact</a>
          </div>
        </div>

        <!-- Mobile Menu Icon -->
        <div class="menu-icon" @click="toggleMenu">☰</div>
      </nav>

      <!-- Mobile Menu -->
      <div v-if="isMobileMenuOpen" class="mobile-menu">
        <a href="#" class="mobile-link">Home</a>
        <a href="#" class="mobile-link">Report</a>
        <a href="#" class="mobile-link">Insights</a>
        <a href="#" class="mobile-link">Sources</a>
        <a href="#" class="mobile-link">Contact</a>
      </div>
    </header>
    <main class="content">
      <!-- Summary Section -->
      <section class="summary">
        <div class="summary-header">
          <h1>{{ report.title }}</h1>
          <a :href="report.downloadUrl" download="DataBreach_Report" class="download-btn">Download Report</a>
        </div>
        <h5 class="date">{{ report.date }}</h5>
        <p>{{ report.summary }}</p>
        <p>{{ report.details }}</p>
        <p>{{ report.stepsTaken }}</p>
      </section>

      <!-- Key Details Section -->
      <section class="key-details">
        <h2>Key Details</h2>
        <ul>
          <li v-for="(value, key) in keyDetails" :key="key">
            <span class="icon">{{ value.icon }}</span>
            <strong>{{ value.title }}:</strong> {{ value.description }}
          </li>
        </ul>
      </section>


      <!-- Insights Section -->
      <section class="insights">
        <h2>Insights</h2>
        <ul>
          <li v-for="(insight, index) in insights" :key="index">
            <span class="icon">{{ insight.icon }}</span>
            {{ insight.text }}
          </li>
        </ul>
      </section>
<!-- Images Section -->
<section class="images">
  <h2>Visual Insights</h2>
  <div class="image-row">
    <div v-for="image in images" :key="image.id" class="image-container">
      <img :src="image.image_url" :alt="image.alt_text" />
      <p>{{ image.title }}</p>
    </div>
  </div>
</section>
      <!-- Sources Section -->
      <section class="sources">
        <h2>🔗Sources</h2>
        <ul>
          <li v-for="(source, index) in sources" :key="index">
            <a :href="source.url" target="_blank">{{ source.title }}</a>
          </li>
        </ul>
      </section>
    </main>

    <!-- Footer (same as before) --><!-- Footer -->
    <footer class="footer">
      <div class="footer-container">
        <div class="footer-column">
          <h3>Quick Links</h3>
          <ul>
            <li><a href="#">Home</a></li>
            <li><a href="#">About Us</a></li>
            <li><a href="#">Services</a></li>
            <li><a href="#">Privacy Policy</a></li>
          </ul>
        </div>
        <div class="footer-column">
          <h3>Address</h3>
          <p>
            Cyber Khabar Headquarters<br />
            1234 Digital Security Blvd,<br />
            Tech City, Cyber State,<br />
            12345-6789, India
          </p>
        </div>
        <div class="footer-column">
          <h3>Contact Us</h3>
          <p>Phone: +1(800) 123-4567</p>
          <p>Email: contact@cyberkhabar.co</p>
        </div>
      </div>
      <div class="footer-bottom">
        <p>&copy; 2024 Cyber Khabar. All Rights Reserved.</p>
      </div>
    </footer>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "DataBreachPage",
  data() {
    return {
      report: {
        title: "",
        date: "",
        summary: "",
        details: "",
        stepsTaken: "",
        downloadUrl: ""
      },
      keyDetails: [],
      insights: [],
      sources: [],
    };
  },
  methods: {
    async fetchData() {
      try {
        // Fetch report data
        const reportResponse = await axios.get("http://localhost:3000/api/report");
        this.report = reportResponse.data;

        // Fetch key details, insights, and sources (You can create more API routes for these)
        const keyDetailsResponse = await axios.get("http://localhost:3000/api/key-details");
        this.keyDetails = keyDetailsResponse.data;

        const insightsResponse = await axios.get("http://localhost:3000/api/insights");
        this.insights = insightsResponse.data;

        const sourcesResponse = await axios.get("http://localhost:3000/api/sources");
        this.sources = sourcesResponse.data;
      } catch (error) {
        console.error("Error fetching data", error);
      }
    }
  },
  created() {
    this.fetchData();
  }
};
</script>
<style scoped>
/* General Styles */
.container {
  font-family: 'Roboto', sans-serif;
  color: #d9faff;
  background-color: #101320;
  padding: 20px;
  line-height: 1.6;
}

/* Body and General Settings */
body {
  margin: 0;
  font-family: 'Roboto', sans-serif;
  background-color: #101320;
  color: #d9faff;
}

/* Container */
.container {
  margin: 0 auto;
  padding: 20px;
}

/* Header */
.header {
  background-color: rgba(0, 0, 0, 0.9);
  padding: 10px 20px;
  position: sticky;
  top: 0;
  z-index: 1000;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #0ff;
  box-shadow: 0 0 10px #0ff;
}

.logo {
  font-size: 24px;
  font-weight: bold;
  color: #00ffcc;
}

.navbar {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
}
.nav-items {
  display: flex;
  align-items: center;
}
.search-bar {
  padding: 5px;
  font-size: 14px;
  margin-right: 20px;
  border: 1px solid #00ffcc;
  border-radius: 5px;
  background-color: #101320;
  color: #00ffcc;
}

.nav-links {
  display: flex;
  gap: 20px;
}

.nav-link {
  color: #00ffcc;
  text-decoration: none;
  font-size: 14px;
  padding: 5px 10px;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.nav-link:hover {
  background-color: #00ccaa;
}

.menu-icon {
  display: none;
  font-size: 24px;
  cursor: pointer;
  color: #00ffcc;
}

.mobile-menu {
  background-color: rgba(0, 0, 0, 0.9);
  position: absolute;
  top: 60px;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.mobile-link {
  color: #00ffcc;
  text-decoration: none;
  padding: 10px;
  font-size: 16px;
}

.mobile-link:hover {
  background-color: #00ccaa;
}

/* Summary, Key Details, Insights, and Sources */
.summary,
.key-details,
.insights,
.sources {
  text-align: left;
  margin-top: 20px;
  background-color: rgba(0, 0, 0, 0.8);
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 15px #0ff;
  border: 1px solid #0ff;
}
.summary-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 10px;
   margin-left: 200px;
}

.summary-header h1 {
  margin: 0;
  font-size: 24px;
  color: #0ff;
}

.download-btn {
  text-decoration: none;
  background-color: #0ff;
  color: #101320;
  font-size: 14px;
  font-weight: bold;
  padding: 10px 15px;
  border-radius: 5px;
  transition: 0.3s;
  box-shadow: 0 0 10px #0ff;
}

.download-btn:hover {
  background-color: #00bcd4;
  box-shadow: 0 0 15px #00bcd4;
  color: #d9faff;
}
.summary h1,
.summary h5 {
  text-align: center;
  color: #d9faff;
}

.key-details ul,
.insights ul,
.sources ul {
  list-style: none;
  padding: 0;
}

.key-details li,
.insights li,
.sources li {
  margin-bottom: 10px;
  display: flex;
  align-items: flex-start;
  color: #d9faff;
}

.key-details li .icon,
.insights li .icon,
.sources li .icon {
  margin-right: 8px;
  font-size: 16px;
  color: #0ff;
}

.nested-list li {
  margin-left: 20px;
}

/* Footer */
.footer {
  background-color: rgba(0, 0, 0, 0.9);
  padding: 30px;
  color: #d9faff;
  border-top: 1px solid #0ff;
  box-shadow: 0 -5px 15px #0ff;
}

.footer-container {
  display: flex;
  justify-content: space-between;
}

.footer-column ul {
  list-style: none;
  padding: 0;
}

.footer-column ul li a {
  color: #d9faff;
  text-decoration: none;
}

.footer-column ul li a:hover {
  color: #00ccaa;
}
</style>
