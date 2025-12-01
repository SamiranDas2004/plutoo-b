<template>
  <section class="cta">
    <div class="container">
      <div class="cta-content">
        <h2 class="cta-title">Ready to Transform Your Customer Support?</h2>
        <p class="cta-description">Join thousands of companies using Plutoo to deliver exceptional customer experiences</p>
        <div class="cta-actions">
          <button class="btn-secondary-large">Schedule a Demo</button>
        </div>

      </div>
    </div>
    <div class="cta-bg">
      <div class="gradient-orb orb-1"></div>
      <div class="gradient-orb orb-2"></div>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
.cta {
  padding: 6rem 0;
  background: white;
  position: relative;
  overflow: hidden;
}

.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 0 2rem;
  position: relative;
  z-index: 1;
}

.cta-content {
  text-align: center;
}

.cta-title {
  font-size: 3rem;
  font-weight: 800;
  color: #1a1a1a;
  margin-bottom: 1.5rem;
  line-height: 1.2;
}

.cta-description {
  font-size: 1.25rem;
  color: #4a5568;
  margin-bottom: 2.5rem;
  line-height: 1.6;
}

.cta-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-bottom: 1.5rem;
}

.btn-primary-large, .btn-secondary-large {
  padding: 1rem 2rem;
  border-radius: 12px;
  font-weight: 600;
  font-size: 1.1rem;
  cursor: pointer;
  transition: all 0.3s;
  border: none;
}

.btn-primary-large {
  background: white;
  color: #667eea;
}

.btn-primary-large:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.2);
}

.btn-secondary-large {
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  color: white;
  border: none;
  position: relative;
  overflow: hidden;
}

.btn-secondary-large::before {
  content: '';
  position: absolute;
  top: 0;
  left: -100%;
  width: 100%;
  height: 100%;
  background: linear-gradient(135deg, #2ED0E6 0%, #5dd9e8 100%);
  transition: left 0.5s;
}

.btn-secondary-large:hover::before {
  left: 100%;
}

.btn-secondary-large:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 35px rgba(46, 208, 230, 0.4);
}

.cta-note {
  color: rgba(255, 255, 255, 0.8);
  font-size: 0.95rem;
}

.cta-bg {
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

@media (max-width: 768px) {
  .cta-title {
    font-size: 2rem;
  }

  .cta-actions {
    flex-direction: column;
  }

  .btn-primary-large, .btn-secondary-large {
    width: 100%;
  }
}
</style>
