<template>
  <section class="compatible">
    <div class="container">
      <div class="section-header">
        <h2 class="section-title">Compatible with <span class="gradient-text">All Frameworks</span></h2>
        <p class="section-description">Integrate seamlessly with your favorite frontend frameworks</p>
      </div>
      <div class="scroll-wrapper">
        <div class="scroll-track" :style="{ transform: `translateX(${scrollPosition}px)` }">
          <div class="framework-card" v-for="(framework, index) in [...frameworks, ...frameworks, ...frameworks]" :key="index">
            <img :src="framework.logo" :alt="framework.name" class="framework-logo" />
            <div class="framework-name">{{ framework.name }}</div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

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

const frameworks = [
  {name:'HTML',logo:'/src/assets/logos_svg/html-5-svgrepo-com.svg'},
  { name: 'React', logo: '/src/assets/logos_svg/react-svgrepo-com.svg' },
  { name: 'Vue.js', logo: '/src/assets/logos_svg/vue-svgrepo-com.svg' },
  { name:'WordPress',logo:'/src/assets/logos_svg/wordpress-logo-svgrepo-com.svg'},
  { name: 'Angular', logo: '/src/assets/logos_svg/angular-icon-svgrepo-com.svg' },
  { name: 'Svelte', logo: '/src/assets/logos_svg/svelte-svgrepo-com.svg' },
  { name: 'Next.js', logo: '/src/assets/logos_svg/nextjs-icon-svgrepo-com.svg' },
  { name: 'Nuxt.js', logo: '/src/assets/logos_svg/Nuxt JS.svg' },
  { name: 'Laravel', logo: '/src/assets/logos_svg/laravel.svg' },
  { name: 'Backbone.js', logo: '/src/assets/logos_svg/backbonejs-svgrepo-com.svg' },
  
]
</script>

<style scoped>
.compatible {
  padding: 4rem 0;
  background: linear-gradient(180deg, #ffffff 0%, #f7fafc 100%);
  overflow: hidden;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.section-header {
  text-align: center;
  margin-bottom: 3rem;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 800;
  color: #1a1a1a;
  margin-bottom: 1rem;
}

.gradient-text {
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.section-description {
  font-size: 1.1rem;
  color: #718096;
}

.scroll-wrapper {
  overflow: hidden;
  margin: 0 -2rem;
}

.scroll-track {
  display: flex;
  gap: 2rem;
  will-change: transform;
}

.framework-card {
  min-width: 200px;
  flex-shrink: 0;
  background: white;
  padding: 2rem;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1rem;
  transition: all 0.3s;
}

.framework-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);
}

.framework-logo {
  width: 60px;
  height: 60px;
  object-fit: contain;
}

.framework-name {
  font-size: 1.1rem;
  font-weight: 600;
  color: #1a1a1a;
}

@media (max-width: 768px) {
  .section-title {
    font-size: 2rem;
  }

  .framework-card {
    min-width: 150px;
    padding: 1.5rem;
  }
}
</style>
