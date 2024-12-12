<template>
  <div id="app">
    <div class="min-h-screen w-full bg-slate-900">
      <!-- Header -->
      <div class="flex justify-between items-center px-6 py-4 bg-slate-800">
        <div class="title">
          <h1 class="text-3xl font-bold text-blue-400">CyberKhabar</h1>
        </div>
        <div class="flex gap-4">
          <button class="px-4 py-2 text-blue-400 border border-blue-400 rounded-md hover:bg-blue-400/10 transition-all">
            Reload
          </button>
        </div>
      </div>

      <!-- Search Bar (Below Header) -->
      <div class="w-full bg-slate-800 py-4 px-6">
        <input 
          type="text" 
          class="w-full px-6 py-3 bg-slate-700 rounded-md text-slate-200" 
          placeholder="Search News..." 
          v-model="searchQuery" 
        />
      </div>

      <!-- Main Content (Flex Container) -->
      <div class="flex px-6 py-6 gap-6">
        <!-- Left Filters (Dropdowns) -->
        <aside class="bg-slate-800 rounded-lg p-6 w-1/4 max-w-xs flex-shrink-0">
          <h3 class="text-xl font-semibold text-blue-400 mb-4">
            <i class="fas fa-filter"></i> Filters
          </h3>
          <div class="space-y-6">
            <!-- Filter Section 1: Date Range -->
            <div>
              <h4 class="text-lg font-semibold text-slate-200 mb-2">Date Range</h4>
              <select class="w-full px-3 py-2 bg-slate-700 rounded-md border-none text-slate-200">
                <option>Last 24 hours</option>
                <option>Last Week</option>
                <option>Last Month</option>
              </select>
            </div>

            <!-- Filter Section 2: Severity -->
            <div>
              <h4 class="text-lg font-semibold text-slate-200 mb-2">Severity</h4>
              <select class="w-full px-3 py-2 bg-slate-700 rounded-md border-none text-slate-200">
                <option>Low</option>
                <option>Medium</option>
                <option>High</option>
                <option>Critical</option>
              </select>
            </div>

            <!-- Filter Section 3: Location -->
            <div>
              <h4 class="text-lg font-semibold text-slate-200 mb-2">Location</h4>
              <select class="w-full px-3 py-2 bg-slate-700 rounded-md border-none text-slate-200">
                <option>North India</option>
                <option>South India</option>
                <option>Cental India</option>
              </select>
            </div>

            <!-- Filter Section 4: Attack Type -->
            <div>
              <h4 class="text-lg font-semibold text-slate-200 mb-2">Attack Type</h4>
              <select class="w-full px-3 py-2 bg-slate-700 rounded-md border-none text-slate-200">
                <option>Ransomware</option>
                <option>Phishing</option>
                <option>DDoS</option>
                <option>Malware</option>
              </select>
            </div>
          </div>
        </aside>

        <!-- Main Content (Cyber Threat Updates) -->
        <main class="flex-1 space-y-6 max-w-2xl">
          <!-- Marquee for Flashing News (Inside Specific Box) -->
          <div class="bg-slate-700 p-3 mb-6 rounded-lg overflow-hidden">
            <div class="marquee-content text-slate-200 text-lg font-semibold">
              Flashing News: Ransomware Attack on Healthcare → Phishing Campaign Targets Banks → DDoS Attack on Government Websites...
            </div>
          </div>

          <!-- News Section (Cyber Threat Updates) -->
          <section class="bg-slate-800 rounded-lg p-6">
            <h2 class="text-2xl font-semibold text-blue-400 mb-4">
              <i class="fas fa-newspaper"></i> Cyber Threat Updates
            </h2>
            <div>
              <div v-for="news in filteredNews" :key="news.id" class="bg-slate-700 rounded-lg overflow-hidden hover:-translate-y-1 transition-transform mb-4">
                <div class="p-4">
                  <h3 class="text-slate-100 font-medium mb-2">{{ news.title }}</h3>
                  <p class="text-slate-400 mb-4">{{ news.description }}</p>
                  <router-link :to="'/news/' + news.id" class="text-blue-400 hover:text-blue-300 transition-colors">
                    Read More →
                  </router-link>
                </div>
              </div>
            </div>
          </section>
        </main>

        <!-- Right Statistics (Adjusted Content Size) -->
        <div class="bg-slate-800 rounded-lg p-6 flex flex-col justify-start">
          <h3 class="text-xl font-semibold text-blue-400 mb-4">
            <i class="fas fa-chart-line"></i> Current Status
          </h3>
          <div class="space-y-4">
            <div v-for="(value, key) in currentStats" :key="key" class="bg-slate-700 p-3 rounded-lg flex items-center gap-3 hover:bg-slate-600 transition-colors">
              <i :class="getStatsIcon(key)" class="text-blue-400"></i>
              <span class="text-slate-100">{{ key }}: {{ value }}</span>
            </div>
            <div class="mt-6 text-center">
              <span class="text-4xl font-bold text-blue-400 block">
                {{ currentStats.relatedIncidents }}
              </span>
              <span class="text-slate-400">Related Incidents</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'CyberKhabar',
  data() {
    return {
      attackTypes: [],
      impactLevels: [],
      locations: [],
      selectedFilters: {
        type: [],
        impact: [],
        location: [],
        recency: '7',
      },
      news: [],
      currentStats: {
        'Active Threats': 0,
        'Resolved Incidents': 0,
        'Pending Alerts': 0,
        relatedIncidents: 0,
      },
      searchQuery: '', // New data property for search query
    };
  },
  computed: {
    filteredNews() {
      const query = this.searchQuery.toLowerCase().split(/\s+/); // Split search query into keywords

      // Function to count the number of keyword matches in a title
      const countKeywordMatches = (title, query) => {
        return query.reduce((count, keyword) => {
          return title.includes(keyword) ? count + 1 : count;
        }, 0);
      };

      // Sort the news based on keyword matches in descending order
      return this.news
        .map((newsItem) => ({
          ...newsItem,
          matchCount: countKeywordMatches(newsItem.title.toLowerCase(), query),
        }))
        .filter((newsItem) => newsItem.matchCount > 0) // Filter out news with no matches
        .sort((a, b) => b.matchCount - a.matchCount); // Sort by match count in descending order
    },
  },
  methods: {
    getStatsIcon(key) {
      const icons = {
        'Active Threats': 'fas fa-exclamation-triangle',
        'Resolved Incidents': 'fas fa-check-circle',
        'Pending Alerts': 'fas fa-clock',
      };
      return icons[key] || 'fas fa-info-circle';
    },
    async fetchNews() {
      const response = await fetch('http://localhost:5001/api/news');
      this.news = await response.json();
    },
    async fetchAttackTypes() {
      const response = await fetch('http://localhost:5001/api/attack-types');
      this.attackTypes = await response.json();
    },
    async fetchImpactLevels() {
      const response = await fetch('http://localhost:5001/api/impact-levels');
      this.impactLevels = await response.json();
    },
    async fetchLocations() {
      const response = await fetch('http://localhost:5001/api/locations');
      this.locations = await response.json();
    },
    async fetchCurrentStats() {
      const response = await fetch('http://localhost:5001/api/current-stats');
      this.currentStats = await response.json();
    },
  },
  async created() {
    try {
      await Promise.all([
        this.fetchNews(),
        this.fetchAttackTypes(),
        this.fetchImpactLevels(),
        this.fetchLocations(),
        this.fetchCurrentStats(),
      ]);
    } catch (error) {
      console.error('Error fetching data:', error);
    }
  },
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html,
body {
  margin: 0;
  padding: 0;
  overflow-x: hidden;
}

#app {
  max-width: 100%;
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.marquee-content {
  display: inline-block;
  white-space: nowrap;
  animation: marquee 20s linear infinite;
}

@keyframes marquee {
  0% {
    transform: translateX(100%);
  }
  100% {
    transform: translateX(-100%);
  }
}
</style>
