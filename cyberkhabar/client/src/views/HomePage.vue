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
        <input type="text" class="w-full px-6 py-3 bg-slate-700 rounded-md text-slate-200" placeholder="Search News..." />
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
                <option>North America</option>
                <option>Europe</option>
                <option>Asia</option>
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
      attackTypes: ['Ransomware', 'Phishing', 'DDoS', 'Malware'],
      impactLevels: ['High', 'Medium', 'Low'],
      locations: ['North America', 'Europe', 'Asia'],
      selectedFilters: {
        type: [],
        impact: [],
        location: [],
        recency: '7'
      },
      news: [
        {
          id: 1,
          title: 'Ransomware Attack on Healthcare',
          description: 'A major ransomware attack has affected healthcare facilities...',
          image: 'path/to/image1.jpg'
        },
        {
          id: 2,
          title: 'Phishing Campaign Targets Banks',
          description: 'A new phishing campaign is targeting major banks...',
          
        },
        {
          id: 3,
          title: 'DDoS Attack on Government Websites',
          description: 'Government websites have been hit by a DDoS attack...',
          
        },
        {
          id:4,
          title:'Cosmos Bank Cyber Attack',
          description:'Banking transaction and customer data was stolen...'
        }
      ],
      currentStats: {
        'Active Threats': 5,
        'Resolved Incidents': 12,
        'Pending Alerts': 3,
        relatedIncidents: 20
      }
    };
  },
  computed: {
    filteredNews() {
      return this.news.filter(newsItem => {
        return (
          (this.selectedFilters.type.length === 0 || this.selectedFilters.type.includes(newsItem.type)) &&
          (this.selectedFilters.impact.length === 0 || this.selectedFilters.impact.includes(newsItem.impact)) &&
          (this.selectedFilters.location.length === 0 || this.selectedFilters.location.includes(newsItem.location))
        );
      });
    }
  },
  methods: {
    getStatsIcon(key) {
      const icons = {
        'Active Threats': 'fas fa-exclamation-triangle',
        'Resolved Incidents': 'fas fa-check-circle',
        'Pending Alerts': 'fas fa-clock'
      };
      return icons[key] || 'fas fa-info-circle';
    }
  }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

html, body {
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