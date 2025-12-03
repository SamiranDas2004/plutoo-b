<template>
  <section class="cta">
    <div class="container">
      <div class="cta-content">
        <div class="cta-badge">Get Started Today</div>
        <h2 class="cta-title">Ready to Transform Your Customer Support?</h2>
        <p class="cta-description">Join 500+ companies using Pluto AI to deliver exceptional customer experiences. Start your free trial today - no credit card required.</p>
        
        <div class="cta-features">
          <div class="feature-item">
            <i class="fas fa-check-circle"></i>
            <span>14-day free trial</span>
          </div>
          <div class="feature-item">
            <i class="fas fa-check-circle"></i>
            <span>No credit card required</span>
          </div>
          <div class="feature-item">
            <i class="fas fa-check-circle"></i>
            <span>Setup in 5 minutes</span>
          </div>
        </div>
        
        <!-- <div class="product-demo">
        
          <div class="demo-features">
            <div class="demo-feature">
              <i class="fas fa-robot"></i>
              <span>AI responds instantly</span>
            </div>
            <div class="demo-feature">
              <i class="fas fa-brain"></i>
              <span>Learns from your content</span>
            </div>
            <div class="demo-feature">
              <i class="fas fa-chart-line"></i>
              <span>Improves over time</span>
            </div>
          </div>
        </div> -->
        
        <div class="cta-actions">
          <button class="btn-primary-large">Start Free Trial</button>
          <button class="btn-secondary-large">Schedule a Demo</button>
        </div>
        
        <div class="cta-note">
          <p>Trusted by 500+ companies worldwide • 98% customer satisfaction</p>
        </div>
      </div>
    </div>
    <div class="cta-bg">
      <div class="gradient-orb orb-1"></div>
      <div class="gradient-orb orb-2"></div>
      <div class="floating-elements">
        <div class="floating-element element-1"></div>
        <div class="floating-element element-2"></div>
        <div class="floating-element element-3"></div>
      </div>
    </div>
  </section>
</template>

<script setup>
</script>

<style scoped>
.cta {
  padding: 6rem 0;
  background: linear-gradient(135deg, #f8fafc 0%, #ffffff 50%, #f8fafc 100%);
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

.cta-badge {
  display: inline-block;
  padding: 0.5rem 1rem;
  background: linear-gradient(135deg, #e0f2fe 0%, #b3e5fc 100%);
  color: #0277bd;
  border-radius: 50px;
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 1.5rem;
  border: 1px solid rgba(2, 119, 189, 0.2);
}

.cta-title {
  font-size: 2.8rem;
  font-weight: 800;
  color: #1e293b;
  margin-bottom: 1.5rem;
  line-height: 1.2;
}

.cta-description {
  font-size: 1.2rem;
  color: #64748b;
  margin-bottom: 2rem;
  line-height: 1.6;
  max-width: 700px;
  margin-left: auto;
  margin-right: auto;
}

.cta-features {
  display: flex;
  justify-content: center;
  gap: 2rem;
  margin-bottom: 2.5rem;
  flex-wrap: wrap;
}

.feature-item {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #059669;
  font-weight: 500;
}

.feature-item i {
  font-size: 1.1rem;
}

.cta-actions {
  display: flex;
  gap: 1rem;
  justify-content: center;
  margin-bottom: 2rem;
}

.btn-primary-large, .btn-secondary-large {
  padding: 1rem 2rem;
  border-radius: 12px;
  font-weight: 600;
  font-size: 1.1rem;
  cursor: pointer;
  transition: all 0.3s;
  border: none;
  position: relative;
  overflow: hidden;
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
  color: #2C3E50;
  border: 2px solid #e2e8f0;
}

.btn-secondary-large:hover {
  transform: translateY(-3px);
  box-shadow: 0 15px 35px rgba(0, 0, 0, 0.1);
  border-color: #2ED0E6;
  color: #2ED0E6;
}

.product-demo {
  margin: 2rem 0;
  display: flex;
  flex-direction: column;
  align-items: center;
  gap: 1.5rem;
}

.demo-video {
  position: relative;
  width: 100%;
  max-width: 600px;
  border-radius: 16px;
  overflow: hidden;
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.15);
  border: 1px solid #e2e8f0;
}

.demo-video video,
.demo-video img {
  width: 100%;
  height: auto;
  display: block;
}

.demo-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  opacity: 0;
  transition: opacity 0.3s;
  cursor: pointer;
}

.demo-video:hover .demo-overlay {
  opacity: 1;
}

.play-button {
  width: 60px;
  height: 60px;
  background: rgba(255, 255, 255, 0.9);
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #2C3E50;
  font-size: 1.5rem;
  transition: transform 0.3s;
}

.play-button:hover {
  transform: scale(1.1);
}

.demo-features {
  display: flex;
  gap: 2rem;
  flex-wrap: wrap;
  justify-content: center;
}

.demo-feature {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  color: #2C3E50;
  font-weight: 500;
  font-size: 0.95rem;
}

.demo-feature i {
  color: #2ED0E6;
  font-size: 1.1rem;
}

.cta-note {
  color: #64748b;
  font-size: 0.95rem;
  margin: 0;
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
  filter: blur(100px);
  opacity: 0.2;
}

.orb-1 {
  width: 600px;
  height: 600px;
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  top: -300px;
  right: -200px;
}

.orb-2 {
  width: 500px;
  height: 500px;
  background: linear-gradient(135deg, #2ED0E6 0%, #5dd9e8 100%);
  bottom: -250px;
  left: -200px;
}

.floating-elements {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}

.floating-element {
  position: absolute;
  border-radius: 50%;
  background: linear-gradient(135deg, rgba(46, 208, 230, 0.1) 0%, rgba(44, 62, 80, 0.1) 100%);
  animation: float 6s ease-in-out infinite;
}

.element-1 {
  width: 80px;
  height: 80px;
  top: 20%;
  left: 10%;
  animation-delay: 0s;
}

.element-2 {
  width: 60px;
  height: 60px;
  top: 60%;
  right: 15%;
  animation-delay: 2s;
}

.element-3 {
  width: 100px;
  height: 100px;
  bottom: 20%;
  left: 20%;
  animation-delay: 4s;
}

@keyframes float {
  0%, 100% {
    transform: translateY(0px) rotate(0deg);
  }
  50% {
    transform: translateY(-20px) rotate(180deg);
  }
}

@media (max-width: 768px) {
  .cta-title {
    font-size: 2rem;
  }

  .cta-features {
    flex-direction: column;
    align-items: center;
    gap: 1rem;
  }

  .demo-features {
    flex-direction: column;
    gap: 1rem;
  }

  .cta-actions {
    flex-direction: column;
  }

  .btn-primary-large, .btn-secondary-large {
    width: 100%;
  }

  .floating-element {
    display: none;
  }
}
</style>
