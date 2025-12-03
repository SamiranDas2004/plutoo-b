<template>
  <section id="features" class="features">
    <div class="container">
      <div class="section-header">
        <div class="badge">Features</div>
        <h2 class="section-title">Everything You Need for <span class="gradient-text">Smart Support</span></h2>
        <p class="section-description">Powerful AI-driven features that transform how you handle customer support</p>
      </div>
      
      <!-- Main Feature Highlight -->
      <div class="main-feature">
        <div class="main-feature-content">
          <div class="main-feature-text">
            <h3>AI-Powered RAG Technology</h3>
            <p>Our advanced Retrieval-Augmented Generation system provides contextually accurate responses by intelligently searching through your knowledge base and generating human-like answers.</p>
            <ul class="feature-benefits">
              <li>✓ 95% accuracy in responses</li>
              <li>✓ Sub-second response times</li>
              <li>✓ Learns from your content</li>
            </ul>
          </div>
          <div class="main-feature-visual">
            <div class="ai-demo">
              <div class="demo-chat">
                <div class="chat-message user">How do I reset my password?</div>
                <div class="chat-message ai">I can help you reset your password. Click on "Forgot Password" on the login page...</div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="features-grid">
        <div class="feature-card" v-for="(feature, index) in features" :key="index" @click="goToFeature(index)">
          <div class="feature-icon">
            <i :class="feature.icon"></i>
          </div>
          <h3 class="feature-title">{{ feature.title }}</h3>
          <p class="feature-description">{{ feature.description }}</p>
          <div class="feature-stats" v-if="feature.stats">
            <span class="stat">{{ feature.stats }}</span>
          </div>
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
    icon: 'fas fa-database',
    title: 'Smart Knowledge Base',
    description: 'Upload documents, PDFs, and websites. Our AI automatically organizes and indexes your content for instant retrieval.',
    stats: '10x faster setup'
  },
  {
    icon: 'fas fa-bolt',
    title: 'Instant Responses',
    description: 'Sub-second response times with 95% accuracy. Your customers get immediate, relevant answers 24/7.',
    stats: '<0.5s response time'
  },
  {
    icon: 'fas fa-shield-alt',
    title: 'Enterprise Security',
    description: 'Bank-level encryption, SOC2 compliance, and GDPR ready. Your data stays secure and private.',
    stats: 'SOC2 + GDPR compliant'
  },
  {
    icon: 'fas fa-chart-line',
    title: 'Advanced Analytics',
    description: 'Real-time insights into customer satisfaction, response accuracy, and support performance.',
    stats: '360° visibility'
  },
  {
    icon: 'fas fa-plug',
    title: 'Easy Integration',
    description: 'Deploy in minutes with our simple widget or robust API. Works with your existing tools.',
    stats: '5-minute setup'
  },
  {
    icon: 'fas fa-users',
    title: 'Multi-Channel Support',
    description: 'Consistent AI support across website, mobile app, email, and social media platforms.',
    stats: 'All channels covered'
  }
]
</script>

<style scoped>
.features {
  padding: 6rem 0;
  background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
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
  background: linear-gradient(135d, #e0f2fe 0%, #b3e5fc 100%);
  color: #0277bd;
  border-radius: 50px;
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 1rem;
  border: 1px solid rgba(2, 119, 189, 0.2);
}

.section-title {
  font-size: 2.5rem;
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
  font-size: 1.2rem;
  color: #64748b;
  max-width: 700px;
  margin: 0 auto;
  line-height: 1.6;
}

.main-feature {
  background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
  border-radius: 20px;
  padding: 3rem;
  margin: 4rem 0;
  border: 1px solid #e2e8f0;
}

.main-feature-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 3rem;
  align-items: center;
}

.main-feature-text h3 {
  font-size: 1.8rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 1rem;
}

.main-feature-text p {
  font-size: 1.1rem;
  color: #64748b;
  line-height: 1.7;
  margin-bottom: 1.5rem;
}

.feature-benefits {
  list-style: none;
  padding: 0;
}

.feature-benefits li {
  color: #059669;
  font-weight: 500;
  margin-bottom: 0.5rem;
}

.main-feature-visual {
  display: flex;
  justify-content: center;
}

.ai-demo {
  background: #ffffff;
  border-radius: 16px;
  padding: 1.5rem;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
  border: 1px solid #e2e8f0;
  width: 100%;
  max-width: 350px;
}

.demo-chat {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.chat-message {
  padding: 0.75rem 1rem;
  border-radius: 12px;
  font-size: 0.9rem;
  line-height: 1.4;
}

.chat-message.user {
  background: #e0f2fe;
  color: #0277bd;
  align-self: flex-end;
  max-width: 80%;
}

.chat-message.ai {
  background: #f1f5f9;
  color: #334155;
  align-self: flex-start;
  max-width: 90%;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
  margin-top: 3rem;
}

.feature-card {
  background: white;
  padding: 2rem;
  border-radius: 16px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  transition: all 0.3s ease;
  cursor: pointer;
  border: 1px solid #f1f5f9;
  position: relative;
}

.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
  border-color: #e2e8f0;
}

.feature-icon {
  width: 50px;
  height: 50px;
  background: linear-gradient(135deg, #2ED0E6 0%, #2C3E50 100%);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  font-size: 1.2rem;
  margin-bottom: 1.5rem;
}

.feature-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.75rem;
}

.feature-description {
  color: #64748b;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.feature-stats {
  display: flex;
  align-items: center;
}

.stat {
  background: linear-gradient(135deg, #e0f2fe 0%, #b3e5fc 100%);
  color: #0277bd;
  padding: 0.25rem 0.75rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 600;
}

@media (max-width: 768px) {
  .section-title {
    font-size: 2rem;
  }

  .main-feature {
    padding: 2rem;
  }

  .main-feature-content {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .features-grid {
    grid-template-columns: 1fr;
  }
}
</style>
