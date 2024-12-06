<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const isLoggedIn = ref(false)
const showLoginDialog = ref(false)

onMounted(() => {
  // Check if user is logged in (e.g. by checking localStorage or session)
  const token = localStorage.getItem('userToken')
  if (token) {
    isLoggedIn.value = true
    router.push('/home')
  } else {
    showLoginDialog.value = true
  }
})

const handleLogin = () => {
  // Add login logic here
  isLoggedIn.value = false 
  showLoginDialog.value = false
  router.push('/home')
}
</script>

<template>
  <div class="app">
    <dialog v-if="showLoginDialog" class="login-dialog">
      <h2>Login</h2>
      <form @submit.prevent="handleLogin">
        <div class="form-group">
          <label>Username:</label>
          <input type="text" required>
        </div>
        <div class="form-group">
          <label>Password:</label>
          <input type="password" required>
        </div>
        <button type="submit">Login</button>
      </form>
    </dialog>
  </div>
</template>

<style scoped>
.app {
  height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
}

.login-dialog {
  padding: 20px;
  border-radius: 8px;
  border: 1px solid #ccc;
}

.form-group {
  margin: 10px 0;
}

.form-group label {
  display: block;
  margin-bottom: 5px;
}

.form-group input {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

button {
  width: 100%;
  padding: 10px;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  margin-top: 10px;
}

button:hover {
  background-color: #45a049;
}
</style>