<template>
  <nav class="navbar" :class="{ scrolled: isScrolled }">
    <div class="container">
      <div class="logo">
        <img :src="logoImage" alt="Pluto" class="logo-image" />
      </div>
      <ul class="nav-links" :class="{ active: mobileMenuOpen }">
        <li><a href="#features" @click="closeMobileMenu">Features</a></li>
        <li><a href="#how-it-works" @click="closeMobileMenu">How It Works</a></li>
        <li><a href="#pricing" @click="closeMobileMenu">Pricing</a></li>
        <li><a href="#testimonials" @click="closeMobileMenu">Testimonials</a></li>
      </ul>
      <div class="nav-actions">
        <button class="btn-secondary" @click="$router.push('/demo')">Demo</button>
        <button class="btn-primary" @click="$router.push('/signup')">Start 14 Days Free Trial</button>
      </div>
      <button class="mobile-toggle" @click="toggleMobileMenu">
        <span></span>
        <span></span>
        <span></span>
      </button>
    </div>
  </nav>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import logoImage from '../assets/logo.png'

const isScrolled = ref(false)
const mobileMenuOpen = ref(false)

const handleScroll = () => {
  isScrolled.value = window.scrollY > 50
}

const toggleMobileMenu = () => {
  mobileMenuOpen.value = !mobileMenuOpen.value
}

const closeMobileMenu = () => {
  mobileMenuOpen.value = false
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
.navbar {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  z-index: 1000;
  background: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(10px);
  transition: all 0.3s ease;
  padding: 0.5rem 0;
}

.navbar.scrolled {
  background: rgba(255, 255, 255, 0.95);
  box-shadow: 0 2px 20px rgba(0, 0, 0, 0.1);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.logo {
  display: flex;
  align-items: center;
}

.logo-image {
  height: 50px;
  width: auto;
}

.nav-links {
  display: flex;
  list-style: none;
  gap: 2rem;
}

.nav-links a {
  text-decoration: none;
  color: #4a5568;
  font-weight: 500;
  transition: color 0.3s;
}

.nav-links a:hover {
  color: #2ED0E6;
}

.nav-actions {
  display: flex;
  gap: 1rem;
}

.btn-secondary, .btn-primary {
  padding: 0.6rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  border: none;
  font-size: 0.95rem;
}

.btn-secondary {
  background: transparent;
  color: #4a5568;
}

.btn-secondary:hover {
  background: #f7fafc;
}

.btn-primary {
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(46, 208, 230, 0.3);
}

.mobile-toggle {
  display: none;
  flex-direction: column;
  gap: 4px;
  background: none;
  border: none;
  cursor: pointer;
}

.mobile-toggle span {
  width: 25px;
  height: 3px;
  background: #1a1a1a;
  border-radius: 2px;
  transition: all 0.3s;
}

@media (max-width: 768px) {
  .nav-links {
    position: fixed;
    top: 70px;
    left: -100%;
    flex-direction: column;
    background: white;
    width: 100%;
    padding: 2rem;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    transition: left 0.3s;
  }

  .nav-links.active {
    left: 0;
  }

  .nav-actions {
    display: none;
  }

  .mobile-toggle {
    display: flex;
  }
}
</style>
