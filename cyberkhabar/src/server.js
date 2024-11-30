const express = require("express");
const { Pool } = require("pg");
const bodyParser = require("body-parser");
const cors = require("cors");

const app = express();
app.use(cors());
app.use(bodyParser.json());

// PostgreSQL Configuration
const pool = new Pool({
  user: "your_username",
  host: "localhost",
  database: "your_database",
  password: "your_password",
  port: 5432,
});

// Endpoint to fetch indicator data
app.get("/indicators", async (req, res) => {
  try {
    const result = await pool.query("SELECT * FROM indicators;");
    res.json(result.rows);
  } catch (err) {
    console.error(err);
    res.status(500).send("Database Error");
  }
});

// Start server
app.listen(5000, () => {
  console.log("Server running on port 5000");
});
