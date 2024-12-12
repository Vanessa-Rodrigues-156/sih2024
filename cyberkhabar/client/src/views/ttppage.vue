<template>
    <div class="min-h-screen w-full bg-gray-900">
      <!-- Header -->
      <div class="flex justify-between items-center p-6 bg-gray-800">
        <div class="title">
          <h1 class="text-3xl font-bold text-blue-400">CyberKhabar</h1>
        </div>
        <div class="flex gap-4">
          <button @click="reloadReport" class="px-4 py-2 text-blue-400 border border-blue-400 rounded-md hover:bg-blue-400/10 transition-all">
            Reload
          </button>
        </div>
      </div>
  
      <!-- Report Details -->
      <div class="px-6 py-6 space-y-4">
        <div v-if="report" class="bg-gray-800 rounded-lg p-6">
          <h3 class="text-xl font-semibold text-blue-400">Report Analysis</h3>
          <div class="space-y-4">
            <div class="bg-gray-700 p-4 rounded-lg">
              <h4 class="text-gray-100 font-medium">URL:</h4>
              <p class="text-gray-400">{{ report.url }}</p>
            </div>
  
            <div class="bg-gray-700 p-4 rounded-lg">
              <h4 class="text-gray-100 font-medium">Keywords:</h4>
              <ul class="text-gray-400">
                <li v-for="(keyword, index) in report.keywords" :key="index">{{ keyword }}</li>
              </ul>
            </div>
  
            <div class="bg-gray-700 p-4 rounded-lg">
              <h4 class="text-gray-100 font-medium">Date:</h4>
              <p class="text-gray-400">{{ report.date }}</p>
            </div>
  
            <div class="bg-gray-700 p-4 rounded-lg">
              <h4 class="text-gray-100 font-medium">Text:</h4>
              <p class="text-gray-400">{{ report.text }}</p>
            </div>
  
            <div class="bg-gray-700 p-4 rounded-lg">
              <h4 class="text-gray-100 font-medium">TTP</h4>
              <p class="text-gray-400">{{ report.ttp }}</p>
            </div>
          </div>
        </div>
        <div v-else class="text-center text-gray-400">
          No report found.
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import axios from "axios";
  
  export default {
    name: "ReportDetailsPage",
    data() {
      return {
        report: null, // Single report instead of an array
      };
    },
    mounted() {
      this.reloadReport(); // Fetch the report when the component is mounted
    },
    methods: {
      async reloadReport() {
        try {
          const response = await axios.get("/api/report"); // Update with the correct backend API endpoint for a single report
          this.report = response.data; // Assuming the response data is a single report object
        } catch (error) {
          console.error("Error fetching report:", error);
        }
      },
    },
  };
  </script>
  
  <style scoped>
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
  
  .bg-gray-700 {
    background-color: #2d3748;
  }
  
  .bg-gray-800 {
    background-color: #1e293b;
  }
  
  .text-blue-400 {
    color: #63b3ed;
  }
  
  .text-gray-100 {
    color: #f7fafc;
  }
  
  .text-gray-400 {
    color: #cbd5e0;
  }
  
  .text-gray-200 {
    color: #edf2f7;
  }
  
  .font-semibold {
    font-weight: 600;
  }
  
  .font-medium {
    font-weight: 500;
  }
  
  .transition-all {
    transition: all 0.3s;
  }
  
  .hover\:bg-blue-400\/10:hover {
    background-color: rgba(99, 179, 237, 0.1);
  }
  
  .rounded-lg {
    border-radius: 0.5rem;
  }
  
  .p-4 {
    padding: 1rem;
  }
  
  .px-6 {
    padding-left: 1.5rem;
    padding-right: 1.5rem;
  }
  
  .py-6 {
    padding-top: 1.5rem;
    padding-bottom: 1.5rem;
  }
  
  input:focus {
    outline: none;
    border-color: #63b3ed;
  }
  </style>
  