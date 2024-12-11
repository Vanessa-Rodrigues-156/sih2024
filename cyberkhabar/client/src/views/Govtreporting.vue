<template>
    <div class="p-6 text-white">
      <div class="mb-8">
        <h1 class="text-3xl font-bold mb-2">Government Reporting Dashboard</h1>
        <p class="text-slate-300">Manage and submit your cybersecurity reports</p>
      </div>

      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
        <!-- Report Card -->
        <div class="bg-slate-800 rounded-lg p-6 hover:bg-slate-700 transition-all">
          <h2 class="text-xl font-semibold mb-4">New Report</h2>
          <div class="space-y-4">
            <div>
              <label class="block text-sm font-medium mb-2">Incident Type</label>
              <select v-model="reportData.incidentType" class="w-full bg-slate-900 rounded p-2 border border-slate-600">
                <option value="phishing">Phishing Attack</option>
                <option value="malware">Malware</option>
                <option value="databreach">Data Breach</option>
                <option value="ransomware">Ransomware</option>
              </select>
            </div>
          
            <div>
              <label class="block text-sm font-medium mb-2">Description</label>
              <textarea 
                v-model="reportData.description"
                class="w-full bg-slate-900 rounded p-2 border border-slate-600 h-24"
                placeholder="Describe the incident..."
              ></textarea>
            </div>

            <button 
              @click="submitReport"
              class="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded transition-colors"
            >
              Submit Report
            </button>
          </div>
        </div>

        <!-- Recent Reports -->
        <div class="bg-slate-800 rounded-lg p-6">
          <h2 class="text-xl font-semibold mb-4">Recent Reports</h2>
          <div class="space-y-4">
            <div v-for="(report, index) in recentReports" :key="index" class="border-b border-slate-700 pb-4">
              <div class="flex justify-between items-start">
                <div>
                  <p class="font-medium">{{ report.type }}</p>
                  <p class="text-sm text-slate-400">{{ report.date }}</p>
                </div>
                <span :class="getStatusClass(report.status)" class="px-2 py-1 rounded text-xs">
                  {{ report.status }}
                </span>
              </div>
            </div>
          </div>
        </div>

        <!-- Statistics Card -->
        <div class="bg-slate-800 rounded-lg p-6">
          <h2 class="text-xl font-semibold mb-4">Report Statistics</h2>
          <div class="space-y-4">
            <div class="flex justify-between items-center">
              <span>Total Reports</span>
              <span class="font-bold">{{ statistics.total }}</span>
            </div>
            <div class="flex justify-between items-center">
              <span>Pending</span>
              <span class="text-yellow-500 font-bold">{{ statistics.pending }}</span>
            </div>
            <div class="flex justify-between items-center">
              <span>Resolved</span>
              <span class="text-green-500 font-bold">{{ statistics.resolved }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
</template>

<script>
export default {
    name: 'Govtreporting',
    data() {
      return {
        reportData: {
          incidentType: 'phishing',
          description: ''
        },
        recentReports: [
          { type: 'Phishing Attack', date: '2024-01-15', status: 'pending' },
          { type: 'Data Breach', date: '2024-01-14', status: 'resolved' },
          { type: 'Ransomware', date: '2024-01-13', status: 'in-progress' }
        ],
        statistics: {
          total: 45,
          pending: 12,
          resolved: 33
        }
      }
    },
    methods: {
      submitReport() {
        // Handle report submission logic here
        console.log('Report submitted:', this.reportData)
      },
      getStatusClass(status) {
        const classes = {
          pending: 'bg-yellow-500/20 text-yellow-500',
          resolved: 'bg-green-500/20 text-green-500',
          'in-progress': 'bg-blue-500/20 text-blue-500'
        }
        return classes[status]
      }
    }
}
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap');
.grid {
    animation: fadeIn 0.3s ease-in-out;
}

@keyframes fadeIn {
    from {
      opacity: 0;
      transform: translateY(10px);
    }
    to {
      opacity: 1;
      transform: translateY(0);
    }
}

select, textarea {
    outline: none;
}

select:focus, textarea:focus {
    border-color: #3b82f6;
}
</style>
