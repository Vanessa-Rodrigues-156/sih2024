<script>
export default {
    name: 'Dashboard',
    data() {
        return {
            incidents: [
                { title: 'Ransomware Attack', sector: 'Affected Sector: Healthcare', severity: 'High' },
                { title: 'Data Breach', sector: 'Affected Sector: Finance', severity: 'Medium' },
                { title: 'DDoS Attack', sector: 'Affected Sector: Government', severity: 'Low' },
                { title: 'Phishing Campaign', sector: 'Affected Sector: Education', severity: 'Medium' },
                { title: 'Malware Infection', sector: 'Affected Sector: Retail', severity: 'High' }
            ],
            threats: [
                {
                    title: 'Ransomware Threat',
                    description: 'Increased activity of ransomware targeting the healthcare sector. Recommended actions for CII operators.'
                },
                {
                    title: 'IoT Botnet Attacks',
                    description: 'Emerging threat of IoT botnets targeting critical infrastructure. Mitigation strategies for CII operators.'
                },
                {
                    title: 'Supply Chain Vulnerabilities',
                    description: 'Increased exploitation of supply chain vulnerabilities. Guidance for CII operators on third-party risk management.'
                }
            ],
            reports: [
                { title: 'Quarterly Cyber Incident Report', date: 'Q2 2023 | Published: June 30, 2023' },
                { title: 'Sector-Specific Incident Report', date: 'Banking and Finance | Published: May 15, 2023' },
                { title: 'Critical Infrastructure Incident Report', date: 'Energy Sector | Published: April 1, 2023' }
            ],
            alerts: [
                { title: 'Ransomware Alert', date: 'June 28, 2023', severity: 'High' },
                { title: 'DDoS Attack Alert', date: 'June 15, 2023', severity: 'Medium' },
                { title: 'IoT Botnet Alert', date: 'June 5, 2023', severity: 'Low' }
            ]
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
        }
    }
};
</script>
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
<style>
/* Add any additional custom styles here if needed */
</style>