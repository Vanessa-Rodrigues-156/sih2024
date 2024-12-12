<template>
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
  
      <!-- Search Bar -->
      <div class="px-6 py-4">
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Search by Keyword, URL, Date, or Text"
          class="w-full px-4 py-2 bg-slate-700 text-slate-100 border border-slate-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-400"
        />
      </div>
  
      <!-- Report Details -->
      <div class="px-6 py-6">
        <div v-if="filteredReport" class="bg-slate-800 rounded-lg p-6">
          <h2 class="text-2xl font-semibold text-blue-400 mb-4">Report Details</h2>
          <div class="space-y-4">
            <div class="bg-slate-700 p-4 rounded-lg">
              <h3 class="text-slate-100 font-medium">URL:</h3>
              <p class="text-slate-400">{{ filteredReport.url }}</p>
            </div>
  
            <div class="bg-slate-700 p-4 rounded-lg">
              <h3 class="text-slate-100 font-medium">Keywords:</h3>
              <ul class="text-slate-400">
                <li v-for="keyword in filteredReport.keywords" :key="keyword">{{ keyword }}</li>
              </ul>
            </div>
  
            <div class="bg-slate-700 p-4 rounded-lg">
              <h3 class="text-slate-100 font-medium">Date:</h3>
              <p class="text-slate-400">{{ filteredReport.date }}</p>
            </div>
  
            <div class="bg-slate-700 p-4 rounded-lg">
              <h3 class="text-slate-100 font-medium">Text:</h3>
              <p class="text-slate-400">{{ filteredReport.text }}</p>
            </div>
          </div>
        </div>
        <div v-else class="text-center text-slate-400">
          No report found matching your search.
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: "ReportDetailsPage",
    data() {
      return {
        searchQuery: "",
        reports: [
          {
            url: "https://example.com/report1",
            keywords: ["Ransomware", "Phishing", "Banking"],
            date: "2024-12-10",
            text: "A new ransomware attack targets banking systems in North India."
          },
          {
            url: "https://example.com/report2",
            keywords: ["DDoS", "Government", "Website"],
            date: "2024-12-11",
            text: "Government websites were targeted in a DDoS attack last night."
          },
          {
            url: "https://example.com/report3",
            keywords: ["Malware", "Healthcare"],
            date: "2024-12-12",
            text: "A healthcare organization was breached by a malware attack."
          }
        ]
      };
    },
    computed: {
      filteredReport() {
        if (!this.searchQuery) return null;
        const lowerCaseSearch = this.searchQuery.toLowerCase();
        return this.reports.find(report => {
          return (
            report.url.toLowerCase().includes(lowerCaseSearch) ||
            report.keywords.some(keyword => keyword.toLowerCase().includes(lowerCaseSearch)) ||
            report.date.toLowerCase().includes(lowerCaseSearch) ||
            report.text.toLowerCase().includes(lowerCaseSearch)
          );
        });
      }
    }
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
  
  .bg-slate-700 {
    background-color: #2d3748;
  }
  
  .bg-slate-800 {
    background-color: #1e293b;
  }
  
  .text-blue-400 {
    color: #63b3ed;
  }
  
  .text-slate-100 {
    color: #f7fafc;
  }
  
  .text-slate-400 {
    color: #cbd5e0;
  }
  
  .text-slate-200 {
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
  