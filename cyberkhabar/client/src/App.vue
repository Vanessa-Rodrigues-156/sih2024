<template>
  <div id="app">
    <div class="min-h-screen w-full bg-slate-900 flex">
      <!-- Check if loggedIn is true, then show the Sidebar and Main Content -->
      <div v-if="!loggedIn" class="w-full flex justify-center items-center">
        <!-- Show Login and Signup Form -->
        <form @submit.prevent="login" class="bg-slate-800 p-6 rounded-md w-96">
          <h2 class="text-white mb-4 text-2xl">Login</h2>
          <div class="mb-4">
            <label for="username" class="text-white">Username</label>
            <input v-model="loginUsername" type="text" id="username" class="mt-2 p-2 w-full" required />
          </div>
          <div class="mb-4">
            <label for="password" class="text-white">Password</label>
            <input v-model="loginPassword" type="password" id="password" class="mt-2 p-2 w-full" required />
          </div>
          <button type="submit" class="w-full bg-blue-500 text-white p-2 rounded-md">Login</button>
          <p class="mt-4 text-white">
            Don't have an account? <span @click="showSignup" class="text-blue-400 cursor-pointer">Sign Up</span>
          </p>
        </form>
      </div>

      <div v-else class="flex w-full">
        <!-- Sidebar -->
        <aside class="bg-slate-800 w-20 py-4 flex flex-col justify-between items-center">
          <div class="flex flex-col gap-4">
            <!-- Home Button -->
            <button @click="currentView = 'HomePage'"
              :class="currentView === 'HomePage' ? 'bg-blue-500' : 'hover:bg-slate-700'"
              class="w-12 h-12 flex items-center justify-center rounded-md transition-all">
              <font-awesome-icon :icon="['fas', 'home']" class="text-slate-200 text-lg" />
            </button>
            <!-- Dashboard Button -->
            <button @click="currentView = 'Dashboard'"
              :class="currentView === 'Dashboard' ? 'bg-blue-500' : 'hover:bg-slate-700'"
              class="w-12 h-12 flex items-center justify-center rounded-md transition-all">
              <font-awesome-icon :icon="['fas', 'chart-line']" class="text-slate-200 text-lg" />
            </button>
            <!-- Government Reporting Button -->
            <button @click="currentView = 'Govtreporting'"
              :class="currentView === 'Govtreporting' ? 'bg-blue-500' : 'hover:bg-slate-700'"
              class="w-12 h-12 flex items-center justify-center rounded-md transition-all">
              <font-awesome-icon :icon="['fas', 'file-alt']" class="text-slate-200 text-lg" />
            </button>
          </div>
        </aside>

        <!-- Main Content -->
        <div class="flex-1 p-4">
          <component :is="currentViewComponent" />
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { library } from "@fortawesome/fontawesome-svg-core";
import { faHome, faChartLine, faFileAlt } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

// Import your components
import HomePage from "./views/HomePage.vue";
import Dashboard from "./views/Dashboard.vue";
import Govtreporting from "./views/Govtreporting.vue";
import ttppage from './views/ttppage.vue';

// Add icons to the library
library.add(faHome, faChartLine, faFileAlt);

export default {
  name: "App",
  components: {
    HomePage,
    Dashboard,
    Govtreporting,
    ttppage,
    FontAwesomeIcon,
  },
  data() {
    return {
      currentView: "HomePage", // Default to Homepage
      loggedIn: false, // Track login state
      loginUsername: '',
      loginPassword: ''
    };
  },
  computed: {
    currentViewComponent() {
      switch (this.currentView) {
        case "Dashboard":
          return Dashboard;
        case "Govtreporting":
          return Govtreporting;
        default:
          return HomePage;
      }
    },
  },
  methods: {
    async login() {
      const response = await fetch('http://localhost:5001/api/auth/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          username: this.loginUsername,
          password: this.loginPassword,
        })
      });

      const data = await response.json();
      if (data.message) {
        // Show an alert on successful login
        window.alert(data.message);
        // Set loggedIn to true
        this.loggedIn = true;
        // After login, show the dashboard or home page
        this.currentView = 'Dashboard'; // or set to 'HomePage' if preferred
      } else {
        window.alert('Login failed!');
      }
    },

    showSignup() {
      // Handle showing signup logic here (optional)
      console.log('Show signup form');
    }
  }
};
</script>

<style>
/* Ensure full height for parent container */
#app {
  min-height: 100vh;
}

/* Sidebar styling */
aside {
  min-width: 80px;
  background-color: #2d3748;
}

button {
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

button:hover {
  background-color: rgba(96, 125, 139, 0.2);
}

/* Main Content */
.flex-1 {
  background-color: #1a202c;
  min-height: 100vh;
  padding: 20px;
  overflow-y: auto;
}

.bg-slate-900 {
  background-color: #1a202c;
}

.bg-slate-800 {
  background-color: #2d3748;
}

.w-96 {
  width: 24rem; /* width of the form */
}
</style>
