<template>
  <section id="pricing" class="pricing">
    <div class="container">
      <div class="section-header">
        <div class="badge">Pricing</div>
        <h2 class="section-title">Simple, <span class="gradient-text">Transparent Pricing</span></h2>
        <p class="section-description">Choose the perfect plan for your business needs</p>
      </div>
      <div class="pricing-grid">
        <div class="pricing-card" v-for="(plan, index) in plans" :key="index" :class="{ featured: plan.featured }">
          <div class="popular-badge" v-if="plan.featured">Most Popular</div>
          <h3 class="plan-name">{{ plan.name }}</h3>
          <div class="plan-price">
            <span class="currency">$</span>
            <span class="amount">{{ plan.price }}</span>
            <span class="period">/month</span>
          </div>
          <p class="plan-description">{{ plan.description }}</p>
          <ul class="plan-features">
            <li v-for="(feature, idx) in plan.features" :key="idx">
              <span class="check">✓</span>
              {{ feature }}
            </li>
          </ul>
          <button class="plan-button" :class="{ primary: plan.featured }">
            {{ plan.buttonText }}
          </button>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
const plans = [
  {
    name: 'Starter',
    price: 29,
    description: 'Perfect for small businesses',
    features: [
      '1,000 messages/month',
      'Basic analytics',
      'Email support',
      '1 knowledge base',
      'Widget integration'
    ],
    buttonText: 'Start Free Trial',
    featured: false
  },
  {
    name: 'Professional',
    price: 99,
    description: 'For growing companies',
    features: [
      '10,000 messages/month',
      'Advanced analytics',
      'Priority support',
      '5 knowledge bases',
      'API access',
      'Custom branding',
      'Multi-channel support'
    ],
    buttonText: 'Start Free Trial',
    featured: true
  },
  {
    name: 'Enterprise',
    price: 299,
    description: 'For large organizations',
    features: [
      'Unlimited messages',
      'Custom analytics',
      'Dedicated support',
      'Unlimited knowledge bases',
      'Advanced API',
      'White-label solution',
      'SLA guarantee',
      'Custom integrations'
    ],
    buttonText: 'Contact Sales',
    featured: false
  }
]
</script>

<style scoped>
.pricing {
  padding: 6rem 0;
  background: linear-gradient(180deg, #f7fafc 0%, #ffffff 100%);
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
  margin-bottom: 1rem;
}

.gradient-text {
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.section-description {
  font-size: 1.1rem;
  color: #718096;
}

.pricing-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 2rem;
  max-width: 1000px;
  margin: 0 auto;
}

.pricing-card {
  background: white;
  padding: 2.5rem;
  border-radius: 20px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.08);
  position: relative;
  transition: all 0.3s ease;
  border: 2px solid transparent;
}

.pricing-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);
}

.pricing-card.featured {
  border: 2px solid #2ED0E6;
  transform: scale(1.05);
}

.pricing-card.featured:hover {
  transform: scale(1.05) translateY(-8px);
}

.popular-badge {
  position: absolute;
  top: -12px;
  left: 50%;
  transform: translateX(-50%);
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  color: white;
  padding: 0.4rem 1.2rem;
  border-radius: 50px;
  font-size: 0.85rem;
  font-weight: 600;
}

.plan-name {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 1rem;
}

.plan-price {
  display: flex;
  align-items: baseline;
  margin-bottom: 1rem;
}

.currency {
  font-size: 1.5rem;
  color: #718096;
  font-weight: 600;
}

.amount {
  font-size: 3rem;
  font-weight: 800;
  color: #1a1a1a;
  margin: 0 0.25rem;
}

.period {
  font-size: 1rem;
  color: #718096;
}

.plan-description {
  color: #718096;
  margin-bottom: 2rem;
}

.plan-features {
  list-style: none;
  margin-bottom: 2rem;
}

.plan-features li {
  padding: 0.75rem 0;
  color: #4a5568;
  display: flex;
  align-items: center;
  gap: 0.75rem;
}

.check {
  color: #10b981;
  font-weight: 700;
  font-size: 1.2rem;
}

.plan-button {
  width: 100%;
  padding: 1rem;
  border-radius: 12px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s;
  border: 2px solid #e2e8f0;
  background: white;
  color: #4a5568;
}

.plan-button:hover {
  border-color: #2ED0E6;
  color: #2ED0E6;
}

.plan-button.primary {
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  color: white;
  border: none;
}

.plan-button.primary:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(46, 208, 230, 0.3);
}

@media (max-width: 768px) {
  .section-title {
    font-size: 2rem;
  }

  .pricing-grid {
    grid-template-columns: 1fr;
  }

  .pricing-card.featured {
    transform: scale(1);
  }
}
</style>
