<template>
  <section id="how-it-works" class="how-it-works">
    <div class="container">
      <div class="section-header">
        <div class="badge">How It Works</div>
        <h2 class="section-title">Get Started in <span class="gradient-text">3 Simple Steps</span></h2>
      </div>
      <div class="steps">
        <div class="step" v-for="(step, index) in steps" :key="index">
          <div class="step-number">{{ index + 1 }}</div>
          <div class="step-content">
            <h3 class="step-title">{{ step.title }}</h3>
            <p class="step-description">{{ step.description }}</p>
            <a @click="goToStep(index)" class="learn-more">Learn More →</a>
          </div>
        </div>
      </div>
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
    icon: '📤',
    title: 'Upload Your Content',
    description: 'Import your documents, PDFs, website URLs, or connect your knowledge base in seconds'
  },
  {
    icon: '🎨',
    title: 'Customize & Train',
    description: 'Personalize the AI assistant with your brand and let it learn from your content'
  },
  {
    icon: '🚀',
    title: 'Deploy & Scale',
    description: 'Add the widget to your website or integrate via API and start helping customers instantly'
  }
]
</script>

<style scoped>
.how-it-works {
  padding: 6rem 0;
  background: linear-gradient(180deg, #ffffff 0%, #f7fafc 100%);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.section-header {
  text-align: center;
  margin-bottom: 3rem;
}

.badge {
  display: inline-block;
  padding: 0.5rem 1rem;
  background: linear-gradient(135deg, #d4f4f7 0%, #b8eef3 100%);
  color: #2C3E50;
  border-radius: 50px;
  font-size: 0.9rem;
  font-weight: 600;
  margin-bottom: 1rem;
}

.section-title {
  font-size: 2.5rem;
  font-weight: 800;
  color: #1a1a1a;
}

.gradient-text {
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.steps {
  display: flex;
  flex-direction: row;
  gap: 2rem;
  justify-content: center;
}

.step {
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  flex: 1;
  max-width: 350px;
}

.step-number {
  width: 60px;
  height: 60px;
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  color: white;
  border-radius: 16px;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.8rem;
  font-weight: 700;
  box-shadow: 0 8px 20px rgba(46, 208, 230, 0.3);
  margin-bottom: 1rem;
}

.step-content {
  width: 100%;
}

.step-title {
  font-size: 1.4rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 0.5rem;
}

.step-description {
  color: #718096;
  line-height: 1.7;
  font-size: 1rem;
  margin-bottom: 1rem;
}

.learn-more {
  display: inline-block;
  color: #2ED0E6;
  font-weight: 600;
  font-size: 0.95rem;
  cursor: pointer;
  transition: all 0.3s ease;
}

.learn-more:hover {
  color: #2C3E50;
  transform: translateX(4px);
}

@media (max-width: 768px) {
  .section-title {
    font-size: 2rem;
  }

  .steps {
    flex-direction: column;
    align-items: center;
  }
}
</style>
