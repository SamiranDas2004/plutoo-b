<template>
  <div class="feature-detail">
    <section class="feature-hero">
      <div class="container">
        <div class="back-button" @click="$router.push('/')">
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/>
          </svg>
          Back to Home
        </div>
        <div class="hero-grid">
          <div class="hero-left">
            <h1 class="feature-title">{{ feature.title }}</h1>
            <p class="feature-subtitle">{{ feature.description }}</p>
            <div class="feature-stats">
              <div class="stat">
                <div class="stat-number">10K+</div>
                <div class="stat-label">Active Users</div>
              </div>
              <div class="stat">
                <div class="stat-number">99%</div>
                <div class="stat-label">Satisfaction</div>
              </div>
            </div>
          </div>
          <div class="hero-right">
            <div class="floating-card card-1">
              <div class="card-icon">{{ feature.floatingCards[0].icon }}</div>
              <div class="card-text">{{ feature.floatingCards[0].text }}</div>
            </div>
            <div class="floating-card card-2">
              <div class="card-icon">{{ feature.floatingCards[1].icon }}</div>
              <div class="card-text">{{ feature.floatingCards[1].text }}</div>
            </div>
            <div class="floating-card card-3">
              <div class="card-icon">{{ feature.floatingCards[2].icon }}</div>
              <div class="card-text">{{ feature.floatingCards[2].text }}</div>
            </div>
            <div class="feature-visual">
              <img :src="feature.image" :alt="feature.title" />
            </div>
          </div>
        </div>
      </div>
      <div class="hero-bg">
        <div class="gradient-orb orb-1"></div>
        <div class="gradient-orb orb-2"></div>
      </div>
    </section>

    <section class="feature-content">
      <div class="container">
        <div class="content-grid">
          <div class="content-section">
            <h2>Overview</h2>
            <p>{{ feature.overview }}</p>
          </div>
          <div class="content-section">
            <h2>Key Benefits</h2>
            <ul>
              <li v-for="(benefit, index) in feature.benefits" :key="index">{{ benefit }}</li>
            </ul>
          </div>
          <div class="content-section">
            <h2>How It Works</h2>
            <p>{{ feature.howItWorks }}</p>
          </div>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'
import { useSeo } from '../composables/useSeo'
import { routeMeta } from '../utils/seo'

const route = useRoute()

const features = {
  'ai-rag': {
    icon: `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z"/></svg>`,
    title: 'AI-Powered RAG',
    description: 'Advanced retrieval-augmented generation for accurate, context-aware responses',
    color: 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)',
    image: 'https://images.unsplash.com/photo-1677442136019-21780ecad995?w=600&h=400&fit=crop',
    floatingCards: [
      { icon: '🤖', text: 'Retrieval + Generation' },
      { icon: '🎯', text: 'Grounded Answers' },
      { icon: '🧠', text: 'Learns Continuously' }
    ],
    overview: 'Our AI-Powered RAG system combines the best of retrieval and generation to provide accurate, contextual responses. It searches through your knowledge base and generates human-like answers tailored to your customers needs.',
    benefits: [
      'Context-aware responses based on your documentation',
      'Reduces hallucinations with grounded information',
      'Continuously learns from interactions',
      'Supports multiple languages',
      'Real-time knowledge updates'
    ],
    howItWorks: 'When a customer asks a question, our system retrieves relevant information from your knowledge base, then uses advanced AI to generate a natural, accurate response. This ensures answers are both factual and conversational.'
  },
  'knowledge-base': {
    icon: `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>`,
    title: 'Knowledge Base',
    description: 'Upload documents, PDFs, and websites to create your intelligent knowledge base',
    color: 'linear-gradient(135deg, #f093fb 0%, #f5576c 100%)',
    image: 'https://images.unsplash.com/photo-1481627834876-b7833e8f5570?w=600&h=400&fit=crop',
    floatingCards: [
      { icon: '📄', text: 'PDFs & Docs' },
      { icon: '🌐', text: 'Website Scraping' },
      { icon: '🔄', text: 'Auto-Sync Updates' }
    ],
    overview: 'Build a comprehensive knowledge base by uploading various document types. Our system automatically processes and indexes your content for instant retrieval.',
    benefits: [
      'Support for PDFs, Word docs, text files',
      'Website scraping and indexing',
      'Automatic content categorization',
      'Version control for documents',
      'Bulk upload capabilities'
    ],
    howItWorks: 'Simply upload your documents or provide website URLs. Our system extracts, processes, and indexes the content, making it instantly searchable and ready for AI-powered responses.'
  },
  'instant-responses': {
    icon: `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>`,
    title: 'Instant Responses',
    description: 'Lightning-fast answers with sub-second response times for better UX',
    color: 'linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)',
    image: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&h=400&fit=crop',
    floatingCards: [
      { icon: '⚡', text: '<100ms Response' },
      { icon: '🚀', text: 'Global CDN' },
      { icon: '📊', text: '99.9% Uptime' }
    ],
    overview: 'Deliver instant gratification to your customers with our optimized response system that provides answers in milliseconds.',
    benefits: [
      'Sub-second response times',
      'Optimized for high traffic',
      'Cached frequent queries',
      'Global CDN distribution',
      ' 99.9% uptime guarantee'
    ],
    howItWorks: 'Our distributed infrastructure and intelligent caching ensure that responses are delivered instantly, even during peak traffic periods.'
  },
  'high-accuracy': {
    icon: `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>`,
    title: 'High Accuracy',
    description: '99% accuracy rate with continuous learning from interactions',
    color: 'linear-gradient(135deg, #43e97b 0%, #38f9d7 100%)',
    image: 'https://images.unsplash.com/photo-1460925895917-afdab827c52f?w=600&h=400&fit=crop',
    floatingCards: [
      { icon: '🎯', text: '99% Accuracy Rate' },
      { icon: '🔄', text: 'Feedback Learning' },
      { icon: '👥', text: 'Human-in-Loop' }
    ],
    overview: 'Achieve industry-leading accuracy with our continuously learning AI system that improves with every interaction.',
    benefits: [
      '99% accuracy rate',
      'Continuous learning from feedback',
      'Human-in-the-loop training',
      'Quality assurance monitoring',
      'Regular model updates'
    ],
    howItWorks: 'Our AI learns from every interaction, feedback, and correction. Human reviewers periodically audit responses to ensure quality and accuracy.'
  },
  'enterprise-security': {
    icon: `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 15v2m-6 4h12a2 2 0 002-2v-6a2 2 0 00-2-2H6a2 2 0 00-2 2v6a2 2 0 002 2zm10-10V7a4 4 0 00-8 0v4h8z"/></svg>`,
    title: 'Enterprise Security',
    description: 'Bank-level encryption and compliance with SOC2, GDPR, and HIPAA',
    color: 'linear-gradient(135deg, #fa709a 0%, #fee140 100%)',
    image: 'https://images.unsplash.com/photo-1563986768609-322da13575f3?w=600&h=400&fit=crop',
    floatingCards: [
      { icon: '🔒', text: 'End-to-End Encryption' },
      { icon: '🛡️', text: 'SOC2 Type II' },
      { icon: '✓', text: 'HIPAA Compliant' }
    ],
    overview: 'Enterprise-grade security with multiple compliance certifications to protect your data and your customers information.',
    benefits: [
      'SOC2 Type II certified',
      'GDPR compliant',
      'HIPAA ready',
      'End-to-end encryption',
      'Regular security audits'
    ],
    howItWorks: 'All data is encrypted in transit and at rest. We follow industry best practices and undergo regular third-party security audits.'
  },
  'analytics': {
    icon: `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>`,
    title: 'Analytics Dashboard',
    description: 'Real-time insights into customer interactions and support metrics',
    color: 'linear-gradient(135deg, #30cfd0 0%, #330867 100%)',
    image: 'https://images.unsplash.com/photo-1551288049-bebda4e38f71?w=600&h=400&fit=crop',
    floatingCards: [
      { icon: '📊', text: 'Live Metrics' },
      { icon: '📈', text: 'Customer Insights' },
      { icon: '🎯', text: 'Query Analytics' }
    ],
    overview: 'Gain deep insights into customer behavior, common questions, and support performance with our comprehensive analytics dashboard.',
    benefits: [
      'Real-time metrics',
      'Customer satisfaction tracking',
      'Query analysis',
      'Performance reports',
      'Custom dashboards'
    ],
    howItWorks: 'Track every interaction, measure response quality, and identify trends to continuously improve your customer support.'
  },
  'multi-channel': {
    icon: `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M21 12a9 9 0 01-9 9m9-9a9 9 0 00-9-9m9 9H3m9 9a9 9 0 01-9-9m9 9c1.657 0 3-4.03 3-9s-1.343-9-3-9m0 18c-1.657 0-3-4.03-3-9s1.343-9 3-9m-9 9a9 9 0 019-9"/></svg>`,
    title: 'Multi-Channel',
    description: 'Deploy on website, mobile app, Slack, and other platforms',
    color: 'linear-gradient(135deg, #a8edea 0%, #fed6e3 100%)',
    image: 'https://images.unsplash.com/photo-1557804506-669a67965ba0?w=600&h=400&fit=crop',
    floatingCards: [
      { icon: '🌐', text: 'Website Widget' },
      { icon: '💬', text: 'Slack & Teams' },
      { icon: '📱', text: 'WhatsApp Business' }
    ],
    overview: 'Reach your customers wherever they are with support for multiple platforms and channels.',
    benefits: [
      'Website widget',
      'Mobile SDK',
      'Slack integration',
      'Microsoft Teams',
      'WhatsApp Business'
    ],
    howItWorks: 'Deploy once, reach everywhere. Our unified platform ensures consistent support across all channels.'
  },
  'easy-integration': {
    icon: `<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z"/><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 12a3 3 0 11-6 0 3 3 0 016 0z"/></svg>`,
    title: 'Easy Integration',
    description: 'Simple API and widget integration in minutes, no coding required',
    color: 'linear-gradient(135deg, #ff9a9e 0%, #fecfef 100%)',
    image: 'https://images.unsplash.com/photo-1555949963-aa79dcee981c?w=600&h=400&fit=crop',
    floatingCards: [
      { icon: '⚡', text: '5-Minute Setup' },
      { icon: '🔌', text: 'RESTful API' },
      { icon: '📦', text: 'SDKs Included' }
    ],
    overview: 'Get up and running in minutes with our simple integration options. No technical expertise required.',
    benefits: [
      'One-line widget installation',
      'RESTful API',
      'SDKs for popular languages',
      'Detailed documentation',
      'Live support during setup'
    ],
    howItWorks: 'Copy a single line of code to add the widget to your website, or use our API for custom integrations. Setup takes less than 5 minutes.'
  }
}

const feature = computed(() => {
  const id = route.params.id
  return features[id] || features['ai-rag']
})

const metaKey = computed(() => `feature-${route.params.id}`)
useSeo(computed(() => routeMeta[metaKey.value] || routeMeta['feature-ai-rag']))
</script>

<style scoped>
.feature-hero {
  position: relative;
  min-height: 80vh;
  display: flex;
  align-items: center;
  padding: 8rem 0 4rem;
  overflow: hidden;
  background: white;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  position: relative;
  z-index: 1;
}

.hero-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
  color: #1a1a1a;
}

.hero-left {
  text-align: left;
}

.back-button {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  color: #6366f1;
  font-weight: 600;
  cursor: pointer;
  margin-bottom: 2rem;
  transition: all 0.3s;
}

.back-button:hover {
  transform: translateX(-5px);
  color: #4f46e5;
}

.back-button svg {
  width: 20px;
  height: 20px;
}

.feature-icon {
  width: 80px;
  height: 80px;
  border-radius: 16px;
  display: inline-flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 2rem;
  color: white;
}

.feature-icon :deep(svg) {
  width: 50px;
  height: 50px;
}

.feature-title {
  font-size: 3rem;
  font-weight: 800;
  margin-bottom: 1rem;
  line-height: 1.2;
}

.feature-subtitle {
  font-size: 1.25rem;
  color: #4a5568;
  margin-bottom: 2rem;
  line-height: 1.6;
}

.feature-stats {
  display: flex;
  gap: 3rem;
  margin-top: 2rem;
}

.stat-number {
  font-size: 2rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 0.25rem;
}

.stat-label {
  font-size: 0.9rem;
  color: #718096;
}

.hero-right {
  position: relative;
  height: 500px;
}

.floating-card {
  position: absolute;
  background: white;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.2);
  display: flex;
  align-items: center;
  gap: 0.75rem;
  animation: float 3s ease-in-out infinite;
  z-index: 2;
}

.card-1 {
  top: 10%;
  left: -10%;
  animation-delay: 0s;
}

.card-2 {
  top: 50%;
  right: -5%;
  animation-delay: 1s;
}

.card-3 {
  bottom: 10%;
  left: 5%;
  animation-delay: 2s;
}

.card-icon {
  font-size: 1.5rem;
}

.card-text {
  font-weight: 600;
  color: #1a1a1a;
}

.feature-visual {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 80%;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.3);
  background: white;
  padding: 2rem;
}

.feature-visual img {
  width: 100%;
  height: auto;
  display: block;
  border-radius: 12px;
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}

.hero-bg {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  z-index: 0;
  overflow: hidden;
}

.gradient-orb {
  position: absolute;
  border-radius: 50%;
  filter: blur(80px);
  opacity: 0.3;
}

.orb-1 {
  width: 500px;
  height: 500px;
  background: linear-gradient(135deg, #6366f1 0%, #8b5cf6 100%);
  top: -200px;
  right: -100px;
}

.orb-2 {
  width: 400px;
  height: 400px;
  background: linear-gradient(135deg, #ec4899 0%, #f43f5e 100%);
  bottom: -150px;
  left: -100px;
}

.feature-content {
  padding: 6rem 0;
  background: white;
}

.content-grid {
  display: grid;
  gap: 3rem;
}

.content-section h2 {
  font-size: 2rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 1rem;
}

.content-section p {
  font-size: 1.1rem;
  color: #4a5568;
  line-height: 1.8;
}

.content-section ul {
  list-style: none;
  padding: 0;
}

.content-section ul li {
  font-size: 1.1rem;
  color: #4a5568;
  padding: 0.75rem 0;
  padding-left: 2rem;
  position: relative;
}

.content-section ul li:before {
  content: '✓';
  position: absolute;
  left: 0;
  color: #10b981;
  font-weight: 700;
  font-size: 1.3rem;
}

@media (max-width: 768px) {
  .hero-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .hero-left {
    text-align: center;
  }

  .feature-icon {
    margin-left: auto;
    margin-right: auto;
  }

  .feature-stats {
    justify-content: center;
  }

  .feature-title {
    font-size: 2.5rem;
  }
}
</style>
