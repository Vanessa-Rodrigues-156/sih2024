<template>
  <div class="auth-container">
    <h2>Signup</h2>
    <form @submit.prevent="signup">
      <input type="text" v-model="signupUsername" placeholder="Username" required>
      <input type="password" v-model="signupPassword" placeholder="Password" required>
      <button type="submit">Signup</button>
    </form>

    <h2>Login</h2>
    <form @submit.prevent="login">
      <input type="text" v-model="loginUsername" placeholder="Username" required>
      <input type="password" v-model="loginPassword" placeholder="Password" required>
      <button type="submit">Login</button>
    </form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      signupUsername: '',
      signupPassword: '',
      loginUsername: '',
      loginPassword: ''
    };
  },
  methods: {
    async signup() {
      try {
        const response = await fetch('/api/auth/signup', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            username: this.signupUsername,
            password: this.signupPassword
          })
        });
        const data = await response.json();
        console.log(data);
      } catch (error) {
        console.error('Error:', error);
      }
    },
    async login() {
      try {
        const response = await fetch('/api/auth/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            username: this.loginUsername,
            password: this.loginPassword
          })
        });
        const data = await response.json();
        console.log(data);
      } catch (error) {
        console.error('Error:', error);
      }
    }
  }
};
</script>

<style scoped>
.auth-container {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

form {
  margin-bottom: 20px;
}

input {
  display: block;
  width: 100%;
  padding: 10px;
  margin-bottom: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

button {
  padding: 10px 20px;
  border: none;
  border-radius: 5px;
  background-color: #007bff;
  color: white;
  cursor: pointer;
}

button:hover {
  background-color: #0056b3;
}
</style>