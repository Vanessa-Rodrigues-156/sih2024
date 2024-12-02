<template>
  <div id="incident-report-form" class="dark-theme">
    <h2>Report Cybersecurity Incident</h2>
    <form @submit.prevent="submitForm">
      <!-- Incident Type -->
      <label for="incident-type">Type of Incident</label>
      <select id="incident-type" v-model="formData.incidentType" required>
        <option disabled value="">Select Incident Type</option>
        <option v-for="type in incidentTypes" :key="type" :value="type">{{ type }}</option>
      </select>

     <!-- Location -->
      <label for="location">Orgaisation</label>
      <input type="text" id="location" v-model="formData.location" placeholder="Enter organisation (e.g., google,microsoft,...)" />


      <!-- Location -->
      <label for="location">Location (Optional)</label>
      <input type="text" id="location" v-model="formData.location" placeholder="Enter location (e.g., city or region)" />

      <!-- Incident Details -->
      <label for="details">Incident Details</label>
      <textarea
        id="details"
        v-model="formData.details"
        placeholder="Provide details of the incident..."
        required
      ></textarea>

      <!-- Evidence Upload -->
      <label for="evidence">Upload Evidence (Optional)</label>
      <input type="file" id="evidence" @change="handleFileUpload" />

      <!-- Impact -->
      <label for="impact">Impact of Incident</label>
      <select id="impact" v-model="formData.impact">
        <option disabled value="">Select Impact</option>
        <option v-for="impact in impacts" :key="impact" :value="impact">{{ impact }}</option>
      </select>

      <!-- Severity -->
      <label for="severity">Severity Level</label>
      <select id="severity" v-model="formData.severity" required>
        <option disabled value="">Select Severity</option>
        <option v-for="severity in severities" :key="severity" :value="severity">{{ severity }}</option>
      </select>

      

      <!-- Submit Button -->
      <button type="submit">Submit Report</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      incidentTypes: [
        "Phishing",
        "Malware",
        "DDoS Attack",
        "Data Breach",
        "Unauthorized Access",
        "Other",
      ],
      impacts: [
        "Financial Loss",
        "Data Loss",
        "Service Disruption",
        "Reputation Damage",
      ],
      severities: ["Low", "Medium", "High", "Critical"],
      formData: {
        incidentType: "",
        date: "",
        time: "",
        location: "",
        details: "",
        evidence: null,
        impact: "",
        severity: "",
        allowContact: false,
        contactEmail: "",
      },
    };
  },
  methods: {
    handleFileUpload(event) {
      this.formData.evidence = event.target.files[0];
    },
    submitForm() {
      console.log("Form Data Submitted:", this.formData);
      alert("Your incident report has been submitted anonymously.");
      this.resetForm();
    },
    resetForm() {
      this.formData = {
        incidentType: "",
        date: "",
        time: "",
        location: "",
        details: "",
        evidence: null,
        impact: "",
        severity: "",
        allowContact: false,
        contactEmail: "",
      };
    },
  },
};
</script>

<style scoped>

#incident-report-form {
  width: 50%;
  margin: auto;
  padding: 20px;
  background-color: #101320;
  border: 1px solid #0ff;
  border-radius: 10px;
  box-shadow: 0 0 10px #0ff;
  color: #00ffcc;
  font-family: "Roboto", sans-serif;
}

#incident-report-form h2 {
  text-align: center;
  margin-bottom: 20px;
}

#incident-report-form label {
  display: block;
  margin: 10px 0 5px;
}

#incident-report-form input,
#incident-report-form select,
#incident-report-form textarea {
  width: 100%;
  padding: 10px;
  margin-bottom: 15px;
  border: 1px solid #0ff;
  border-radius: 5px;
  background-color: #1a1a3d;
  color: #00ffcc;
}

#incident-report-form button {
  width: 100%;
  padding: 10px;
  background-color: #0ff;
  color: #101320;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
}

#incident-report-form button:hover {
  background-color: #00cc99;
}
</style>
