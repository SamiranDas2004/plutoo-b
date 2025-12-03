<template>
  <div class="signup-page">
    <div class="signup-container">
      <div class="signup-box">
        <div class="logo-section">
          <h1>Pluto</h1>
          <p>Start your 14-day free trial</p>
        </div>

        <form @submit.prevent="handleSignup" class="signup-form">
          <input v-model="form.full_name" type="text" placeholder="Full name" required />
          <input v-model="form.email" type="email" placeholder="Work email" required />
          <input v-model="form.company_name" type="text" placeholder="Company name" required />
          <input v-model="form.password" type="password" placeholder="Password (min. 8 characters)" required minlength="8" />

          <button type="submit" class="signup-btn" :disabled="loading">
            {{ loading ? 'Creating account...' : 'Get Started' }}
          </button>
        </form>

        <p v-if="error" class="error">{{ error }}</p>

        <p class="terms">By signing up, you agree to our <a href="#">Terms</a> and <a href="#">Privacy Policy</a></p>
        <p class="login">Already have an account? <a href="#">Sign in</a></p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useSeo } from '../composables/useSeo'

useSeo({
  title: 'Start Free Trial | Pluto AI Customer Support',
  description: 'Start your 14-day free trial of Pluto AI customer support. No credit card required.',
  keywords: 'free trial, signup, AI customer support'
})

const router = useRouter()
const loading = ref(false)
const error = ref('')

const form = ref({
  full_name: '',
  email: '',
  company_name: '',
  password: ''
})

const handleSignup = async () => {
  loading.value = true
  error.value = ''

  try {
    const response = await fetch('http://localhost:8000/auth/signup', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        full_name: form.value.full_name,
        email: form.value.email,
        company_name: form.value.company_name,
        password: form.value.password
      })
    })

    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.detail || 'Signup failed')
    }

    // Store user data
    localStorage.setItem('pluto_user', JSON.stringify({
      ...data.user,
      full_name: form.value.full_name,
      company_name: form.value.company_name
    }))

    // Redirect to success page with bot token
    router.push(`/signup-success?token=${data.user.bot_token}`)

  } catch (err) {
    error.value = err.message || 'Something went wrong. Please try again.'
  } finally {
    loading.value = false
  }
}
</script>

<style scoped>
.signup-page {
  min-height: 100vh;
  background: #fafafa;
  display: flex;
  align-items: center;
  justify-content: center;
  padding: 2rem;
}

.signup-container {
  width: 100%;
  max-width: 420px;
}

.signup-box {
  background: white;
  border-radius: 12px;
  padding: 3rem 2.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.logo-section {
  text-align: center;
  margin-bottom: 2rem;
}

.logo-section h1 {
  font-size: 2rem;
  font-weight: 800;
  color: #1a1a1a;
  margin-bottom: 0.5rem;
}

.logo-section p {
  color: #64748b;
  font-size: 1rem;
}

.signup-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  margin-bottom: 1.5rem;
}

.signup-form input {
  padding: 0.875rem 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  font-size: 0.95rem;
  transition: all 0.2s;
}

.signup-form input:focus {
  outline: none;
  border-color: #2ED0E6;
  box-shadow: 0 0 0 3px rgba(46, 208, 230, 0.1);
}

.signup-btn {
  padding: 0.875rem;
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.2s;
  margin-top: 0.5rem;
}

.signup-btn:hover:not(:disabled) {
  transform: translateY(-1px);
  box-shadow: 0 4px 12px rgba(46, 208, 230, 0.3);
}

.signup-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.error {
  color: #ef4444;
  font-size: 0.9rem;
  text-align: center;
  margin-bottom: 1rem;
  padding: 0.75rem;
  background: #fee2e2;
  border-radius: 6px;
}

.terms {
  text-align: center;
  font-size: 0.85rem;
  color: #64748b;
  margin-bottom: 1rem;
}

.terms a {
  color: #2ED0E6;
  text-decoration: none;
}

.terms a:hover {
  text-decoration: underline;
}

.login {
  text-align: center;
  font-size: 0.9rem;
  color: #64748b;
  padding-top: 1.5rem;
  border-top: 1px solid #e2e8f0;
}

.login a {
  color: #2ED0E6;
  text-decoration: none;
  font-weight: 600;
}

.login a:hover {
  text-decoration: underline;
}

@media (max-width: 480px) {
  .signup-box {
    padding: 2rem 1.5rem;
  }

  .logo-section h1 {
    font-size: 1.75rem;
  }
}
</style>
