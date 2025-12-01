<template>
  <section id="features" class="features">
    <div class="container">
      <div class="section-header">
        <div class="badge">Features</div>
        <h2 class="section-title">Everything You Need for <span class="gradient-text">Smart Support</span></h2>
        <p class="section-description">Powerful features designed to revolutionize your customer support experience</p>
      </div>
      <div class="features-grid">
        <div class="feature-card" v-for="(feature, index) in features" :key="index" @click="goToFeature(index)">
          <div class="feature-icon" :style="{ background: feature.color }">
            {{ feature.icon }}
          </div>
          <h3 class="feature-title">{{ feature.title }}</h3>
          <p class="feature-description">{{ feature.description }}</p>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const featureIds = [
  'ai-rag',
  'knowledge-base',
  'instant-responses',
  'enterprise-security',
  'analytics',
  'easy-integration'
]

const goToFeature = (index) => {
  router.push(`/feature/${featureIds[index]}`)
}

const features = [
  {
    icon: '🤖',
    title: 'AI-Powered RAG',
    description: 'Advanced retrieval-augmented generation for accurate, context-aware responses',
    color: 'linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%)'
  },
  {
    icon: '📚',
    title: 'Knowledge Base',
    description: 'Upload documents, PDFs, and websites to create your intelligent knowledge base',
    color: 'linear-gradient(135deg, #2ED0E6 0%, #5dd9e8 100%)'
  },
  {
    icon: '⚡',
    title: 'Instant Responses',
    description: 'Lightning-fast answers with sub-second response times for better UX',
    color: 'linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%)'
  },
  {
    icon: '🔒',
    title: 'Enterprise Security',
    description: 'Bank-level encryption and compliance with SOC2, GDPR, and HIPAA',
    color: 'linear-gradient(135deg, #2ED0E6 0%, #5dd9e8 100%)'
  },
  {
    icon: '📊',
    title: 'Analytics Dashboard',
    description: 'Real-time insights into customer interactions and support metrics',
    color: 'linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%)'
  },
  {
    icon: '🔧',
    title: 'Easy Integration',
    description: 'Simple API and widget integration in minutes, no coding required',
    color: 'linear-gradient(135deg, #2ED0E6 0%, #5dd9e8 100%)'
  }
]
</script>

<style scoped>
.features {
  padding: 6rem 0;
  background: linear-gradient(180deg, #ffffff 0%, #f7fafc 100%);
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
  max-width: 600px;
  margin: 0 auto;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 2rem;
}

.feature-card {
  background: white;
  padding: 2rem;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
  cursor: pointer;
  position: relative;
  overflow: hidden;
}

.feature-card::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(135deg, rgba(46, 208, 230, 0.1) 0%, rgba(44, 62, 80, 0.1) 100%);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.feature-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 20px 60px rgba(46, 208, 230, 0.2);
}

.feature-card:hover::before {
  opacity: 1;
}

.feature-icon {
  width: 60px;
  height: 60px;
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.8rem;
  margin-bottom: 1.5rem;
}

.feature-title {
  font-size: 1.3rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 0.75rem;
}

.feature-description {
  color: #718096;
  line-height: 1.6;
}

@media (max-width: 768px) {
  .section-title {
    font-size: 2rem;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }
}
</style>
