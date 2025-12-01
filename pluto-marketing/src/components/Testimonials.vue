<template>
  <section id="partners" class="partners">
    <div class="container">
      <div class="section-header">
        <div class="badge">Trusted By</div>
        <h2 class="section-title">Our <span class="gradient-text">Partners</span></h2>
        <p class="section-description">Powering customer support for leading companies worldwide</p>
      </div>
      <div class="scroll-wrapper">
        <div class="scroll-track" :style="{ transform: `translateX(${scrollPosition}px)` }">
          <div class="partner-card" v-for="(partner, index) in [...partners, ...partners, ...partners]" :key="index">
            <div class="partner-glow"></div>
            <img :src="partner.logo" :alt="partner.name" class="partner-logo" />
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'
import redxLogo from '../assets/redx.png'
import fotatoLogo from '../assets/fotato.png'
import jusgoLogo from '../assets/jusgo.png'
import hostasiaLogo from '../assets/hostasia.png'
import vistaLogo from '../assets/vista.png'

const scrollPosition = ref(0)
let animationFrame = null

const animate = () => {
  scrollPosition.value -= 1
  animationFrame = requestAnimationFrame(animate)
}

onMounted(() => {
  animate()
})

onUnmounted(() => {
  if (animationFrame) {
    cancelAnimationFrame(animationFrame)
  }
})

const partners = [
  { name: 'RedX', logo: redxLogo },
  { name: 'Fotato', logo: fotatoLogo },
  { name: 'Jusgo', logo: jusgoLogo },
  { name: 'Hostasia', logo: hostasiaLogo },
  { name: 'Vista', logo: vistaLogo }
]
</script>

<style scoped>
.partners {
  padding: 6rem 0;
  background: linear-gradient(180deg, #ffffff 0%, #f7fafc 50%, #ffffff 100%);
  position: relative;
  overflow: hidden;
}

.partners::before {
  content: '';
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  width: 800px;
  height: 800px;
  background: radial-gradient(circle, rgba(46, 208, 230, 0.1) 0%, transparent 70%);
  pointer-events: none;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.section-header {
  text-align: center;
  margin-bottom: 4rem;
}

.badge {
  display: inline-block;
  padding: 0.5rem 1rem;
  background: linear-gradient(135deg, #d4f4f7 0%, #b8eef3 100%);
  color: #2C3E50;
  border-radius: 50px;
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 1rem;
  border: 1px solid rgba(46, 208, 230, 0.2);
}

.section-description {
  font-size: 1.1rem;
  color: #718096;
  margin-top: 1rem;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 800;
  color: #1a1a1a;
}

.gradient-text {
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.scroll-wrapper {
  overflow: hidden;
  margin: 0 -2rem;
}

.scroll-track {
  display: flex;
  gap: 2.5rem;
  will-change: transform;
}

.partner-card {
  min-width: 220px;
  flex-shrink: 0;
  position: relative;
  background: linear-gradient(135deg, #ffffff 0%, #f9fafb 100%);
  padding: 3rem 2rem;
  border-radius: 20px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
  border: 1px solid rgba(46, 208, 230, 0.1);
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.4s cubic-bezier(0.4, 0, 0.2, 1);
  overflow: hidden;
}

.partner-glow {
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(46, 208, 230, 0.15) 0%, transparent 70%);
  opacity: 0;
  transition: opacity 0.4s;
}

.partner-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 20px 60px rgba(46, 208, 230, 0.2);
  border-color: rgba(46, 208, 230, 0.3);
}

.partner-card:hover .partner-glow {
  opacity: 1;
}

.partner-logo {
  width: 100%;
  height: auto;
  max-width: 140px;
  object-fit: contain;
  transition: all 0.4s;
  position: relative;
  z-index: 1;
}

.partner-card:hover .partner-logo {
  transform: scale(1.05);
}

@media (max-width: 768px) {
  .section-title {
    font-size: 2rem;
  }

  .section-description {
    font-size: 1rem;
  }

  .partner-card {
    min-width: 180px;
    padding: 2rem 1.5rem;
  }

  .partner-logo {
    max-width: 120px;
  }
}
</style>
