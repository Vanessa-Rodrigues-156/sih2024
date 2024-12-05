<script>
import { LineChart, Line, XAxis, YAxis, CartesianGrid, ResponsiveContainer } from 'recharts';
export default {
  data() {
    return {
      graphData: [
        { name: 'Jan', line1: 400, line2: 240 },
        { name: 'Feb', line1: 300, line2: 139 },
        { name: 'Mar', line1: 200, line2: 980 },
        { name: 'Apr', line1: 278, line2: 390 },
        { name: 'May', line1: 189, line2: 480 },
      ],
      incidentTypes: [
        { type: 'Phishing', count: 120 },
        { type: 'Malware', count: 98 },
        { type: 'DDoS', count: 76 },
      ],
      sectors: [
        { type: 'Finance', count: 45 },
        { type: 'Healthcare', count: 32 },
        { type: 'Retail', count: 27 },
      ],
      locations: [
        { type: 'North America', count: 150 },
        { type: 'Europe', count: 120 },
        { type: 'Asia', count: 90 },
      ],
      recentIncidents: [
        { title: 'Data Breach', sector: 'Finance', severity: 'high', time: '2 hours ago' },
        { title: 'Ransomware Attack', sector: 'Healthcare', severity: 'medium', time: '1 day ago' },
        { title: 'DDoS Attack', sector: 'Retail', severity: 'low', time: '3 days ago' },
      ],
      alerts: [
        { name: 'System Alert', message: 'High CPU usage detected', time: '5 minutes ago' },
        { name: 'Security Alert', message: 'Unauthorized access attempt', time: '10 minutes ago' },
        { name: 'Network Alert', message: 'Network latency increased', time: '15 minutes ago' },
      ],
    };
  },
  methods: {
    getSeverityColor(severity) {
      switch (severity) {
        case 'high':
          return 'bg-red-500';
        case 'medium':
          return 'bg-yellow-500';
        case 'low':
          return 'bg-green-500';
        default:
          return 'bg-gray-500';
      }
    },
    mounted(){
      console.log("mounted");
    }
  },
};
</script>

<template>
  <div class="min-h-screen bg-slate-900 p-6">

    <div class="mb-6">
      <h1 class="text-2xl font-bold text-slate-100">Cyber Incident Monitor</h1>
      <p class="text-sm text-slate-400">Real-time Monitoring</p>
    </div>

    <!-- Main Graph -->

    <div class="bg-slate-800 rounded-lg p-6 mb-6">

      <div class="flex justify-between items-center mb-4">

        <div>
          <h2 class="text-slate-400 text-sm">Cyber Incidents</h2>
          <p class="text-3xl font-bold text-slate-100">2,389</p>
        </div>
      </div>

      <!-- <div class="h-64">
        <ResponsiveContainer width="100%"
          height="100%">
          <LineChart :data="graphData">
            <CartesianGrid strokeDasharray="3 3"
              stroke="#334155" />
            <XAxis dataKey="name"
              stroke="#64748b" />
            <YAxis stroke="#64748b" />
            <Line type="monotone"
              dataKey="line1"
              stroke="#3b82f6"
              :strokeWidth="2"
              :dot="false" />
            <Line type="monotone"
              dataKey="line2"
              stroke="#ef4444"
              :strokeWidth="2"
              :dot="false" />
          </LineChart>
        </ResponsiveContainer>
      </div> -->
      
    </div>

    <!-- Stats Grid -->

    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
      <!-- Incident Types -->

      <div class="bg-slate-800 rounded-lg p-6">

        <div class="flex justify-between items-center mb-4">
          <h2 class="text-slate-100 font-medium">Incident Types</h2>

          <span class="text-sm text-slate-400">Incidents</span>
        </div>

        <div class="space-y-4">

          <div v-for="(item, index) in incidentTypes"
            :key="index"
            class="flex justify-between items-center">

            <span class="text-slate-400">{{ item.type }}</span>

            <span class="text-slate-100">{{ item.count }}</span>
          </div>
        </div>
        <button class="mt-4 text-blue-400 text-sm hover:text-blue-300">View All →</button>
      </div>

      <!-- Affected Sectors -->

      <div class="bg-slate-800 rounded-lg p-6">

        <div class="flex justify-between items-center mb-4">
          <h2 class="text-slate-100 font-medium">Affected Sectors</h2>

          <span class="text-sm text-slate-400">Incidents</span>
        </div>

        <div class="space-y-4">

          <div v-for="(item, index) in sectors"
            :key="index"
            class="flex justify-between items-center">

            <span class="text-slate-400">{{ item.type }}</span>

            <span class="text-slate-100">{{ item.count }}</span>
          </div>
        </div>
        <button class="mt-4 text-blue-400 text-sm hover:text-blue-300">View All →</button>
      </div>

      <!-- Geographic Distribution -->

      <div class="bg-slate-800 rounded-lg p-6">

        <div class="flex justify-between items-center mb-4">
          <h2 class="text-slate-100 font-medium">Geographic Distribution</h2>

          <span class="text-sm text-slate-400">Incidents</span>
        </div>

        <div class="space-y-4">

          <div v-for="(item, index) in locations"
            :key="index"
            class="flex justify-between items-center">

            <span class="text-slate-400">{{ item.type }}</span>

            <span class="text-slate-100">{{ item.count }}</span>
          </div>
        </div>
        <button class="mt-4 text-blue-400 text-sm hover:text-blue-300">View All →</button>
      </div>
    </div>

    <!-- Bottom Row -->

    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
      <!-- Recent Incidents -->

      <div class="bg-slate-800 rounded-lg p-6">

        <div class="flex justify-between items-center mb-4">
          <h2 class="text-slate-100 font-medium">Recent Incidents</h2>
          <button class="bg-slate-700 px-3 py-1 rounded text-sm text-slate-300 hover:bg-slate-600">
            Filter
          </button>
        </div>

        <div class="space-y-4">

          <div v-for="(incident, index) in recentIncidents"
            :key="index"
            class="flex items-start space-x-3">

            <div :class="['w-2 h-2 rounded-full mt-2', getSeverityColor(incident.severity)]"></div>

            <div>
              <h3 class="text-slate-100 font-medium">{{ incident.title }}</h3>
              <p class="text-sm text-slate-400">Affected: {{ incident.sector }}</p>
            </div>

            <span class="ml-auto text-sm text-slate-500">{{ incident.time }}</span>
          </div>
        </div>
        <button class="mt-4 text-blue-400 text-sm hover:text-blue-300">View All →</button>
      </div>

      <!-- Alerts -->

      <div class="bg-slate-800 rounded-lg p-6">

        <div class="flex justify-between items-center mb-4">
          <h2 class="text-slate-100 font-medium">Alerts</h2>
          <button class="bg-slate-700 px-3 py-1 rounded text-sm text-slate-300 hover:bg-slate-600">
            Manage
          </button>
        </div>

        <div class="space-y-4">

          <div v-for="(alert, index) in alerts"
            :key="index"
            class="flex items-start space-x-3">

            <div class="w-8 h-8 rounded-full bg-slate-700 flex items-center justify-center">

              <span class="text-slate-300 text-sm">{{ alert.name[0] }}</span>
            </div>

            <div>
              <h3 class="text-slate-100 font-medium">{{ alert.name }}</h3>
              <p class="text-sm text-slate-400">{{ alert.message }}</p>
            </div>

            <span class="ml-auto text-sm text-slate-500">{{ alert.time }}</span>
          </div>
        </div>
        <button class="mt-4 text-blue-400 text-sm hover:text-blue-300">View All →</button>
      </div>
    </div>
  </div>
</template>

<style>
</style>