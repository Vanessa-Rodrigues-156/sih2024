<template>
  <div id="app">
    <div class="form-container">
      <h1>Report Cybersecurity Incident (Anonymous)</h1>
      <p>
        Your report is completely anonymous. We will not store any personal
        information, and your identity will remain confidential.
      </p>
      <form @submit.prevent="submitForm">
        <div class="form-group">
          <label for="incidentType">Type of Incident</label>
          <select id="incidentType" v-model="form.incidentType" required>
            <option value="" disabled>Select Incident Type</option>
            <option v-for="type in incidentTypes" :key="type" :value="type">
              {{ type }}
            </option>
          </select>
        </div>

        <div class="form-group">
          <label for="organization">Organization</label>
          <input
            id="organization"
            type="text"
            v-model="form.organization"
            placeholder="Enter organization (e.g., Google, Microsoft...)"
            required
          />
        </div>

        <div class="form-group">
          <label for="location">Location (Optional)</label>
          <input
            id="location"
            type="text"
            v-model="form.location"
            placeholder="Enter location (e.g., city or region)"
          />
        </div>

        <div class="form-group">
          <label for="incidentDetails">Incident Details</label>
          <textarea
            id="incidentDetails"
            v-model="form.incidentDetails"
            placeholder="Provide details of the incident..."
            required
          ></textarea>
        </div>

        <div class="form-group">
          <label for="source">Source of Information</label>
          <input
            id="source"
            type="text"
            v-model="form.source"
            placeholder="Enter the source (e.g., internal report, Twitter...)"
          />
        </div>

        <div class="form-group">
          <label for="evidence">Upload Evidence (Optional)</label>
          <input
            id="evidence"
            type="file"
            @change="handleFileUpload"
            accept=".jpg,.png,.pdf,.docx"
          />
        </div>

        <div class="form-group">
          <label for="impact">Impact of Incident (Optional)</label>
          <select id="impact" v-model="form.impact">
            <option value="" disabled>Select Impact</option>
            <option v-for="impact in impactLevels" :key="impact" :value="impact">
              {{ impact }}
            </option>
          </select>
        </div>

        <div class="form-group">
          <label for="severity">Severity Level (Optional)</label>
          <select id="severity" v-model="form.severity">
            <option value="" disabled>Select Severity</option>
            <option v-for="level in severityLevels" :key="level" :value="level">
              {{ level }}
            </option>
          </select>
        </div>

        <button type="submit" class="submit-btn">Submit Report</button>
      </form>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        incidentType: '',
        organization: '',
        location: '',
        incidentDetails: '',
        source: '',
        evidence: null,
        impact: '',
        severity: '',
      },
      incidentTypes: [
        'Phishing Attack',
        'Data Breach',
        'Malware Infection',
        'DDoS Attack',
        'Other',
      ],
      impactLevels: ['Low', 'Medium', 'High', 'Critical'],
      severityLevels: ['Informational', 'Low', 'Medium', 'High', 'Critical'],
    };
  },
  methods: {
    handleFileUpload(event) {
      this.form.evidence = event.target.files[0];
    },
    submitForm() {
      console.log('Form submitted:', this.form);
      alert('Report submitted successfully!');
      this.resetForm();
    },
    resetForm() {
      this.form = {
        incidentType: '',
        organization: '',
        location: '',
        incidentDetails: '',
        source: '',
        evidence: null,
        impact: '',
        severity: '',
      };
    },
  },
};
</script>

<style>
body {
  margin: 0;
  font-family: 'Arial', sans-serif;
  background-color: #001f3f; /* Dark Blue Background */
  color: #ffffff;
}

#app {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 100vh;
}

.form-container {
  background: #002b5c;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.2);
  width: 90%;
  max-width: 600px;
}

h1 {
  font-size: 24px;
  margin-bottom: 10px;
  text-align: center;
}

p {
  font-size: 14px;
  margin-bottom: 20px;
  text-align: center;
  line-height: 1.5;
}

.form-group {
  margin-bottom: 15px;
}

label {
  display: block;
  font-size: 14px;
  margin-bottom: 5px;
}

input,
textarea,
select {
  width: 100%;
  padding: 10px;
  font-size: 14px;
  border: none;
  border-radius: 4px;
  background: #f0f8ff;
  color: #001f3f;
}

textarea {
  resize: vertical;
}

.submit-btn {
  width: 100%;
  padding: 12px;
  font-size: 16px;
  border: none;
  border-radius: 4px;
  background: #0074d9;
  color: white;
  cursor: pointer;
  transition: background 0.3s;
}

.submit-btn:hover {
  background: #0056a6;
}
</style>
