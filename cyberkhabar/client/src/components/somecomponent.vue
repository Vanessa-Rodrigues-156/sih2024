<template>

    <div class="min-h-screen bg-slate-900 p-6">

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
            <!-- Latest Incidents Block -->

            <div class="bg-slate-800 rounded-lg p-6">
                <h2 class="text-2xl font-semibold text-slate-100 mb-2">Latest Incidents</h2>
                <p class="text-sm text-slate-400 mb-4">Real-time updates on cyber incidents affecting the Indian cyber space.</p>

                <div class="space-y-4">

                    <div v-for="(incident, index) in incidents"
                        :key="index"
                        class="flex items-center justify-between">

                        <div>
                            <h3 class="text-slate-100 font-medium">{{ incident.title }}</h3>
                            <p class="text-sm text-slate-400">{{ incident.sector }}</p>
                        </div>

                        <span :class="getSeverityClass(incident.severity)"
                            class="px-3 py-1 rounded-full text-sm font-medium">
                            {{ incident.severity }}
                        </span>
                    </div>
                </div>
                <button class="text-blue-400 hover:text-blue-300 mt-4 text-sm">
                    View All Incidents
                </button>
            </div>

            <!-- Threat Assessment Block -->

            <div class="bg-slate-800 rounded-lg p-6">
                <h2 class="text-2xl font-semibold text-slate-100 mb-2">Threat Assessment</h2>
                <p class="text-sm text-slate-400 mb-4">Insights and analysis on potential threats to the Indian cyber space.</p>

                <div class="space-y-6">

                    <div v-for="(threat, index) in threats"
                        :key="index">
                        <h3 class="text-slate-100 font-medium mb-2">{{ threat.title }}</h3>
                        <p class="text-sm text-slate-400">{{ threat.description }}</p>
                    </div>
                </div>
                <button class="text-blue-400 hover:text-blue-300 mt-4 text-sm">
                    View Threat Assessment
                </button>
            </div>

            <!-- Incident Reports Block -->

            <div class="bg-slate-800 rounded-lg p-6">
                <h2 class="text-2xl font-semibold text-slate-100 mb-2">Incident Reports</h2>
                <p class="text-sm text-slate-400 mb-4">Comprehensive reports on cyber incidents affecting the Indian cyber space.</p>

                <div class="space-y-4">

                    <div v-for="(report, index) in reports"
                        :key="index"
                        class="flex items-center justify-between">

                        <div>
                            <h3 class="text-slate-100 font-medium">{{ report.title }}</h3>
                            <p class="text-sm text-slate-400">{{ report.date }}</p>
                        </div>
                        <button class="bg-slate-700 hover:bg-slate-600 text-slate-100 px-4 py-2 rounded-md text-sm">
                            Download
                        </button>
                    </div>
                </div>
                <button class="text-blue-400 hover:text-blue-300 mt-4 text-sm">
                    View All Reports
                </button>
            </div>

            <!-- Alerts Block -->

            <div class="bg-slate-800 rounded-lg p-6">
                <h2 class="text-2xl font-semibold text-slate-100 mb-2">Alerts</h2>
                <p class="text-sm text-slate-400 mb-4">Real-time alerts on critical cyber incidents and threats.</p>

                <div class="space-y-4">

                    <div v-for="(alert, index) in alerts"
                        :key="index"
                        class="flex items-center justify-between">

                        <div>
                            <h3 class="text-slate-100 font-medium">{{ alert.title }}</h3>
                            <p class="text-sm text-slate-400">Issued: {{ alert.date }}</p>
                        </div>

                        <span :class="getSeverityClass(alert.severity)"
                            class="px-3 py-1 rounded-full text-sm font-medium">
                            {{ alert.severity }}
                        </span>
                    </div>
                </div>
                <button class="text-blue-400 hover:text-blue-300 mt-4 text-sm">
                    View All Alerts
                </button>
            </div>
        </div>
    </div>
</template>

<script>
export default {
    data() {
        return {
            incidents: [],
            threats: [],
            reports: [],
            alerts: []
        };
    },
    methods: {
        getSeverityClass(severity) {
            const classes = {
                High: 'bg-red-500/20 text-red-400',
                Medium: 'bg-orange-500/20 text-orange-400',
                Low: 'bg-yellow-500/20 text-yellow-400'
            };
            return classes[severity] || '';
        },
        async fetchIncidents() {
            const response = await fetch('http://localhost:5001/api/incidents');
            this.incidents = await response.json();
        },
        async fetchThreats() {
            const response = await fetch('http://localhost:5001/api/threats');
            this.threats = await response.json();
        },
        async fetchReports() {
            const response = await fetch('http://localhost:5001/api/reports');
            this.reports = await response.json();
        },
        async fetchAlerts() {
            const response = await fetch('http://localhost:5001/api/alerts');
            this.alerts = await response.json();
        }
    },
    async created() {
        try {
            await Promise.all([
                this.fetchIncidents(),
                this.fetchThreats(),
                this.fetchReports(),
                this.fetchAlerts()
            ]);
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    }
};
</script>


<style scoped>
/* Add your custom styles here */
</style>