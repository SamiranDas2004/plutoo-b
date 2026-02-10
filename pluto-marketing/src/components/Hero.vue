<template>
  <section class="hero">
    <div class="container">
      <div class="hero-content">
        <div class="badge">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
            <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"/>
          </svg>
          AI-Powered Customer Support
        </div>
        <h1 class="hero-title">
          Transform Your Customer Support with 
          <span class="gradient-text">Intelligent AI Agents</span>
        </h1>
        <p class="hero-description">
          Plutoo delivers instant, accurate answers using advanced RAG technology. 
          Reduce support costs by 80% while improving customer satisfaction.
        </p>
        <div class="hero-actions">
          <button class="btn-primary-large" @click="$router.push('/signup')">
            Start Free Trial
            <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M5 12h14M12 5l7 7-7 7"/>
            </svg>
          </button>
          <button class="btn-secondary-large" @click="openDemo">
            <svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor">
              <polygon points="5 3 19 12 5 21 5 3"/>
            </svg>
            Watch Demo
          </button>
        </div>
        <!-- <div class="trust-bar">
          <span class="trust-text">Trusted by leading companies</span>
          <div class="company-logos">
            <div class="logo-placeholder"></div>
            <div class="logo-placeholder"></div>
            <div class="logo-placeholder"></div>
            <div class="logo-placeholder"></div>
          </div>
        </div> -->
        <div class="hero-stats">
          <div class="stat">
            <div class="stat-number">500+</div>
            <div class="stat-label">Active Users</div>
          </div>
          <div class="stat-divider"></div>
          <div class="stat">
            <div class="stat-number">99.9%</div>
            <div class="stat-label">Uptime SLA</div>
          </div>
          <div class="stat-divider"></div>
          <div class="stat">
            <div class="stat-number">80%</div>
            <div class="stat-label">Cost Reduction</div>
          </div>
        </div>
      </div>
      <div class="hero-visual">
        <div class="floating-card card-1">
          <div class="card-icon-wrapper">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/>
            </svg>
          </div>
          <div class="card-content">
            <div class="card-title">Real-time Chat</div>
            <div class="card-metric">< 2s response</div>
          </div>
        </div>
        <div class="floating-card card-2">
          <div class="card-icon-wrapper success">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"/>
              <polyline points="22 4 12 14.01 9 11.01"/>
            </svg>
          </div>
          <div class="card-content">
            <div class="card-title">High Accuracy</div>
            <div class="card-metric">99% precision</div>
          </div>
        </div>
        <div class="floating-card card-3">
          <div class="card-icon-wrapper warning">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/>
            </svg>
          </div>
          <div class="card-content">
            <div class="card-title">Instant Deploy</div>
            <div class="card-metric">5 min setup</div>
          </div>
        </div>
        <div class="main-visual">
          <div class="chat-interface">
            <div class="chat-header">
              <div class="chat-status">
                <span class="status-dot"></span>
                <span>AI Assistant</span>
              </div>
              <div class="chat-controls">
                <span class="control-dot"></span>
                <span class="control-dot"></span>
                <span class="control-dot"></span>
              </div>
            </div>
            <div class="chat-messages">
              <div class="message user">
                <div class="message-content">How do I integrate Plutoo with my existing system?</div>
                <div class="message-time">2:34 PM</div>
              </div>
              <div class="message bot">
                <div class="bot-avatar">
                  <svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor">
                    <path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5"/>
                  </svg>
                </div>
                <div class="message-content">
                  I can help you with that! Integration takes just 5 minutes with our SDK. Here's what you need to do...
                </div>
              </div>
              <div class="typing-indicator">
                <div class="typing-dots">
                  <span></span>
                  <span></span>
                  <span></span>
                </div>
              </div>
            </div>
          </div>
        </div>
        <div class="visual-decoration">
          <div class="grid-pattern"></div>
        </div>
      </div>
    </div>
    <div class="hero-bg">
      <div class="gradient-orb orb-1"></div>
      <div class="gradient-orb orb-2"></div>
    </div>
  </section>

  <!-- Video Modal -->
  <div v-if="showModal" class="modal-overlay" @click="showModal = false">
    <div class="modal-content" @click.stop>
      <button class="modal-close" @click="showModal = false">&times;</button>
      <iframe
        src="https://www.loom.com/embed/09b3c7aa948b474fb82dfbe6d4855752"
        frameborder="0"
        webkitallowfullscreen
        mozallowfullscreen
        allowfullscreen
        style="width: 100%; height: 100%;"
      ></iframe>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

const showModal = ref(false);

const openDemo = () => {
  showModal.value = true;
};
</script>

<style scoped>
* {
  box-sizing: border-box;
}

.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 8rem 0 6rem;
  overflow: hidden;
  background: #fafbfc;
}

.container {
  max-width: 1280px;
  margin: 0 auto;
  padding: 0 3rem;
  display: grid;
  grid-template-columns: 1.1fr 1fr;
  gap: 6rem;
  align-items: center;
  position: relative;
  z-index: 1;
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
  margin-bottom: 2rem;
  letter-spacing: 0.02em;
}

.badge svg {
  width: 16px;
  height: 16px;
  color: #2ED0E6;
}

.hero-title {
  font-size: 3.5rem;
  font-weight: 700;
  line-height: 1.15;
  color: #1a202c;
  margin-bottom: 1.5rem;
  letter-spacing: -0.02em;
}

.gradient-text {
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
  font-weight: 700;
}

.hero-description {
  font-size: 1.25rem;
  color: #4a5568;
  line-height: 1.7;
  margin-bottom: 2.5rem;
  max-width: 90%;
  font-weight: 400;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  margin-bottom: 3rem;
}

.btn-primary-large,
.btn-secondary-large {
  padding: 1rem 2rem;
  border-radius: 10px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
  border: none;
  display: inline-flex;
  align-items: center;
  gap: 0.5rem;
  font-family: inherit;
  letter-spacing: 0.01em;
}

.btn-primary-large {
  background: linear-gradient(135deg, #2C3E50 0%, #34495e 100%);
  color: white;
  box-shadow: 0 4px 12px rgba(44, 62, 80, 0.2);
}

.btn-primary-large:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 24px rgba(44, 62, 80, 0.3);
  background: linear-gradient(135deg, #243342 0%, #2C3E50 100%);
}

.btn-primary-large svg {
  transition: transform 0.3s;
}

.btn-primary-large:hover svg {
  transform: translateX(4px);
}

.btn-secondary-large {
  background: white;
  color: #2C3E50;
  border: 2px solid #e2e8f0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.btn-secondary-large:hover {
  border-color: #2ED0E6;
  color: #2ED0E6;
  box-shadow: 0 4px 12px rgba(46, 208, 230, 0.15);
}

.btn-secondary-large svg {
  opacity: 0.8;
}

.trust-bar {
  display: flex;
  align-items: center;
  gap: 2rem;
  margin-bottom: 2.5rem;
  padding-bottom: 2.5rem;
  border-bottom: 1px solid #e2e8f0;
}

.trust-text {
  font-size: 0.875rem;
  color: #718096;
  font-weight: 500;
  white-space: nowrap;
}

.company-logos {
  display: flex;
  gap: 1.5rem;
  align-items: center;
}

.logo-placeholder {
  width: 80px;
  height: 28px;
  background: linear-gradient(90deg, #e2e8f0 0%, #cbd5e0 50%, #e2e8f0 100%);
  border-radius: 4px;
  opacity: 0.6;
}

.hero-stats {
  display: flex;
  align-items: center;
  gap: 2.5rem;
}

.stat {
  flex: 1;
}

.stat-divider {
  width: 1px;
  height: 40px;
  background: #e2e8f0;
}

.stat-number {
  font-size: 2rem;
  font-weight: 700;
  color: #1a202c;
  margin-bottom: 0.25rem;
  letter-spacing: -0.02em;
}

.stat-label {
  font-size: 0.875rem;
  color: #718096;
  font-weight: 500;
}

.hero-visual {
  position: relative;
  height: 600px;
}

.floating-card {
  position: absolute;
  background: white;
  padding: 1.25rem;
  border-radius: 16px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.08);
  display: flex;
  align-items: center;
  gap: 1rem;
  animation: float 4s ease-in-out infinite;
  border: 1px solid rgba(226, 232, 240, 0.8);
  backdrop-filter: blur(10px);
  z-index: 3;
}

.card-icon-wrapper {
  width: 48px;
  height: 48px;
  border-radius: 12px;
  background: linear-gradient(135deg, rgba(46, 208, 230, 0.1) 0%, rgba(46, 208, 230, 0.05) 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: #2ED0E6;
  flex-shrink: 0;
}

.card-icon-wrapper.success {
  background: linear-gradient(135deg, rgba(72, 187, 120, 0.1) 0%, rgba(72, 187, 120, 0.05) 100%);
  color: #48bb78;
}

.card-icon-wrapper.warning {
  background: linear-gradient(135deg, rgba(237, 137, 54, 0.1) 0%, rgba(237, 137, 54, 0.05) 100%);
  color: #ed8936;
}

.card-content {
  flex: 1;
}

.card-title {
  font-weight: 600;
  color: #1a202c;
  font-size: 0.95rem;
  margin-bottom: 0.25rem;
}

.card-metric {
  font-size: 0.813rem;
  color: #718096;
}

/* Modal Styles */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.8);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
}

.modal-content {
  position: relative;
  width: 90%;
  max-width: 1000px;
  height: 80vh;
  background: #000;
  border-radius: 12px;
  overflow: hidden;
}

.modal-close {
  position: absolute;
  top: -40px;
  right: 0;
  background: none;
  border: none;
  color: white;
  font-size: 2.5rem;
  cursor: pointer;
  z-index: 10000;
  line-height: 1;
  padding: 0;
  width: 40px;
  height: 40px;
  transition: opacity 0.2s;
}

.modal-close:hover {
  opacity: 0.7;
  font-weight: 500;
}

.card-1 {
  top: 8%;
  left: -8%;
  animation-delay: 0s;
}

.card-2 {
  top: 35%;
  right: -12%;
  animation-delay: 1.5s;
}

.card-3 {
  bottom: 15%;
  left: 0%;
  animation-delay: 3s;
}

.main-visual {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 85%;
  z-index: 2;
}

.chat-interface {
  background: white;
  border-radius: 20px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.12);
  overflow: hidden;
  border: 1px solid rgba(226, 232, 240, 0.6);
}

.chat-header {
  background: linear-gradient(135deg, #2C3E50 0%, #34495e 100%);
  padding: 1.25rem 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.chat-status {
  display: flex;
  align-items: center;
  gap: 0.625rem;
  color: white;
  font-weight: 600;
  font-size: 0.938rem;
}

.status-dot {
  width: 10px;
  height: 10px;
  background: #4ade80;
  border-radius: 50%;
  animation: pulse 2s ease-in-out infinite;
  box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7);
}

.chat-controls {
  display: flex;
  gap: 0.5rem;
}

.control-dot {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.3);
}

.chat-messages {
  padding: 2rem;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  min-height: 280px;
  background: #fafbfc;
}

.message {
  display: flex;
  flex-direction: column;
  max-width: 85%;
  animation: slideIn 0.3s ease-out;
}

.message.user {
  align-self: flex-end;
}

.message.bot {
  align-self: flex-start;
  flex-direction: row;
  gap: 0.75rem;
  align-items: flex-start;
}

.bot-avatar {
  width: 36px;
  height: 36px;
  border-radius: 10px;
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  display: flex;
  align-items: center;
  justify-content: center;
  color: white;
  flex-shrink: 0;
}

.message-content {
  padding: 1rem 1.25rem;
  border-radius: 16px;
  font-size: 0.938rem;
  line-height: 1.6;
}

.message.user .message-content {
  background: white;
  color: #1a202c;
  border: 1px solid #e2e8f0;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.04);
}

.message.bot .message-content {
  background: linear-gradient(135deg, #2C3E50 0%, #34495e 100%);
  color: white;
  flex: 1;
}

.message-time {
  font-size: 0.75rem;
  color: #a0aec0;
  margin-top: 0.375rem;
  text-align: right;
  font-weight: 500;
}

.typing-indicator {
  align-self: flex-start;
  margin-left: 3rem;
}

.typing-dots {
  display: flex;
  gap: 0.375rem;
  padding: 1rem 1.25rem;
  background: white;
  border-radius: 16px;
  border: 1px solid #e2e8f0;
}

.typing-dots span {
  width: 8px;
  height: 8px;
  background: #cbd5e0;
  border-radius: 50%;
  animation: typing 1.4s ease-in-out infinite;
}

.typing-dots span:nth-child(2) {
  animation-delay: 0.2s;
}

.typing-dots span:nth-child(3) {
  animation-delay: 0.4s;
}

.visual-decoration {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  pointer-events: none;
  z-index: 0;
}

.grid-pattern {
  width: 100%;
  height: 100%;
  background-image: 
    linear-gradient(rgba(46, 208, 230, 0.03) 1px, transparent 1px),
    linear-gradient(90deg, rgba(46, 208, 230, 0.03) 1px, transparent 1px);
  background-size: 50px 50px;
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
  filter: blur(100px);
  opacity: 0.15;
}

.orb-1 {
  width: 600px;
  height: 600px;
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  top: -250px;
  right: -150px;
}

.orb-2 {
  width: 500px;
  height: 500px;
  background: linear-gradient(135deg, #2ED0E6 0%, #5dd9e8 100%);
  bottom: -200px;
  left: -150px;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0) rotate(0deg);
  }
  50% {
    transform: translateY(-25px) rotate(1deg);
  }
}

@keyframes pulse {
  0%, 100% {
    opacity: 1;
    box-shadow: 0 0 0 0 rgba(74, 222, 128, 0.7);
  }
  50% {
    opacity: 0.8;
    box-shadow: 0 0 0 8px rgba(74, 222, 128, 0);
  }
}

@keyframes slideIn {
  from {
    opacity: 0;
    transform: translateY(10px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes typing {
  0%, 60%, 100% {
    opacity: 0.3;
    transform: translateY(0);
  }
  30% {
    opacity: 1;
    transform: translateY(-8px);
  }
}

@media (max-width: 1024px) {
  .container {
    grid-template-columns: 1fr;
    gap: 4rem;
    padding: 0 2rem;
  }

  .hero-title {
    font-size: 2.75rem;
  }

  .hero-visual {
    height: 500px;
    margin-top: 2rem;
  }

  .floating-card {
    transform: scale(0.9);
  }
}

@media (max-width: 768px) {
  .hero {
    padding: 6rem 0 4rem;
  }

  .hero-title {
    font-size: 2.25rem;
  }

  .hero-description {
    font-size: 1.1rem;
    max-width: 100%;
  }

  .hero-actions {
    flex-direction: column;
    width: 100%;
  }

  .btn-primary-large,
  .btn-secondary-large {
    width: 100%;
    justify-content: center;
  }

  .trust-bar {
    flex-direction: column;
    align-items: flex-start;
    gap: 1rem;
  }

  .hero-stats {
    flex-wrap: wrap;
    gap: 1.5rem;
  }

  .stat-divider {
    display: none;
  }

  .hero-visual {
    height: 450px;
  }

  .card-1,
  .card-2,
  .card-3 {
    transform: scale(0.85);
  }

  .main-visual {
    width: 95%;
  }
}
</style>