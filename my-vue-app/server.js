const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const multer = require("multer");
const cors = require("cors");
const path = require("path");
const fs = require("fs");
require("dotenv").config();

const app = express();

// Environment Variables
const PORT = process.env.PORT || 5000;
const MONGO_URI = process.env.MONGO_URI || "mongodb://localhost:27017/cyber_backend";

// Ensure uploads directory exists
const uploadDir = "./uploads/";
if (!fs.existsSync(uploadDir)) {
  fs.mkdirSync(uploadDir);
}

// MongoDB Connection
mongoose
  .connect(MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log("MongoDB connected"))
  .catch((err) => console.error("MongoDB connection error:", err));

// Middleware
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));
app.use("/uploads", express.static(path.join(__dirname, "uploads")));

// File Upload Setup
const storage = multer.diskStorage({
  destination: uploadDir,
  filename: (req, file, cb) => {
    cb(null, `${Date.now()}-${file.originalname}`);
  },
});
const upload = multer({ storage });

// Schemas and Models
// News Schema
const newsSchema = new mongoose.Schema({
  title: String,
  content: String,
  type: String,
  severity: String,
  impact: String,
  region: String,
  views: { type: Number, default: 0 },
  date: { type: Date, default: Date.now },
});
const News = mongoose.model("News", newsSchema);

// Incident Report Schema
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
const Incident = mongoose.model("Incident", incidentSchema);

// Cybersecurity Report Schema
const reportSchema = new mongoose.Schema({
  title: String,
  date: String,
  summary: String,
  reportLink: String,
  details: Object,
  insights: [
    {
      key: String,
      value: String,
    },
  ],
  sources: [
    {
      title: String,
      url: String,
    },
  ],
});
const Report = mongoose.model("Report", reportSchema);

// Routes
// Home Route
app.get("/", (req, res) => {
  res.send("Cyber Backend API is running.");
});

// News Routes
app.get("/api/news", async (req, res) => {
  try {
    const { type, severity, impact } = req.query;
    const filters = {};

    if (type) filters.type = type;
    if (severity) filters.severity = severity;
    if (impact) filters.impact = impact;

    const news = await News.find(filters);
    res.json(news);
  } catch (err) {
    res.status(500).send(err);
  }
});

app.get("/api/stat", async (req, res) => {
  try {
    const totalArticles = await News.countDocuments({
      date: { $gte: new Date().setHours(0, 0, 0, 0) },
    });

    const trendingTopic = await News.aggregate([
      { $group: { _id: "$type", count: { $sum: 1 } } },
      { $sort: { count: -1 } },
      { $limit: 1 },
    ]);

    const topRegion = await News.aggregate([
      { $group: { _id: "$region", count: { $sum: 1 } } },
      { $sort: { count: -1 } },
      { $limit: 1 },
    ]);

    const topArticle = await News.findOne().sort({ views: -1 }).exec();

    res.json({
      totalArticles,
      trendingTopic: trendingTopic[0]?._id || "N/A",
      topRegion: topRegion[0]?._id || "N/A",
      topArticle: topArticle ? topArticle.title : "N/A",
    });
  } catch (err) {
    res.status(500).send(err);
  }
});

// Incident Report Routes
app.post("/api/incidents", upload.single("evidence"), async (req, res) => {
  try {
    const { incidentType, organisation, location, details, source, impact, severity } = req.body;
    const evidence = req.file ? req.file.filename : null;

    if (!incidentType || !organisation || !details || !source) {
      return res.status(400).json({ message: "Required fields are missing." });
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
    res.status(201).json({ message: "Incident report submitted successfully." });
  } catch (err) {
    res.status(500).json({ message: "Error submitting incident report.", error: err.message });
  }
});

app.get("/api/reports", async (req, res) => {
  const { page = 1, limit = 10 } = req.query;
  try {
    const reports = await Incident.find()
      .skip((page - 1) * limit)
      .limit(parseInt(limit));
    const total = await Incident.countDocuments();
    res.status(200).json({ total, page, limit, reports });
  } catch (err) {
    res.status(500).json({ message: "Error fetching reports.", error: err.message });
  }
});

// Cybersecurity Reports
app.post("/api/reports", async (req, res) => {
  try {
    const newReport = new Report(req.body);
    await newReport.save();
    res.status(201).json(newReport);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.get("/api/reports/cyber", async (req, res) => {
  try {
    const report = await Report.findOne();
    if (!report) {
      return res.status(404).json({ message: "No report found." });
    }
    res.json(report);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Start the Server
app.listen(PORT, () => {
  console.log(`Server is running on http://localhost:${PORT}`);
});
