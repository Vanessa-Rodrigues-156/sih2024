<template>
  <div id="news-page" class="bright-theme">
    <header>
      <h1>Cyber News Portal</h1>
    </header>

    <div class="container">
      <!-- Filters Section -->
      <aside class="filters">
        <h2>Filters</h2>
        <label for="type">Incident Type</label>
        <select v-model="filters.incidentType">
          <option disabled value="">Select Type</option>
          <option v-for="type in incidentTypes" :key="type">{{ type }}</option>
        </select>

        <label for="severity">Severity</label>
        <select v-model="filters.severity">
          <option disabled value="">Select Severity</option>
          <option v-for="severity in severities" :key="severity">{{ severity }}</option>
        </select>

        <label for="impact">Impact</label>
        <select v-model="filters.impact">
          <option disabled value="">Select Impact</option>
          <option v-for="impact in impacts" :key="impact">{{ impact }}</option>
        </select>

        <button @click="applyFilters">Apply Filters</button>
      </aside>

      <!-- News Section -->
      <main class="news">
        <h2>Latest Cybersecurity News</h2>
        <div v-for="article in filteredNews" :key="article.id" class="news-item">
          <h3>{{ article.title }}</h3>
          <p>{{ article.content }}</p>
        </div>
      </main>

      <!-- Stats Section -->
      <aside class="stats">
        <h2>Insights</h2>
        <p><strong>Most Trending Topic:</strong> {{ stats.trendingTopic }}</p>
        <p><strong>Top Contributing Region:</strong> {{ stats.topRegion }}</p>
        <p><strong>Total Articles Published Today:</strong> {{ stats.totalArticles }}</p>
        <p><strong>Top Viewed Article:</strong> "{{ stats.topArticle }}"</p>
      </aside>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      incidentTypes: [
        "Phishing",
        "Malware",
        "DDoS Attack",
        "Data Breach",
        "Unauthorized Access",
        "Ransomware",
        "Spyware",
      ],
      severities: ["Low", "Medium", "High", "Critical"],
      impacts: ["Financial Loss", "Data Loss", "Reputation Damage", "Service Disruption", "Legal Issues"],
      filters: {
        incidentType: "",
        severity: "",
        impact: "",
      },
      newsArticles: [
        {
          id: 1,
          title: "Massive Phishing Attack Targets Users Worldwide",
          content: "A phishing scam targeting users of a major social media platform has compromised over 1 million accounts...",
          type: "Phishing",
          severity: "High",
          impact: "Reputation Damage",
        },
        {
          id: 2,
          title: "Malware Strikes Top Financial Institutions",
          content: "Malware found in the network of top financial institutions is causing disruptions in digital banking services...",
          type: "Malware",
          severity: "Critical",
          impact: "Data Loss",
        },
        {
          id: 3,
          title: "Massive DDoS Attack Cripples Major Websites",
          content: "A DDoS attack has taken down several major e-commerce websites, causing millions of dollars in lost revenue...",
          type: "DDoS Attack",
          severity: "High",
          impact: "Service Disruption",
        },
        {
          id: 4,
          title: "Data Breach Exposes Personal Information of 500k Users",
          content: "A data breach in a popular e-commerce platform has exposed the personal data of over 500,000 users...",
          type: "Data Breach",
          severity: "Critical",
          impact: "Data Loss",
        },
      ],
      stats: {
        trendingTopic: "Data Breach",
        topRegion: "North India",
        totalArticles: 247,
        topArticle: "Massive Phishing Attack Targets Users Worldwide",
      },
    };
  },
  computed: {
    filteredNews() {
      return this.newsArticles.filter((article) => {
        return (
          (!this.filters.incidentType ||
            article.type === this.filters.incidentType) &&
          (!this.filters.severity || article.severity === this.filters.severity) &&
          (!this.filters.impact || article.impact === this.filters.impact)
        );
      });
    },
  },
  methods: {
    applyFilters() {
      console.log("Filters applied:", this.filters);
    },
  },
};
</script>

<style scoped>
/* General Styles */
.bright-theme {
  background-color: #101320;
  color: #ffffff; /* Brighter White Font */
  font-family: "Roboto", sans-serif;
}

header {
  background-color: #1a1a3d;
  padding: 10px 0;
  text-align: center;
  color: #0ff;
  box-shadow: 0 0 10px #0ff;
}

.container {
  display: flex;
  padding: 20px;
  gap: 20px;
}

/* Filters */
.filters {
  flex: 1;
  padding: 10px;
  background-color: #1a1a3d;
  border-radius: 5px;
  box-shadow: 0 0 5px #0ff;
}

.filters h2 {
  text-align: center;
  color: #ffffff;
}

.filters label {
  display: block;
  margin: 10px 0 5px;
}

.filters select,
.filters button {
  width: 100%;
  padding: 8px;
  margin-bottom: 10px;
  border: 1px solid #0ff;
  border-radius: 5px;
  background-color: #101320;
  color: #ffffff;
}

/* News */
.news {
  flex: 2;
  padding: 10px;
}

.news h2 {
  margin-bottom: 10px;
  color: #ffffff;
}

.news-item {
  background-color: #1a1a3d;
  border: 1px solid #0ff;
  border-radius: 5px;
  padding: 10px;
  margin-bottom: 10px;
  box-shadow: 0 0 5px #0ff;
}

.news-item h3 {
  color: #0ff;
}

.news-item p {
  color: #ffffff;
}

/* Stats */
.stats {
  flex: 1;
  padding: 10px;
  background-color: #1a1a3d;
  border-radius: 5px;
  box-shadow: 0 0 5px #0ff;
}

.stats h2 {
  text-align: center;
  color: #ffffff;
}

.stats p {
  margin: 10px 0;
  color: #ffffff;
}
</style>
