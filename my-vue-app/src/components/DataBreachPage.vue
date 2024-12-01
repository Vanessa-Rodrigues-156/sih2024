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
      <h1>Massive Data Breach Exposes Over 20 Million User Accounts</h1>
      <a href="report.pdf" download="DataBreach_Report" class="download-btn">Download Report</a>
    </div>
    <h3 class="date">Date: August 27, 2024</h3>
    <p>
      A major social media platform has suffered a devastating breach,
      exposing personal data like usernames, email addresses, and encrypted
      passwords. This incident underscores the urgent need for strong
      cybersecurity measures and user awareness.
    </p>
    <p>
      Initial investigations reveal that attackers gained unauthorized
      access through a combination of sophisticated phishing campaigns and
      unpatched software vulnerabilities. The breach remained undetected
      for over 10 days, allowing the attackers to exfiltrate sensitive data
      with little resistance.
    </p>
    <p>
      The company has since taken immediate steps to contain the breach,
      including disabling compromised accounts, enhancing security protocols,
      and collaborating with law enforcement and cybersecurity experts to
      mitigate the damage.
    </p>
    <p>
      This breach not only impacts the platform's users but also raises
      serious concerns about the industry's preparedness against advanced
      persistent threats. It serves as a wake-up call for organizations
      worldwide to prioritize cybersecurity and adopt proactive measures.
    </p>
  </section>
      <!-- Key Details Section -->
      <section class="key-details">
        <h2>Key Details</h2>
        <ul>
          <li>
            <span class="icon">🔒</span>
            <strong>Platform Affected:</strong> Popular Social Media Platform
          </li>
          <li>
            <span class="icon">👥</span>
            <strong>Number of Users Affected:</strong> Over 20 million
          </li>
          <li>
            <span class="icon">📂</span>
            <strong>Types of Data Compromised:</strong>
            <ul class="nested-list">
              <li>🔑 Usernames</li>
              <li>📧 Email addresses</li>
              <li>🔐 Encrypted passwords</li>
              <li>💳 Credit card details (limited cases)</li>
            </ul>
          </li>
          <li>
            <span class="icon">⏱️</span>
            <strong>Breach Duration:</strong> 10 days (undetected)
          </li>
          <li>
            <span class="icon">🌐</span>
            <strong>Geographic Impact:</strong> Global, with the majority of
            affected users in the USA, UK, and India
          </li>
          <li>
            <span class="icon">📋</span>
            <strong>Current Status:</strong> Investigation ongoing; user
            notifications are being sent
          </li>
        </ul>
      </section>
      <!-- Insights Section -->
      <section class="insights">
        <h2>Insights</h2>
        <ul>
          <li>
            <span class="icon">⚠️</span>
            Cybersecurity experts indicate that the breach was likely the result
            of a sophisticated phishing campaign targeting employees of the
            platform.
          </li>
          <li>
            <span class="icon">🔧</span>
            Attackers exploited vulnerabilities in the backend infrastructure.
          </li>
          <li>
            <span class="icon">🔑</span>
            Multi-factor authentication (MFA) adoption among users could have
            mitigated some of the risks from this breach.
          </li>
          <li>
            <span class="icon">📊</span>
            Analysis suggests a 35% increase in credential reuse attacks after
            the breach was disclosed.
          </li>
          <li>
            <span class="icon">📈</span>
            Users should:
            <ul class="nested-list">
              <li>Use strong, unique passwords</li>
              <li>Enable two-factor authentication</li>
              <li>Monitor accounts for suspicious activity</li>
              <li>Regularly update privacy settings on social platforms</li>
            </ul>
          </li>
        </ul>
      </section>
      <!-- Images Section -->
      <section class="images">
        <h2>Visual Insights</h2>
        <div class="image-row">
          <img
            src="https://via.placeholder.com/400x200?text=Cyber+Security"
            alt="Cyber Security Visual 1"
          />
          <img
            src="https://via.placeholder.com/400x200?text=Data+Breach"
            alt="Cyber Security Visual 2"
          />
        </div>
      </section>
      <!-- Sources Section -->
      <section class="sources">
        <h2>🔗Sources</h2>
        <ul>
          <li>
            <span class="icon"></span>
            <a href="https://www.socialmedia-platform.com/news/data-breach">
              Official Company Statement
            </a>
          </li>
          <li>
            <span class="icon"></span>
            <a
              href="https://www.cybersecuritynews.com/data-breach-analysis"
            >
              Cybersecurity Expert Analysis
            </a>
          </li>
          <li>
            <span class="icon"></span>
            <a href="https://www.cybersecurity.gov/advisories/data-breach">
              Government Advisory
            </a>
          </li>
          <li>
            <span class="icon"></span>
            <a
              href="https://www.usersafety.org/testimonials/data-breach"
            >
              User Testimonials
            </a>
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
export default {
  name: "DataBreachPage",
  data() {
    return {
      isMobileMenuOpen: false,
    };
  },
  methods: {
    toggleMenu() {
      this.isMobileMenuOpen = !this.isMobileMenuOpen;
    },
  },
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
.summary h3 {
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