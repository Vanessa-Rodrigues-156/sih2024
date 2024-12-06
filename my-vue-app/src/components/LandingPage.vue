<template>
  <div id="landing-page">
    <div class="grid-container">
      <!-- Bottom Row Content (Swapped to Top Row) -->
      <section id="incident-timeline" class="grid-item" @click="zoomSection">
        <div class="timeline-container">
          <h2>Greatest Cybersecurity News by Year</h2>
          <div class="filter-container">
            <label for="year-filter">Filter by Year:</label>
            <select id="year-filter" v-model="selectedYear" @change="filterNews">
              <option value="">All Years</option>
              <option v-for="year in uniqueYears" :key="year" :value="year">{{ year }}</option>
            </select>
          </div>
          <div class="timeline">
            <div v-for="news in filteredNews" :key="news.year" class="timeline-item">
              <span class="year">{{ news.year }}</span>
              <p>{{ news.title }}</p>
              <p>{{ news.description }}</p>
            </div>
          </div>
        </div>
      </section>

      <section id="top-insights" class="grid-item" @click="zoomSection">
        <div class="insights-container">
          <h2>Top Insights for the Day</h2>
          <ul>
            <li>⚠️ Ransomware attacks surge by 30% globally in Q4.</li>
            <li>🌐 New zero-day vulnerabilities discovered in IoT devices.</li>
            <li>🔒 Passwordless authentication gaining popularity among enterprises.</li>
            <li>📊 Credential stuffing attacks up 20% compared to last year.</li>
          </ul>
        </div>
      </section>

      <!-- Top Row Content (Swapped to Bottom Row) -->
      <section id="about-us" class="grid-item" @click="zoomSection">
        <div class="about-container">
          <h2>About Us</h2>
          <p>
            At <strong>Cyber Khabar</strong>, we are dedicated to empowering individuals and organizations with the latest insights into cybersecurity threats and solutions.
            We aim to be your trusted source for understanding digital risks and improving online safety. Our mission is to make the digital world a safer place.
          </p>
          <p>
            Our team of cybersecurity experts delivers reliable, up-to-date news, resources, and educational content to help you mitigate threats and secure your personal and professional data.
          </p>
          <p>
            Whether you're an individual looking to enhance your cybersecurity knowledge, a business seeking to safeguard your operations, or a government organization aiming to improve national security, we are here to help.
          </p>
        </div>
      </section>

      <section id="resources" class="grid-item" @click="zoomSection">
        <div class="resources-container">
          <h2>Cybersecurity Resources</h2>
          <ul>
            <li><a href="https://us-cert.cisa.gov/" target="_blank">US-CERT (CISA) Official Cybersecurity Resources</a></li>
            <li><a href="https://www.cyberessentials.ncsc.gov.uk/" target="_blank">Cyber Essentials by NCSC</a></li>
            <li><a href="https://haveibeenpwned.com/" target="_blank">Check if your email is compromised: Have I Been Pwned</a></li>
            <li><a href="https://owasp.org/" target="_blank">OWASP (Open Web Application Security Project)</a></li>
            <li><a href="https://nvlpubs.nist.gov/nistpubs/CSWP/NIST.CSWP.04162018.pdf" target="_blank">NIST Cybersecurity Framework (PDF)</a></li>
            <li><a href="https://www.sans.org/" target="_blank">SANS Institute Cybersecurity Training and Resources</a></li>
            <li><a href="https://www.csoonline.com/" target="_blank">CSO Online Cybersecurity News</a></li>
          </ul>
        </div>
      </section>
    </div>
  </div>
</template>

<script>
export default {
  name: "LandingPage",
  data() {
    return {
      selectedYear: "",
      news: [
        { year: 1986, title: "First PC Virus: Brain", description: "The first PC virus, Brain, was created in Pakistan and marked the beginning of modern malware." },
        { year: 2000, title: "Love Bug Email Worm", description: "The Love Bug worm caused over $10 billion in damages globally through email propagation." },
        { year: 2017, title: "WannaCry Ransomware Attack", description: "A global ransomware attack infected over 200,000 systems, exploiting unpatched vulnerabilities." },
        { year: 2020, title: "SolarWinds Supply Chain Attack", description: "A sophisticated supply chain attack compromised thousands of organizations worldwide." },
        { year: 2024, title: "Major Data Breach", description: "A massive data breach exposed sensitive information of 5 million users globally." },
      ],
      filteredNews: [],
    };
  },
  computed: {
    uniqueYears() {
      return [...new Set(this.news.map((item) => item.year))].sort((a, b) => b - a);
    },
  },
  methods: {
    filterNews() {
      this.filteredNews = this.selectedYear
        ? this.news.filter((item) => item.year === parseInt(this.selectedYear))
        : this.news;
    },
    zoomSection(event) {
      const section = event.currentTarget;
      section.classList.add("zoom");
      setTimeout(() => section.classList.remove("zoom"), 300);
    },
  },
  mounted() {
    this.filterNews();
  },
};
</script>

<style scoped>
/* General styles remain unchanged */
/* General Styles */
#landing-page {
  background-color: black;
  color: #cce7ff;
  font-family: "Roboto", sans-serif;
  padding: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

/* Grid Layout */
.grid-container {
  display: grid;
  grid-template-columns: repeat(2, 1fr); /* 2 columns layout */
  grid-gap: 20px;
  max-width: 1200px;
  width: 100%;
}

.grid-item {
  background-color: #1a1a3d;
  padding: 20px;
  border-radius: 10px;
  box-shadow: 0 0 10px #0ff;
  cursor: pointer;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
  min-height: 220px; /* Reduced height for uniformity */
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

/* Scrollable content */
.grid-item .about-container,
.grid-item .resources-container,
.grid-item .insights-container,
.grid-item .timeline-container {
  overflow-y: auto;
  max-height: 200px; /* Limit height and make content scrollable */
}

/* Hide scrollbars but keep scrolling functionality */
.grid-item .about-container::-webkit-scrollbar,
.grid-item .resources-container::-webkit-scrollbar,
.grid-item .insights-container::-webkit-scrollbar,
.grid-item .timeline-container::-webkit-scrollbar {
  width: 0;
  height: 0;
}

/* Optional for Firefox */
.grid-item .about-container,
.grid-item .resources-container,
.grid-item .insights-container,
.grid-item .timeline-container {
  scrollbar-width: none; /* For Firefox */
}

.grid-item:hover {
  transform: scale(1.05);
  box-shadow: 0 0 20px #00ccff;
}

/* Zoom Effect */
.zoom {
  transform: scale(1.1);
  box-shadow: 0 0 25px #00ccff;
}

/* Section Titles */
h2 {
  text-align: center;
  color: #0ff;
  margin-bottom: 10px;
}

/* Links */
a {
  color: white;
  text-decoration: none;
}

a:hover {
  text-decoration: underline;
}

/* Insights List */
.insights-container ul {
  list-style: none;
  padding: 0;
}

.insights-container li {
  margin-bottom: 10px;
  display: flex;
  align-items: center;
  gap: 5px;
  font-size: 16px;
}

/* Timeline Section */
.filter-container {
  margin-bottom: 20px;
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 10px;
}

.filter-container label {
  color: #cce7ff;
}

.filter-container select {
  padding: 5px;
  border-radius: 5px;
  background-color: #101320;
  color: #0ff;
  border: 1px solid #0ff;
}

.timeline {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.timeline-item {
  padding: 10px;
  border: 1px solid #0ff;
  border-radius: 5px;
  background-color: #101320;
}

.timeline-item .year {
  font-weight: bold;
  font-size: 18px;
  color: #0ff;
}
</style>
