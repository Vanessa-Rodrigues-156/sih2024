<template>
  <div id="app">
    <router-view>
    <div class="min-h-screen w-full bg-gray-900 flex">
      <!-- Sidebar -->
      <aside class="bg-gray-800 w-20 py-4 flex flex-col justify-between items-center">
        <div class="flex flex-col gap-4">
          <!-- Home Button -->
          <button
            @click="currentView = 'HomePage'"
            :class="currentView === 'HomePage' ? 'bg-blue-500' : 'hover:bg-gray-700'"
            class="w-12 h-12 flex items-center justify-center rounded-md transition-all">
            <font-awesome-icon :icon="['fas', 'home']" class="text-gray-200 text-lg" />
          </button>

          <!-- Dashboard Button -->
          <button
            @click="currentView = 'Dashboard'"
            :class="currentView === 'Dashboard' ? 'bg-blue-500' : 'hover:bg-gray-700'"
            class="w-12 h-12 flex items-center justify-center rounded-md transition-all">
            <font-awesome-icon :icon="['fas', 'chart-line']" class="text-gray-200 text-lg" />
          </button>

          <!-- Form Page Button -->
          <button
            @click="currentView = 'Govtreporting'"
            :class="currentView === 'Govtreporting' ? 'bg-blue-500' : 'hover:bg-gray-700'"
            class="w-12 h-12 flex items-center justify-center rounded-md transition-all">
            <font-awesome-icon :icon="['fas', 'file-alt']" class="text-gray-200 text-lg" />
          </button>

          <!-- Search Page Button -->
          <button
            @click="currentView = 'searchpage'"
            :class="currentView === 'searchpage' ? 'bg-blue-500' : 'hover:bg-gray-700'"
            class="w-12 h-12 flex items-center justify-center rounded-md transition-all">
            <font-awesome-icon :icon="['fas', 'search']" class="text-gray-200 text-lg" />
          </button>
        </div>
      </aside>

      <!-- Main Content -->
      <div class="flex-1 p-4">
        <component :is="currentViewComponent" />
      </div>
    </div>
    </router-view>
  </div>
</template>

<script>
import { library } from "@fortawesome/fontawesome-svg-core";
import { faHome, faChartLine, faFileAlt, faSearch } from "@fortawesome/free-solid-svg-icons";
import { FontAwesomeIcon } from "@fortawesome/vue-fontawesome";

// Import your components
import HomePage from "./views/HomePage.vue";
import Dashboard from "./views/Dashboard.vue";
import Govtreporting from "./views/Govtreporting.vue";
import searchpage from "./views/searchpage.vue";

// Add icons to the library
library.add(faHome, faChartLine, faFileAlt, faSearch);

export default {
  name: "App",
  components: {
    HomePage,
    Dashboard,
    Govtreporting,
    searchpage,
    FontAwesomeIcon,
  },
  data() {
    return {
      currentView: "HomePage", // Default to Homepage
    };
  },
  computed: {
    currentViewComponent() {
      switch (this.currentView) {
        case "Dashboard":
          return Dashboard;
        case "Govtreporting":
          return Govtreporting;
        case "searchpage":
          return searchpage;
        default:
          return HomePage;
      }
    },
  },
};
</script>

<style>
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
</style>
