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
          <a :href="report.downloadLink" download="DataBreach_Report" class="download-btn">Download Report</a>
        </div>
        <h3 class="date">{{ report.date }}</h3>
        <p>{{ report.summary }}</p>
      </section>

      <!-- Key Details Section -->
      <section v-if="report.details" class="key-details">
        <h2>Key Details</h2>
        <ul>
          <li v-for="(value, key) in report.details" :key="key">
            <strong>{{ formatKey(key) }}:</strong> 
            <template v-if="Array.isArray(value)">
              <ul>
                <li v-for="(item, index) in value" :key="index">{{ item }}</li>
              </ul>
            </template>
            <template v-else>{{ value }}</template>
          </li>
        </ul>
      </section>

      <!-- Insights Section -->
      <section v-if="report.insights.length" class="insights">
        <h2>Insights</h2>
        <ul>
          <li v-for="(insight, index) in report.insights" :key="index">
            <p>{{ insight.title }}</p>
            <p v-if="insight.description">{{ insight.description }}</p>
            <p v-if="insight.impact"><strong>Impact:</strong> {{ insight.impact }}</p>
          </li>
        </ul>
      </section>

      <!-- Sources Section -->
      <section v-if="report.sources.length" class="sources">
        <h2>🔗 Sources</h2>
        <ul>
          <li v-for="(source, index) in report.sources" :key="index">
            <a :href="source.url" target="_blank">{{ source.title }}</a>
          </li>
        </ul>
      </section>
    </main>

    <!-- Footer -->
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
import axios from 'axios';

export default {
  name: "DataBreachPage",
  data() {
    return {
      isMobileMenuOpen: false,
      report: {
        title: '',
        date: '',
        summary: '',
        downloadLink: '',
        details: {},
        insights: [],
        sources: []
      }
    };
  },
  methods: {
    toggleMenu() {
      this.isMobileMenuOpen = !this.isMobileMenuOpen;
    },
    fetchData() {
      axios
        .get("http://localhost:3000/api/reports")
        .then((response) => {
          const data = response.data || {};
          this.report = {
            title: data.title || 'No Title Available',
            date: data.date || 'Unknown Date',
            summary: data.summary || 'Summary not available.',
            downloadLink: data.reportLink || '',
            details: data.details || {},
            insights: data.insights || [],
            sources: data.sources || []
          };
        })
        .catch((error) => {
          console.error("Error fetching data:", error);
          this.report.summary = "Failed to load report details.";
        });
    },
    formatKey(key) {
      return key
        .replace(/([A-Z])/g, " $1")
        .replace(/^./, (str) => str.toUpperCase());
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
}
h1, h2 {
  color: #00ffcc;
}
h3 {
  color: #00ffcc;
  font-size: 16px;
  margin-top: 10px;
}
ul {
  list-style-type: none;
  padding-left: 20px;
}
li {
  margin-bottom: 10px;
}
.nested-list {
  padding-left: 20px;
}
.download-btn {
  background-color: #00ccaa;
  color: #fff;
  padding: 10px 20px;
  border-radius: 5px;
  text-decoration: none;
  font-weight: bold;
  transition: background-color 0.3s ease;
}
.download-btn:hover {
  background-color: #00ff66;
}
/* Footer */
.footer {
  margin-top: 20px;
  background-color: #101320;
  color: #d9faff;
  padding: 20px;
  border-top: 1px solid #0ff;
}
.footer-container {
  display: flex;
  justify-content: space-between;
  gap: 40px;
}
.footer-column h3 {
  color: #00ffcc;
}
.footer-column ul {
  list-style-type: none;
  padding-left: 0;
}
.footer-column li {
  margin-bottom: 10px;
}
.footer-column a {
  color: #d9faff;
  text-decoration: none;
  transition: color 0.3s ease;
}
.footer-column a:hover {
  color: #00ffcc;
}
.footer-bottom {
  text-align: center;
  margin-top: 20px;
}
@media (max-width: 768px) {
  .navbar {
    flex-direction: column;
  }
  .menu-icon {
    display: block;
  }
  .nav-items {
    flex-direction: column;
    align-items: flex-start;
  }
  .nav-links {
    display: none;
  }
  .mobile-menu {
    display: block;
  }
}
</style>
