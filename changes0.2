<template>
  <div id="app" class="dashboard">
    <!-- Left Filters -->
    <aside class="filters">
      <h3>Filters</h3>
      <div>
        <h4>Type of Attack</h4>
        <div v-for="type in attackTypes" :key="type">
          <input type="checkbox" :id="type" :value="type" v-model="selectedFilters.type" />
          <label :for="type">{{ type }}</label>
        </div>
      </div>
      <div>
        <h4>Impact Level</h4>
        <div v-for="level in impactLevels" :key="level">
          <input type="checkbox" :id="level" :value="level" v-model="selectedFilters.impact" />
          <label :for="level">{{ level }}</label>
        </div>
      </div>
      <div>
        <h4>Area of Attack</h4>
        <div v-for="location in locations" :key="location">
          <input type="checkbox" :id="location" :value="location" v-model="selectedFilters.location" />
          <label :for="location">{{ location }}</label>
        </div>
      </div>
      <div>
        <h4>Relevance</h4>
        <input type="range" v-model="selectedFilters.relevance" min="1" max="100" />
        <label>{{ selectedFilters.relevance }}%</label>
      </div>
      <div>
        <h4>Recency</h4>
        <select v-model="selectedFilters.recency">
          <option value="1">Last Day</option>
          <option value="7">Last Week</option>
          <option value="30">Last Month</option>
        </select>
      </div>
    </aside>

    <!-- Main Content -->
    <main class="content">
      <!-- Marquee -->
      <div class="marquee">
        <marquee>
          <div v-for="headline in newsHeadlines" :key="headline.id" class="marquee-item">
            {{ headline.title }}
          </div>
        </marquee>
      </div>

      <!-- News Display -->
      <section class="news">
        <h2>Major Ransomware Attack Disrupts</h2>
        <div class="news-item" v-for="news in filteredNews" :key="news.id">
          <img :src="news.image" alt="news" />
          <h3>{{ news.title }}</h3>
          <p>{{ news.description }}</p>
        </div>
      </section>
    </main>

    <!-- Right Statistics -->
    <aside class="statistics">
      <h3>Current Status</h3>
      <p>Severity: {{ currentStats.severity }}</p>
      <p>Category: {{ currentStats.category }}</p>
      <p>Origin: {{ currentStats.origin }}</p>
      <p>First Seen: {{ currentStats.firstSeen }}</p>
      <p>Last Seen: {{ currentStats.lastSeen }}</p>
      <h4>Related Incidents</h4>
      <p>{{ currentStats.relatedIncidents }} incidents</p>
    </aside>
  </div>
</template>

<script>
export default {
  data() {
    return {
      attackTypes: ["Phishing", "Hacking and Exploits", "Ransomware", "Malware"],
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
          description: "An Australian former Fortnite player has been accused of stealing $3.5M through meme coin scams.",
          image: "path/to/image.jpg",
        },
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
  computed: {
    filteredNews() {
      return this.news.filter((item) => {
        return (
          (this.selectedFilters.type.length === 0 || this.selectedFilters.type.includes(item.type)) &&
          (this.selectedFilters.impact.length === 0 || this.selectedFilters.impact.includes(item.impact))
        );
      });
    },
  },
};
</script>

<style>
.dashboard {
  display: grid;
  grid-template-columns: 1fr 2fr 1fr;
  gap: 20px;
  padding-left: 20px;
  color: #fff;
}
.filters, .statistics {
  background-color: #292c36;
  border-radius: 10px;
  padding: 15px;
}
.content {
  background-color: #2e313c;
  border-radius: 10px;
  padding: 15px;
}
.marquee {
  background-color: #3c3f4a;
  padding: 10px;
  border-radius: 8px;
  margin-bottom: 20px;
}
.news-item {
  margin: 10px 0;
  padding: 10px;
  background-color: #3c3f4a;
  border-radius: 5px;
}
</style>
