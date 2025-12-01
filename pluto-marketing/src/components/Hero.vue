<template>
  <section class="hero">
    <div class="container">
      <div class="hero-content">
        <div class="badge">✨ AI-Powered Customer Support</div>
        <h1 class="hero-title">
          Transform Your Customer Support with 
          <span class="gradient-text">Intelligent AI Agents</span>
        </h1>
        <p class="hero-description">
          Plutoo delivers instant, accurate answers using advanced RAG technology. 
          Reduce support costs by 80% while improving customer satisfaction.
        </p>
        <div class="hero-actions">
          <button class="btn-primary-large">Start Free Trial</button>
          <button class="btn-secondary-large">
            <span class="play-icon">▶</span>
            Watch Demo
          </button>
        </div>
        <div class="hero-stats">
          <div class="stat">
            <div class="stat-number">10K+</div>
            <div class="stat-label">Active Users</div>
          </div>
          <div class="stat">
            <div class="stat-number">99.9%</div>
            <div class="stat-label">Uptime</div>
          </div>
          <div class="stat">
            <div class="stat-number">80%</div>
            <div class="stat-label">Cost Reduction</div>
          </div>
        </div>
      </div>
      <div class="hero-visual">
        <div class="floating-card card-1">
          <div class="card-icon">💬</div>
          <div class="card-text">Real-time Chat Support</div>
        </div>
        <div class="floating-card card-2">
          <div class="card-icon">🎯</div>
          <div class="card-text">99% Accuracy</div>
        </div>
        <div class="floating-card card-3">
          <div class="card-icon">⚡</div>
          <div class="card-text">Instant Responses</div>
        </div>
        <div class="main-visual">
          <div class="chat-interface">
            <div class="chat-header">
              <div class="chat-status">
                <span class="status-dot"></span>
                AI Assistant Online
              </div>
            </div>
            <div class="chat-messages">
              <div class="message user">How do I integrate Plutoo?</div>
              <div class="message bot">I can help you with that! Integration takes just 5 minutes...</div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="hero-bg">
      <div class="gradient-orb orb-1"></div>
      <div class="gradient-orb orb-2"></div>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
.hero {
  position: relative;
  min-height: 100vh;
  display: flex;
  align-items: center;
  padding: 8rem 0 4rem;
  overflow: hidden;
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 4rem;
  align-items: center;
  position: relative;
  z-index: 1;
}

.badge {
  display: inline-block;
  padding: 0.5rem 1rem;
  background: linear-gradient(135deg, #d4f4f7 0%, #b8eef3 100%);
  color: #2C3E50;
  border-radius: 50px;
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
}

.hero-title {
  font-size: 2.8rem;
  font-weight: 800;
  line-height: 1.2;
  color: #1a1a1a;
  margin-bottom: 1.5rem;
}

.gradient-text {
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.hero-description {
  font-size: 1.1rem;
  color: #4a5568;
  line-height: 1.8;
  margin-bottom: 2rem;
}

.hero-actions {
  display: flex;
  gap: 1rem;
  margin-bottom: 3rem;
}

.btn-primary-large, .btn-secondary-large {
  padding: 1rem 2rem;
  border-radius: 12px;
  font-weight: 600;
  font-size: 1.1rem;
  cursor: pointer;
  transition: all 0.3s;
  border: none;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.btn-primary-large {
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  color: white;
}

.btn-primary-large:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 35px rgba(46, 208, 230, 0.4);
}

.btn-secondary-large {
  background: white;
  color: #4a5568;
  border: 2px solid #e2e8f0;
}

.btn-secondary-large:hover {
  border-color: #2ED0E6;
  color: #2ED0E6;
}

.play-icon {
  font-size: 0.8rem;
}

.hero-stats {
  display: flex;
  gap: 3rem;
}

.stat-number {
  font-size: 1.6rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 0.25rem;
}

.stat-label {
  font-size: 0.9rem;
  color: #718096;
}

.hero-visual {
  position: relative;
  height: 500px;
}

.floating-card {
  position: absolute;
  background: white;
  padding: 1rem 1.5rem;
  border-radius: 12px;
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
  display: flex;
  align-items: center;
  gap: 0.75rem;
  animation: float 3s ease-in-out infinite;
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

.main-visual {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 80%;
}

.chat-interface {
  background: white;
  border-radius: 16px;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
  overflow: hidden;
}

.chat-header {
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  padding: 1rem;
  color: white;
}

.chat-status {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-weight: 600;
}

.status-dot {
  width: 8px;
  height: 8px;
  background: #4ade80;
  border-radius: 50%;
  animation: pulse 2s ease-in-out infinite;
}

.chat-messages {
  padding: 1.5rem;
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.message {
  padding: 0.75rem 1rem;
  border-radius: 12px;
  max-width: 80%;
}

.message.user {
  background: #f0f9ff;
  color: #1a1a1a;
  align-self: flex-end;
}

.message.bot {
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  color: white;
  align-self: flex-start;
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
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  top: -200px;
  right: -100px;
}

.orb-2 {
  width: 400px;
  height: 400px;
  background: linear-gradient(135deg, #2ED0E6 0%, #5dd9e8 100%);
  bottom: -150px;
  left: -100px;
}

@keyframes float {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-20px); }
}

@keyframes pulse {
  0%, 100% { opacity: 1; }
  50% { opacity: 0.5; }
}

@media (max-width: 768px) {
  .container {
    grid-template-columns: 1fr;
    gap: 2rem;
  }

  .hero-title {
    font-size: 2rem;
  }

  .hero-actions {
    flex-direction: column;
  }

  .hero-stats {
    gap: 1.5rem;
  }

  .hero-visual {
    height: 400px;
  }
}
</style>
