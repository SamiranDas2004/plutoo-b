<template>
  <div class="solution-page">
    <div class="hero-section">
      <div class="container">
        <h1>Analytics & Insights</h1>
        <p>Track performance, understand your customers, and optimize your chatbot with powerful analytics</p>
      </div>
    </div>

    <div class="container content">
      <section class="feature-section">
        <h2>Real-Time Dashboard</h2>
        <p>Monitor your chatbot's performance with comprehensive metrics and visualizations.</p>
        
        <div class="feature-grid">
          <div class="feature-card">
            <i class="fas fa-chart-line"></i>
            <h3>Visitor Tracking</h3>
            <p>See how many visitors interact with your chatbot daily, weekly, and monthly.</p>
          </div>
          
          <div class="feature-card">
            <i class="fas fa-comments"></i>
            <h3>Message Analytics</h3>
            <p>Track total messages, response times, and conversation patterns.</p>
          </div>
          
          <div class="feature-card">
            <i class="fas fa-clock"></i>
            <h3>Response Time</h3>
            <p>Monitor average response times and ensure fast customer service.</p>
          </div>
          
          <div class="feature-card">
            <i class="fas fa-percentage"></i>
            <h3>Resolution Rate</h3>
            <p>See what kind of queries customers are most likely to be resolved by your chatbot.</p>
          </div>
        </div>
      </section>

      <section class="feature-section">
        <h2>Conversation Insights</h2>
        <p>Dive deep into customer interactions to improve your service.</p>
        
        <ul class="benefit-list">
          <li><i class="fas fa-check-circle"></i> View complete chat session history</li>
          <li><i class="fas fa-check-circle"></i> Identify common customer questions</li>
          <li><i class="fas fa-check-circle"></i> Track visitor information and behavior</li>
          <li><i class="fas fa-check-circle"></i> Monitor support ticket creation</li>
          <li><i class="fas fa-check-circle"></i> Export data for further analysis</li>
        </ul>
      </section>

      <section class="feature-section">
        <h2>Key Metrics You'll Track</h2>
        <div class="metrics-grid">
          <div class="metric-card">
            <div class="metric-icon">👥</div>
            <h3>Daily Visitors</h3>
            <p>Track unique visitors engaging with your chatbot</p>
          </div>
          
          <div class="metric-card">
            <div class="metric-icon">💬</div>
            <h3>Total Messages</h3>
            <p>Monitor conversation volume and trends</p>
          </div>
          
          <div class="metric-card">
            <div class="metric-icon">⚡</div>
            <h3>Response Speed</h3>
            <p>Ensure lightning-fast customer service</p>
          </div>
          
          <div class="metric-card">
            <div class="metric-icon">🎯</div>
            <h3>Accuracy Rate</h3>
            <p>Measure chatbot answer quality</p>
          </div>
          
          <div class="metric-card">
            <div class="metric-icon">🎟️</div>
            <h3>Support Tickets</h3>
            <p>Track escalations to human agents</p>
          </div>
          
          <div class="metric-card">
            <div class="metric-icon">📈</div>
            <h3>Growth Trends</h3>
            <p>Visualize 7-day and 30-day trends</p>
          </div>
        </div>
      </section>

      <section class="feature-section">
        <h2>Actionable Reports</h2>
        <div class="report-features">
          <div class="report-item">
            <h3>📊 Time-Based Analysis</h3>
            <p>Compare performance across different time periods (7 days, 30 days, custom ranges)</p>
          </div>
          <div class="report-item">
            <h3>👤 Visitor Profiles</h3>
            <p>See detailed information about each visitor and their conversation history</p>
          </div>
          <div class="report-item">
            <h3>🚀 Smart Recommendations</h3>
            <p>Get AI-powered suggestions to improve your chatbot's performance</p>
          </div>
        </div>
      </section>

      <section class="cta-section">
        <h2>Start Making Data-Driven Decisions</h2>
        <p>Get insights that help you improve customer satisfaction</p>
        <button class="cta-button" @click="$router.push('/signup')">Try Analytics Free</button>
      </section>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.solution-page {
  padding-top: 80px;
}

.hero-section {
  background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
  color: white;
  padding: 4rem 0;
  text-align: center;
}

.hero-section h1 {
  font-size: 3rem;
  margin-bottom: 1rem;
}

.hero-section p {
  font-size: 1.25rem;
  color: rgba(255, 255, 255, 0.8);
}

.container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 0 2rem;
}

.content {
  padding: 4rem 2rem;
}

.feature-section {
  margin-bottom: 4rem;
}

.feature-section h2 {
  font-size: 2rem;
  color: #1e293b;
  margin-bottom: 1rem;
}

.feature-section > p {
  font-size: 1.125rem;
  color: #64748b;
  margin-bottom: 2rem;
}

.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.feature-card {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
  transition: all 0.3s;
}

.feature-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 4px 16px rgba(0, 0, 0, 0.15);
}

.feature-card i {
  font-size: 3rem;
  color: #2ED0E6;
  margin-bottom: 1rem;
}

.feature-card h3 {
  font-size: 1.25rem;
  color: #1e293b;
  margin-bottom: 0.75rem;
}

.feature-card p {
  color: #64748b;
  line-height: 1.6;
}

.benefit-list {
  list-style: none;
  padding: 0;
}

.benefit-list li {
  display: flex;
  align-items: center;
  gap: 1rem;
  padding: 0.75rem 0;
  font-size: 1.125rem;
  color: #475569;
}

.benefit-list i {
  color: #22c55e;
  font-size: 1.5rem;
}

.metrics-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}

.metric-card {
  background: linear-gradient(135deg, #f8fafc 0%, #e2e8f0 100%);
  padding: 1.5rem;
  border-radius: 12px;
  text-align: center;
}

.metric-icon {
  font-size: 2.5rem;
  margin-bottom: 0.75rem;
}

.metric-card h3 {
  font-size: 1.125rem;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.metric-card p {
  color: #64748b;
  font-size: 0.95rem;
}

.report-features {
  display: grid;
  gap: 1.5rem;
  margin-top: 2rem;
}

.report-item {
  background: white;
  padding: 2rem;
  border-radius: 12px;
  border-left: 4px solid #2ED0E6;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.08);
}

.report-item h3 {
  font-size: 1.25rem;
  color: #1e293b;
  margin-bottom: 0.75rem;
}

.report-item p {
  color: #64748b;
  line-height: 1.6;
}

.cta-section {
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  color: white;
  padding: 3rem;
  border-radius: 16px;
  text-align: center;
}

.cta-section h2 {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.cta-section p {
  font-size: 1.125rem;
  margin-bottom: 2rem;
  opacity: 0.9;
}

.cta-button {
  background: white;
  color: #2C3E50;
  padding: 1rem 2.5rem;
  border: none;
  border-radius: 8px;
  font-size: 1.125rem;
  font-weight: 600;
  cursor: pointer;
  transition: all 0.3s;
}

.cta-button:hover {
  transform: translateY(-2px);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
}

@media (max-width: 768px) {
  .hero-section h1 {
    font-size: 2rem;
  }
  
  .feature-grid, .metrics-grid {
    grid-template-columns: 1fr;
  }
}
</style>
