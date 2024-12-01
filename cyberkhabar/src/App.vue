<template>


  <div class="main-container">
    <div class="header">
      <h1 class="neon-title">Cyber Khabar</h1>
    </div>
    <div id="app">
      <LoginPage v-if="!isLoggedIn" @login-success="handleLoginSuccess" />
      <HomePage v-else />
    </div>
  </div>




</template>

<script setup lang="ts">
import { ref } from 'vue'
import LoginPage from "./components/loginpage.vue"
import HomePage from "./components/homepage.vue"

const isLoggedIn = ref(false)

const handleLoginSuccess = () => {
  isLoggedIn.value = true
}
</script>

<style>





.main-container {
  display: flex;
  flex-direction: column;
  min-height: 100vh;
}

.header {
  padding: 0.5rem;
  text-align: center;
  background-color: rgba(29, 31, 39, 0.95);
}

.neon-title {
  margin: 0;
  font-size: 2.5rem;
  text-transform: uppercase;
  letter-spacing: 2px;
  color: #4CAF50;
  text-shadow: 0 0 10px #4CAF50, 0 0 20px #4CAF50, 0 0 30px #4CAF50;
  animation: neonPulse 1.5s infinite alternate;
}

@keyframes neonPulse {
  from {
    text-shadow: 0 0 10px #4CAF50, 0 0 20px #4CAF50, 0 0 30px #4CAF50;
  }
  to {
    text-shadow: 0 0 15px #4CAF50, 0 0 25px #4CAF50, 0 0 35px #4CAF50;
  }
}

body {
  margin: 0;


  padding: 0;
  font-family: 'Arial', sans-serif;
  background-color: #1d1f27;
  color: #ffffff;

}
</style>
