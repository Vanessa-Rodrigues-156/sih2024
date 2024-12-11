<template>
    <div class="min-h-screen bg-gray-900 py-8 px-4 sm:px-6 lg:px-8">
        <div id="cyber-report-form" class="max-w-4xl mx-auto bg-gray-800 text-white rounded-lg p-5 shadow-lg">
            <header>
                <h1 class="text-center  text-blue-400 mb-4:text-3xl lg:text-4xl font-bold">Report Cybersecurity Incident</h1>

              
            </header>
            <form @submit.prevent="submitReport" class="mt-8 space-y-6">
                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="form-group">
                        <label for="incidentType" class="block mb-1 font-bold text-gray-200">Type of Incident</label>
                        <select v-model="form.incidentType" id="incidentType" required class="w-full p-2 text-base border border-gray-600 rounded bg-gray-700 text-white">
                            <option disabled value="">Select Incident Type</option>
                            <option>Phishing</option>
                            <option>Data Breach</option>
                            <option>Ransomware</option>
                            <option>Denial of Service</option>
                            <option>Other</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="organization" class="block mb-1 font-bold text-gray-200">Organization</label>
                        <input type="text" id="organization" v-model="form.organization" placeholder="Enter organization (e.g., Google, Microsoft...)" class="w-full p-2 text-base border border-gray-600 rounded bg-gray-700 text-white placeholder-gray-400" />
                    </div>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div class="form-group">
                        <label for="location" class="block mb-1 font-bold text-gray-200">Location (Optional)</label>
                        <input type="text" id="location" v-model="form.location" placeholder="Enter location (e.g., city or region)" class="w-full p-2 text-base border border-gray-600 rounded bg-gray-700 text-white placeholder-gray-400" />
                    </div>

                    <div class="form-group">
                        <label for="source" class="block mb-1 font-bold text-gray-200">Source of Information</label>
                        <input type="text" id="source" v-model="form.source" placeholder="Enter the source (e.g., internal report, Twitter, Reddit...)" class="w-full p-2 text-base border border-gray-600 rounded bg-gray-700 text-white placeholder-gray-400" />
                    </div>
                </div>

                <div class="form-group">
                    <label for="details" class="block mb-1 font-bold text-gray-200">Incident Details</label>
                    <textarea id="details" v-model="form.details" rows="5" placeholder="Provide details of the incident..." required class="w-full p-2 text-base border border-gray-600 rounded bg-gray-700 text-white placeholder-gray-400"></textarea>
                </div>

                <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
                    <div class="form-group">
                        <label for="evidence" class="block mb-1 font-bold text-gray-200">Upload Evidence (Optional)</label>
                        <input type="file" id="evidence" @change="handleFileUpload" class="w-full p-2 text-base border border-gray-600 rounded bg-gray-700 text-white"/>
                    </div>

                    <div class="form-group">
                        <label for="impact" class="block mb-1 font-bold text-gray-200">Impact of Incident</label>
                        <select v-model="form.impact" id="impact" class="w-full p-2 text-base border border-gray-600 rounded bg-gray-700 text-white">
                            <option disabled value="">Select Impact</option>
                            <option>Low</option>
                            <option>Medium</option>
                            <option>High</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="severity" class="block mb-1 font-bold text-gray-200">Severity Level</label>
                        <select v-model="form.severity" id="severity" class="w-full p-2 text-base border border-gray-600 rounded bg-gray-700 text-white">
                            <option disabled value="">Select Severity</option>
                            <option>Low</option>
                            <option>Moderate</option>
                            <option>Critical</option>
                        </select>
                    </div>
                </div>

                <button type="submit" class="w-full p-3 bg-blue-500 rounded text-xl text-white hover:bg-gray-700 hover:border transition-colors duration-300">Submit Report</button>
            </form>
            <footer class="text-center mt-8 text-xs md:text-sm text-gray-400">
                <p>© 2024 Cyberkhabar. Empowering a secure digital India.</p>
            </footer>
        </div>
    </div>
</template>

<script>
export default {
    name: 'GovtReporting',
    data() {
        return {
            form: {
                incidentType: '',
                organization: '',
                location: '',
                details: '',
                source: '',
                evidence: null,
                impact: '',
                severity: ''
            }
        }
    },
    methods: {
        handleFileUpload(event) {
            this.form.evidence = event.target.files[0]
        },
        async submitReport() {
            try {
                const formData = new FormData()
                
                Object.keys(this.form).forEach(key => {
                    formData.append(key, this.form[key])
                })

                const response = await fetch('/api/reports', {
                    method: 'POST',
                    body: formData
                })

                if (response.ok) {
                    this.resetForm()
                    alert('Report submitted successfully!')
                } else {
                    throw new Error('Failed to submit report')
                }
            } catch (error) {
                console.error('Error submitting report:', error)
                alert('Failed to submit report. Please try again.')
            }
        },
        resetForm() {
            this.form = {
                incidentType: '',
                organization: '',
                location: '',
                details: '',
                source: '',
                evidence: null,
                impact: '',
                severity: ''
            }
        }
    }
}
</script>
