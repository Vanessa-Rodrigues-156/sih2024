const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();

// Middleware
app.use(cors());
app.use(express.json());

// MongoDB Connection
mongoose
  .connect("mongodb://localhost:27017/cyber_khabar", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log("Connected to MongoDB"))
  .catch((err) => console.error("MongoDB connection error:", err));

// Schema and Model
const reportSchema = new mongoose.Schema({
  title: String,
  date: String,
  summary: String,
  reportLink: String,
  details: Object, // Accepts any key-value structure
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
app.get("/api/reports", async (req, res) => {
  try {
    const report = await Report.findOne(); // Get the first report
    if (!report) {
      return res.status(404).json({ message: "No report found." });
    }
    res.json(report);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

app.post("/api/reports", async (req, res) => {
  try {
    const newReport = new Report(req.body);
    await newReport.save();
    res.status(201).json(newReport);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Server Listening
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running at http://localhost:${PORT}`);
});
