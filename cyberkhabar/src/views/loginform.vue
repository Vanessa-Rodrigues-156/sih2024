<template>
  <div class="login-form">
    <form @submit.prevent="handleLogin">
      <div class="form-group">
        <label for="username">Username</label>
        <input 
          type="text"
          id="username"
          v-model="username"
          class="form-control"
          required
        >
      </div>
      <div class="form-group">
        <label for="password">Password</label>
        <input 
          type="password"
          id="password"
          v-model="password"
          class="form-control"
          required
        >
      </div>
      <button type="submit" class="btn btn-primary">Login</button>
      <p v-if="error" class="error">{{ error }}</p>
    </form>
  </div>
</template>

<script>
export default {
  name: 'LoginForm',
  data() {
    return {
      username: '',
      password: '',
      error: null
    }
  },
  methods: {
    async handleLogin() {
      try {
        // Here you would typically make an API call to validate credentials
        // This is a mock validation
        if (this.username && this.password) {
          const userData = {
            username: this.username,
            isAuthenticated: true,
            token: 'mock-token-' + Date.now() // In real app, this would come from backend
          }
          
          // Store user data in session storage
          sessionStorage.setItem('user', JSON.stringify(userData))
          
          // Emit login success event
          this.$emit('login-success', userData)
          
          // Redirect to dashboard or home page
          this.$router.push('/homepage')
        } else {
          this.error = 'Please enter both username and password'
        }
      } catch (err) {
        this.error = 'Login failed. Please try again.'
        console.error('Login error:', err)
      }
    }
  }
}
</script>

<style scoped>
.login-form {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
}

.form-group {
  margin-bottom: 15px;
}

.form-control {
  width: 100%;
  padding: 8px;
  border: 1px solid #ddd;
  border-radius: 4px;
}

.btn {
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
}

.btn:hover {
  background-color: #0056b3;
}

.error {
  color: red;
  margin-top: 10px;
  text-align: center;
}
</style>
