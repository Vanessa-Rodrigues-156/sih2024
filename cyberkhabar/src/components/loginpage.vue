  <template>
    <div class="login-container">
      <div class="form-container">
        <div class="toggle-buttons">
          <button 
            :class="{ active: isLogin }" 
            @click="isLogin = true"
            @mouseover="buttonHover = 'login'"
            @mouseleave="buttonHover = ''"
          >Login</button>
          <button 
            :class="{ active: !isLogin }" 
            @click="isLogin = false"
            @mouseover="buttonHover = 'signup'"
            @mouseleave="buttonHover = ''"
          >Sign Up</button>
        </div>

        <!-- Login Form -->
        <form v-if="isLogin" @submit.prevent="handleLogin" class="form">
          <h2 class="glow-text">Welcome Back</h2>
          <div class="form-group">
            <input 
              type="email" 
              v-model="loginForm.email" 
              placeholder="Email"
              :class="{ 'input-focus': activeInput === 'email' }"
              @focus="activeInput = 'email'"
              @blur="activeInput = ''"
              required
            >
          </div>
          <div class="form-group">
            <input 
              type="password" 
              v-model="loginForm.password" 
              placeholder="Password"
              :class="{ 'input-focus': activeInput === 'password' }"
              @focus="activeInput = 'password'"
              @blur="activeInput = ''"
              required
            >
          </div>
          <button type="submit" class="submit-btn" :class="{ 'btn-hover': buttonHover === 'submit' }"
            @mouseover="buttonHover = 'submit'"
            @mouseleave="buttonHover = ''">
            Login
          </button>
        </form>

        <!-- Signup Form -->
        <form v-else @submit.prevent="handleSignup" class="form">
          <h2 class="glow-text">Create Account</h2>
          <div class="form-group">
            <input 
              type="text" 
              v-model="signupForm.username" 
              placeholder="Username"
              :class="{ 'input-focus': activeInput === 'username' }"
              @focus="activeInput = 'username'"
              @blur="activeInput = ''"
              required
            >
          </div>
          <div class="form-group">
            <input 
              type="email" 
              v-model="signupForm.email" 
              placeholder="Email"
              :class="{ 'input-focus': activeInput === 'signupEmail' }"
              @focus="activeInput = 'signupEmail'"
              @blur="activeInput = ''"
              required
            >
          </div>
          <div class="form-group">
            <input 
              type="password" 
              v-model="signupForm.password" 
              placeholder="Password"
              :class="{ 'input-focus': activeInput === 'signupPassword' }"
              @focus="activeInput = 'signupPassword'"
              @blur="activeInput = ''"
              required
            >
          </div>
          <div class="form-group">
            <input 
              type="password" 
              v-model="signupForm.confirmPassword" 
              placeholder="Confirm Password"
              :class="{ 'input-focus': activeInput === 'confirmPassword' }"
              @focus="activeInput = 'confirmPassword'"
              @blur="activeInput = ''"
              required
            >
          </div>
          <button type="submit" class="submit-btn" :class="{ 'btn-hover': buttonHover === 'submit' }"
            @mouseover="buttonHover = 'submit'"
            @mouseleave="buttonHover = ''">
            Sign Up
          </button>
        </form>
      </div>
    </div>
  </template>

  <script setup lang="ts">
  import { ref, reactive } from 'vue'

  const isLogin = ref(true)
  const activeInput = ref('')
  const buttonHover = ref('')

  const loginForm = reactive({
    email: '',
    password: ''
  })

  const signupForm = reactive({
    username: '',
    email: '',
    password: '',
    confirmPassword: ''
  })

  const handleLogin = () => {
    console.log('Login attempt:', loginForm)
  }

  const handleSignup = () => {
    if (signupForm.password !== signupForm.confirmPassword) {
      alert('Passwords do not match!')
      return
    }
    console.log('Signup attempt:', signupForm)
  }
  </script>

  <style scoped>
  .login-container {
    display: flex;
    justify-content: center;
    align-items: center;
    min-height: calc(100vh - 100px);
    background-color: #1d1f27;
  }

  .form-container {
    background-color: rgba(42, 45, 58, 0.95);
    padding: 2.5rem;
    border-radius: 15px;
    box-shadow: 0 0 30px rgba(76, 175, 80, 0.2);
    width: 100%;
    max-width: 400px;
    backdrop-filter: blur(10px);
  }

  .toggle-buttons {
    display: flex;
    margin-bottom: 2rem;
    gap: 1rem;
  }

  .toggle-buttons button {
    flex: 1;
    padding: 0.75rem;
    border: none;
    background-color: #363a4f;
    color: #ffffff;
    cursor: pointer;
    border-radius: 5px;
    transition: all 0.3s ease;
    text-transform: uppercase;
    letter-spacing: 1px;
  }

  .toggle-buttons button.active {
    background-color: #4CAF50;
    box-shadow: 0 0 15px rgba(76, 175, 80, 0.5);
  }

  .glow-text {
    text-align: center;
    color: #ffffff;
    text-shadow: 0 0 10px rgba(76, 175, 80, 0.5);
    margin-bottom: 1.5rem;
  }

  .form {
    display: flex;
    flex-direction: column;
    gap: 1.2rem;
  }

  .form-group input {
    width: 100%;
    padding: 0.75rem;
    border: 1px solid #363a4f;
    border-radius: 5px;
    font-size: 1rem;
    background-color: #363a4f;
    color: #ffffff;
    transition: all 0.3s ease;
  }

  .input-focus {
    border-color: #4CAF50 !important;
    box-shadow: 0 0 10px rgba(76, 175, 80, 0.3);
    background-color: #404359 !important;
  }

  .submit-btn {
    background-color: #4CAF50;
    color: white;
    padding: 0.75rem;
    border: none;
    border-radius: 5px;
    cursor: pointer;
    font-size: 1rem;
    text-transform: uppercase;
    letter-spacing: 1px;
    transition: all 0.3s ease;
  }

  .btn-hover {
    background-color: #45a049;
    box-shadow: 0 0 20px rgba(76, 175, 80, 0.5);
    transform: translateY(-2px);
  }

  input::placeholder {
    color: #8c8fa3;
  }

  @keyframes glow {
    0% { box-shadow: 0 0 5px rgba(76, 175, 80, 0.5); }
    50% { box-shadow: 0 0 20px rgba(76, 175, 80, 0.8); }
    100% { box-shadow: 0 0 5px rgba(76, 175, 80, 0.5); }
  }

  .form-container:hover {
    animation: glow 2s infinite;
  }
  </style>
