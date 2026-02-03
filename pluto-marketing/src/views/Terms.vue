<template>
  <div class="legal-page">
    <div class="container">
      <h1>Terms of Service</h1>
      <p class="updated">Last Updated: January 29, 2025</p>

      <section>
        <h2>1. Acceptance of Terms</h2>
        <p>By accessing and using Plutoo AI ("Service"), you accept and agree to be bound by these Terms of Service. If you do not agree to these terms, please do not use our Service.</p>
      </section>

      <section>
        <h2>2. Description of Service</h2>
        <p>Plutoo AI provides an AI-powered customer support platform that enables businesses to automate customer service through intelligent chatbots, document processing, and analytics.</p>
      </section>

      <section>
        <h2>3. User Accounts</h2>
        <p>You must create an account to use our Service. You are responsible for:</p>
        <ul>
          <li>Maintaining the confidentiality of your account credentials</li>
          <li>All activities that occur under your account</li>
          <li>Notifying us immediately of any unauthorized use</li>
          <li>Ensuring your account information is accurate and up-to-date</li>
        </ul>
      </section>

      <section>
        <h2>4. Acceptable Use</h2>
        <p>You agree not to:</p>
        <ul>
          <li>Use the Service for any illegal or unauthorized purpose</li>
          <li>Violate any laws in your jurisdiction</li>
          <li>Infringe on intellectual property rights</li>
          <li>Transmit malicious code or viruses</li>
          <li>Attempt to gain unauthorized access to our systems</li>
          <li>Use the Service to harass, abuse, or harm others</li>
          <li>Resell or redistribute the Service without permission</li>
        </ul>
      </section>

      <section>
        <h2>5. Subscription and Payment</h2>
        <p>Our Service is offered on a subscription basis with the following terms:</p>
        <ul>
          <li>14-day free trial with no credit card required</li>
          <li>Subscription fees are billed monthly or annually</li>
          <li>All fees are non-refundable except as stated in our Refund Policy</li>
          <li>We reserve the right to change pricing with 30 days notice</li>
          <li>Failure to pay may result in service suspension or termination</li>
        </ul>
      </section>

      <section>
        <h2>6. Data and Privacy</h2>
        <p>Your use of the Service is also governed by our Privacy Policy. We collect, use, and protect your data as described in that policy.</p>
      </section>

      <section>
        <h2>7. Intellectual Property</h2>
        <p>The Service and its original content, features, and functionality are owned by Plutoo AI and are protected by international copyright, trademark, and other intellectual property laws.</p>
      </section>

      <section>
        <h2>8. Service Availability</h2>
        <p>We strive to provide 99.9% uptime but do not guarantee uninterrupted service. We may perform maintenance, updates, or modifications that temporarily affect availability.</p>
      </section>

      <section>
        <h2>9. Limitation of Liability</h2>
        <p>To the maximum extent permitted by law, Plutoo AI shall not be liable for any indirect, incidental, special, consequential, or punitive damages resulting from your use of the Service.</p>
      </section>

      <section>
        <h2>10. Termination</h2>
        <p>We may terminate or suspend your account immediately, without prior notice, for any breach of these Terms. Upon termination, your right to use the Service will cease immediately.</p>
      </section>

      <section>
        <h2>11. Changes to Terms</h2>
        <p>We reserve the right to modify these Terms at any time. We will notify users of material changes via email or through the Service. Continued use after changes constitutes acceptance.</p>
      </section>

      <section>
        <h2>12. Contact Information</h2>
        <p>For questions about these Terms, please contact us at:</p>
        <p><strong>Email:</strong> support@plutoo.chat<br>
        </p> 
      </section>
    </div>
  </div>
</template>

<script setup>
import { useSeo } from '../composables/useSeo'

useSeo({
  title: 'Terms of Service | Plutoo AI',
  description: 'Terms of Service for Plutoo AI customer support platform',
  keywords: 'terms, legal, service agreement'
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

p {
  color: #475569;
  line-height: 1.8;
  margin-bottom: 1rem;
}

ul {
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
}
</style>
