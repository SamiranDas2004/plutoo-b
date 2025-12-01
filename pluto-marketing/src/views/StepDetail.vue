<template>
  <div class="step-detail">
    <section class="step-hero">
      <div class="container">
        <div class="hero-grid">
          <div class="hero-left">
            <h1 class="step-title">{{ step.title }}</h1>
            <p class="step-subtitle">{{ step.description }}</p>
            <button class="hero-learn-more-btn">
              <span>Watch Demo</span>
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 9l-7 7-7-7"/>
              </svg>
            </button>
          </div>
          <div class="hero-right">
            <div class="video-container">
              <video :src="step.video" autoplay loop muted playsinline></video>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="step-content">
      <div class="container">
        <div class="content-grid">
          <div class="content-section">
            <h2>Overview</h2>
            <p>{{ step.overview }}</p>
          </div>
          <div class="content-section">
            <h2>Key Features</h2>
            <ul>
              <li v-for="(feature, index) in step.features" :key="index">{{ feature }}</li>
            </ul>
          </div>
          <div class="content-section">
            <h2>How It Works</h2>
            <p>{{ step.howItWorks }}</p>
          </div>
          <div class="content-section" v-if="step.benefits">
            <h2>Benefits</h2>
            <ul>
              <li v-for="(benefit, index) in step.benefits" :key="index">{{ benefit }}</li>
            </ul>
          </div>
          <div class="content-section" v-if="step.useCases">
            <h2>Use Cases</h2>
            <ul>
              <li v-for="(useCase, index) in step.useCases" :key="index">{{ useCase }}</li>
            </ul>
          </div>
        </div>
        <div class="cta-section">
          <button class="learn-more-btn" @click="$router.push('/')">
            <span>Back to Home</span>
            <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 7l5 5m0 0l-5 5m5-5H6"/>
            </svg>
          </button>
        </div>
      </div>
    </section>
  </div>
</template>

<script setup>
import { computed } from 'vue'
import { useRoute } from 'vue-router'

const route = useRoute()

const steps = {
  'upload-content': {
    number: '1',
    title: 'Upload Your Content',
    description: 'Import your documents, PDFs, website URLs, or connect your knowledge base in seconds',
    video: new URL('../assets/features_video/upload.mp4', import.meta.url).href,
    overview: 'Start by uploading your existing content to build your AI knowledge base. Our platform supports various file formats including PDFs, Word documents, text files, and can even scrape content directly from your website. With intelligent content processing, your documents are transformed into a searchable, AI-ready knowledge base that powers accurate responses.',
    features: [
      'Support for PDFs, DOCX, TXT, CSV, JSON, and more',
      'Bulk upload up to 100 files simultaneously',
      'Website URL scraping with automatic sitemap detection',
      'Automatic content extraction and parsing with OCR support',
      'Real-time processing and indexing with progress tracking',
      'Content preview and validation before finalizing',
      'Duplicate detection and content deduplication',
      'Support for password-protected PDFs',
      'Automatic language detection for multilingual content',
      'Integration with Google Drive, Dropbox, and OneDrive',
      'API endpoints for programmatic content upload',
      'Version control and content history tracking'
    ],
    howItWorks: 'Simply drag and drop your files or paste website URLs into our intuitive upload interface. Our advanced AI system automatically extracts text, images, tables, and structured data from your documents. The content is then processed through our NLP pipeline, which breaks it down into semantic chunks, creates embeddings, and indexes everything for lightning-fast retrieval. You can monitor the upload progress in real-time and preview the processed content before it goes live. The entire process typically takes just seconds, even for large document collections.'
  },
  'customize-train': {
    number: '2',
    title: 'Customize & Train',
    description: 'Personalize the AI assistant with your brand and let it learn from your content',
    video: new URL('../assets/features_video/training.mp4', import.meta.url).href,
    overview: 'Make the AI assistant truly yours by customizing its appearance, personality, and behavior. Train it on your specific content and set custom rules to ensure responses align with your brand voice. Our advanced customization engine allows you to create a unique AI experience that feels like a natural extension of your brand.',
    features: [
      'Full widget customization with colors, logos, and fonts',
      'Personalized greeting messages and conversation starters',
      'Tone and personality customization (professional, friendly, casual)',
      'Custom response templates and pre-defined answers',
      'Training on specific topics with priority weighting',
      'Set response guidelines, rules, and content filters',
      'Custom fallback messages for unknown queries',
      'Multi-language support with automatic translation',
      'A/B testing for different AI personalities',
      'Fine-tune response length and detail level',
      'Add custom disclaimers and legal notices',
      'Configure confidence thresholds for responses',
      'Set business hours and out-of-office messages',
      'Create custom conversation flows and decision trees'
    ],
    howItWorks: 'Use our intuitive visual dashboard to customize every aspect of your AI assistant. Start by uploading your brand assets and selecting your color scheme. Then, define the AI personality by choosing tone, formality level, and response style. The system automatically trains on your uploaded content using advanced machine learning algorithms. You can provide example conversations to teach the AI your preferred response patterns. Set up custom rules like "always mention our 30-day guarantee" or "redirect pricing questions to sales team." The AI continuously learns from user interactions and feedback, improving its accuracy over time. You can monitor training progress and test the AI in a sandbox environment before deploying to production.'
  },
  'deploy-scale': {
    number: '3',
    title: 'Deploy & Scale',
    description: 'Add the widget to your website or integrate via API and start helping customers instantly',
    video: new URL('../assets/features_video/deployement.mp4', import.meta.url).href,
    overview: 'Deploy your AI assistant in minutes with a simple code snippet or API integration. Our enterprise-grade infrastructure automatically scales to handle any traffic volume, from startups to Fortune 500 companies. With global CDN distribution and 99.9% uptime SLA, your customers always get instant, reliable support.',
    features: [
      'Simple one-line widget installation with no coding required',
      'RESTful API with comprehensive documentation',
      'Mobile SDK for iOS and Android with native UI components',
      'Automatic scaling to handle millions of conversations',
      'Global CDN with 200+ edge locations worldwide',
      'Real-time analytics dashboard with custom reports',
      'Webhook support for event notifications',
      'SSO integration with SAML and OAuth',
      'Custom domain support with SSL certificates',
      'Load balancing and failover protection',
      'Rate limiting and DDoS protection',
      'Staging and production environments',
      'Version control with rollback capabilities',
      'Integration with Slack, Teams, and Zendesk',
      'White-label options for agencies',
      'Multi-region deployment for data residency'
    ],
    howItWorks: 'Deployment is incredibly simple. For websites, copy a single line of JavaScript code from your dashboard and paste it before the closing </body> tag. The widget will automatically appear on your site with all your customizations. For mobile apps, install our SDK via npm, CocoaPods, or Gradle, then initialize it with your API key. For custom integrations, use our RESTful API to send messages and receive responses programmatically. Our infrastructure automatically handles scaling, so whether you have 10 or 10 million users, response times stay consistently fast. The system uses intelligent caching, load balancing, and edge computing to deliver sub-second responses globally. Monitor everything through our real-time dashboard, which shows active conversations, response times, user satisfaction scores, and system health. Set up alerts for anomalies and receive notifications via email, Slack, or webhooks. You can deploy updates instantly without downtime using our blue-green deployment system.'
  }
}

const step = computed(() => {
  const id = route.params.id
  return steps[id] || steps['upload-content']
})
</script>

<style scoped>
.step-hero {
  position: relative;
  min-height: 70vh;
  display: flex;
  align-items: center;
  padding: 8rem 0 4rem;
  background: linear-gradient(180deg, #ffffff 0%, #f7fafc 100%);
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
}

.hero-left {
  text-align: left;
}

.step-title {
  font-size: 3rem;
  font-weight: 800;
  margin-bottom: 1rem;
  line-height: 1.2;
  color: #1a1a1a;
}

.step-subtitle {
  font-size: 1.25rem;
  color: #4a5568;
  line-height: 1.6;
  margin-bottom: 2rem;
}

.hero-learn-more-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.875rem 2rem;
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  color: white;
  border: none;
  border-radius: 50px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 8px 25px rgba(46, 208, 230, 0.3);
}

.hero-learn-more-btn:hover {
  transform: translateY(-2px);
  box-shadow: 0 12px 35px rgba(46, 208, 230, 0.4);
}

.hero-learn-more-btn svg {
  width: 18px;
  height: 18px;
  transition: transform 0.3s ease;
}

.hero-learn-more-btn:hover svg {
  transform: translateY(3px);
}

.hero-right {
  display: flex;
  align-items: center;
  justify-content: center;
}

.video-container {
  width: 100%;
  max-width: 600px;
  border-radius: 20px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
}

.video-container video {
  width: 100%;
  height: auto;
  display: block;
}

.step-content {
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
  color: #2ED0E6;
  font-weight: 700;
  font-size: 1.3rem;
}

.cta-section {
  margin-top: 4rem;
  text-align: center;
}

.learn-more-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  padding: 1rem 2.5rem;
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  color: white;
  border: none;
  border-radius: 50px;
  font-size: 1.1rem;
  font-weight: 700;
  cursor: pointer;
  transition: all 0.3s ease;
  box-shadow: 0 10px 30px rgba(46, 208, 230, 0.3);
}

.learn-more-btn:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 40px rgba(46, 208, 230, 0.4);
}

.learn-more-btn svg {
  width: 20px;
  height: 20px;
  transition: transform 0.3s ease;
}

.learn-more-btn:hover svg {
  transform: translateX(5px);
}

@media (max-width: 768px) {
  .hero-grid {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .step-title {
    font-size: 2.5rem;
  }

  .video-container {
    max-width: 100%;
  }
}
</style>
