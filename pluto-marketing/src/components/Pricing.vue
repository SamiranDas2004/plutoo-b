<template>
  <section id="pricing" class="pricing">
    <div class="container">
      <div class="section-header">
        <div class="badge">Pricing</div>
        <h2 class="section-title">Simple, <span class="gradient-text">Transparent Pricing</span></h2>
        <p class="section-description">Start free, scale as you grow. No hidden fees, cancel anytime.</p>
      </div>
      
      <div class="pricing-grid">
        <div class="pricing-card" v-for="(plan, index) in plans" :key="index" :class="{ featured: plan.featured }">
          <div class="popular-badge" v-if="plan.featured">Most Popular</div>
          
          <div class="plan-header">
            <h3 class="plan-name">{{ plan.name }}</h3>
            <div class="plan-price">
              <span class="currency">₹</span>
              <span class="amount">{{ plan.price }}</span>
              <span class="period">/month</span>
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
            <button 
              class="plan-button" 
              :class="{ primary: plan.featured }"
              @click="handlePlanSelect(plan)"
              :disabled="loading"
            >
              {{ loading ? 'Processing...' : plan.buttonText }}
            </button>
            <p class="trial-note" v-if="plan.trial">{{ plan.trial }}</p>
          </div>
        </div>
      </div>
    </div>

    <!-- Payment Modal -->
    <div v-if="showPaymentModal" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <button class="close-btn" @click="closeModal">✕</button>
        <h3>Complete Your Purchase</h3>
        <p class="modal-plan">{{ selectedPlan?.name }} Plan - ₹{{ selectedPlan?.price }}/month</p>
        
        <form @submit.prevent="processPayment" class="payment-form">
          <input v-model="paymentForm.email" type="email" placeholder="Your Email *" required />
          <p class="info-text">Enter the email you used to create your account</p>
          
          <button type="submit" class="pay-btn" :disabled="loading">
            {{ loading ? 'Processing...' : `Pay ₹${selectedPlan?.price}` }}
          </button>
        </form>
        
        <p class="secure-note">🔒 Secure payment powered by Razorpay</p>
        <p class="account-note">Don't have an account? <a href="/signup">Create one first</a></p>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()
const loading = ref(false)
const showPaymentModal = ref(false)
const selectedPlan = ref(null)
const paymentForm = ref({
  email: ''
})

const plans = [
  {
    name: 'Starter',
    price: 0,
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
    price: 499,
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
    trial: '',
    featured: true
  },
  {
    name: 'Enterprise',
    price: 1499,
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
    trial: '',
    featured: false
  }
]

const handlePlanSelect = (plan) => {
  if (plan.price === 0) {
    router.push('/signup')
  } else if (plan.name === 'Enterprise') {
    window.location.href = 'mailto:sales@plutoo.chat'
  } else {
    selectedPlan.value = plan
    showPaymentModal.value = true
  }
}

const closeModal = () => {
  showPaymentModal.value = false
  selectedPlan.value = null
}

const processPayment = async () => {
  loading.value = true
  
  try {
    const BACKEND_URL = import.meta.env.VITE_BACKEND_URL || 'https://backend.plutoo.chat'
    
    const orderRes = await fetch(`${BACKEND_URL}/payment/create-order`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        amount: selectedPlan.value.price * 100,
        plan_name: selectedPlan.value.name,
        email: paymentForm.value.email
      })
    })
    
    if (!orderRes.ok) {
      const errorData = await orderRes.json()
      alert(errorData.detail || 'Failed to create order')
      loading.value = false
      return
    }
    
    const orderData = await orderRes.json()
    
    const script = document.createElement('script')
    script.src = 'https://checkout.razorpay.com/v1/checkout.js'
    script.async = true
    document.body.appendChild(script)
    
    script.onload = () => {
      const options = {
        key: orderData.key,
        amount: orderData.amount,
        currency: orderData.currency,
        order_id: orderData.order_id,
        name: 'Plutoo AI',
        description: `${selectedPlan.value.name} Plan`,
        handler: async function (response) {
          const verifyRes = await fetch(`${BACKEND_URL}/payment/verify-payment`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({
              razorpay_order_id: response.razorpay_order_id,
              razorpay_payment_id: response.razorpay_payment_id,
              razorpay_signature: response.razorpay_signature,
              plan_name: selectedPlan.value.name,
              email: paymentForm.value.email
            })
          })
          
          const verifyData = await verifyRes.json()
          
          if (verifyRes.ok) {
            alert('Payment successful! Your account has been upgraded.')
            window.location.href = 'https://dashboard.plutoo.chat'
          } else {
            alert('Payment verification failed: ' + verifyData.detail)
          }
          
          loading.value = false
          closeModal()
        },
        prefill: {
          email: paymentForm.value.email
        },
        theme: {
          color: '#2ED0E6'
        },
        modal: {
          ondismiss: function() {
            loading.value = false
          }
        }
      }
      
      const rzp = new window.Razorpay(options)
      rzp.open()
    }
  } catch (error) {
    console.error('Payment error:', error)
    alert('Payment failed. Please try again.')
    loading.value = false
  }
}
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

.plan-button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
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

.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.7);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 10000;
}

.modal-content {
  background: white;
  border-radius: 16px;
  padding: 2rem;
  max-width: 500px;
  width: 90%;
  position: relative;
}

.close-btn {
  position: absolute;
  top: 1rem;
  right: 1rem;
  background: none;
  border: none;
  font-size: 1.5rem;
  cursor: pointer;
  color: #64748b;
}

.modal-content h3 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.modal-plan {
  color: #64748b;
  margin-bottom: 1.5rem;
}

.payment-form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.payment-form input {
  padding: 0.875rem 1rem;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  font-size: 0.95rem;
}

.payment-form input:focus {
  outline: none;
  border-color: #2ED0E6;
  box-shadow: 0 0 0 3px rgba(46, 208, 230, 0.1);
}

.pay-btn {
  padding: 1rem;
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  color: white;
  border: none;
  border-radius: 8px;
  font-weight: 600;
  font-size: 1rem;
  cursor: pointer;
  transition: all 0.3s;
}

.pay-btn:hover:not(:disabled) {
  transform: translateY(-2px);
  box-shadow: 0 10px 25px rgba(46, 208, 230, 0.3);
}

.pay-btn:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.secure-note {
  text-align: center;
  color: #64748b;
  font-size: 0.85rem;
  margin-top: 1rem;
  margin-bottom: 0.5rem;
}

.account-note {
  text-align: center;
  color: #64748b;
  font-size: 0.9rem;
  margin-top: 0.5rem;
}

.account-note a {
  color: #2ED0E6;
  text-decoration: none;
  font-weight: 600;
}

.account-note a:hover {
  text-decoration: underline;
}

.info-text {
  color: #64748b;
  font-size: 0.85rem;
  margin-top: -0.5rem;
  margin-bottom: 0.5rem;
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
