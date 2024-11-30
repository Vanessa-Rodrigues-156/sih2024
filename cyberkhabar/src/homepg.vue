<template>
  <div
    id="app"
    class="dashboard">
    <header class="header">
      <h1>Indicator of Compromise</h1>
    </header>
    <div class="content">
      <div class="sidebar">
        <h2>Threat Feeds</h2>
        <ul>
          <li
            v-for="feed in threatFeeds"
            :key="feed.id">
            {{ feed.name }}
          </li>
        </ul>
      </div>
      <div class="main">
        <div class="heatmap">
          <h3>Indicator Heatmap</h3>
          <div
            v-for="day in indicatorData"
            :key="day.id"
            class="day"
            :class="{ active: day.active }">
            {{ day.date }}
          </div>
        </div>
        <div class="details">
          <h3>Details</h3>
          <p><strong>Severity:</strong> {{ severity }}</p>
          <p><strong>Category:</strong> {{ category }}</p>
          <p><strong>First Seen:</strong> {{ firstSeen }}</p>
          <p><strong>Last Seen:</strong> {{ lastSeen }}</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      threatFeeds: [],
      indicatorData: [],
      severity: "Critical",
      category: "IP Address",
      firstSeen: "July 16, 2008",
      lastSeen: "May 5, 2022",
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get("http://localhost:5000/indicators");
        this.indicatorData = response.data;
      } catch (error) {
        console.error("Error fetching data:", error);
      }
    },
  },
};
</script>

<style>
.dashboard {
  display: flex;
  flex-direction: column;
  font-family: Arial, sans-serif;
}
.header {
  background-color: #333;
  color: #fff;
  padding: 1rem;
}
.content {
  display: flex;
  padding: 1rem;
}
.sidebar {
  width: 20%;
  background-color: #f4f4f4;
  padding: 1rem;
}
.main {
  width: 80%;
  padding: 1rem;
}
.heatmap {
  display: grid;
  grid-template-columns: repeat(7, 1fr);
  gap: 0.5rem;
}
.day {
  width: 2rem;
  height: 2rem;
  background-color: #ccc;
  text-align: center;
  line-height: 2rem;
}
.day.active {
  background-color: red;
  color: white;
}
</style>
