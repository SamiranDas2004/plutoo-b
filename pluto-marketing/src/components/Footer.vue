<template>
  <footer class="footer">
    <div class="container">
      <div class="footer-content">
        <div class="footer-section footer-brand">
          <div class="footer-logo">
            <span class="logo-icon">🚀</span>
            <span class="logo-text">Pluto</span>
          </div>
          <p class="footer-description">
            Transform your customer support with AI-powered solutions that scale with your business. Deliver exceptional experiences 24/7.
          </p>
          <div class="social-links">
            <a href="#" class="social-link" aria-label="Twitter">
              <i class="fab fa-twitter"></i>
            </a>
            <a href="#" class="social-link" aria-label="LinkedIn">
              <i class="fab fa-linkedin-in"></i>
            </a>
            <a href="#" class="social-link" aria-label="Facebook">
              <i class="fab fa-facebook-f"></i>
            </a>
            <a href="#" class="social-link" aria-label="Email">
              <i class="fas fa-envelope"></i>
            </a>
          </div>
          <div class="footer-contact">
            <p><i class="fas fa-envelope"></i> hello@plutoai.com</p>
            <p><i class="fas fa-phone"></i> +1 (555) 123-4567</p>
          </div>
        </div>
        
        <div class="footer-section">
          <h4 class="footer-title">Product</h4>
          <ul class="footer-links">
            <li><a href="#features">Features</a></li>
            <li><a href="#pricing">Pricing</a></li>
            <li><a href="#">API Documentation</a></li>
            <li><a href="#">Integrations</a></li>
            <li><a href="#">Changelog</a></li>
            <li><a href="#">Roadmap</a></li>
          </ul>
        </div>
        
        <div class="footer-section">
          <h4 class="footer-title">Solutions</h4>
          <ul class="footer-links">
            <li><a href="#">Customer Support</a></li>
            <li><a href="#">Sales Automation</a></li>
            <li><a href="#">Knowledge Management</a></li>
            <li><a href="#">Analytics & Insights</a></li>
            <li><a href="#">Enterprise</a></li>
          </ul>
        </div>
        
       
        
      
      </div>
      
      <div class="footer-bottom">
        <div class="footer-bottom-left">
          <p>&copy; 2024 Pluto AI. All rights reserved.</p>
          <div class="footer-legal">
            <a href="#">Privacy Policy</a>
            <a href="#">Terms of Service</a>
            <a href="#">Cookie Policy</a>
            <a href="#">GDPR</a>
          </div>
        </div>
        <div class="footer-bottom-right">
          <div class="footer-badges">
            <div class="badge">SOC2 Compliant</div>
            <div class="badge">GDPR Ready</div>
            <div class="badge">ISO 27001</div>
          </div>
        </div>
      </div>
    </div>
  </footer>
</template>

<script setup>
</script>

<style scoped>
.footer {
  background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
  color: white;
  padding: 4rem 0 2rem;
  position: relative;
}

.footer::before {
  content: '';
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  height: 1px;
  background: linear-gradient(90deg, transparent 0%, #2ED0E6 50%, transparent 100%);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.footer-content {
  display: grid;
  grid-template-columns: 2fr 1fr 1fr;
  gap: 3rem;
  margin-bottom: 3rem;
}

.footer-brand {
  max-width: 350px;
}

.footer-logo {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  font-size: 1.8rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
}

.logo-icon {
  font-size: 2rem;
}

.logo-text {
  background: linear-gradient(135deg, #2ED0E6 0%, #ffffff 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  background-clip: text;
}

.footer-description {
  color: rgba(255, 255, 255, 0.8);
  line-height: 1.7;
  margin-bottom: 2rem;
  font-size: 1rem;
}

.social-links {
  display: flex;
  gap: 1rem;
  margin-bottom: 2rem;
}

.social-link {
  width: 44px;
  height: 44px;
  background: rgba(46, 208, 230, 0.1);
  border: 1px solid rgba(46, 208, 230, 0.2);
  border-radius: 12px;
  display: flex;
  align-items: center;
  justify-content: center;
  color: #2ED0E6;
  text-decoration: none;
  transition: all 0.3s;
  font-size: 1.1rem;
}

.social-link:hover {
  background: rgba(46, 208, 230, 0.2);
  border-color: #2ED0E6;
  transform: translateY(-2px);
  color: white;
}

.footer-contact {
  display: flex;
  flex-direction: column;
  gap: 0.75rem;
}

.footer-contact p {
  display: flex;
  align-items: center;
  gap: 0.75rem;
  color: rgba(255, 255, 255, 0.7);
  font-size: 0.95rem;
  margin: 0;
}

.footer-contact i {
  color: #2ED0E6;
  width: 16px;
}

.footer-title {
  font-size: 1.1rem;
  font-weight: 700;
  margin-bottom: 1.5rem;
  color: white;
  position: relative;
}

.footer-title::after {
  content: '';
  position: absolute;
  bottom: -0.5rem;
  left: 0;
  width: 30px;
  height: 2px;
  background: linear-gradient(135deg, #2ED0E6 0%, #2C3E50 100%);
  border-radius: 1px;
}

.footer-links {
  list-style: none;
}

.footer-links li {
  margin-bottom: 0.75rem;
}

.footer-links a {
  color: rgba(255, 255, 255, 0.7);
  text-decoration: none;
  transition: all 0.3s;
  font-size: 0.95rem;
  position: relative;
}

.footer-links a:hover {
  color: #2ED0E6;
  padding-left: 0.5rem;
}

.footer-bottom {
  padding-top: 2rem;
  border-top: 1px solid rgba(255, 255, 255, 0.1);
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.footer-bottom-left {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}

.footer-bottom-left p {
  color: rgba(255, 255, 255, 0.6);
  font-size: 0.9rem;
  margin: 0;
}

.footer-legal {
  display: flex;
  gap: 1.5rem;
}

.footer-legal a {
  color: rgba(255, 255, 255, 0.5);
  text-decoration: none;
  font-size: 0.85rem;
  transition: color 0.3s;
}

.footer-legal a:hover {
  color: #2ED0E6;
}

.footer-bottom-right {
  display: flex;
  align-items: center;
}

.footer-badges {
  display: flex;
  gap: 1rem;
}

.badge {
  background: rgba(46, 208, 230, 0.1);
  border: 1px solid rgba(46, 208, 230, 0.2);
  color: #2ED0E6;
  padding: 0.4rem 0.8rem;
  border-radius: 20px;
  font-size: 0.8rem;
  font-weight: 500;
}

@media (max-width: 1024px) {
  .footer-content {
    grid-template-columns: 1fr 1fr;
    gap: 2rem;
  }

  .footer-brand {
    grid-column: 1 / -1;
    max-width: none;
  }
}

@media (max-width: 768px) {
  .footer {
    padding: 3rem 0 1.5rem;
  }

  .container {
    padding: 0 1rem;
  }

  .footer-content {
    grid-template-columns: 1fr 1fr;
    gap: 2rem 1.5rem;
    margin-bottom: 2rem;
    align-items: start;
  }

  .footer-brand {
    grid-column: 1 / -1;
    max-width: none;
    text-align: center;
  }

  .footer-logo {
    justify-content: center;
  }

  .footer-description {
    text-align: center;
    font-size: 0.9rem;
  }

  .social-links {
    justify-content: center;
  }

  .footer-contact {
    align-items: center;
  }

  .footer-contact p {
    font-size: 0.85rem;
  }

  .footer-title {
    font-size: 1rem;
  }

  .footer-links li {
    margin-bottom: 0.6rem;
  }

  .footer-links a {
    font-size: 0.85rem;
  }

  .footer-bottom {
    flex-direction: column;
    gap: 1.5rem;
    padding-top: 1.5rem;
  }

  .footer-bottom-left {
    align-items: center;
    text-align: center;
  }

  .footer-legal {
    flex-wrap: wrap;
    justify-content: center;
    gap: 1rem;
  }

  .footer-badges {
    justify-content: center;
    flex-wrap: wrap;
  }
}
</style>
