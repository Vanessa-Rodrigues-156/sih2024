<template>
    <div class="min-h-screen bg-slate-900">
        <!-- Header -->
        <div class="flex justify-between items-center px-6 py-4 bg-slate-800">
            <div class="title">
                <h1 class="text-4xl font-bold text-blue-400">CyberKhabar</h1>
            </div>
        </div>

        <!-- Report Content -->
        <div class="container mx-auto px-6 py-8">
            <div class="bg-slate-800 rounded-lg shadow-lg p-8">
                <!-- Report Header -->
                <div class="mb-8">
                    <h2 class="text-4xl font-semibold text-slate-100 mb-3">{{ report.title }}</h2>

                    <div class="flex items-center gap-6">
                        <span :class="getSeverityClass(report.severity)"
                            class="px-4 py-2 rounded-full text-sm font-medium">
                            {{ report.severity }}
                        </span>
                        <span class="text-slate-400">Incident ID: {{ report.id }}</span>
                        <span class="text-slate-400">{{ report.date }}</span>
                    </div>
                </div>

                <!-- Report Details -->
                <div class="grid grid-cols-1 md:grid-cols-2 gap-10 mb-8">
                    <div class="space-y-6">
                        <div>
                            <h3 class="text-xl font-semibold text-blue-400 mb-2">Incident Overview</h3>
                            <p class="text-slate-300">{{ report.description }}</p>
                        </div>

                        <div>
                            <h3 class="text-xl font-semibold text-blue-400 mb-2">Affected Sectors</h3>
                            <div class="flex flex-wrap gap-2">
                                <span v-for="sector in report.affectedSectors"
                                    :key="sector"
                                    class="bg-slate-700 text-slate-300 px-4 py-2 rounded-full text-sm">
                                    {{ sector }}
                                </span>
                            </div>
                        </div>
                    </div>

                    <div class="space-y-6">
                        <div>
                            <h3 class="text-xl font-semibold text-blue-400 mb-2">Impact Analysis</h3>
                            <ul class="list-disc list-inside text-slate-300 space-y-2">
                                <li v-for="impact in report.impacts"
                                    :key="impact">{{ impact }}</li>
                            </ul>
                        </div>

                        <div>
                            <h3 class="text-xl font-semibold text-blue-400 mb-2">Technical Details</h3>
                            <div class="bg-slate-900 p-4 rounded-lg">
                                <pre class="text-slate-300 whitespace-pre-wrap">{{ report.technicalDetails }}</pre>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Mitigation Steps -->
                <div class="mb-8">
                    <h3 class="text-xl font-semibold text-blue-400 mb-4">Mitigation Steps</h3>
                    <div class="bg-slate-700 rounded-lg p-6">
                        <ol class="list-decimal list-inside space-y-3 text-slate-300">
                            <li v-for="step in report.mitigationSteps"
                                :key="step">{{ step }}</li>
                        </ol>
                    </div>
                </div>

                <!-- Related Incidents -->
                <div>
                    <h3 class="text-xl font-semibold text-blue-400 mb-4">Related Incidents</h3>
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div v-for="incident in report.relatedIncidents"
                            :key="incident.id"
                            class="bg-slate-700 p-6 rounded-lg hover:bg-slate-600 transition-all">
                            <h4 class="text-slate-100 font-medium mb-2">{{ incident.title }}</h4>
                            <router-link :to="'/report/' + incident.id"
                                class="text-blue-400 hover:text-blue-300 text-sm">
                                View Report →
                            </router-link>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>
<script>
export default {
    name: 'ReportPage',
    data() {
        return {
            report: {
                id: '',
                title: '',
                severity: '',
                date: '',
                description: '',
                affectedSectors: [],
                impacts: [],
                technicalDetails: '',
                mitigationSteps: [],
                relatedIncidents: []
            }
        }
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
        async fetchReport() {
            try {
                const response = await fetch(`http://localhost:5001/api/reports/${this.$route.params.id}`);
                const data = await response.json();
                this.report = data;
            } catch (error) {
                console.error('Error fetching report:', error);
            }
        }
    },
    created() {
        this.fetchReport();
    },
    watch: {
        '$route.params.id': {
            handler: 'fetchReport',
            immediate: true
        }
    }
}
</script>
