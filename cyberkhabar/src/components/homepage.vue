<template>
  <div id="app">
    <div class="header">
      <div class="title">
        <h1>CyberKhabar</h1>
      </div>
      <div class="auth-buttons">
        <button class="login-btn">Login</button>
        <button class="signup-btn">Sign Up</button>
      </div>
    </div>

    <div class="dashboard">
      <!-- Left Filters -->
      <aside class="filters">
        <h3><i class="fas fa-filter"></i> Filters</h3>
        <div class="filter-section">
          <h4><i class="fas fa-shield-alt"></i> Type of Attack</h4>
          <div v-for="type in attackTypes" :key="type" class="filter-item">
            <input type="checkbox" :id="type" :value="type" v-model="selectedFilters.type" />
            <label :for="type">{{ type }}</label>
          </div>
        </div>
        <div class="filter-section">
          <h4><i class="fas fa-exclamation-triangle"></i> Impact Level</h4>
          <div v-for="level in impactLevels" :key="level" class="filter-item">
            <input type="checkbox" :id="level" :value="level" v-model="selectedFilters.impact" />
            <label :for="level">{{ level }}</label>
          </div>
        </div>
        <div class="filter-section">
          <h4><i class="fas fa-globe"></i> Area of Attack</h4>
          <div v-for="location in locations" :key="location" class="filter-item">
            <input type="checkbox" :id="location" :value="location" v-model="selectedFilters.location" />
            <label :for="location">{{ location }}</label>
          </div>
        </div>
        <div class="filter-section">
          <h4><i class="fas fa-star"></i> Relevance</h4>
          <input type="range" v-model="selectedFilters.relevance" min="1" max="100" />
          <label>{{ selectedFilters.relevance }}%</label>
        </div>
        <div class="filter-section">
          <h4><i class="fas fa-clock"></i> Recency</h4>
          <select v-model="selectedFilters.recency">
            <option value="1">Last Day</option>
            <option value="7">Last Week</option>
            <option value="30">Last Month</option>
          </select>
        </div>
      </aside>

      <!-- Main Content -->
      <main class="content">
        <!-- Single line Marquee -->
        <div class="marquee">
          <div class="marquee-content">
            <span v-for="headline in newsHeadlines" :key="headline.id" class="marquee-item">
              {{ headline.title }}     |    
            </span>
          </div>
        </div>

        <!-- News Display with Infinite Scroll -->
        <section class="news" v-infinite-scroll="loadMore">
          <h2><i class="fas fa-newspaper"></i> Cyber Threat Updates</h2>
          <div class="news-container">
            <div v-for="news in filteredNews" :key="news.id" class="news-item">
              <img :src="news.image" :alt="news.title" class="news-image"/>
              <div class="news-content">
                <h3>{{ news.title }}</h3>
                <p>{{ news.description }}</p>
                <router-link :to="'/news/' + news.id" class="read-more">Read More →</router-link>
              </div>
            </div>
          </div>
        </section>
      </main>

    <!-- Right Statistics -->
    <aside class="statistics">
      <h3><i class="fas fa-chart-line"></i> Current Status</h3>
      <div class="stats-item">
        <i class="fas fa-radiation-alt"></i>
        <span>Severity: {{ currentStats.severity }}</span>
      </div>
      <div class="stats-item">
        <i class="fas fa-tag"></i>
        <span>Category: {{ currentStats.category }}</span>
      </div>
      <div class="stats-item">
        <i class="fas fa-globe"></i>
        <span>Origin: {{ currentStats.origin }}</span>
      </div>
      <div class="stats-item">
        <i class="fas fa-calendar-alt"></i>
        <span>First Seen: {{ currentStats.firstSeen }}</span>
      </div>
      <div class="stats-item">
        <i class="fas fa-history"></i>
        <span>Last Seen: {{ currentStats.lastSeen }}</span>
      </div>
      <div class="related-incidents">
        <h4>Related Incidents</h4>
        <span class="incident-number">{{ currentStats.relatedIncidents }}</span>
        <span class="incident-text">incidents</span>
      </div>
    </aside>
  </div>
</template>

<style>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 20px;
  background-color: #1a1b26;
}

.title h1 {
  font-family: 'Blender Pro', 'Orbitron', sans-serif;
  font-size: 2.5em;
  color: #00ff88;
  text-transform: uppercase;
  margin: 0;
  letter-spacing: 2px;
  text-shadow: 0 0 10px rgba(0, 255, 136, 0.5);
}

.auth-buttons {
  display: flex;
  gap: 15px;
}

.login-btn, .signup-btn {
  font-family: 'Share Tech Mono', monospace;
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 1em;
  transition: all 0.3s ease;
}

.login-btn {
  background-color: transparent;
  border: 2px solid #00ff88;
  color: #00ff88;
}

.signup-btn {
  background-color: #00ff88;
  color: #1a1b26;
}

.login-btn:hover {
  background-color: rgba(0, 255, 136, 0.1);
  transform: translateY(-2px);
}

.signup-btn:hover {
  background-color: #00cc6a;
  transform: translateY(-2px);
}

/* Your existing styles remain the same */
</style>

<script>
export default {
  data() {
    return {
      // Mock data for news headlines but add the backend logic here to get data from the database ~vanessa 
      attackTypes: [
        "Phishing",
        "Hacking and Exploits",
        "Ransomware",
        "Malware",
      ],
      impactLevels: ["Low", "Medium", "High"],
      locations: ["USA", "Europe", "Asia", "Global"],
      selectedFilters: {
        type: [],
        impact: [],
        location: [],
        relevance: 50,
        recency: "7",
      },
      newsHeadlines: [
        { id: 1, title: "Major Cyber Attack Disrupts Energy Sector" },
        { id: 2, title: "Data Breach Impacts Millions of Users" },
      ],
      news: [
        {
          id: 1,
          title: "Former Fortnite Player Accused of Meme Coin Scam",
          description:
            "An Australian former Fortnite player has been accused of stealing $3.5M through meme coin scams.",
          image: "/images/crypto-scam.jpg",
        },
        {
          id: 2,
          title: "Major Banking System Breach Detected",
          description: "Several banks report unauthorized access attempts from sophisticated threat actors.",
          image: "/images/bank-breach.jpg",
        },
        {
          id: 3,
          title: "New Ransomware Strain Targets Healthcare",
          description: "Healthcare facilities worldwide on high alert as new ransomware variant emerges.",
          image: "/images/healthcare-cyber.jpg",
          image: "/images/crypto-scam.jpg",
        },
        {
          id: 2,
          title: "Major Banking System Breach Detected",
          description: "Several banks report unauthorized access attempts from sophisticated threat actors.",
          image: "/images/bank-breach.jpg",
        },
        {
          id: 3,
          title: "New Ransomware Strain Targets Healthcare",
          description: "Healthcare facilities worldwide on high alert as new ransomware variant emerges.",
          image: "/images/healthcare-cyber.jpg",
          image: "/images/crypto-scam.jpg",
        },
        {
          id: 2,
          title: "Major Banking System Breach Detected",
          description:
            "Several banks report unauthorized access attempts from sophisticated threat actors.",
          image: "/images/bank-breach.jpg",
        },
        {
          id: 3,
          title: "New Ransomware Strain Targets Healthcare",
          description:
            "Healthcare facilities worldwide on high alert as new ransomware variant emerges.",
          image: "/images/healthcare-cyber.jpg",
        },
        // Add more news items
        // Add more news items
      ],
      currentStats: {
        severity: "Critical",
        category: "IP Address",
        origin: "External",
        firstSeen: "Today",
        lastSeen: "1 hour ago",
        relatedIncidents: 30,
      },
    };
  },
  // perfect ~vanessa 
  computed: {
    filteredNews() {
      return this.news.filter((item) => {
        return (
          (this.selectedFilters.type.length === 0 ||
            this.selectedFilters.type.includes(item.type)) &&
          (this.selectedFilters.impact.length === 0 ||
            this.selectedFilters.impact.includes(item.impact))
        );
      });
    },
  },
  methods: {
    loadMore() {
      // Implement infinite scroll logic
      //imcomplete yet to be done ~vanessa 
      const page = Math.ceil(this.news.length / 10) + 1;
            const loading = true;
            
            // Simulating API call with setTimeout
            setTimeout(async () => {
              try {
                // Replace this with actual API call
                const response = await fetch(`/api/news?page=${page}&limit=10`);
                const newItems = await response.json();
                
                if (newItems.length > 0) {
                  this.news = [...this.news, ...newItems];
                }
                
                loading = false;
              } catch (error) {
                console.error('Error loading more news:', error);
                loading = false;
              }
            }, 1000);
      
    },
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700&display=swap');

@import url("https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Orbitron:wght@400;700&display=swap");
.dashboard {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  gap: 20px;
  padding: 20px;
  font-family: "Share Tech Mono", monospace;
  background-color: #1a1b26;
}

.filters, .statistics {
  background-color: #292c36;
  border-radius: 10px;
  padding: 20px;
  text-align: left;
}

.filter-section {
  margin-bottom: 20px;
  padding: 20px;
  text-align: left;
}
.filter-section {
  margin-bottom: 20px;
}

.filter-item {
  padding: 5px 0;
  transition: all 0.3s ease;
}

.filter-item:hover {
  background-color: #3c3f4a;
.filter-item {
  padding: 5px 0;
  transition: all 0.3s ease;
}
.filter-item:hover {
  background-color: #3c3f4a;
}

.marquee {
  background-color: #3c3f4a;
  padding: 10px;
  white-space: nowrap;
  overflow: hidden;
}

.marquee-content {
  display: inline-block;
  animation: marquee 20s linear infinite;
}

.news-container {
  display: grid;
  gap: 20px;
  white-space: nowrap;
  overflow: hidden;
}
.marquee-content {
  display: inline-block;
  animation: marquee 20s linear infinite;
}
.news-container {
  padding-top:10px;
  display: grid;
  gap: 20px;
  /* overflow-y: scroll;
  max-height: 60%; */
}

.news-item {
  background-color: #3c3f4a;
  border-radius: 10px;
  overflow: hidden;
  transition: transform 0.3s ease;
}
.news-item:hover {
  transform: translateY(-5px);
}
.news-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}
.incident-number {
  font-family: "Orbitron", sans-serif;
  font-size: 3em;
  color: #00ff88;
  display: block;
  text-align: center;
}
.incident-text {
  font-family: "Orbitron", sans-serif;
  font-size: 1.2em;
  color: #ffffff;
  display: block;
  text-align: center;
}
h2,
h3,
h4 {
  font-family: "Orbitron", sans-serif;
  color: #00ff88;
}
@keyframes marquee {
  0% {
    transform: translateX(100%);
  }
  100% {
    transform: translateX(-100%);
  }
}
.read-more {
  color: #00ff88;
  text-decoration: none;
  font-weight: bold;
}
.stats-item {
  display: flex;
  align-items: center;
  gap: 10px;
  background-color: #3c3f4a;
  border-radius: 10px;
  overflow: hidden;
  transition: transform 0.3s ease;
}

.news-item:hover {
  transform: translateY(-5px);
}

.news-image {
  width: 100%;
  height: 200px;
  object-fit: cover;
}

.incident-number {
  font-family: "Orbitron", sans-serif;
  font-size: 3em;
  color: #00ff88;
  display: block;
  text-align: center;
}
h2, h3, h4 {
  font-family: 'Orbitron', sans-serif;
  color: #00ff88;
}

@keyframes marquee {
  0% { transform: translateX(100%); }
  100% { transform: translateX(-100%); }
}

.read-more {
  color: #00ff88;
  text-decoration: none;
  font-weight: bold;
}
.stats-item {
  display: flex;
  align-items: center;
  gap: 10px;
  margin: 10px 0;
}
/* Add hover effects for interactivity */
.filter-item:hover, .stats-item:hover {
  cursor: pointer;
  background-color: #3c3f4a;
  border-radius: 5px;
  padding-left: 10px;
}
</style>
