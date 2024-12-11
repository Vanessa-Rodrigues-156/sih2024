<template>
  <div id="app">
    <Dashboard />
    <Govtreporting />
  
 
  </div>
</template>

<script>

import Dashboard from "./views/Dashboard.vue";
import Govtreporting from "./views/Govtreporting.vue";

export default {
  name: "App",
  components: {
    Dashboard,
    Govtreporting
   
  },
};
</script> 
