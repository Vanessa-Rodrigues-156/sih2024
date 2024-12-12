<template>

  <div id="app">

    <div class="min-h-screen w-auto bg-slate-900 flex">
      <!-- Sidebar -->
      <aside class="bg-slate-800 flex flex-col justify-between items-center py-4 w-[4%]">

        <div class="flex flex-col gap-4">
          <!-- Home Button -->
          <button @click="currentView = 'HomePage'"
            :class="currentView === 'HomePage' ? 'bg-blue-500' : 'hover:bg-slate-700'"
            class="w-12 h-12 flex items-center justify-center rounded-md transition-all">
            <font-awesome-icon :icon="['fas', 'home']"
              class="text-slate-200 text-lg" />
          </button>

          <!-- Dashboard Button -->
          <button @click="currentView = 'Dashboard'"
            :class="currentView === 'Dashboard' ? 'bg-blue-500' : 'hover:bg-slate-700'"
            class="w-12 h-12 flex items-center justify-center rounded-md transition-all">
            <font-awesome-icon :icon="['fas', 'chart-line']"
              class="text-slate-200 text-lg" />
          </button>

          <!-- Government Reporting Button -->
          <button @click="currentView = 'Govtreporting'"
            :class="currentView === 'Govtreporting' ? 'bg-blue-500' : 'hover:bg-slate-700'"
            class="w-12 h-12 flex items-center justify-center rounded-md transition-all">
            <font-awesome-icon :icon="['fas', 'file-alt']"
              class="text-slate-200 text-lg" />
          </button>
          
        </div>
      </aside>

      <!-- Main Content -->

      <div class="flex-1">
        <!-- Dynamically load the correct component based on currentView -->
        <component :is="currentViewComponent" />
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
};
</script>

<style>
/* Sidebar Button Animation */
button {
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
}

button:hover {
  background-color: rgba(96, 125, 139, 0.2);
}
</style>
