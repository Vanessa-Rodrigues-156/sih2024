<template>
  <div class="flex justify-center items-center min-h-screen bg-gray-900 text-white">
    <div class="bg-gray-800 p-8 rounded-lg shadow-lg w-full max-w-md">
      <!-- Login Form -->
      <div v-if="showLogin">
        <h2 class="text-2xl font-semibold text-center mb-6">Login</h2>
        <form @submit.prevent="login" class="space-y-4">
          <div>
            <input
              type="text"
              v-model="loginUsername"
              placeholder="Username"
              class="w-full px-4 py-2 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white"
              required
            />
          </div>
          <div>
            <input
              type="password"
              v-model="loginPassword"
              placeholder="Password"
              class="w-full px-4 py-2 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white"
              required
            />
          </div>
          <button
            type="submit"
            class="w-full py-2 px-4 bg-blue-600 text-white rounded-lg hover:bg-blue-700 focus:outline-none"
          >
            Login
          </button>
        </form>
        <p class="text-center text-sm mt-4">
          Don't have an account?
          <span @click="toggleForm" class="text-blue-400 cursor-pointer">Signup</span>
        </p>
      </div>

      <!-- Signup Form -->
      <div v-if="!showLogin">
        <h2 class="text-2xl font-semibold text-center mb-6">Signup</h2>
        <form @submit.prevent="signup" class="space-y-4">
          <div>
            <input
              type="text"
              v-model="signupUsername"
              placeholder="Username"
              class="w-full px-4 py-2 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white"
              required
            />
          </div>
          <div>
            <input
              type="password"
              v-model="signupPassword"
              placeholder="Password"
              class="w-full px-4 py-2 border border-gray-600 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500 bg-gray-700 text-white"
              required
            />
          </div>
          <button
            type="submit"
            class="w-full py-2 px-4 bg-blue-600 text-white rounded-lg hover:bg-blue-700 focus:outline-none"
          >
            Signup
          </button>
        </form>
        <p class="text-center text-sm mt-4">
          Already have an account?
          <span @click="toggleForm" class="text-blue-400 cursor-pointer">Login</span>
        </p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'Authentication',
  data() {
    return {
      showLogin: true, // Determines whether to show login or signup form
      signupUsername: '',
      signupPassword: '',
      loginUsername: '',
      loginPassword: '',
    };
  },
  methods: {
    async signup() {
      try {
        const response = await fetch('http://localhost:5001/api/auth/signup', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            username: this.signupUsername,
            password: this.signupPassword,
          }),
        });

        const data = await response.json();

        if (data.message) {
          // Show an alert on successful signup
          window.alert(data.message);
          // Reset the signup form fields
          this.signupUsername = '';
          this.signupPassword = '';
          // After signup, switch to login form
          this.toggleForm();
        }
      } catch (error) {
        console.error('Error:', error);
        window.alert('Signup failed. Please try again.');
      }
    },
    async login() {
      try {
        const response = await fetch('http://localhost:5001/api/auth/login', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({
            username: this.loginUsername,
            password: this.loginPassword,
          }),
        });

        const data = await response.json();

        if (data.message) {
          // Show an alert on successful login
          window.alert(data.message);
          // Reset the login form fields
          this.loginUsername = '';
          this.loginPassword = '';
          //after login go to homepage 
          this.$router.push('/home');
        } else {
          window.alert('Invalid credentials. Please try again.');
        }
      } catch (error) {
        console.error('Error:', error);
        window.alert('Login failed. Please try again.');
      }
    },
    toggleForm() {
      this.showLogin = !this.showLogin; // Toggle between login and signup
    },
  },
};
</script>

<style scoped>
/* Dark Mode Styles */
body {
  background-color: #1a202c; /* Dark background */
}
</style>
