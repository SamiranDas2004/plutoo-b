<template>
  <div class="legal-page">
    <div class="container">
      <h1>Privacy Policy</h1>
      <p class="updated">Last Updated: January 29, 2025</p>

      <section>
        <h2>1. Introduction</h2>
        <p>Plutoo AI ("we," "our," or "us") is committed to protecting your privacy. This Privacy Policy explains how we collect, use, disclose, and safeguard your information when you use our Service.</p>
      </section>

      <section>
        <h2>2. Information We Collect</h2>
        
        <h3>Personal Information</h3>
        <ul>
          <li>Name and email address</li>
          <li>Company name and information</li>
          <li>Payment and billing information</li>
          <li>Account credentials</li>
        </ul>

        <h3>Usage Data</h3>
        <ul>
          <li>Chat conversations and messages</li>
          <li>Documents and files uploaded</li>
          <li>IP addresses and browser information</li>
          <li>Device information and operating system</li>
          <li>Usage patterns and analytics</li>
        </ul>

        <h3>Cookies and Tracking</h3>
        <p>We use cookies and similar tracking technologies to track activity on our Service and hold certain information.</p>
      </section>

      <section>
        <h2>3. How We Use Your Information</h2>
        <p>We use the collected information for:</p>
        <ul>
          <li>Providing and maintaining our Service</li>
          <li>Processing your transactions</li>
          <li>Improving and personalizing user experience</li>
          <li>Sending administrative information and updates</li>
          <li>Responding to customer support requests</li>
          <li>Analyzing usage patterns and trends</li>
          <li>Detecting and preventing fraud or abuse</li>
          <li>Complying with legal obligations</li>
        </ul>
      </section>

      <section>
        <h2>4. Data Storage and Security</h2>
        <p>We implement industry-standard security measures to protect your data:</p>
        <ul>
          <li>Encryption of data in transit and at rest</li>
          <li>Secure authentication and access controls</li>
          <li>Regular security audits and monitoring</li>
          <li>Compliance with SOC 2 and GDPR standards</li>
        </ul>
        <p>However, no method of transmission over the Internet is 100% secure, and we cannot guarantee absolute security.</p>
      </section>

      <section>
        <h2>5. Data Sharing and Disclosure</h2>
        <p>We do not sell your personal information. We may share your information with:</p>
        
        <h3>Service Providers</h3>
        <p>Third-party vendors who perform services on our behalf (payment processing, hosting, analytics).</p>

        <h3>Legal Requirements</h3>
        <p>When required by law, court order, or government request.</p>

        <h3>Business Transfers</h3>
        <p>In connection with a merger, acquisition, or sale of assets.</p>

        <h3>With Your Consent</h3>
        <p>When you explicitly authorize us to share your information.</p>
      </section>

      <section>
        <h2>6. Your Data Rights</h2>
        <p>You have the right to:</p>
        <ul>
          <li><strong>Access:</strong> Request a copy of your personal data</li>
          <li><strong>Correction:</strong> Update or correct inaccurate information</li>
          <li><strong>Deletion:</strong> Request deletion of your personal data</li>
          <li><strong>Portability:</strong> Receive your data in a portable format</li>
          <li><strong>Opt-out:</strong> Unsubscribe from marketing communications</li>
          <li><strong>Restriction:</strong> Request limitation of data processing</li>
        </ul>
        <p>To exercise these rights, contact us at privacy@plutoo.chat</p>
      </section>

      <section>
        <h2>7. Data Retention</h2>
        <p>We retain your information for as long as necessary to:</p>
        <ul>
          <li>Provide our Service to you</li>
          <li>Comply with legal obligations</li>
          <li>Resolve disputes and enforce agreements</li>
        </ul>
        <p>After account termination, we may retain certain data for backup, archival, or audit purposes.</p>
      </section>

      <section>
        <h2>8. International Data Transfers</h2>
        <p>Your information may be transferred to and processed in countries other than your own. We ensure appropriate safeguards are in place to protect your data in accordance with this Privacy Policy.</p>
      </section>

      <section>
        <h2>9. Children's Privacy</h2>
        <p>Our Service is not intended for children under 13 years of age. We do not knowingly collect personal information from children under 13.</p>
      </section>

      <section>
        <h2>10. Third-Party Links</h2>
        <p>Our Service may contain links to third-party websites. We are not responsible for the privacy practices of these external sites.</p>
      </section>

      <section>
        <h2>11. Changes to This Policy</h2>
        <p>We may update this Privacy Policy from time to time. We will notify you of material changes via email or through the Service. Your continued use after changes constitutes acceptance.</p>
      </section>

      <section>
        <h2>12. Contact Us</h2>
        <p>For questions about this Privacy Policy or our data practices:</p>
        <p>
          <strong>Email:</strong> support@plutoo.chat<br>
       
          <!-- <strong>Address:</strong> [Your Company Address] -->
        </p>
      </section>
    </div>
  </div>
</template>

<script setup>
import { useSeo } from '../composables/useSeo'

useSeo({
  title: 'Privacy Policy | Plutoo AI',
  description: 'Privacy Policy for Plutoo AI - How we collect, use, and protect your data',
  keywords: 'privacy, data protection, GDPR, security'
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

  h3 {
    font-size: 1.1rem;
  }
}
</style>
