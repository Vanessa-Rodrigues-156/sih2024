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
        <line-chart :chart-data="chartData" :options="chartOptions" />
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
import { ref, onMounted, onBeforeUnmount } from "vue";

const chartData = ref({});
const incidents = ref([]);
const alerts = ref([]);
const stats = ref({});

const fetchData = async () => {
  try {
    const [dashboardStatsResponse, chartDataResponse, recentIncidentsResponse, alertsResponse] = await Promise.all([
      fetch('http://localhost:5001/api/dashboard/stats'),
      fetch('http://localhost:5001/api/dashboard/chart-data'),
      fetch('http://localhost:5001/api/incidents/recent'),
      fetch('http://localhost:5001/api/alerts')
    ]);

    if (!dashboardStatsResponse.ok || !chartDataResponse.ok || !recentIncidentsResponse.ok || !alertsResponse.ok) {
      throw new Error('Network response was not ok');
    }

    const dashboardStats = await dashboardStatsResponse.json();
    const chartData = await chartDataResponse.json();
    const recentIncidents = await recentIncidentsResponse.json();
    const alerts = await alertsResponse.json();

    stats.value = dashboardStats;
    chartData.value = chartData;
    incidents.value = recentIncidents;
    alerts.value = alerts;
  } catch (error) {
    console.error('Error fetching data:', error);
  }
};

let interval;
onMounted(async () => {
  await fetchData();
  interval = setInterval(fetchData, 5000);
});

onBeforeUnmount(() => {
  clearInterval(interval);
});

const handleNewIncident = async (incidentData) => {
  try {
    const response = await fetch('http://localhost:5001/api/incidents', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(incidentData)
    });

    if (!response.ok) {
      throw new Error('Network response was not ok');
    }

    await fetchData();
  } catch (error) {
    console.error('Error creating new incident:', error);
  }
};
</script>


<style scoped>
/* Add any component-specific styles here */
</style>
