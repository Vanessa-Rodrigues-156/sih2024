<template>
  <div id="app">
    <somecomponent />
 
  </div>
</template>

<script>

import somecomponent from "./components/somecomponent.vue";

export default {
  name: "App",
  components: {
    somecomponent,

  },
};
</script>