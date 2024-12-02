
<template>
  <div class="dashboard-container">
    <!-- Threat Intelligence Dashboard -->
    <div class="threat-dashboard">
      <h2 class="dashboard-title">Threat Intelligence Dashboard</h2>
      
      <div class="stats-grid">
        <div class="stat-card">
          <h3>Active Threats</h3>
          <div class="stat-value">247</div>
          <div class="stat-trend up">+12% ↑</div>
        </div>
        <div class="stat-card">
          <h3>Critical Vulnerabilities</h3>
          <div class="stat-value">18</div>
          <div class="stat-trend down">-5% ↓</div>
        </div>
        <div class="stat-card">
          <h3>Security Incidents</h3>
          <div class="stat-value">34</div>
          <div class="stat-trend up">+8% ↑</div>
        </div>
        <div class="stat-card">
          <h3>Threat Score</h3>
          <div class="stat-value">7.8</div>
          <div class="stat-indicator high">High</div>
        </div>
      </div>

      <div class="threat-map">
        <h3>Global Threat Map</h3>
        <!-- Placeholder for threat map -->
        <div class="map-placeholder">
          Interactive Threat Map
        </div>
      </div>
    </div>

    <!-- News Feed Section -->
    <div class="news-feed">
      <h2 class="dashboard-title">Recent Security News</h2>
      
      <div class="news-list">
        <div class="news-item">
          <div class="news-date">Dec 15, 2023</div>
          <h3>Major Ransomware Attack Hits Global Infrastructure</h3>
          <p>Multiple organizations across Europe report sophisticated ransomware incidents...</p>
          <div class="news-tag critical">Critical</div>
        </div>

        <div class="news-item">
          <div class="news-date">Dec 14, 2023</div>
          <h3>New Zero-Day Vulnerability Discovered in Popular Framework</h3>
          <p>Security researchers uncover critical vulnerability affecting millions of applications...</p>
          <div class="news-tag high">High</div>
        </div>

        <div class="news-item">
          <div class="news-date">Dec 14, 2023</div>
          <h3>AI-Powered Cyber Attacks on the Rise</h3>
          <p>Experts warn about increasing sophistication of AI-driven cyber threats...</p>
          <div class="news-tag medium">Medium</div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.dashboard-container {
  padding: 2rem;
  background: #f8f9fa;
}

.dashboard-title {
  color: #2c3e50;
  margin-bottom: 1.5rem;
  font-size: 1.8rem;
}

.stats-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.stat-card {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  transition: transform 0.2s;
}

.stat-card:hover {
  transform: translateY(-5px);
}

.stat-card h3 {
  color: #6c757d;
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
}

.stat-value {
  font-size: 2rem;
  font-weight: bold;
  color: #2c3e50;
}

.stat-trend {
  font-size: 0.9rem;
  margin-top: 0.5rem;
}

.stat-trend.up {
  color: #28a745;
}

.stat-trend.down {
  color: #dc3545;
}

.stat-indicator {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border-radius: 15px;
  font-size: 0.8rem;
  margin-top: 0.5rem;
}

.stat-indicator.high {
  background: #ffecec;
  color: #dc3545;
}

.threat-map {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
  margin-bottom: 2rem;
}

.map-placeholder {
  height: 300px;
  background: #f8f9fa;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
  color: #6c757d;
}

.news-feed {
  background: white;
  padding: 1.5rem;
  border-radius: 12px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.05);
}

.news-list {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.news-item {
  padding: 1rem;
  border-radius: 8px;
  background: #f8f9fa;
  transition: background-color 0.2s;
}

.news-item:hover {
  background: #e9ecef;
}

.news-date {
  font-size: 0.8rem;
  color: #6c757d;
}

.news-item h3 {
  margin: 0.5rem 0;
  color: #2c3e50;
  font-size: 1.1rem;
}

.news-item p {
  color: #6c757d;
  font-size: 0.9rem;
  margin-bottom: 0.5rem;
}

.news-tag {
  display: inline-block;
  padding: 0.25rem 0.75rem;
  border-radius: 15px;
  font-size: 0.8rem;
}

.news-tag.critical {
  background: #ffecec;
  color: #dc3545;
}

.news-tag.high {
  background: #fff3cd;
  color: #856404;
}

.news-tag.medium {
  background: #e2e3e5;
  color: #383d41;
}
</style>

<script>
export default {
  name: 'ThreatDashboard',
  data() {
    return {
      // Add reactive data here if needed
    }
  },
  methods: {
    // Add methods here if needed
  }
}
</script>
