<template>
  <section id="pricing" class="pricing">
    <div class="container">
      <div class="section-header">
        <div class="badge">Pricing</div>
        <h2 class="section-title">Simple, <span class="gradient-text">Transparent Pricing</span></h2>
        <p class="section-description">Start free, scale as you grow. No hidden fees, cancel anytime.</p>
        
        <div class="pricing-toggle">
          <span :class="{ active: !isAnnual }">Monthly</span>
          <div class="toggle-switch" @click="togglePricing">
            <div class="toggle-slider" :class="{ annual: isAnnual }"></div>
          </div>
          <span :class="{ active: isAnnual }">Annual <span class="discount">Save 20%</span></span>
        </div>
      </div>
      
      <div class="pricing-grid">
        <div class="pricing-card" v-for="(plan, index) in plans" :key="index" :class="{ featured: plan.featured }">
          <div class="popular-badge" v-if="plan.featured">Most Popular</div>
          
          <div class="plan-header">
            <h3 class="plan-name">{{ plan.name }}</h3>
            <div class="plan-price">
              <span class="currency">₹</span>
              <span class="amount">{{ isAnnual ? plan.annualPrice : plan.price }}</span>
              <span class="period">/{{ isAnnual ? 'year' : 'month' }}</span>
            </div>
            <div class="price-note" v-if="isAnnual && plan.monthlySavings">
              Save ${{ plan.monthlySavings }}/month
            </div>
            <p class="plan-description">{{ plan.description }}</p>
          </div>
          
          <div class="plan-features-section">
            <h4>What's included:</h4>
            <ul class="plan-features">
              <li v-for="(feature, idx) in plan.features" :key="idx">
                <span class="check">✓</span>
                {{ feature }}
              </li>
            </ul>
          </div>
          
          <div class="plan-footer">
            <button class="plan-button" :class="{ primary: plan.featured }">
              {{ plan.buttonText }}
            </button>
            <p class="trial-note" v-if="plan.trial">{{ plan.trial }}</p>
          </div>
        </div>
      </div>
      
      <!-- <div class="enterprise-section">
        <div class="enterprise-content">
          <h3>Need something custom?</h3>
          <p>Enterprise solutions with dedicated support, custom integrations, and SLA guarantees.</p>
          <button class="enterprise-button">Contact Sales</button>
        </div>
      </div> -->
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'

const isAnnual = ref(false)

const togglePricing = () => {
  isAnnual.value = !isAnnual.value
}

const plans = [
  {
    name: 'Starter',
    price: 0,
    annualPrice: 0,
    monthlySavings: 0,
    description: 'Perfect for small businesses getting started',
    features: [
      '1,000 AI responses/month',
      'Basic analytics dashboard',
      'Email support',
      '1 knowledge base',
      'Website widget',
      'Standard integrations'
    ],
    buttonText: 'Start Free Trial',
    trial: '14-day free trial',
    featured: false
  },
  {
    name: 'Professional',
    price: 999,
    annualPrice: 950,
    monthlySavings: 20,
    description: 'For growing companies with higher volume',
    features: [
      '10,000 AI responses/month',
      'Advanced analytics & insights',
      'Priority support (24/7)',
      '5 knowledge bases',
      'Full API access',
      'Custom branding',
      'Multi-channel support',
      'Advanced integrations'
    ],
    buttonText: 'Start Free Trial',
    trial: '14-day free trial',
    featured: true
  },
  {
    name: 'Enterprise',
    price: 2999,
    annualPrice: 2870,
    monthlySavings: 60,
    description: 'For large organizations with custom needs',
    features: [
      'Unlimited AI responses',
      'Custom analytics & reporting',
      'Dedicated success manager',
      'Unlimited knowledge bases',
      'Advanced API & webhooks',
      'White-label solution',
      '99.9% SLA guarantee',
      'Custom integrations',
      'SSO & advanced security',
      'On-premise deployment option'
    ],
    buttonText: 'Contact Sales',
    trial: 'Custom trial available',
    featured: false
  }
]
</script>

<style scoped>
.pricing {
  padding: 6rem 0;
  background: linear-gradient(180deg, #ffffff 0%, #f8fafc 50%, #ffffff 100%);
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

.pricing-toggle {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 1rem;
  margin-bottom: 2rem;
}

.pricing-toggle span {
  font-weight: 600;
  color: #64748b;
  transition: color 0.3s;
}

.pricing-toggle span.active {
  color: #1e293b;
}

.discount {
  background: #dcfce7;
  color: #059669;
  padding: 0.2rem 0.5rem;
  border-radius: 12px;
  font-size: 0.8rem;
  margin-left: 0.5rem;
}

.toggle-switch {
  width: 50px;
  height: 26px;
  background: #e2e8f0;
  border-radius: 13px;
  position: relative;
  cursor: pointer;
  transition: background 0.3s;
}

.toggle-slider {
  width: 22px;
  height: 22px;
  background: white;
  border-radius: 50%;
  position: absolute;
  top: 2px;
  left: 2px;
  transition: transform 0.3s;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.2);
}

.toggle-slider.annual {
  transform: translateX(24px);
}

.pricing-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(320px, 1fr));
  gap: 2rem;
  max-width: 1100px;
  margin: 0 auto;
}

.pricing-card {
  background: white;
  border-radius: 20px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.06);
  position: relative;
  transition: all 0.3s ease;
  border: 2px solid #f1f5f9;
  overflow: hidden;
}

.pricing-card:hover {
  transform: translateY(-8px);
  box-shadow: 0 20px 60px rgba(0, 0, 0, 0.1);
  border-color: #e2e8f0;
}

.pricing-card.featured {
  border: 2px solid #2ED0E6;
  transform: scale(1.02);
}

.pricing-card.featured:hover {
  transform: scale(1.02) translateY(-8px);
}

.popular-badge {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  color: white;
  padding: 0.5rem;
  text-align: center;
  font-size: 0.85rem;
  font-weight: 600;
}

.plan-header {
  padding: 2rem 2rem 1rem;
  text-align: center;
}

.pricing-card.featured .plan-header {
  padding-top: 3rem;
}

.plan-name {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 1rem;
}

.plan-price {
  display: flex;
  align-items: baseline;
  justify-content: center;
  margin-bottom: 0.5rem;
}

.currency {
  font-size: 1.2rem;
  color: #64748b;
  font-weight: 600;
}

.amount {
  font-size: 2.5rem;
  font-weight: 800;
  color: #1e293b;
  margin: 0 0.25rem;
}

.period {
  font-size: 1rem;
  color: #64748b;
}

.price-note {
  color: #059669;
  font-size: 0.9rem;
  font-weight: 500;
  margin-bottom: 1rem;
}

.plan-description {
  color: #64748b;
  line-height: 1.5;
  margin-bottom: 1.5rem;
}

.plan-features-section {
  padding: 0 2rem;
}

.plan-features-section h4 {
  font-size: 1rem;
  font-weight: 600;
  color: #1e293b;
  margin-bottom: 1rem;
}

.plan-features {
  list-style: none;
  margin-bottom: 2rem;
}

.plan-features li {
  padding: 0.5rem 0;
  color: #475569;
  display: flex;
  align-items: flex-start;
  gap: 0.75rem;
  font-size: 0.95rem;
  line-height: 1.5;
}

.check {
  color: #059669;
  font-weight: 700;
  font-size: 1rem;
  margin-top: 0.1rem;
  flex-shrink: 0;
}

.plan-footer {
  padding: 0 2rem 2rem;
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
  color: #475569;
  margin-bottom: 1rem;
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

.trial-note {
  text-align: center;
  color: #64748b;
  font-size: 0.9rem;
  margin: 0;
}

.enterprise-section {
  margin-top: 4rem;
  text-align: center;
  background: linear-gradient(135deg, #f8fafc 0%, #ffffff 100%);
  padding: 3rem;
  border-radius: 20px;
  border: 1px solid #e2e8f0;
}

.enterprise-content h3 {
  font-size: 1.8rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.enterprise-content p {
  color: #64748b;
  font-size: 1.1rem;
  margin-bottom: 2rem;
  max-width: 500px;
  margin-left: auto;
  margin-right: auto;
}

.enterprise-button {
  background: linear-gradient(135deg, #1e293b 0%, #334155 100%);
  color: white;
  padding: 1rem 2rem;
  border: none;
  border-radius: 12px;
  font-size: 1rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s ease;
}

.enterprise-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 10px 30px rgba(30, 41, 59, 0.3);
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

  .pricing-toggle {
    flex-direction: column;
    gap: 0.5rem;
  }
}
</style>
