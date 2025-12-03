<template>
  <div class="demo-page">
    <div class="demo-container">
      <div class="demo-header">
        <h1>Book a Demo</h1>
        <p>Schedule a personalized demo with our team to see how Pluto can transform your customer support</p>
      </div>

      <div class="demo-grid">
        <div class="demo-content">
          <h2>What You'll Learn</h2>
          <ul class="benefits-list">
            <li>
              <div class="icon">🎯</div>
              <div>
                <h3>AI-Powered RAG</h3>
                <p>95% accurate responses</p>
              </div>
            </li>
            <li>
              <div class="icon">⚡</div>
              <div>
                <h3>Quick Integration</h3>
                <p>5-minute setup</p>
              </div>
            </li>
            <li>
              <div class="icon">📊</div>
              <div>
                <h3>Analytics</h3>
                <p>Real-time insights</p>
              </div>
            </li>
            <li>
              <div class="icon">🔒</div>
              <div>
                <h3>Security</h3>
                <p>SOC2 & GDPR</p>
              </div>
            </li>
          </ul>

          <div class="stats">
            <div class="stat">
              <div class="stat-number">80%</div>
              <div class="stat-label">Cost Cut</div>
            </div>
            <div class="stat">
              <div class="stat-number">&lt;0.5s</div>
              <div class="stat-label">Response</div>
            </div>
          </div>
        </div>

        <div class="calendar-wrapper">
          <iframe 
            src="https://calendar.google.com/calendar/appointments/schedules/AcZssZ1hmEfhF4EmpqVi6DL_75yYQStGQx0IaGSzu0L-vn8BMo8A5CxCCyDxFjsc4lZeTELqYaJS41By?gv=true"
            style="border:0"
            width="100%"
            height="600"
            frameborder="0"
          ></iframe>
        </div>
      </div>

      <div class="demo-footer">
        <p>Can't find a suitable time? <a href="mailto:samiran4209@gmail.com">Email us</a> directly.</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useSeo } from '../composables/useSeo'

useSeo({
  title: 'Book a Demo | Pluto AI Customer Support',
  description: 'Schedule a personalized demo of Pluto AI customer support platform. See how RAG technology can reduce your support costs by 80%.',
  keywords: 'Pluto demo, AI support demo, schedule demo, book meeting'
})
</script>

<style scoped>
.demo-page {
  min-height: 100vh;
  background: #fafafa;
  padding-top: 80px;
}

.demo-container {
  max-width: 1400px;
  margin: 0 auto;
  padding: 3rem 2rem;
}

.demo-header {
  text-align: center;
  margin-bottom: 3rem;
}

.demo-header h1 {
  font-size: 2.5rem;
  font-weight: 800;
  color: #1a1a1a;
  margin-bottom: 1rem;
}

.demo-header p {
  font-size: 1.1rem;
  color: #64748b;
  max-width: 700px;
  margin: 0 auto;
  line-height: 1.6;
}

.demo-grid {
  display: grid;
  grid-template-columns: 30% 70%;
  gap: 2rem;
  align-items: start;
}

.demo-content h2 {
  font-size: 1.5rem;
  font-weight: 700;
  color: #1a1a1a;
  margin-bottom: 1.5rem;
}

.benefits-list {
  list-style: none;
  padding: 0;
  display: flex;
  flex-direction: column;
  gap: 1.25rem;
  margin-bottom: 2rem;
}

.benefits-list li {
  display: flex;
  gap: 0.75rem;
  align-items: start;
}

.icon {
  font-size: 1.5rem;
  flex-shrink: 0;
}

.benefits-list h3 {
  font-size: 1rem;
  font-weight: 600;
  color: #1a1a1a;
  margin-bottom: 0.15rem;
}

.benefits-list p {
  color: #64748b;
  line-height: 1.4;
  font-size: 0.875rem;
}

.stats {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 1rem;
  padding: 1.5rem;
  background: white;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
}

.stat {
  text-align: center;
}

.stat-number {
  font-size: 1.75rem;
  font-weight: 800;
  color: #2ED0E6;
  margin-bottom: 0.25rem;
}

.stat-label {
  font-size: 0.8rem;
  color: #64748b;
  font-weight: 500;
}

.calendar-wrapper {
  background: white;
  border-radius: 12px;
  padding: 2rem;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.08);
}

.calendar-wrapper iframe {
  border-radius: 8px;
}

.demo-footer {
  text-align: center;
  color: #64748b;
  font-size: 0.95rem;
  margin-top: 3rem;
}

.demo-footer a {
  color: #2ED0E6;
  text-decoration: none;
  font-weight: 600;
}

.demo-footer a:hover {
  text-decoration: underline;
}

@media (max-width: 968px) {
  .demo-grid {
    grid-template-columns: 1fr;
  }

  .stats {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .demo-header h1 {
    font-size: 2rem;
  }

  .calendar-wrapper {
    padding: 1rem;
  }

  .demo-container {
    padding: 2rem 1rem;
  }

  .demo-content h2 {
    font-size: 1.25rem;
  }
}
</style>
