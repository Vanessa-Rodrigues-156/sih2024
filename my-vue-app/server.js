const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');
const multer = require('multer');
const path = require('path');
const cors = require('cors');
const fs = require('fs');

// Environment Variables
require('dotenv').config();
const PORT = process.env.PORT || 3000;
const MONGO_URI = process.env.MONGO_URI || 'mongodb://localhost:27017/cybersecurity-reports';

// Ensure uploads directory exists
const uploadDir = './uploads/';
if (!fs.existsSync(uploadDir)) {
    fs.mkdirSync(uploadDir);
}

const app = express();

// Connect to MongoDB
mongoose
    .connect(MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
    .then(() => console.log('MongoDB connected'))
    .catch(err => console.error('MongoDB connection error:', err));

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use('/uploads', express.static(path.join(__dirname, 'uploads')));

// File Upload Setup
const storage = multer.diskStorage({
    destination: uploadDir,
    filename: (req, file, cb) => {
        cb(null, `${Date.now()}-${file.originalname}`);
    },
});
const upload = multer({ storage });

// Mongoose Schema and Model
const incidentSchema = new mongoose.Schema({
    incidentType: { type: String, required: true },
    organisation: { type: String, required: true },
    location: { type: String },
    details: { type: String, required: true },
    source: { type: String, required: true },
    evidence: { type: String },
    impact: { type: String },
    severity: { type: String },
});
const Incident = mongoose.model('Incident', incidentSchema);

// Routes
app.get('/', (req, res) => {
    res.send('Cybersecurity Incident Report API is running.');
});

app.post('/api/submit', upload.single('evidence'), async (req, res) => {
    try {
        const { incidentType, organisation, location, details, source, impact, severity } = req.body;
        const evidence = req.file ? req.file.filename : null;

        if (!incidentType || !organisation || !details || !source) {
            return res.status(400).json({ message: 'Required fields are missing.' });
        }

        const incident = new Incident({
            incidentType,
            organisation,
            location,
            details,
            source,
            evidence,
            impact,
            severity,
        });

        await incident.save();
        res.status(201).json({ message: 'Incident report submitted successfully.' });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Error submitting incident report.', error: error.message });
    }
});

app.get('/api/reports', async (req, res) => {
    const { page = 1, limit = 10 } = req.query;
    try {
        const reports = await Incident.find()
            .skip((page - 1) * limit)
            .limit(parseInt(limit));
        const total = await Incident.countDocuments();
        res.status(200).json({ total, page, limit, reports });
    } catch (error) {
        console.error(error);
        res.status(500).json({ message: 'Error fetching reports.', error: error.message });
    }
});

// Start Server
app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
});
