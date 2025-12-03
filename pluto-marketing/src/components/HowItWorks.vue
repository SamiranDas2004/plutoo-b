<template>
  <section id="how-it-works" class="how-it-works">
    <div class="container">
      <div class="section-header">
        <div class="badge">How It Works</div>
        <h2 class="section-title">Get Started in <span class="gradient-text">3 Simple Steps</span></h2>
        <p class="section-description">Deploy AI-powered customer support in minutes, not months</p>
      </div>
      
      <div class="timeline-container">
        <div class="timeline-line"></div>
        <div class="step" v-for="(step, index) in steps" :key="index" :class="{ 'step-reverse': index % 2 === 1 }">
          <div class="step-content">
            <h3 class="step-title">{{ step.title }}</h3>
            <p class="step-description">{{ step.description }}</p>
            <div class="step-features">
              <ul>
                <li v-for="feature in step.features" :key="feature">✓ {{ feature }}</li>
              </ul>
            </div>
            <div class="step-time">
              <span class="time-badge">{{ step.time }}</span>
            </div>
          </div>
          <div class="step-number">
            <span>{{ index + 1 }}</span>
          </div>
          <div class="step-video">
            <video autoplay muted loop playsinline>
              <source :src="step.video" type="video/mp4">
            </video>
          </div>
        </div>
      </div>
      
      <!-- <div class="cta-section">
        <div class="cta-content">
          <h3>Ready to transform your customer support?</h3>
          <p>Join 500+ companies already using Pluto AI</p>
          <button class="cta-button">Start Free Trial</button>
        </div>
      </div> -->
    </div>
  </section>
</template>

<script setup>
import { useRouter } from 'vue-router'

const router = useRouter()

const stepIds = [
  'upload-content',
  'customize-train',
  'deploy-scale'
]

const goToStep = (index) => {
  router.push(`/step/${stepIds[index]}`)
}

const steps = [
  {
    title: 'Upload Your Content',
    description: 'Import your existing knowledge base, documents, PDFs, or website content. Our AI automatically processes and indexes everything.',
    features: ['Drag & drop interface', 'Multiple file formats', 'Bulk upload support'],
    time: '2 minutes',
    video: './src/assets/features_video/upload.mp4'
  },
  {
    title: 'Customize & Train',
    description: 'Personalize the AI with your brand colors, tone, and specific responses. The system learns from your content automatically.',
    features: ['Brand customization', 'Tone adjustment', 'Auto-training'],
    time: '5 minutes',
    video: './src/assets/features_video/training.mp4'
  },
  {
    title: 'Deploy & Scale',
    description: 'Add our widget to your website with a single line of code, or integrate via our robust API. Start helping customers instantly.',
    features: ['One-click deployment', 'API integration', 'Real-time analytics'],
    time: '1 minute',
    video: './src/assets/features_video/deployement.mp4'
  }
]
</script>

<style scoped>
.how-it-works {
  padding: 6rem 0;
  background: linear-gradient(180deg, #f8fafc 0%, #ffffff 50%, #f8fafc 100%);
  position: relative;
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
  margin-bottom: 2rem;
}

.timeline-container {
  position: relative;
  max-width: 1400px;
  margin: 0 auto;
  padding: 2rem;
}

.timeline-line {
  position: absolute;
  left: 50%;
  top: 0;
  bottom: 0;
  width: 2px;
  background: linear-gradient(180deg, #2ED0E6 0%, #2C3E50 50%, #2ED0E6 100%);
  transform: translateX(-50%);
  z-index: 1;
}

.step {
  display: grid;
  grid-template-columns: 1fr 80px 1fr;
  gap: 3rem;
  align-items: flex-start;
  margin-bottom: 5rem;
  position: relative;
}

.step-reverse {
  grid-template-areas: "video number content";
}

.step:not(.step-reverse) {
  grid-template-areas: "content number video";
}

.step-content {
  grid-area: content;
  background: white;
  padding: 2rem;
  border-radius: 16px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
  border: 1px solid #f1f5f9;
  transition: all 0.3s ease;
}

.step-content:hover {
  transform: translateY(-4px);
  box-shadow: 0 10px 40px rgba(0, 0, 0, 0.1);
}

.step-number {
  grid-area: number;
  width: 50px;
  height: 50px;
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.3rem;
  font-weight: 700;
  box-shadow: 0 4px 15px rgba(46, 208, 230, 0.4);
  position: relative;
  z-index: 2;
  justify-self: center;
  align-self: flex-start;
  margin-top: 2rem;
  border: 3px solid white;
}

.step-title {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.75rem;
}

.step-description {
  color: #64748b;
  line-height: 1.7;
  font-size: 1.1rem;
  margin-bottom: 1.5rem;
}

.step-features {
  margin-bottom: 1.5rem;
}

.step-features ul {
  list-style: none;
  padding: 0;
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 0.5rem;
}

.step-features li {
  background: #f1f5f9;
  color: #059669;
  padding: 0.4rem 0.8rem;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 500;
}

.step-time {
  display: flex;
  align-items: center;
}

.time-badge {
  background: linear-gradient(135deg, #e0f2fe 0%, #b3e5fc 100%);
  color: #0277bd;
  padding: 0.4rem 1rem;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: 600;
  border: 1px solid rgba(2, 119, 189, 0.2);
}

.step-video {
  grid-area: video;
  position: relative;
  width: 100%;
  max-width: 350px;
  border-radius: 12px;
  overflow: hidden;
  box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
  border: 1px solid #e2e8f0;
  transition: all 0.3s ease;
  justify-self: center;
  align-self: flex-start;
}

.step-video:hover {
  transform: scale(1.02);
  box-shadow: 0 15px 40px rgba(0, 0, 0, 0.15);
}

.step-video video {
  width: 100%;
  height: auto;
  display: block;
}

.cta-section {
  margin-top: 4rem;
  text-align: center;
  background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
  padding: 3rem;
  border-radius: 20px;
  border: 1px solid #e2e8f0;
}

.cta-content h3 {
  font-size: 1.8rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.cta-content p {
  color: #64748b;
  font-size: 1.1rem;
  margin-bottom: 2rem;
}

.cta-button {
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  color: white;
  padding: 1rem 2rem;
  border: none;
  border-radius: 12px;
  font-size: 1.1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.cta-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 30px rgba(46, 208, 230, 0.3);
}

@media (max-width: 768px) {
  .how-it-works {
    padding: 3rem 0;
  }

  .container {
    padding: 0 1rem;
  }

  .section-header {
    margin-bottom: 2rem;
  }

  .badge {
    font-size: 0.8rem;
    padding: 0.4rem 0.8rem;
  }

  .section-title {
    font-size: 1.5rem;
  }

  .section-description {
    font-size: 0.95rem;
  }

  .timeline-container {
    padding: 0;
  }

  .timeline-line {
    display: none;
  }

  .step {
    display: flex;
    flex-direction: column;
    gap: 1rem;
    margin-bottom: 2.5rem;
  }

  .step-reverse {
    flex-direction: column;
  }

  .step-number {
    width: 40px;
    height: 40px;
    font-size: 1.1rem;
    margin: 0 0 0.5rem 0;
    align-self: flex-start;
  }

  .step-content {
    padding: 1.25rem;
  }

  .step-title {
    font-size: 1.2rem;
  }

  .step-description {
    font-size: 0.9rem;
    line-height: 1.6;
  }

  .step-features ul {
    grid-template-columns: 1fr;
    gap: 0.4rem;
  }

  .step-features li {
    font-size: 0.8rem;
    padding: 0.35rem 0.7rem;
  }

  .time-badge {
    font-size: 0.8rem;
    padding: 0.35rem 0.8rem;
  }

  .step-video {
    max-width: 100%;
    width: 100%;
  }

  .cta-section {
    padding: 2rem 1rem;
    margin-top: 2rem;
  }

  .cta-content h3 {
    font-size: 1.4rem;
  }

  .cta-content p {
    font-size: 0.95rem;
  }

  .cta-button {
    padding: 0.85rem 1.5rem;
    font-size: 1rem;
  }
}
</style>
