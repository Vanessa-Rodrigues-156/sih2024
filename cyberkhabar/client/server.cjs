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
const PORT = 5001;
const MONGO_URI = "mongodb+srv://Vashni:Vashni001@cluster0.kdgbh.mongodb.net/cyber_backend?retryWrites=true&w=majority";


// Ensure uploads directory exists
const uploadDir = "./uploads/";
if (!fs.existsSync(uploadDir)) {
  fs.mkdirSync(uploadDir);
}

// MongoDB Connection
mongoose
.connect(MONGO_URI, {
  useNewUrlParser: true,
  useUnifiedTopology: true,
})
.then(() => console.log("MongoDB connected successfully."))
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
  app.listen(PORT, () => {
    console.log(`Server is running on http://localhost:${PORT}`);
  });  