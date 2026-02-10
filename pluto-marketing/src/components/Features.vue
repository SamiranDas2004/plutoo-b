<template>
  <section id="features" class="features">
    <div class="container">
      <div class="section-header">
        <div class="badge">
          <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <rect x="3" y="3" width="7" height="7"/>
            <rect x="14" y="3" width="7" height="7"/>
            <rect x="14" y="14" width="7" height="7"/>
            <rect x="3" y="14" width="7" height="7"/>
          </svg>
          Platform Features
        </div>
        <h2 class="section-title">
          Everything You Need for 
          <span class="gradient-text">Smart Support</span>
        </h2>
        <p class="section-description">
          Powerful AI-driven features that transform how you handle customer support, 
          with enterprise-grade reliability and security
        </p>
      </div>
      
      <!-- Main Feature Highlight -->
      <div class="main-feature">
        <div class="main-feature-content">
          <div class="main-feature-text">
            <div class="feature-label">Core Technology</div>
            <h3>AI-Powered RAG Technology</h3>
            <p>Our advanced Retrieval-Augmented Generation system provides contextually accurate responses by intelligently searching through your knowledge base and generating human-like answers in real-time.</p>
            <div class="feature-benefits">
              <div class="benefit-item">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                  <polyline points="20 6 9 17 4 12"/>
                </svg>
                <div class="benefit-content">
                  <span class="benefit-title">95% Accuracy Rate</span>
                  <span class="benefit-desc">Industry-leading precision</span>
                </div>
              </div>
              <div class="benefit-item">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                  <polyline points="20 6 9 17 4 12"/>
                </svg>
                <div class="benefit-content">
                  <span class="benefit-title">Sub-second Response</span>
                  <span class="benefit-desc">Lightning-fast answers</span>
                </div>
              </div>
              <div class="benefit-item">
                <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
                  <polyline points="20 6 9 17 4 12"/>
                </svg>
                <div class="benefit-content">
                  <span class="benefit-title">Continuous Learning</span>
                  <span class="benefit-desc">Adapts to your content</span>
                </div>
              </div>
            </div>
          </div>
          <div class="main-feature-visual">
            <div class="ai-demo">
              <div class="demo-header">
                <div class="demo-title">
                  <div class="demo-icon">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                      <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
                    </svg>
                  </div>
                  <span>AI Assistant</span>
                </div>
                <div class="demo-status">
                  <span class="status-indicator"></span>
                  Active
                </div>
              </div>
              <div class="demo-chat">
                <div class="chat-message user">
                  <div class="message-content">How do I reset my password?</div>
                  <div class="message-meta">2:34 PM</div>
                </div>
                <div class="chat-message ai">
                  <div class="ai-avatar">
                    <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
                      <circle cx="12" cy="12" r="3"/>
                      <path d="M12 1v6m0 6v6M23 12h-6m-6 0H1"/>
                    </svg>
                  </div>
                  <div class="message-wrapper">
                    <div class="message-content">I can help you reset your password. Click on "Forgot Password" on the login page, enter your email, and you'll receive a reset link within minutes.</div>
                    <div class="message-meta">
                      <span class="confidence-badge">98% confidence</span>
                      <span class="time">2:34 PM</span>
                    </div>
                  </div>
                </div>
              </div>
              <div class="demo-footer">
                <div class="processing-indicator">
                  <span class="pulse-dot"></span>
                  Processing with RAG...
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <div class="features-grid">
        <div 
          class="feature-card" 
          v-for="(feature, index) in features" 
          :key="index" 
          @click="goToFeature(index)"
          :class="{ 'featured': feature.featured }"
        >
          <div class="card-header">
            <div class="feature-icon" :class="feature.iconClass">
              <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path :d="feature.iconPath"/>
              </svg>
            </div>
            <div class="feature-badge" v-if="feature.badge">{{ feature.badge }}</div>
          </div>
          <h3 class="feature-title">{{ feature.title }}</h3>
          <p class="feature-description">{{ feature.description }}</p>
          <div class="feature-footer">
            <div class="feature-stats" v-if="feature.stats">
              <div class="stat-item">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                  <polyline points="22 12 18 12 15 21 9 3 6 12 2 12"/>
                </svg>
                <span>{{ feature.stats }}</span>
              </div>
            </div>
            <div class="feature-link">
              <span>Learn more</span>
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
                <path d="M5 12h14M12 5l7 7-7 7"/>
              </svg>
            </div>
          </div>
        </div>
      </div>
    </div>
    
    <!-- Background decorations -->
    <div class="features-bg">
      <div class="bg-grid"></div>
      <div class="bg-gradient-1"></div>
      <div class="bg-gradient-2"></div>
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
    iconPath: 'M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4',
    iconClass: 'icon-primary',
    title: 'Smart Knowledge Base',
    description: 'Upload documents, PDFs, and websites. Our AI automatically organizes and indexes your content for instant retrieval with semantic search.',
    stats: '10x faster setup',
    badge: 'Popular',
    featured: true
  },
  {
    iconPath: 'M13 10V3L4 14h7v7l9-11h-7z',
    iconClass: 'icon-accent',
    title: 'Instant Responses',
    description: 'Sub-second response times with 95% accuracy. Your customers get immediate, relevant answers 24/7 without waiting.',
    stats: '<0.5s response time',
    badge: null,
    featured: false
  },
  {
    iconPath: 'M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z',
    iconClass: 'icon-success',
    title: 'Enterprise Security',
    description: 'Bank-level encryption, SOC2 Type II compliance, and GDPR ready. Your data stays secure and private with zero-knowledge architecture.',
    stats: 'SOC2 + GDPR',
    badge: null,
    featured: false
  },
  {
    iconPath: 'M3 3v18h18M18.7 8l-5.1 5.2-2.8-2.7L7 14.3',
    iconClass: 'icon-warning',
    title: 'Advanced Analytics',
    description: 'Real-time insights into customer satisfaction, response accuracy, and support performance with actionable recommendations.',
    stats: '360° visibility',
    badge: null,
    featured: false
  },
  {
    iconPath: 'M20 16v-2a4 4 0 0 0-4-4H8a4 4 0 0 0-4 4v2M12 2v6m0 0L9 5m3 3l3-3',
    iconClass: 'icon-info',
    title: 'Easy Integration',
    description: 'Deploy in minutes with our simple widget or robust API. Works seamlessly with your existing tools and workflows.',
    stats: '5-minute setup',
    badge: null,
    featured: false
  },
  {
    iconPath: 'M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2M23 21v-2a4 4 0 0 0-3-3.87M16 3.13a4 4 0 0 1 0 7.75M9 7a4 4 0 1 1-8 0 4 4 0 0 1 8 0z',
    iconClass: 'icon-primary',
    title: 'Multi-Channel Support',
    description: 'Consistent AI support across website, mobile app, email, and social media platforms with unified conversation history.',
    stats: 'All channels',
    badge: null,
    featured: false
  }
]
</script>

<style scoped>
.features {
  padding: 8rem 0;
  background: #fafbfc;
  position: relative;
  overflow: hidden;
}

.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 3rem;
  position: relative;
  z-index: 1;
}

.section-header {
  text-align: center;
  margin-bottom: 5rem;
}

.badge {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.5rem 1.25rem;
  background: rgba(46, 208, 230, 0.08);
  border: 1px solid rgba(46, 208, 230, 0.2);
  color: #2C3E50;
  border-radius: 100px;
  font-size: 0.875rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
  letter-spacing: 0.02em;
}

.badge svg {
  color: #2ED0E6;
}

.section-title {
  font-size: 3rem;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 1.25rem;
  line-height: 1.2;
  letter-spacing: -0.02em;
}

.gradient-text {
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 700;
}

.section-description {
  font-size: 1.125rem;
  color: #64748b;
  max-width: 720px;
  margin: 0 auto;
  line-height: 1.7;
  font-weight: 400;
}

.main-feature {
  background: white;
  border-radius: 24px;
  padding: 4rem;
  margin: 5rem 0;
  border: 1px solid rgba(226, 232, 240, 0.8);
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.04);
  position: relative;
  overflow: hidden;
}

.main-feature::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 4px;
  background: linear-gradient(90deg, #2C3E50 0%, #2ED0E6 100%);
}

.main-feature-content {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
}

.feature-label {
  display: inline-block;
  font-size: 0.813rem;
  font-weight: 600;
  color: #2ED0E6;
  text-transform: uppercase;
  letter-spacing: 0.05em;
  margin-bottom: 1rem;
}

.main-feature-text h3 {
  font-size: 2rem;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 1.25rem;
  letter-spacing: -0.01em;
}

.main-feature-text p {
  font-size: 1.063rem;
  color: #4a5568;
  line-height: 1.7;
  margin-bottom: 2rem;
}

.feature-benefits {
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
}

.benefit-item {
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  padding: 1.25rem;
  background: #fafbfc;
  border-radius: 12px;
  border: 1px solid #f1f5f9;
  transition: all 0.3s ease;
}

.benefit-item:hover {
  background: white;
  border-color: rgba(46, 208, 230, 0.3);
  transform: translateX(4px);
}

.benefit-item svg {
  color: #48bb78;
  flex-shrink: 0;
  margin-top: 0.125rem;
  stroke-width: 2.5;
}

.benefit-content {
  display: flex;
  flex-direction: column;
  gap: 0.25rem;
}

.benefit-title {
  font-weight: 600;
  color: #1a202c;
  font-size: 0.938rem;
}

.benefit-desc {
  font-size: 0.875rem;
  color: #64748b;
}

.main-feature-visual {
  display: flex;
  justify-content: center;
  align-items: center;
}

.ai-demo {
  background: #ffffff;
  border-radius: 20px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.08);
  border: 1px solid #e2e8f0;
  width: 100%;
  max-width: 420px;
  overflow: hidden;
}

.demo-header {
  background: linear-gradient(135deg, #2C3E50 0%, #34495e 100%);
  padding: 1.25rem 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.demo-title {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: white;
  font-weight: 600;
  font-size: 0.938rem;
}

.demo-icon {
  width: 32px;
  height: 32px;
  background: rgba(255, 255, 255, 0.15);
  border-radius: 8px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
}

.demo-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 0.813rem;
  color: rgba(255, 255, 255, 0.9);
  font-weight: 500;
}

.status-indicator {
  width: 8px;
  height: 8px;
  background: #4ade80;
  border-radius: 50%;
  animation: pulse-indicator 2s ease-in-out infinite;
}

.demo-chat {
  padding: 2rem 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
  background: #fafbfc;
  min-height: 260px;
}

.chat-message {
  display: flex;
  flex-direction: column;
  max-width: 85%;
  animation: fadeIn 0.4s ease-out;
}

.chat-message.user {
  align-self: flex-end;
}

.chat-message.ai {
  align-self: flex-start;
  flex-direction: row;
  gap: 0.75rem;
  max-width: 100%;
}

.ai-avatar {
  width: 36px;
  height: 36px;
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  border-radius: 10px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.message-wrapper {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
  flex: 1;
}

.message-content {
  padding: 1rem 1.25rem;
  border-radius: 16px;
  font-size: 0.875rem;
  line-height: 1.6;
}

.chat-message.user .message-content {
  background: white;
  color: #1a202c;
  border: 1px solid #e2e8f0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.chat-message.ai .message-content {
  background: linear-gradient(135deg, #2C3E50 0%, #34495e 100%);
  color: white;
}

.message-meta {
  font-size: 0.75rem;
  color: #a0aec0;
  font-weight: 500;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.chat-message.user .message-meta {
  align-self: flex-end;
  margin-top: 0.375rem;
}

.confidence-badge {
  background: rgba(72, 187, 120, 0.15);
  color: #48bb78;
  padding: 0.25rem 0.625rem;
  border-radius: 12px;
  font-weight: 600;
  font-size: 0.688rem;
}

.time {
  color: #cbd5e0;
}

.demo-footer {
  padding: 1rem 1.5rem;
  background: white;
  border-top: 1px solid #f1f5f9;
}

.processing-indicator {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  font-size: 0.813rem;
  color: #64748b;
  font-weight: 500;
}

.pulse-dot {
  width: 6px;
  height: 6px;
  background: #2ED0E6;
  border-radius: 50%;
  animation: pulse-dot 1.5s ease-in-out infinite;
}

.features-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 2rem;
  margin-top: 4rem;
}

.feature-card {
  background: white;
  padding: 2rem;
  border-radius: 20px;
  box-shadow: 0 2px 12px rgba(0, 0, 0, 0.04);
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  cursor: pointer;
  border: 1px solid #f1f5f9;
  position: relative;
  display: flex;
  flex-direction: column;
}

.feature-card:hover {
  transform: translateY(-6px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.08);
  border-color: rgba(46, 208, 230, 0.3);
}

.feature-card.featured {
  border-color: rgba(46, 208, 230, 0.4);
  background: linear-gradient(135deg, rgba(46, 208, 230, 0.02) 0%, white 100%);
}

.card-header {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  margin-bottom: 1.5rem;
}

.feature-icon {
  width: 56px;
  height: 56px;
  border-radius: 14px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  transition: transform 0.3s;
}

.feature-card:hover .feature-icon {
  transform: scale(1.1) rotate(5deg);
}

.icon-primary {
  background: linear-gradient(135deg, #2C3E50 0%, #34495e 100%);
}

.icon-accent {
  background: linear-gradient(135deg, #2ED0E6 0%, #5dd9e8 100%);
}

.icon-success {
  background: linear-gradient(135deg, #48bb78 0%, #38a169 100%);
}

.icon-warning {
  background: linear-gradient(135deg, #ed8936 0%, #dd6b20 100%);
}

.icon-info {
  background: linear-gradient(135deg, #4299e1 0%, #3182ce 100%);
}

.feature-badge {
  background: linear-gradient(135deg, #2ED0E6 0%, #5dd9e8 100%);
  color: white;
  padding: 0.375rem 0.75rem;
  border-radius: 20px;
  font-size: 0.75rem;
  font-weight: 600;
  letter-spacing: 0.02em;
}

.feature-title {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 0.75rem;
  letter-spacing: -0.01em;
}

.feature-description {
  color: #4a5568;
  line-height: 1.7;
  margin-bottom: 1.5rem;
  font-size: 0.938rem;
  flex: 1;
}

.feature-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-top: 1.25rem;
  border-top: 1px solid #f1f5f9;
  margin-top: auto;
}

.feature-stats {
  display: flex;
  gap: 0.75rem;
}

.stat-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(46, 208, 230, 0.08);
  color: #2C3E50;
  padding: 0.5rem 0.875rem;
  border-radius: 20px;
  font-size: 0.813rem;
  font-weight: 600;
}

.stat-item svg {
  color: #2ED0E6;
}

.feature-link {
  display: flex;
  align-items: center;
  gap: 0.375rem;
  color: #2C3E50;
  font-weight: 600;
  font-size: 0.875rem;
  transition: all 0.3s;
}

.feature-card:hover .feature-link {
  color: #2ED0E6;
  gap: 0.625rem;
}

.feature-link svg {
  transition: transform 0.3s;
}

.feature-card:hover .feature-link svg {
  transform: translateX(4px);
}

.features-bg {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
  overflow: hidden;
  pointer-events: none;
}

.bg-grid {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-image: 
    linear-gradient(rgba(46, 208, 230, 0.02) 1px, transparent 1px),
    linear-gradient(90deg, rgba(46, 208, 230, 0.02) 1px, transparent 1px);
  background-size: 60px 60px;
}

.bg-gradient-1 {
  position: absolute;
  width: 500px;
  height: 500px;
  background: radial-gradient(circle, rgba(46, 208, 230, 0.08) 0%, transparent 70%);
  top: 10%;
  right: -10%;
  filter: blur(60px);
}

.bg-gradient-2 {
  position: absolute;
  width: 400px;
  height: 400px;
  background: radial-gradient(circle, rgba(44, 62, 80, 0.05) 0%, transparent 70%);
  bottom: 20%;
  left: -5%;
  filter: blur(60px);
}

@keyframes pulse-indicator {
  0%, 100% {
    opacity: 1;
    box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7);
  }
  50% {
    opacity: 0.7;
    box-shadow: 0 0 0 6px rgba(74, 222, 128, 0);
  }
}

@keyframes pulse-dot {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0.4;
  }
}

@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@media (max-width: 1024px) {
  .features-grid {
    grid-template-columns: repeat(2, 1fr);
  }

  .main-feature-content {
    gap: 3rem;
  }
}

@media (max-width: 768px) {
  .features {
    padding: 5rem 0;
  }

  .container {
    padding: 0 1.5rem;
  }

  .section-header {
    margin-bottom: 3rem;
  }

  .section-title {
    font-size: 2rem;
  }

  .section-description {
    font-size: 1rem;
  }

  .main-feature {
    padding: 2rem;
    margin: 3rem 0;
  }

  .main-feature-content {
    grid-template-columns: 1fr;
    gap: 2.5rem;
  }

  .main-feature-text h3 {
    font-size: 1.5rem;
  }

  .ai-demo {
    max-width: 100%;
  }

  .features-grid {
    grid-template-columns: 1fr;
    gap: 1.5rem;
  }

  .feature-card {
    padding: 1.75rem;
  }
}
</style>