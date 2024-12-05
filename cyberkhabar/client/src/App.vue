<template>

    <div id="app">

        <div class="min-h-screen w-fit bg-slate-900">
            <!-- Header -->

            <div class="flex justify-between items-center px-6 py-4 bg-slate-800">

                <div class="title">
                    <h1 class="text-3xl font-bold text-blue-400">CyberKhabar</h1>
                </div>

                <div class="flex gap-4">
                    <button class="px-4 py-2 text-blue-400 border border-blue-400 rounded-md hover:bg-blue-400/10 transition-all">
                        Login
                    </button>
                    <button class="px-4 py-2 bg-blue-400 text-slate-900 rounded-md hover:bg-blue-500 transition-all">
                        Sign Up
                    </button>
                </div>
            </div>

            <div class="grid grid-cols-[1fr,1fr,1fr] gap-6 p-6">
                <!-- Left Filters -->
                <aside class="bg-slate-800 rounded-lg p-6">
                    <h3 class="text-xl font-semibold text-blue-400 mb-4">
                        <i class="fas fa-filter"></i> Filters
                    </h3>

                    <div class="space-y-6">

                        <div class="filter-section">
                            <h4 class="text-slate-100 font-medium mb-2">
                                <i class="fas fa-shield-alt"></i> Type of Attack
                            </h4>

                            <div v-for="type in attackTypes"
                                :key="type"
                                class="flex items-center py-2 px-3 hover:bg-slate-700 rounded transition-colors">
                                <input type="checkbox"
                                    :id="type"
                                    :value="type"
                                    v-model="selectedFilters.type"
                                    class="mr-2 accent-blue-400" />
                                <label :for="type"
                                    class="text-slate-400">{{ type }}</label>
                            </div>
                        </div>

                        <div class="filter-section">
                            <h4 class="text-slate-100 font-medium mb-2">
                                <i class="fas fa-exclamation-triangle"></i> Impact Level
                            </h4>

                            <div v-for="level in impactLevels"
                                :key="level"
                                class="flex items-center py-2 px-3 hover:bg-slate-700 rounded transition-colors">
                                <input type="checkbox"
                                    :id="level"
                                    :value="level"
                                    v-model="selectedFilters.impact"
                                    class="mr-2 accent-blue-400" />
                                <label :for="level"
                                    class="text-slate-400">{{ level }}</label>
                            </div>
                        </div>

                        <div class="filter-section">
                            <h4 class="text-slate-100 font-medium mb-2">
                                <i class="fas fa-globe"></i> Area of Attack
                            </h4>

                            <div v-for="location in locations"
                                :key="location"
                                class="flex items-center py-2 px-3 hover:bg-slate-700 rounded transition-colors">
                                <input type="checkbox"
                                    :id="location"
                                    :value="location"
                                    v-model="selectedFilters.location"
                                    class="mr-2 accent-blue-400" />
                                <label :for="location"
                                    class="text-slate-400">{{ location }}</label>
                            </div>
                        </div>

                        <div class="filter-section">
                            <h4 class="text-slate-100 font-medium mb-2">
                                <i class="fas fa-star"></i> Relevance
                            </h4>
                            <input type="range"
                                v-model="selectedFilters.relevance"
                                min="1"
                                max="100"
                                class="w-full accent-blue-400" />
                            <label class="text-slate-400">{{ selectedFilters.relevance }}%</label>
                        </div>

                        <div class="filter-section">
                            <h4 class="text-slate-100 font-medium mb-2">
                                <i class="fas fa-clock"></i> Recency
                            </h4>
                            <select v-model="selectedFilters.recency"
                                class="w-full bg-slate-700 text-slate-400 rounded p-2 border-none focus:ring-2 focus:ring-blue-400">
                                <option value="1">Last Day</option>
                                <option value="7">Last Week</option>
                                <option value="30">Last Month</option>
                            </select>
                        </div>
                    </div>
                </aside>

                <!-- Main Content -->
                <main class="space-y-6 ">
                    <!-- Marquee -->

                    <div class="bg-slate-800 rounded-lg p-4 overflow-hidden">

                        <div class="marquee-content">

                            <span v-for="headline in newsHeadlines"
                                :key="headline.id"
                                class="inline-block mr-8 text-slate-100">
                                {{ headline.title }}
                            </span>
                        </div>
                    </div>

                    <!-- News Section -->
                    <section class="bg-slate-800 rounded-lg p-6"
                        v-infinite-scroll="loadMore">
                        <h2 class="text-2xl font-semibold text-blue-400 mb-4">
                            <i class="fas fa-newspaper"></i> Cyber Threat Updates
                        </h2>

                        <div class="grid gap-6">

                            <div v-for="news in filteredNews"
                                :key="news.id"
                                class="bg-slate-700 rounded-lg overflow-hidden hover:-translate-y-1 transition-transform">
                                <img :src="news.image"
                                    :alt="news.title"
                                    class="w-full h-48 object-cover" />

                                <div class="p-4">
                                    <h3 class="text-slate-100 font-medium mb-2">{{ news.title }}</h3>
                                    <p class="text-slate-400 mb-4">{{ news.description }}</p>
                                    <router-link :to="'/news/' + news.id"
                                        class="text-blue-400 hover:text-blue-300 transition-colors">
                                        Read More →
                                    </router-link>
                                </div>
                            </div>
                        </div>
                    </section>
                </main>

                <!-- Right Statistics -->

                <div class="bg-slate-800 rounded-lg p-6">
                    <h3 class="text-xl font-semibold text-blue-400 mb-4">
                        <i class="fas fa-chart-line"></i> Current Status
                    </h3>

                    <div class="space-y-4">

                        <div v-for="(value, key) in currentStats"
                            :key="key"
                            class="bg-slate-700 p-3 rounded-lg flex items-center gap-3 hover:bg-slate-600 transition-colors">
                            <i :class="getStatsIcon(key)"
                                class="text-blue-400"></i>

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
                relevance: 50,
                recency: '7'
            },
            newsHeadlines: [
                { id: 1, title: 'Ransomware Attack on Healthcare' },
                { id: 2, title: 'Phishing Campaign Targets Banks' },
                { id: 3, title: 'DDoS Attack on Government Websites' }
            ],
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
                    image: 'path/to/image2.jpg'
                },
                {
                    id: 3,
                    title: 'DDoS Attack on Government Websites',
                    description: 'Government websites have been hit by a DDoS attack...',
                    image: 'path/to/image3.jpg'
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
            // Implement filtering logic based on selectedFilters
            return this.news.filter(newsItem => {
                // Example filter logic
                return (
                    (this.selectedFilters.type.length === 0 || this.selectedFilters.type.includes(newsItem.type)) &&
                    (this.selectedFilters.impact.length === 0 || this.selectedFilters.impact.includes(newsItem.impact)) &&
                    (this.selectedFilters.location.length === 0 || this.selectedFilters.location.includes(newsItem.location))
                );
            });
        }
    },
    methods: {
        loadMore() {
            // Implement logic to load more news items
            console.log('Load more news items');
        },
        getStatsIcon(key) {
            const icons = {
                'Active Threats': 'fas fa-exclamation-circle',
                'Resolved Incidents': 'fas fa-check-circle',
                'Pending Alerts': 'fas fa-bell'
            };
            return icons[key] || 'fas fa-info-circle';
        }
    }
};
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');

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
