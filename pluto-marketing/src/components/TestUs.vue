<template>
  <section class="test-us">
    <div class="test-us-bg">
      <div class="bg-grid"></div>
      <div class="bg-gradient-1"></div>
      <div class="bg-gradient-2"></div>
    </div>
    <div class="container">
      <div class="test-us-content">
        <div class="section-header">
          <span class="section-badge">Test Us</span>
          <h2 class="section-title">See Plutoo in Action</h2>
        </div>

        <div class="test-us-card">
          <div class="widget-demo">
            <div class="demo-pointer">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M9 18l6-6-6-6"/>
              </svg>
              <span>Look at the bottom left corner!</span>
            </div>
            <p class="demo-text">
              In the <strong>bottom left corner</strong> of this website, you can see a widget – that's Plutoo! 
              Small but powerful, ready to assist you instantly.
            </p>
          </div>

          <div class="integration-info">
            <h3>Make Your Life Easy & Save Money</h3>
            <p>You can also use Plutoo on your own website. After sign up, just paste two lines of code in your <code>index.html</code> file. That's it!</p>
            
            <div class="code-example">
              <div class="code-header">
                <span>index.html</span>
                <button class="copy-btn" @click="copyCode">
                  <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                    <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
                    <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
                  </svg>
                  {{ copied ? 'Copied!' : 'Copy' }}
                </button>
              </div>
              <pre><code>&lt;script src="https://backend.plutoo.chat/widget/widget-direct.js" 
  data-bot-token="YOUR_BOT_TOKEN"&gt;&lt;/script&gt;</code></pre>
            </div>
          </div>

          <div class="training-info">
            <div class="info-icon">
              <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M12 2L2 7l10 5 10-5-10-5z"></path>
                <path d="M2 17l10 5 10-5"></path>
                <path d="M2 12l10 5 10-5"></path>
              </svg>
            </div>
            <div class="info-content">
              <h4>Train Plutoo with Your Data</h4>
              <p>
                Remember, Plutoo is like a child – it will only learn what you teach it. 
                Train Plutoo according to your own data, and watch it become your perfect support assistant.
              </p>
            </div>
          </div>

          <div class="cta-section">
            <p class="cta-text">Don't wait – start using Plutoo now!</p>
            <a href="/signup" class="cta-button">
              Get Started Free
              <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                <path d="M5 12h14M12 5l7 7-7 7"/>
              </svg>
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const copied = ref(false)

const copyCode = () => {
  const code = `<script src="https://backend.plutoo.chat/widget/widget-direct.js" data-bot-token="YOUR_BOT_TOKEN"><\/script>`
  navigator.clipboard.writeText(code)
  copied.value = true
  setTimeout(() => {
    copied.value = false
  }, 2000)
}
</script>

<style scoped>
.test-us {
  padding: 6rem 0;
  background: linear-gradient(180deg, #ffffff 0%, #f8fafc 100%);
  position: relative;
  overflow: hidden;
}

.test-us-bg {
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

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  position: relative;
  z-index: 1;
}

.test-us-content {
  max-width: 900px;
  margin: 0 auto;
}

.section-header {
  text-align: center;
  margin-bottom: 3rem;
}


.section-badge {
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
  font-size: 2.5rem;
  font-weight: 700;
  color: #1a202c;
  letter-spacing: -0.02em;
}

.test-us-card {
  background: white;
  border-radius: 24px;
  padding: 3rem;
  box-shadow: 0 4px 24px rgba(0, 0, 0, 0.06);
  border: 1px solid #e2e8f0;
}

.widget-demo {
  margin-bottom: 2.5rem;
  padding: 2rem;
  background: linear-gradient(135deg, rgba(46, 208, 230, 0.05) 0%, rgba(44, 62, 80, 0.02) 100%);
  border-radius: 16px;
  border: 2px dashed rgba(46, 208, 230, 0.3);
}

.demo-pointer {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #2ED0E6;
  font-weight: 600;
  font-size: 1rem;
  margin-bottom: 1rem;
  animation: bounce 2s infinite;
}

.demo-pointer svg {
  animation: slideRight 1.5s infinite;
}

.demo-text {
  font-size: 1.125rem;
  color: #2C3E50;
  line-height: 1.7;
}

.demo-text strong {
  color: #2ED0E6;
}

.integration-info {
  margin-bottom: 2.5rem;
}

.integration-info h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 1rem;
}

.integration-info p {
  font-size: 1.063rem;
  color: #4a5568;
  line-height: 1.7;
  margin-bottom: 1.5rem;
}

.integration-info code {
  background: rgba(46, 208, 230, 0.1);
  color: #2C3E50;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-family: 'Courier New', monospace;
  font-size: 0.938rem;
}

.code-example {
  background: #1a202c;
  border-radius: 12px;
  overflow: hidden;
  margin: 1.5rem 0;
}

.code-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.75rem 1.25rem;
  background: #2d3748;
  border-bottom: 1px solid #4a5568;
}

.code-header span {
  color: #a0aec0;
  font-size: 0.875rem;
  font-family: 'Courier New', monospace;
}

.copy-btn {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  background: rgba(46, 208, 230, 0.15);
  color: #2ED0E6;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  font-size: 0.813rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.copy-btn:hover {
  background: rgba(46, 208, 230, 0.25);
}

.code-example pre {
  margin: 0;
  padding: 1.5rem 1.25rem;
  overflow-x: auto;
}

.code-example code {
  color: #68d391;
  font-family: 'Courier New', monospace;
  font-size: 0.875rem;
  line-height: 1.6;
}

.training-info {
  display: flex;
  gap: 1.5rem;
  padding: 2rem;
  background: #fafbfc;
  border-radius: 16px;
  border: 1px solid #e2e8f0;
  margin-bottom: 2rem;
}

.info-icon {
  width: 48px;
  height: 48px;
  background: linear-gradient(135deg, #2C3E50 0%, #34495e 100%);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.info-content h4 {
  font-size: 1.25rem;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 0.75rem;
}

.info-content p {
  font-size: 1rem;
  color: #4a5568;
  line-height: 1.7;
}

.cta-section {
  text-align: center;
  padding-top: 2rem;
  border-top: 1px solid #e2e8f0;
}

.cta-text {
  font-size: 1.25rem;
  font-weight: 600;
  color: #2C3E50;
  margin-bottom: 1.5rem;
}

.cta-button {
  display: inline-flex;
  align-items: center;
  gap: 0.75rem;
  background: linear-gradient(135deg, #2C3E50 0%, #34495e 100%);
  color: white;
  padding: 1rem 2rem;
  border-radius: 12px;
  font-size: 1.063rem;
  font-weight: 600;
  text-decoration: none;
  transition: all 0.3s;
  box-shadow: 0 4px 16px rgba(44, 62, 80, 0.2);
}

.cta-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(44, 62, 80, 0.3);
}

@keyframes bounce {
  0%, 100% {
    transform: translateY(0);
  }
  50% {
    transform: translateY(-5px);
  }
}

@keyframes slideRight {
  0%, 100% {
    transform: translateX(0);
  }
  50% {
    transform: translateX(5px);
  }
}

@media (max-width: 768px) {
  .test-us {
    padding: 4rem 0;
  }

  .container {
    padding: 0 1.5rem;
  }

  .section-title {
    font-size: 2rem;
  }

  .test-us-card {
    padding: 2rem 1.5rem;
  }

  .widget-demo {
    padding: 1.5rem;
  }

  .demo-text {
    font-size: 1rem;
  }

  .integration-info h3 {
    font-size: 1.25rem;
  }

  .integration-info p {
    font-size: 1rem;
  }

  .code-example pre {
    padding: 1rem;
  }

  .code-example code {
    font-size: 0.75rem;
  }

  .training-info {
    flex-direction: column;
    padding: 1.5rem;
  }

  .cta-text {
    font-size: 1.125rem;
  }

  .cta-button {
    padding: 0.875rem 1.75rem;
    font-size: 1rem;
  }
}
</style>
