<template>
  <div class="min-h-screen bg-gray-900 py-8 px-4 sm:px-6 lg:px-8">
    <div id="cyber-report-form" class="max-w-4xl mx-auto bg-gray-800 text-white rounded-lg p-5 shadow-lg">
      <header>
        <h1 class="text-center text-blue-400 mb-4 text-3xl lg:text-4xl font-bold">
          Report Cybersecurity Incident
        </h1>
      </header>
      <form @submit.prevent="submitForm" class="mt-8 space-y-6">
        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="form-group">
            <label for="incidentType" class="block mb-1 font-bold text-gray-200">
              Type of Incident
            </label>
            <select
              v-model="formData.incidentType"
              id="incidentType"
              required
              class="w-full p-2 text-base border border-gray-600 rounded bg-gray-700 text-white"
            >
              <option disabled value="">Select Incident Type</option>
              <option v-for="type in incidentTypes" :key="type">{{ type }}</option>
            </select>
          </div>

          <div class="form-group">
            <label for="organisation" class="block mb-1 font-bold text-gray-200">
              Organization
            </label>
            <input
              type="text"
              id="organisation"
              v-model="formData.organisation"
              placeholder="Enter organization (e.g., Google, Microsoft...)"
              class="w-full p-2 text-base border border-gray-600 rounded bg-gray-700 text-white placeholder-gray-400"
              required
            />
          </div>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div class="form-group">
            <label for="location" class="block mb-1 font-bold text-gray-200">
              Location (Optional)
            </label>
            <input
              type="text"
              id="location"
              v-model="formData.location"
              placeholder="Enter location (e.g., city or region)"
              class="w-full p-2 text-base border border-gray-600 rounded bg-gray-700 text-white placeholder-gray-400"
            />
          </div>

          <div class="form-group">
            <label for="source" class="block mb-1 font-bold text-gray-200">
              Source of Information
            </label>
            <input
              type="text"
              id="source"
              v-model="formData.source"
              placeholder="Enter the source (e.g., internal report, Twitter, Reddit...)"
              class="w-full p-2 text-base border border-gray-600 rounded bg-gray-700 text-white placeholder-gray-400"
              required
            />
          </div>
        </div>

        <div class="form-group">
          <label for="details" class="block mb-1 font-bold text-gray-200">
            Incident Details
          </label>
          <textarea
            id="details"
            v-model="formData.details"
            rows="5"
            placeholder="Provide details of the incident..."
            required
            class="w-full p-2 text-base border border-gray-600 rounded bg-gray-700 text-white placeholder-gray-400"
          ></textarea>
        </div>

        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <div class="form-group">
            <label for="evidence" class="block mb-1 font-bold text-gray-200">
              Upload Evidence (Optional)
            </label>
            <input
              type="file"
              id="evidence"
              @change="handleFileUpload"
              class="w-full p-2 text-base border border-gray-600 rounded bg-gray-700 text-white"
            />
          </div>

          <div class="form-group">
            <label for="impact" class="block mb-1 font-bold text-gray-200">
              Impact of Incident
            </label>
            <select
              v-model="formData.impact"
              id="impact"
              class="w-full p-2 text-base border border-gray-600 rounded bg-gray-700 text-white"
            >
              <option disabled value="">Select Impact</option>
              <option v-for="impact in impacts" :key="impact">{{ impact }}</option>
            </select>
          </div>

          <div class="form-group">
            <label for="severity" class="block mb-1 font-bold text-gray-200">
              Severity Level
            </label>
            <select
              v-model="formData.severity"
              id="severity"
              class="w-full p-2 text-base border border-gray-600 rounded bg-gray-700 text-white"
            >
              <option disabled value="">Select Severity</option>
              <option v-for="severity in severities" :key="severity">{{ severity }}</option>
            </select>
          </div>
        </div>

        <button
          type="submit"
          class="w-full p-3 bg-blue-500 rounded text-xl text-white hover:bg-gray-700 transition-colors duration-300"
        >
          Submit Report
        </button>
      </form>
      <footer class="text-center mt-8 text-xs md:text-sm text-gray-400">
        <p>© 2024 Cyberkhabar. Empowering a secure digital India.</p>
      </footer>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      incidentTypes: [
        "Phishing",
        "Data Breach",
        "Ransomware",
        "Denial of Service",
        "Other",
      ],
      impacts: ["Financial Loss","Data Loss","Service Disruption","Reputation Damage"],
      severities: ["Low", "Moderate", "Critical"],
      formData: {
        incidentType: "",
        organisation: "",
        location: "",
        details: "",
        source: "",
        evidence: null,
        impact: "",
        severity: "",
      },
    };
  },
  methods: {
    handleFileUpload(event) {
      this.formData.evidence = event.target.files[0] || null;
    },
    submitForm() {
      if (
        !this.formData.incidentType ||
        !this.formData.organisation ||
        !this.formData.details ||
        !this.formData.source
      ) {
        alert("Please fill in all required fields.");
        return;
      }

      const payload = new FormData();
      Object.keys(this.formData).forEach((key) => {
        if (this.formData[key]) payload.append(key, this.formData[key]);
      });

      fetch("http://localhost:5001/api/incidents", {
        method: "POST",
        body: payload,
      })
        .then((response) => {
          if (!response.ok) {
            return response.json().then((err) => {
              throw new Error(err.message || "Server error occurred");
            });
          }
          return response.json();
        })
        .then((data) => {
          alert("Your report has been submitted.");
          this.resetForm();
        })
        .catch((error) => {
          console.error("Error submitting form:", error);
          alert(`Failed to submit the report: ${error.message}`);
        });
    },
    resetForm() {
      this.formData = {
        incidentType: "",
        organisation: "",
        location: "",
        details: "",
        source: "",
        evidence: null,
        impact: "",
        severity: "",
      };
    },
  },
};
</script>
