<template>
  <div>
    <Hero />
    <Compatible />
    <Features />
    <HowItWorks />
    <Pricing />
    <Testimonials />
    <CTA />
  </div>
</template>

<script setup>
import Hero from '../components/Hero.vue'
import Compatible from '../components/Compatible.vue'
import Features from '../components/Features.vue'
import HowItWorks from '../components/HowItWorks.vue'
import Pricing from '../components/Pricing.vue'
import Testimonials from '../components/Testimonials.vue'
import CTA from '../components/CTA.vue'
import { useSeo } from '../composables/useSeo'
import { routeMeta } from '../utils/seo'

useSeo(routeMeta.home)
</script>
