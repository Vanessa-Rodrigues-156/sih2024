const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const multer = require("multer");
const cors = require("cors");
const path = require("path");
const fs = require("fs");
const bcrypt = require("bcryptjs");
const neo4j = require("neo4j-driver");
require("dotenv").config();

const app = express();

// Environment Variables
const PORT = process.env.PORT || 5001;
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

// Incident Schema
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

// Create Neo4j Driver
const driver = neo4j.driver(
  "bolt://10.150.0.121:7687",
  neo4j.auth.basic("admin", "QWERTYUIOP0")
);

// Function to create a session for the auth database (hardcoded)
function createSession() {
  return driver.session({
    database: "auth",  // Hardcoded 'auth' database
    defaultAccessMode: neo4j.session.WRITE,
  });
}

// Incident Reporting Route
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

// Signup Route
app.post("/api/auth/signup", async (req, res) => {
  const { username, password } = req.body;

  if (!username || !password) {
    return res.status(400).json({ error: "Username and password are required." });
  }

  const session = createSession();

  try {
    const hashedPassword = await bcrypt.hash(password, 10);

    // Create User under the 'auth' database with a specific label
    const result = await session.run(
      "CREATE (u:AuthDataset:User {username: $username, password: $password}) RETURN u",
      { username, password: hashedPassword }
    );

    res.status(201).json({ message: "Signup successful!", user: result.records[0].get("u").properties });
  } catch (error) {
    console.error("Error creating user:", error);
    res.status(500).json({ error: "Internal server error" });
  } finally {
    await session.close();
  }
});

// Login Route
app.post("/api/auth/login", async (req, res) => {
  const { username, password } = req.body;

  if (!username || !password) {
    return res.status(400).json({ error: "Username and password are required." });
  }

  const session = createSession();

  try {
    // Match user under the 'auth' database with the 'AuthDataset' label
    const result = await session.run(
      "MATCH (u:AuthDataset:User {username: $username}) RETURN u",
      { username }
    );

    if (result.records.length === 0) {
      return res.status(404).json({ message: "User not found" });
    }

    const user = result.records[0].get("u").properties;
    const match = await bcrypt.compare(password, user.password);

    if (match) {
      res.status(200).json({ message: "Login successful", user });
    } else {
      res.status(400).json({ message: "Invalid password" });
    }
  } catch (error) {
    console.error("Error during login:", error);
    res.status(500).json({ error: "Internal server error" });
  } finally {
    await session.close();
  }
});

// Start Server
app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
