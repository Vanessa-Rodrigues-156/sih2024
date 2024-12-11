<template>
  <div class="min-h-screen bg-slate-900 p-6">
    <!-- Header -->
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
      <div class="h-64">
        <line-chart :chart-data="chartData" :options="chartOptions"></line-chart>
      </div>
    </div>

    <!-- Stats Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-6">
      <!-- Incident Types -->
      <StatCard title="Incident Types" :items="incidentTypes" />

      <!-- Affected Sectors -->
      <StatCard title="Affected Sectors" :items="sectors" />

      <!-- Geographic Distribution -->
      <StatCard title="Geographic Distribution" :items="locations" />
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
          <div
            v-for="(incident, index) in recentIncidents"
            :key="index"
            class="flex items-start space-x-3"
          >
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
          <div
            v-for="(alert, index) in alerts"
            :key="index"
            class="flex items-start space-x-3"
          >
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

<script setup>
import { ref } from "vue";
import { defineAsyncComponent } from "vue";


// Chart data
const chartData = ref({
  labels: Array.from({ length: 12 }, (_, i) => `Hour ${i + 1}`),
  datasets: [
    {
      label: "Type 1",
      data: Array.from({ length: 12 }, () => Math.random() * 100),
      borderColor: "#3b82f6",
      fill: false,
    },
    {
      label: "Type 2",
      data: Array.from({ length: 12 }, () => Math.random() * 100),
      borderColor: "#ef4444",
      fill: false,
    },
  ],
});
const chartOptions = {
  responsive: true,
  maintainAspectRatio: false,
  plugins: {
    legend: {
      display: true,
    },
  },
};

// Stats
const incidentTypes = ref([
  { type: "Malware", count: "1.5K" },
  { type: "DDoS", count: "800" },
  { type: "Ransomware", count: "450" },
]);

const sectors = ref([
  { type: "Government", count: "1.5K" },
  { type: "Healthcare", count: "1K" },
  { type: "Critical Infrastructure", count: "650" },
]);

const locations = ref([
  { type: "New Delhi", count: "1.2K" },
  { type: "Mumbai", count: "1K" },
  { type: "Bengaluru", count: "800" },
]);

const recentIncidents = ref([
  {
    title: "Ransomware Attack",
    sector: "Government Sector",
    time: "2h ago",
    severity: "high",
  },
  {
    title: "Phishing Campaign",
    sector: "Finance Sector",
    time: "4h ago",
    severity: "medium",
  },
  {
    title: "DDoS Attack Mitigated",
    sector: "Critical Infrastructure",
    time: "8h ago",
    severity: "low",
  },
]);

const alerts = ref([
  {
    name: "John Doe",
    message: "Ransomware attack detected in the government sector.",
    time: "2h ago",
  },
  {
    name: "Sarah Miller",
    message: "Phishing campaign targeting the finance sector.",
    time: "4h ago",
  },
  {
    name: "Michael Kumar",
    message: "DDoS attack on critical infrastructure mitigated.",
    time: "8h ago",
  },
]);

const getSeverityColor = (severity) => {
  const colors = {
    high: "bg-red-500",
    medium: "bg-yellow-500",
    low: "bg-green-500",
  };
  return colors[severity] || "bg-blue-500";
};
</script>

<style scoped>
/* Add any component-specific styles here */
</style>