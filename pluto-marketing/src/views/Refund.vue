<template>
  <div class="legal-page">
    <div class="container">
      <h1>Refund Policy</h1>
      <p class="updated">Last Updated: January 29, 2025</p>

      <section>
        <h2>1. Overview</h2>
        <p>At Plutoo AI, we want you to be completely satisfied with our Service. This Refund Policy outlines the circumstances under which refunds may be issued.</p>
      </section>

      <section>
        <h2>2. Free Trial Period</h2>
        <p>We offer a 14-day free trial with no credit card required. During this period:</p>
        <ul>
          <li>You can explore all features of our Service</li>
          <li>No charges will be made to your account</li>
          <li>You can cancel at any time without any obligation</li>
          <li>No refund is necessary as no payment is collected</li>
        </ul>
      </section>

      <section>
        <h2>3. Subscription Refunds</h2>
        
        <h3>Monthly Subscriptions</h3>
        <p>Monthly subscriptions are generally non-refundable. However, we may issue refunds in the following cases:</p>
        <ul>
          <li><strong>Service Outage:</strong> If our Service experiences significant downtime (more than 24 hours) due to our fault</li>
          <li><strong>Billing Errors:</strong> If you were charged incorrectly due to a system error</li>
          <li><strong>First Month:</strong> If you cancel within 7 days of your first paid subscription, we may offer a prorated refund</li>
        </ul>

        <h3>Annual Subscriptions</h3>
        <p>Annual subscriptions may be eligible for a prorated refund if:</p>
        <ul>
          <li>You cancel within 30 days of purchase</li>
          <li>You have not exceeded reasonable usage limits</li>
          <li>The refund is requested due to service issues on our end</li>
        </ul>
        <p>Refunds for annual plans are calculated on a prorated basis, minus any months already used.</p>
      </section>

      <section>
        <h2>4. Non-Refundable Situations</h2>
        <p>Refunds will NOT be issued in the following cases:</p>
        <ul>
          <li>Change of mind after the refund eligibility period</li>
          <li>Failure to use the Service</li>
          <li>Lack of understanding of features (we provide documentation and support)</li>
          <li>Account termination due to Terms of Service violations</li>
          <li>Third-party service fees or charges</li>
          <li>Partial month usage (except as stated above)</li>
        </ul>
      </section>

      <section>
        <h2>5. How to Request a Refund</h2>
        <p>To request a refund:</p>
        <ol>
          <li>Contact our support team at support@plutoo.chat</li>
          <li>Include your account email and reason for refund request</li>
          <li>Provide any relevant details or documentation</li>
          <li>Allow 3-5 business days for review</li>
        </ol>
        <p>We will review your request and respond within 5 business days.</p>
      </section>

      <section>
        <h2>6. Refund Processing</h2>
        <p>If your refund is approved:</p>
        <ul>
          <li>Refunds are processed to the original payment method</li>
          <li>Processing time: 5-10 business days</li>
          <li>You will receive an email confirmation</li>
          <li>Your account access will be terminated upon refund</li>
        </ul>
      </section>

      <section>
        <h2>7. Cancellation Policy</h2>
        <p>You can cancel your subscription at any time:</p>
        <ul>
          <li>Log into your dashboard and go to Settings</li>
          <li>Click "Cancel Subscription"</li>
          <li>Your service will continue until the end of the billing period</li>
          <li>No refund for the remaining days of the current billing cycle</li>
          <li>You can reactivate your account anytime before it expires</li>
        </ul>
      </section>

      <section>
        <h2>8. Downgrades</h2>
        <p>If you downgrade your plan:</p>
        <ul>
          <li>Changes take effect at the next billing cycle</li>
          <li>No refund for the difference in the current billing period</li>
          <li>You retain access to current plan features until the cycle ends</li>
        </ul>
      </section>

      <section>
        <h2>9. Service Credits</h2>
        <p>In lieu of refunds, we may offer service credits for:</p>
        <ul>
          <li>Extended service outages</li>
          <li>Significant bugs or issues affecting your usage</li>
          <li>Goodwill gestures for loyal customers</li>
        </ul>
        <p>Service credits are applied to your account and can be used for future billing cycles.</p>
      </section>

      <section>
        <h2>10. Chargebacks</h2>
        <p>If you initiate a chargeback:</p>
        <ul>
          <li>Your account will be immediately suspended</li>
          <li>We will provide evidence to your payment provider</li>
          <li>Please contact us first to resolve any billing disputes</li>
          <li>Fraudulent chargebacks may result in permanent account termination</li>
        </ul>
      </section>

      <section>
        <h2>11. Enterprise Plans</h2>
        <p>Enterprise and custom plans have separate refund terms outlined in your service agreement. Please refer to your contract or contact your account manager.</p>
      </section>

      <section>
        <h2>12. Changes to This Policy</h2>
        <p>We reserve the right to modify this Refund Policy at any time. Changes will be effective immediately upon posting. Continued use of the Service after changes constitutes acceptance.</p>
      </section>

      <section>
        <h2>13. Contact Us</h2>
        <p>For refund requests or questions about this policy:</p>
        <p>
          <strong>Email:</strong> support@plutoo.chat<br>
          <!-- <strong>Billing:</strong> billing@plutoo.chat<br> -->
          <strong>Phone:</strong> +91 8927750287<br>
          <strong>Hours:</strong> Monday-Friday, 9 AM - 6 PM EST
        </p>
      </section>

      <div class="satisfaction-guarantee">
        <h3>💯 Our Commitment</h3>
        <p>We're committed to your satisfaction. If you're experiencing issues with our Service, please reach out to our support team before requesting a refund. We're here to help make things right!</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useSeo } from '../composables/useSeo'

useSeo({
  title: 'Refund Policy | Plutoo AI',
  description: 'Refund and cancellation policy for Plutoo AI subscriptions',
  keywords: 'refund, cancellation, billing, subscription'
})
</script>

<style scoped>
.legal-page {
  min-height: 100vh;
  background: #fafafa;
  padding: 100px 0 4rem;
}

.container {
  max-width: 900px;
  margin: 0 auto;
  padding: 0 2rem;
  background: white;
  border-radius: 16px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
  padding: 3rem;
}

h1 {
  font-size: 2.5rem;
  font-weight: 800;
  color: #1a1a1a;
  margin-bottom: 0.5rem;
}

.updated {
  color: #64748b;
  font-size: 0.95rem;
  margin-bottom: 2rem;
}

section {
  margin-bottom: 2.5rem;
}

h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 1rem;
}

h3 {
  font-size: 1.2rem;
  font-weight: 600;
  color: #334155;
  margin-top: 1.5rem;
  margin-bottom: 0.75rem;
}

p {
  color: #475569;
  line-height: 1.8;
  margin-bottom: 1rem;
}

ul, ol {
  color: #475569;
  line-height: 1.8;
  margin-left: 1.5rem;
  margin-bottom: 1rem;
}

li {
  margin-bottom: 0.5rem;
}

strong {
  color: #1e293b;
}

.satisfaction-guarantee {
  background: linear-gradient(135deg, #f0f9ff 0%, #e0f2fe 100%);
  border: 2px solid #bae6fd;
  border-radius: 12px;
  padding: 2rem;
  margin-top: 3rem;
  text-align: center;
}

.satisfaction-guarantee h3 {
  font-size: 1.5rem;
  color: #0284c7;
  margin-bottom: 1rem;
}

.satisfaction-guarantee p {
  color: #0c4a6e;
  font-size: 1.05rem;
  margin: 0;
}

@media (max-width: 768px) {
  .container {
    padding: 2rem 1.5rem;
  }

  h1 {
    font-size: 2rem;
  }

  h2 {
    font-size: 1.25rem;
  }

  h3 {
    font-size: 1.1rem;
  }

  .satisfaction-guarantee {
    padding: 1.5rem;
  }
}
</style>
