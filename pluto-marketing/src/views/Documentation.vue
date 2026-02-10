<template>
  <div class="documentation-page">
    <div class="doc-hero">
      <div class="container">
        <h1 class="doc-title">How to Use Plutoo</h1>
        <p class="doc-subtitle">Complete guide to set up and use your AI chatbot</p>
      </div>
    </div>

    <div class="container doc-container">
      <aside class="doc-sidebar">
        <nav class="doc-nav">
          <h3>Getting Started</h3>
          <ul>
            <li><a href="#signup">Sign Up</a></li>
            <li><a href="#dashboard">Dashboard Overview</a></li>
          </ul>
          
          <h3>Training Your Bot</h3>
          <ul>
            <li><a href="#upload-docs">Upload Documents</a></li>
            <li><a href="#upload-audio">Upload Audio</a></li>
            <li><a href="#add-website">Add Website Content</a></li>
            <li><a href="#write-info">Write Information</a></li>
          </ul>
          
          <h3>Deployment</h3>
          <ul>
            <li><a href="#widget">Install Widget</a></li>
            <li><a href="#customize">Customize Widget</a></li>
          </ul>

          <h3>Monitoring</h3>
          <ul>
            <li><a href="#analytics">View Analytics</a></li>
            <li><a href="#sessions">Chat Sessions</a></li>
            <li><a href="#tickets">Support Tickets</a></li>
          </ul>
        </nav>
      </aside>

      <main class="doc-content">
        <section id="signup" class="doc-section">
          <h2>1. Sign Up & Login</h2>
          <p>Start by creating your account:</p>
          <ol class="step-list">
            <li>Visit <a href="https://dashboard.plutoo.chat" target="_blank">dashboard.plutoo.chat</a></li>
            <li>Click "Sign Up" and enter your details</li>
            <li>Verify your email address</li>
            <li>Login to access your dashboard</li>
          </ol>
          <div class="info-box">
            <i class="fas fa-lightbulb"></i>
            <p>You'll receive your unique Bot Token after signup - keep it safe!</p>
          </div>
        </section>

        <section id="dashboard" class="doc-section">
          <h2>2. Dashboard Overview</h2>
          <p>Your dashboard is divided into several sections:</p>
          <div class="feature-grid">
            <div class="feature-item">
              <i class="fas fa-chart-line"></i>
              <h4>Dashboard</h4>
              <p>View analytics, visitor stats, and message counts</p>
            </div>
            <div class="feature-item">
              <i class="fas fa-upload"></i>
              <h4>Upload Information</h4>
              <p>Train your bot with documents, audio, websites, and text</p>
            </div>
            <div class="feature-item">
              <i class="fas fa-comments"></i>
              <h4>Analytics</h4>
              <p>Monitor chat sessions, visitors, and support tickets</p>
            </div>
            <div class="feature-item">
              <i class="fas fa-cog"></i>
              <h4>Settings</h4>
              <p>Customize widget appearance and manage your account</p>
            </div>
          </div>
        </section>

        <section id="upload-docs" class="doc-section">
          <h2>3. Upload Documents</h2>
          <p>Train your chatbot with your knowledge base:</p>
          <ol class="step-list">
            <li>Go to <strong>Documents</strong> in the sidebar</li>
            <li>Click <strong>"Upload Document"</strong></li>
            <li>Select your file (PDF, DOCX, TXT supported)</li>
            <li>Wait for processing - your bot will learn from this content</li>
          </ol>
          <div class="tip-box">
            <i class="fas fa-check-circle"></i>
            <p><strong>Tip:</strong> Upload FAQs, product manuals, and support guides for best results</p>
          </div>
        </section>

        <section id="upload-audio" class="doc-section">
          <h2>4. Upload Audio Recordings</h2>
          <p>Convert audio content into knowledge:</p>
          <ol class="step-list">
            <li>Navigate to <strong>Audio Recordings</strong></li>
            <li>Click <strong>"Upload Audio"</strong></li>
            <li>Select audio file (MP3, WAV, M4A supported)</li>
            <li>Audio will be transcribed and added to your bot's knowledge</li>
          </ol>
        </section>

        <section id="add-website" class="doc-section">
          <h2>5. Load Website Content</h2>
          <p>Import content directly from your website:</p>
          <ol class="step-list">
            <li>Go to <strong>Website Loader</strong></li>
            <li>Enter your website URL</li>
            <li>Click <strong>"Load Website"</strong></li>
            <li>Content will be extracted and processed automatically</li>
          </ol>
        </section>

        <section id="write-info" class="doc-section">
          <h2>6. Write Information Manually</h2>
          <p>Add custom information directly:</p>
          <ol class="step-list">
            <li>Navigate to <strong>Write Information</strong></li>
            <li>Enter a title for your content</li>
            <li>Write or paste your information</li>
            <li>Click <strong>"Save"</strong> to add it to your bot's knowledge</li>
          </ol>
          <div class="tip-box">
            <i class="fas fa-check-circle"></i>
            <p><strong>Use case:</strong> Perfect for company policies, special offers, or frequently asked questions</p>
          </div>
        </section>

        <section id="widget" class="doc-section">
          <h2>7. Install Widget on Your Website</h2>
          <p>Add the chatbot to your website in 2 minutes:</p>
          <ol class="step-list">
            <li>Go to <strong>Widget Settings</strong></li>
            <li>Copy your unique widget code</li>
            <li>Paste it before the closing <code>&lt;/body&gt;</code> tag in your website</li>
            <li>Save and publish - your chatbot is now live!</li>
          </ol>
          
          <div class="code-block">
            <div class="code-header">
              <span>Widget Code Example</span>
            </div>
            <pre><code>&lt;script src="https://cdn.plutoo.chat/widget.js"&gt;&lt;/script&gt;
&lt;script&gt;
  PlutooWidget.init({
    botToken: 'YOUR_BOT_TOKEN',
    position: 'bottom-right'
  });
&lt;/script&gt;</code></pre>
          </div>
        </section>

        <section id="customize" class="doc-section">
          <h2>8. Customize Widget Appearance</h2>
          <p>Make the widget match your brand:</p>
          <ol class="step-list">
            <li>Go to <strong>Widget Settings</strong></li>
            <li>Choose your primary color</li>
            <li>Set text color and font family</li>
            <li>Select widget position (bottom-right or bottom-left)</li>
            <li>Customize welcome message</li>
            <li>Click <strong>"Save Changes"</strong></li>
          </ol>
        </section>

        <section id="analytics" class="doc-section">
          <h2>9. Monitor Analytics</h2>
          <p>Track your chatbot's performance:</p>
          <ul class="feature-list">
            <li><strong>Dashboard:</strong> View visitors today, messages today, and trends</li>
            <li><strong>Charts:</strong> See activity over 7 or 30 days</li>
            <li><strong>Real-time:</strong> Monitor live conversations</li>
          </ul>
        </section>

        <section id="sessions" class="doc-section">
          <h2>10. View Chat Sessions</h2>
          <p>Review all conversations:</p>
          <ol class="step-list">
            <li>Navigate to <strong>Chat Sessions</strong></li>
            <li>See list of all conversations</li>
            <li>Click on any session to view full chat history</li>
            <li>Analyze customer questions and bot responses</li>
          </ol>
        </section>

        <section id="tickets" class="doc-section">
          <h2>11. Manage Support Tickets</h2>
          <p>Handle escalated conversations:</p>
          <ul class="feature-list">
            <li>View tickets created when bot can't answer</li>
            <li>See customer email and message</li>
            <li>Respond directly to customers</li>
            <li>Track ticket status and resolution</li>
          </ul>
        </section>

        <section class="doc-section">
          <h2>Need Help?</h2>
          <div class="help-grid">
            <div class="help-card">
              <i class="fas fa-envelope"></i>
              <h4>Email Support</h4>
              <p>hello@plutoo.chat</p>
            </div>
            <div class="help-card">
              <i class="fas fa-phone"></i>
              <h4>Phone Support</h4>
              <p>+91 8927750287</p>
            </div>
            <div class="help-card">
              <i class="fas fa-comments"></i>
              <h4>Live Chat</h4>
              <p>Available on our website look at bottom right corner</p>
            </div>
          </div>
        </section>
      </main>
    </div>
  </div>
</template>

<script setup>
</script>

<style scoped>
.documentation-page {
  min-height: 100vh;
  background: #f8fafc;
}

.doc-hero {
  background: linear-gradient(135deg, #1e293b 0%, #0f172a 100%);
  color: white;
  padding: 6rem 0 4rem;
  text-align: center;
}

.doc-title {
  font-size: 3rem;
  font-weight: 700;
  margin-bottom: 1rem;
}

.doc-subtitle {
  font-size: 1.25rem;
  color: rgba(255, 255, 255, 0.8);
}

.doc-container {
  display: grid;
  grid-template-columns: 250px 1fr;
  gap: 3rem;
  padding: 3rem 2rem;
  max-width: 1400px;
  margin: 0 auto;
}

.doc-sidebar {
  position: sticky;
  top: 2rem;
  height: fit-content;
  background: white;
  border-radius: 12px;
  padding: 1.5rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.doc-nav h3 {
  font-size: 0.875rem;
  font-weight: 600;
  color: #64748b;
  text-transform: uppercase;
  margin: 1.5rem 0 0.75rem;
  letter-spacing: 0.05em;
}

.doc-nav h3:first-child {
  margin-top: 0;
}

.doc-nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

.doc-nav li {
  margin-bottom: 0.5rem;
}

.doc-nav a {
  color: #475569;
  text-decoration: none;
  font-size: 0.95rem;
  display: block;
  padding: 0.5rem 0.75rem;
  border-radius: 6px;
  transition: all 0.2s;
}

.doc-nav a:hover {
  background: #f1f5f9;
  color: #2ED0E6;
}

.doc-content {
  background: white;
  border-radius: 12px;
  padding: 3rem;
  box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
}

.doc-section {
  margin-bottom: 3rem;
  padding-bottom: 3rem;
  border-bottom: 1px solid #e2e8f0;
}

.doc-section:last-child {
  border-bottom: none;
}

.doc-section h2 {
  font-size: 2rem;
  font-weight: 700;
  color: #1e293b;
  margin-bottom: 1rem;
}

.doc-section h3 {
  font-size: 1.5rem;
  font-weight: 600;
  color: #334155;
  margin: 2rem 0 1rem;
}

.doc-section h4 {
  font-size: 1.125rem;
  font-weight: 600;
  color: #475569;
  margin: 1.5rem 0 0.75rem;
}

.doc-section p {
  color: #64748b;
  line-height: 1.7;
  margin-bottom: 1rem;
}

.info-box {
  background: #f0f9ff;
  border-left: 4px solid #2ED0E6;
  padding: 1rem 1.5rem;
  border-radius: 8px;
  display: flex;
  align-items: center;
  gap: 1rem;
  margin: 1.5rem 0;
}

.info-box i {
  color: #2ED0E6;
  font-size: 1.25rem;
}

.info-box code {
  background: white;
  padding: 0.25rem 0.5rem;
  border-radius: 4px;
  font-family: 'Courier New', monospace;
  color: #1e293b;
}

.code-block {
  background: #1e293b;
  border-radius: 8px;
  overflow: hidden;
  margin: 1.5rem 0;
}

.code-header {
  background: #0f172a;
  padding: 0.75rem 1.5rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
  border-bottom: 1px solid #334155;
}

.code-header span {
  color: #94a3b8;
  font-size: 0.875rem;
  font-weight: 500;
}

.copy-btn {
  background: transparent;
  border: 1px solid #334155;
  color: #94a3b8;
  padding: 0.25rem 0.75rem;
  border-radius: 4px;
  cursor: pointer;
  transition: all 0.2s;
}

.copy-btn:hover {
  background: #334155;
  color: white;
}

.code-block pre {
  margin: 0;
  padding: 1.5rem;
  overflow-x: auto;
}

.code-block code {
  color: #e2e8f0;
  font-family: 'Courier New', monospace;
  font-size: 0.9rem;
  line-height: 1.6;
}

.example-tabs {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1rem;
}

.tab-btn {
  background: #f1f5f9;
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 6px;
  cursor: pointer;
  font-weight: 500;
  color: #64748b;
  transition: all 0.2s;
}

.tab-btn.active {
  background: #2ED0E6;
  color: white;
}

.sdk-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-top: 1.5rem;
}

.sdk-card {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 8px;
  padding: 1.5rem;
  text-align: center;
}

.sdk-card i {
  font-size: 2.5rem;
  color: #2ED0E6;
  margin-bottom: 1rem;
}

.sdk-card h4 {
  font-size: 1rem;
  margin: 0.5rem 0;
  color: #1e293b;
}

.sdk-card code {
  background: white;
  padding: 0.5rem;
  border-radius: 4px;
  font-size: 0.85rem;
  display: block;
  margin-top: 0.75rem;
}

.step-list {
  list-style: none;
  counter-reset: step-counter;
  padding-left: 0;
}

.step-list li {
  counter-increment: step-counter;
  margin-bottom: 1rem;
  padding-left: 3rem;
  position: relative;
  color: #475569;
  line-height: 1.7;
}

.step-list li::before {
  content: counter(step-counter);
  position: absolute;
  left: 0;
  top: 0;
  background: #2ED0E6;
  color: white;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-weight: 600;
  font-size: 0.9rem;
}

.feature-list {
  list-style: none;
  padding-left: 0;
}

.feature-list li {
  padding-left: 2rem;
  margin-bottom: 0.75rem;
  position: relative;
  color: #475569;
  line-height: 1.7;
}

.feature-list li::before {
  content: '✓';
  position: absolute;
  left: 0;
  color: #2ED0E6;
  font-weight: 700;
  font-size: 1.2rem;
}

.tip-box {
  background: #f0fdf4;
  border-left: 4px solid #22c55e;
  padding: 1rem 1.5rem;
  border-radius: 8px;
  display: flex;
  align-items: flex-start;
  gap: 1rem;
  margin: 1.5rem 0;
}

.tip-box i {
  color: #22c55e;
  font-size: 1.25rem;
  margin-top: 0.25rem;
}

.feature-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 1.5rem;
  margin: 2rem 0;
}

.feature-item {
  background: #f8fafc;
  border: 1px solid #e2e8f0;
  border-radius: 12px;
  padding: 1.5rem;
  text-align: center;
  transition: all 0.3s;
}

.feature-item:hover {
  border-color: #2ED0E6;
  transform: translateY(-4px);
  box-shadow: 0 4px 12px rgba(46, 208, 230, 0.1);
}

.feature-item i {
  font-size: 2.5rem;
  color: #2ED0E6;
  margin-bottom: 1rem;
}

.feature-item h4 {
  font-size: 1.125rem;
  margin: 0.5rem 0;
  color: #1e293b;
}

.feature-item p {
  font-size: 0.9rem;
  color: #64748b;
  margin: 0;
}

.help-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
  gap: 1.5rem;
  margin-top: 2rem;
}

.help-card {
  background: linear-gradient(135deg, #2C3E50 0%, #2ED0E6 100%);
  color: white;
  border-radius: 12px;
  padding: 2rem 1.5rem;
  text-align: center;
}

.help-card i {
  font-size: 2rem;
  margin-bottom: 1rem;
}

.help-card h4 {
  font-size: 1.125rem;
  margin: 0.5rem 0;
  color: white;
}

.help-card p {
  font-size: 0.95rem;
  color: rgba(255, 255, 255, 0.9);
  margin: 0;
}

@media (max-width: 1024px) {
  .doc-container {
    grid-template-columns: 1fr;
  }

  .doc-sidebar {
    position: static;
  }
}

@media (max-width: 768px) {
  .doc-hero {
    padding: 4rem 0 2rem;
  }

  .doc-title {
    font-size: 2rem;
  }

  .doc-subtitle {
    font-size: 1rem;
  }

  .doc-content {
    padding: 1.5rem;
  }

  .doc-section h2 {
    font-size: 1.5rem;
  }
}
</style>
