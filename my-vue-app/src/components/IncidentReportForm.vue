<template>
  <div id="incident-report-form" class="dark-theme">
    <h2>Report Cybersecurity Incident (Anonymous)</h2>
    <p>Your report is completely anonymous. We will not store any personal information, and your identity will remain confidential.</p>
    <form @submit.prevent="submitForm" autocomplete="off">
      <!-- Incident Type (Required) -->
      <label for="incident-type">Type of Incident</label>
      <select id="incident-type" v-model="formData.incidentType" required autocomplete="off">
        <option disabled value="">Select Incident Type</option>
        <option v-for="type in incidentTypes" :key="type" :value="type">{{ type }}</option>
      </select>

      <!-- Organisation (Required) -->
      <label for="organisation">Organisation </label>
      <input
        type="text"
        id="organisation"
        v-model="formData.organisation"
        placeholder="Enter organisation (e.g., Google, Microsoft...) "
        required
        autocomplete="off"
      />

      <!-- Location (Optional) -->
      <label for="location">Location (Optional)</label>
      <input
        type="text"
        id="location"
        v-model="formData.location"
        placeholder="Enter location (e.g., city or region) (Optional)"
        autocomplete="off"
      />

      <!-- Incident Details (Required) -->
      <label for="details">Incident Details</label>
      <textarea
        id="details"
        v-model="formData.details"
        placeholder="Provide details of the incident..."
        required
        autocomplete="off"
      ></textarea>

      <!-- Source of Information -->
      <label for="source">Source of Information</label>
      <input
        type="text"
        id="source"
        v-model="formData.source"
        placeholder="Enter the source (e.g., internal report,twitter,reddit,...)"
        required
        autocomplete="off"
      />

      <!-- Evidence Upload (Optional) -->
      <label for="evidence">Upload Evidence (Optional)</label>
      <input type="file" id="evidence" @change="handleFileUpload" autocomplete="off" />

      <!-- Impact (Optional) -->
      <label for="impact">Impact of Incident (Optional)</label>
      <select id="impact" v-model="formData.impact" autocomplete="off">
        <option disabled value="">Select Impact</option>
        <option v-for="impact in impacts" :key="impact" :value="impact">{{ impact }}</option>
      </select>

      <!-- Severity (Optional) -->
      <label for="severity">Severity Level (Optional)</label>
      <select id="severity" v-model="formData.severity" autocomplete="off">
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
        organisation: "",
        location: "",
        details: "",
        source: "", // New field added here
        evidence: null,
        impact: "",
        severity: "",
      },
    };
  },
  methods: {
    handleFileUpload(event) {
      this.formData.evidence = event.target.files[0];
    },
  submitForm() {
  const payload = new FormData();
  payload.append("incidentType", this.formData.incidentType);
  payload.append("organisation", this.formData.organisation);
  payload.append("location", this.formData.location);
  payload.append("details", this.formData.details);
  payload.append("source", this.formData.source);
  payload.append("impact", this.formData.impact);
  payload.append("severity", this.formData.severity);
  if (this.formData.evidence) {
    payload.append("evidence", this.formData.evidence);
  }

  fetch("http://localhost:5000/api/incidents", {
    method: "POST",
    body: payload, // Use FormData directly
  })
    .then((response) => {
      if (!response.ok) throw new Error("Server error");
      return response.json();
    })
    .then((data) => {
      console.log("Submission successful:", data);
      alert("Your report has been submitted.");
      this.resetForm();
    })
    .catch((error) => {
      console.error("Error submitting form:", error);
      alert("Failed to submit the report. Please try again.");
    });
},
resetForm() {
      this.formData = {
        incidentType: "",
        organisation: "",
        location: "",
        details: "",
        source: "", // Reset the new field
        evidence: null,
        impact: "",
        severity: "",
      };
    },
  },
};
</script>

<style scoped>
/* Styling remains unchanged */
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

#incident-report-form p {
  text-align: center;
  font-size: 14px;
  margin-bottom: 20px;
  color: #00ffcc;
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