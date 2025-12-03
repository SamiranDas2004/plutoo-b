<template>
  <div class="success-page">
    <div class="success-container">
      <div class="success-icon">
        <i class="fas fa-check-circle"></i>
      </div>

      <h1>Welcome to Pluto! 🎉</h1>
      <p class="subtitle">Your 14-day free trial has started</p>

      <div class="widget-card">
        <h2>Your Widget Code</h2>
        <p>Copy and paste this code before the closing <code>&lt;/body&gt;</code> tag on your website:</p>
        
        <div class="code-block">
          <pre><code>&lt;script src="http://127.0.0.1:8000/widget/widget-iframe.js"
    data-bot-token="{{ botToken }}"&gt;
&lt;/script&gt;</code></pre>
          <button @click="copyCode" class="copy-btn">
            <i class="fas" :class="copied ? 'fa-check' : 'fa-copy'"></i>
            {{ copied ? 'Copied!' : 'Copy Code' }}
          </button>
        </div>

        <div class="info-box">
          <i class="fas fa-info-circle"></i>
          <div>
            <strong>Your Bot Token:</strong>
            <code class="token">{{ botToken }}</code>
          </div>
        </div>
      </div>

      <div class="next-steps">
        <h3>Next Steps:</h3>
        <div class="steps">
          <div class="step">
            <div class="step-number">1</div>
            <div>
              <h4>Add Widget to Your Site</h4>
              <p>Paste the code above into your website</p>
            </div>
          </div>
          <div class="step">
            <div class="step-number">2</div>
            <div>
              <h4>Upload Your Knowledge Base</h4>
              <p>Add documents, PDFs, or website URLs</p>
            </div>
          </div>
          <div class="step">
            <div class="step-number">3</div>
            <div>
              <h4>Test Your Chatbot</h4>
              <p>Try asking questions to see it in action</p>
            </div>
          </div>
        </div>
      </div>

      <div class="action-buttons">
        <button @click="goToDashboard" class="btn-primary">
          <i class="fas fa-tachometer-alt"></i>
          Go to Dashboard
        </button>
        <button @click="viewDocs" class="btn-secondary">
          <i class="fas fa-book"></i>
          View Documentation
        </button>
      </div>

      <div class="trial-info">
        <p><strong>Trial ends:</strong> {{ trialEndDate }}</p>
        <p>No credit card required. Cancel anytime.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import { useSeo } from '../composables/useSeo'

useSeo({
  title: 'Welcome to Pluto | Setup Your AI Chatbot',
  description: 'Get started with Pluto AI customer support',
  keywords: 'setup, widget code, integration'
})

const route = useRoute()
const router = useRouter()
const copied = ref(false)
const botToken = ref('')

onMounted(() => {
  botToken.value = route.query.token || '450f988d-c535-11f0-b60c-00ffe4eb716d'
})

const widgetCode = computed(() => {
  return `<script src="http://127.0.0.1:8000/widget/widget-iframe.js"
    data-bot-token="${botToken.value}">
<\/script>`
})

const trialEndDate = computed(() => {
  const date = new Date()
  date.setDate(date.getDate() + 14)
  return date.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric' })
})

const copyCode = () => {
  navigator.clipboard.writeText(widgetCode.value)
  copied.value = true
  setTimeout(() => {
    copied.value = false
  }, 2000)
}

const goToDashboard = () => {
  window.open('http://localhost:3000', '_blank')
}

const viewDocs = () => {
  alert('Documentation coming soon!')
}
</script>

<style scoped>
.success-page {
  min-height: 100vh;
  background: #fafafa;
  padding-top: 80px;
  padding-bottom: 3rem;
}

.success-container {
  max-width: 800px;
  margin: 0 auto;
  padding: 2rem;
  text-align: center;
}

.success-icon {
  font-size: 4rem;
  color: #10b981;
  margin-bottom: 1rem;
}

h1 {
  font-size: 2.5rem;
  font-weight: 800;
  color: #1a1a1a;
  margin-bottom: 0.5rem;
}

.subtitle {
  font-size: 1.2rem;
  color: #64748b;
  margin-bottom: 2rem;
}

.widget-card {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
  margin-bottom: 2rem;
  text-align: left;
}

.widget-card h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 0.5rem;
}

.widget-card > p {
  color: #64748b;
  margin-bottom: 1.5rem;
}

.widget-card code {
  background: #f1f5f9;
  padding: 0.2rem 0.4rem;
  border-radius: 4px;
  font-size: 0.9rem;
  color: #e11d48;
}

.code-block {
  position: relative;
  background: #1e293b;
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
}

.code-block pre {
  margin: 0;
  overflow-x: auto;
}

.code-block code {
  color: #e2e8f0;
  background: transparent;
  font-family: 'Courier New', monospace;
  font-size: 0.9rem;
  line-height: 1.6;
}

.copy-btn {
  position: absolute;
  top: 1rem;
  right: 1rem;
  padding: 0.5rem 1rem;
  background: #334155;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 0.85rem;
  cursor: pointer;
  transition: all 0.3s;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.copy-btn:hover {
  background: #475569;
}

.info-box {
  display: flex;
  gap: 1rem;
  padding: 1rem;
  background: #f0f9ff;
  border: 1px solid #bae6fd;
  border-radius: 8px;
  align-items: start;
}

.info-box i {
  color: #0284c7;
  font-size: 1.25rem;
  margin-top: 0.15rem;
}

.info-box strong {
  display: block;
  margin-bottom: 0.25rem;
  color: #1a1a1a;
}

.token {
  background: white;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-size: 0.85rem;
  color: #0284c7;
  border: 1px solid #bae6fd;
}

.next-steps {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
  margin-bottom: 2rem;
  text-align: left;
}

.next-steps h3 {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 1.5rem;
}

.steps {
  display: flex;
  flex-direction: column;
  gap: 1.5rem;
}

.step {
  display: flex;
  gap: 1rem;
  align-items: start;
}

.step-number {
  width: 40px;
  height: 40px;
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 700;
  flex-shrink: 0;
}

.step h4 {
  font-size: 1.1rem;
  font-weight: 600;
  color: #1a1a1a;
  margin-bottom: 0.25rem;
}

.step p {
  color: #64748b;
  font-size: 0.95rem;
}

.action-buttons {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-bottom: 2rem;
}

.btn-primary,
.btn-secondary {
  padding: 1rem 2rem;
  border-radius: 8px;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
  border: none;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1rem;
}

.btn-primary {
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  color: white;
}

.btn-primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(46, 208, 230, 0.3);
}

.btn-secondary {
  background: white;
  color: #64748b;
  border: 2px solid #e2e8f0;
}

.btn-secondary:hover {
  border-color: #2ED0E6;
  color: #2ED0E6;
}

.trial-info {
  color: #64748b;
  font-size: 0.9rem;
}

.trial-info p {
  margin: 0.25rem 0;
}

.trial-info strong {
  color: #1a1a1a;
}

@media (max-width: 768px) {
  h1 {
    font-size: 2rem;
  }

  .action-buttons {
    flex-direction: column;
  }

  .widget-card,
  .next-steps {
    padding: 1.5rem;
  }

  .copy-btn {
    position: static;
    margin-top: 1rem;
    width: 100%;
    justify-content: center;
  }
}
</style>
