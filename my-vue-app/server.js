const express = require("express");
const mongoose = require("mongoose");
const cors = require("cors");

const app = express();
const port = 5000;

// Enable Cross-Origin Requests
app.use(cors());

// Body parser middleware
app.use(express.json());

// Connect to MongoDB (change the URI if you're using MongoDB Atlas)
mongoose.connect("mongodb://localhost:27017/cybernews", { useNewUrlParser: true, useUnifiedTopology: true })
  .then(() => console.log("MongoDB connected"))
  .catch((err) => console.log(err));

// Define the News schema
const newsSchema = new mongoose.Schema({
  title: String,
  content: String,
  type: String,
  severity: String,
  impact: String,
  region: String,
  views: { type: Number, default: 0 },
  date: { type: Date, default: Date.now }
});

// Create the News model
const News = mongoose.model("News", newsSchema);

// Get all news articles
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
// Get statistics for the dashboard
app.get("/api/stat", async (req, res) => {
  try {
    // Fetch total articles published today
    const totalArticles = await News.countDocuments({
      date: { $gte: new Date().setHours(0, 0, 0, 0) },
    });

    // Fetch most trending topic (most frequent type)
    const trendingTopic = await News.aggregate([
      { $group: { _id: "$type", count: { $sum: 1 } } },
      { $sort: { count: -1 } },
      { $limit: 1 },
    ]);

    // Fetch top contributing region
    const topRegion = await News.aggregate([
      { $group: { _id: "$region", count: { $sum: 1 } } },
      { $sort: { count: -1 } },
      { $limit: 1 },
    ]);

    // Fetch the top viewed article
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

// Start the server
app.listen(port, () => {
  console.log(`Server running at http://localhost:${port}`);
});
