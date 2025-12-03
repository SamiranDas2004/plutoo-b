<template>
  <section id="testimonials" class="testimonials">
    <div class="container">
      <div class="section-header">
        <div class="badge">Testimonials</div>
        <h2 class="section-title">Loved by <span class="gradient-text">Thousands</span></h2>
        <p class="section-description">See what our customers say about transforming their support experience</p>
      </div>
      
      <div class="scroll-wrapper">
        <div class="scroll-track" :style="{ transform: `translateX(${scrollPosition}px)` }">
          <div class="testimonial-card" v-for="(testimonial, index) in [...testimonials, ...testimonials]" :key="index">
          <div class="testimonial-content">
            <div class="quote-icon">"”</div>
            <p class="testimonial-text">{{ testimonial.text }}</p>
            <div class="testimonial-rating">
              <span v-for="star in 5" :key="star" class="star">★</span>
            </div>
          </div>
          <div class="testimonial-author">
            <div class="author-avatar">
              <img :src="testimonial.avatar" :alt="testimonial.name" />
            </div>
            <div class="author-info">
              <h4 class="author-name">{{ testimonial.name }}</h4>
              <p class="author-title">{{ testimonial.title }}</p>
              <p class="author-company">{{ testimonial.company }}</p>
            </div>
          </div>
          </div>
        </div>
      </div>
      
      <div class="stats-section">
        <div class="stat-item">
          <div class="stat-number">50+</div>
          <div class="stat-label">Happy Customers</div>
        </div>
        <div class="stat-item">
          <div class="stat-number">98%</div>
          <div class="stat-label">Customer Satisfaction</div>
        </div>
        <div class="stat-item">
          <div class="stat-number">2M+</div>
          <div class="stat-label">Messages Processed</div>
        </div>
        <div class="stat-item">
          <div class="stat-number">24/7</div>
          <div class="stat-label">AI Support</div>
        </div>
      </div>
      
      <div class="partners-section">
        <h3>Trusted by leading companies</h3>
        <div class="partners-logos">
          <div class="partner-logo" v-for="(partner, index) in partners" :key="index">
            <img :src="partner.logo" :alt="partner.name" />
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
  scrollPosition.value -= 0.5
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

const testimonials = [
  {
    text: "Pluto AI has revolutionized our customer support. Response times dropped from hours to seconds, and our customer satisfaction scores increased by 40%. It's like having a team of expert support agents working 24/7.",
    name: "Sarah Chen",
    title: "Head of Customer Success",
    company: "TechFlow Inc.",
    avatar: "https://images.unsplash.com/photo-1494790108755-2616b612b786?w=150&h=150&fit=crop&crop=face"
  },
  {
    text: "The setup was incredibly easy. Within 30 minutes, we had our entire knowledge base integrated and the AI was answering customer questions accurately. Our support team can now focus on complex issues while AI handles the routine ones.",
    name: "Michael Rodriguez",
    title: "CTO",
    company: "StartupHub",
    avatar: "https://images.unsplash.com/photo-1472099645785-5658abf4ff4e?w=150&h=150&fit=crop&crop=face"
  },
  {
    text: "What impressed us most was the accuracy. The AI understands context and provides relevant answers that actually help our customers. It's not just a chatbot - it's a genuine support solution.",
    name: "Emily Watson",
    title: "Customer Experience Manager",
    company: "GrowthCorp",
    avatar: "https://images.unsplash.com/photo-1438761681033-6461ffad8d80?w=150&h=150&fit=crop&crop=face"
  },
  {
    text: "ROI was immediate. We reduced our support ticket volume by 60% in the first month. The AI handles most queries instantly, and when it can't help, it seamlessly transfers to our human agents with full context.",
    name: "David Kim",
    title: "Operations Director",
    company: "ScaleUp Solutions",
    avatar: "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=150&h=150&fit=crop&crop=face"
  },
  {
    text: "Security was our biggest concern, but Pluto's enterprise-grade security and compliance features gave us complete confidence. Our data stays secure while we deliver exceptional customer experiences.",
    name: "Lisa Thompson",
    title: "CISO",
    company: "SecureBank",
    avatar: "https://images.unsplash.com/photo-1580489944761-15a19d654956?w=150&h=150&fit=crop&crop=face"
  },
  {
    text: "The analytics dashboard provides incredible insights into customer behavior and support performance. We can see exactly how the AI is performing and continuously improve our knowledge base.",
    name: "James Wilson",
    title: "Product Manager",
    company: "DataDriven Co.",
    avatar: "https://images.unsplash.com/photo-1500648767791-00dcc994a43e?w=150&h=150&fit=crop&crop=face"
  }
]

const partners = [
  { name: 'RedX', logo: redxLogo },
  { name: 'Fotato', logo: fotatoLogo },
  { name: 'Jusgo', logo: jusgoLogo },
  { name: 'Hostasia', logo: hostasiaLogo },
  { name: 'Vista', logo: vistaLogo }
]
</script>

<style scoped>
.testimonials {
  padding: 4rem 0;
  background: linear-gradient(180deg, #f8fafc 0%, #ffffff 50%, #f8fafc 100%);
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

.badge {
  display: inline-block;
  padding: 0.5rem 1rem;
  background: linear-gradient(135deg, #e0f2fe 0%, #b3e5fc 100%);
  color: #0277bd;
  border-radius: 50px;
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 1rem;
  border: 1px solid rgba(2, 119, 189, 0.2);
}

.section-title {
  font-size: 2rem;
  font-weight: 800;
  color: #1a1a1a;
  margin-bottom: 1rem;
  line-height: 1.2;
}

.gradient-text {
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.section-description {
  font-size: 1.1rem;
  color: #64748b;
}

.scroll-wrapper {
  overflow: hidden;
  margin: 0 -2rem;
  margin-bottom: 4rem;
}

.scroll-track {
  display: flex;
  gap: 1.5rem;
  will-change: transform;
}

.testimonial-card {
  min-width: 280px;
  max-width: 280px;
  flex-shrink: 0;
  background: white;
  padding: 1.5rem;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
  border: 1px solid #f1f5f9;
  transition: all 0.3s ease;
}

.testimonial-card:hover {
  transform: translateY(-5px);
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
  border-color: #e2e8f0;
}

.testimonial-content {
  margin-bottom: 1rem;
}

.quote-icon {
  font-size: 2.5rem;
  color: #2ED0E6;
  line-height: 1;
  margin-bottom: 0.75rem;
  opacity: 0.7;
}

.testimonial-text {
  font-size: 0.95rem;
  line-height: 1.6;
  color: #374151;
  margin-bottom: 1rem;
  font-style: italic;
}

.testimonial-rating {
  display: flex;
  gap: 0.2rem;
  margin-bottom: 0.75rem;
}

.star {
  color: #fbbf24;
  font-size: 1rem;
}

.testimonial-author {
  display: flex;
  align-items: center;
  gap: 1rem;
}

.author-avatar {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  overflow: hidden;
  flex-shrink: 0;
}

.author-avatar img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.author-info {
  flex: 1;
}

.author-name {
  font-size: 1rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.2rem;
}

.author-title {
  font-size: 0.85rem;
  color: #64748b;
  margin-bottom: 0.2rem;
}

.author-company {
  font-size: 0.85rem;
  color: #2ED0E6;
  font-weight: 600;
}

.stats-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 2rem;
  margin: 4rem 0;
  padding: 3rem;
  background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
  border-radius: 20px;
  border: 1px solid #e2e8f0;
}

.stat-item {
  text-align: center;
}

.stat-number {
  font-size: 2.5rem;
  font-weight: 800;
  color: #1e293b;
  margin-bottom: 0.5rem;
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.stat-label {
  font-size: 1rem;
  color: #64748b;
  font-weight: 500;
}

.partners-section {
  text-align: center;
  margin-top: 4rem;
}

.partners-section h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 2rem;
}

.partners-logos {
  display: flex;
  justify-content: center;
  align-items: center;
  gap: 3rem;
  flex-wrap: wrap;
}

.partner-logo {
  opacity: 0.6;
  transition: opacity 0.3s;
  filter: grayscale(100%);
}

.partner-logo:hover {
  opacity: 1;
  filter: grayscale(0%);
}

.partner-logo img {
  height: 40px;
  width: auto;
  object-fit: contain;
}

@media (max-width: 768px) {
  .section-title {
    font-size: 1.75rem;
  }

  .testimonial-card {
    min-width: 280px;
    padding: 1.25rem;
  }

  .stats-section {
    grid-template-columns: repeat(2, 1fr);
    padding: 2rem;
  }

  .stat-number {
    font-size: 2rem;
  }

  .partners-logos {
    gap: 2rem;
  }

  .partner-logo img {
    height: 30px;
  }
}
</style>
