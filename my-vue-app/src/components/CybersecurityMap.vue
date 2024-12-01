<template>
  <div id="cybersecurity-map-container" class="dark-theme">
    <div id="cybersecurity-map"></div>
    <!-- Sidebar for Cyberattack Information -->
    <div v-if="showSidebar" class="sidebar">
      <h2>Latest Cyberattack</h2>
      <p><strong>Attack Name:</strong> {{ attackName }}</p>
      <p><strong>Severity:</strong> {{ severity }}</p>
      <p><strong>Attack Type:</strong> {{ attackType }}</p>
      <p><strong>Affected Region:</strong> {{ affectedRegion }}</p>
      <p><strong>Timestamp:</strong> {{ timestamp }}</p>
      <p><strong>Status:</strong> {{ connectionStatus }}</p>
      
      <hr />
      
      <h3>Live Updates</h3>
      <div class="live-updates-container">
        <ul>
          <li v-for="(log, index) in attackLogs" :key="index">{{ log }}</li>
        </ul>
      </div>
      <hr />
      
      <p><strong>Total Attacks Simulated:</strong> {{ totalAttacks }}</p>
    </div>
  </div>
</template>
<script>
import * as echarts from "echarts";
import "echarts-gl";
export default {
  name: "CybersecurityMap",
  data() {
    return {
      showSidebar: true,
      attackName: "",
      severity: "",
      attackType: "",
      affectedRegion: "",
      timestamp: "",
      connectionStatus: "Active",
      attackLogs: [],
      totalAttacks: 0,
    };
  },
  mounted() {
    this.initMap();
  },
  methods: {
    async initMap() {
      const chart = echarts.init(document.getElementById("cybersecurity-map"));
      try {
        const response = await fetch("/india.json");
        const indiaGeoJSON = await response.json();
        echarts.registerMap("india", indiaGeoJSON);
        const indianBounds = {
          latMin: 6,
          latMax: 35,
          lonMin: 68,
          lonMax: 97,
        };
        const generateRandomExternalCountry = () => ({
          lat: Math.random() * 90 - 45,
          lon: Math.random() * 360 - 180,
        });
        const generateRandomPointInIndia = () => ({
          lat:
            Math.random() * (indianBounds.latMax - indianBounds.latMin) +
            indianBounds.latMin,
          lon:
            Math.random() * (indianBounds.lonMax - indianBounds.lonMin) +
            indianBounds.lonMin,
        });
        const attackNames = [
          "Phishing Attack",
          "DDoS Attack",
          "Ransomware",
          "SQL Injection",
          "Man-in-the-Middle Attack",
          "Zero-Day Exploit",
        ];
        const severities = ["Low", "Medium", "High", "Critical"];
        const attackTypes = ["Phishing", "DDoS", "Ransomware", "Malware"];
        const regions = ["North India", "South India", "East India", "West India"];
        const generateRandomCyberattack = () => {
          const attack = attackNames[Math.floor(Math.random() * attackNames.length)];
          const severity = severities[Math.floor(Math.random() * severities.length)];
          const attackType = attackTypes[Math.floor(Math.random() * attackTypes.length)];
          const affectedRegion = regions[Math.floor(Math.random() * regions.length)];
          const timestamp = new Date().toLocaleString();
          return { attack, severity, attackType, affectedRegion, timestamp };
        };
        const option = {
          backgroundColor: "#101320",
          geo: {
            map: "india",
            roam: true,
            zoom: 1.2,
            center: [80.0, 22.0],
            itemStyle: {
              normal: {
                areaColor: "#1a1a3d",
                borderColor: "#0ff",
              },
              emphasis: {
                areaColor: "#2a2a5d",
                borderColor: "#ff8800",
              },
            },
          },
          series: [
            {
              name: "Connections",
              type: "lines",
              coordinateSystem: "geo",
              effect: {
                show: true,
                trailLength: 0,
                color: "#ff5555",
                symbol: "arrow",
                symbolSize: 8,
              },
              lineStyle: {
                color: "#ff8800",
                width: 1,
                opacity: 0.7,
              },
              data: [],
            },
            {
              name: "Points",
              type: "effectScatter",
              coordinateSystem: "geo",
              data: [],
              symbolSize: 8,
              rippleEffect: { scale: 2, brushType: "stroke" },
              itemStyle: {
                color: "#00ffcc",
                borderColor: "#ffffff",
                borderWidth: 1,
              },
            },
          ],
          animation: false,
        };
        chart.setOption(option);
        const connections = [];
        const points = [];
        let highlightIndex = null;
        const updateConnections = () => {
          const connection = {
            from: generateRandomExternalCountry(),
            to: generateRandomPointInIndia(),
          };
          const newLine = {
            coords: [
              [connection.from.lon, connection.from.lat],
              [connection.to.lon, connection.to.lat],
            ],
          };
          const newPoint = {
            name: `Point-${Math.random().toString(36).substring(7)}`,
            value: [connection.to.lon, connection.to.lat],
          };
          connections.push(newLine);
          points.push(newPoint);
          if (connections.length > 20) connections.shift();
          if (points.length > 20) points.shift();
          highlightIndex = connections.length - 1;
          chart.setOption({
            series: [
              {
                data: connections.map((line, index) => ({
                  ...line,
                  lineStyle: {
                    color: index === highlightIndex ? "#ff0000" : "#ff8800",
                    width: index === highlightIndex ? 2 : 1,
                    opacity: index === highlightIndex ? 1 : 0.7,
                  },
                })),
              },
              { data: points },
            ],
          });
          const { attack, severity, attackType, affectedRegion, timestamp } = generateRandomCyberattack();
          this.attackName = attack;
          this.severity = severity;
          this.attackType = attackType;
          this.affectedRegion = affectedRegion;
          this.timestamp = timestamp;
          this.attackLogs.push(`Attack detected: ${attack} at ${timestamp}`);
          if (this.attackLogs.length > 10) this.attackLogs.shift(); // Limit log length
          this.totalAttacks += 1;
        };
        setInterval(updateConnections, 1500);
      } catch (error) {
        console.error("Error loading GeoJSON:", error);
      }
    },
  },
};
</script>
<style scoped>
#cybersecurity-map-container {
  display: flex;
  justify-content: flex-start;
  align-items: center;
  height: 100vh;
  background-color: #101320;
}
#cybersecurity-map {
  width: 75%;
  height: 90%;
  border: 1px solid #0ff;
  box-shadow: 0 0 20px #0ff;
  border-radius: 15px;
}
.sidebar {
  position: sticky;
  top: 10%;
  right: 10px;
  background: rgba(0, 0, 0, 0.8);
  color: white;
  padding: 20px;
  border-radius: 10px;
  width: 250px;
  height: 90%;
  box-shadow: 0 0 10px #0ff;
  max-height: 90%;
  overflow-y: auto;
}
.sidebar h2 {
  margin-bottom: 10px;
}
.sidebar p {
  margin: 5px 0;
}
.sidebar ul {
  list-style-type: none;
  padding-left: 0;
}
.sidebar ul li {
  margin: 5px 0;
}
.live-updates-container {
  max-height: 200px; /* Set a max height for live updates */
  overflow-y: auto; /* Enable scrolling */
  padding-right: 10px; /* Add a bit of padding for scrollbar */
}
.dark-theme {
  color: #00ffcc;
  font-family: "Roboto", sans-serif;
}
</style>