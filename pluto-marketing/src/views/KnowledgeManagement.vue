<template>
  <div class="solution-page">
    <div class="hero-section">
      <div class="container">
        <h1>Knowledge Management</h1>
        <p>Centralize your company knowledge and make it instantly accessible to your AI chatbot</p>
      </div>
    </div>

    <div class="container content">
      <section class="feature-section">
        <h2>Unified Knowledge Base</h2>
        <p>Upload and manage all your company information in one place. Plutoo automatically processes and indexes your content for instant retrieval.</p>
        
        <div class="feature-grid">
          <div class="feature-card">
            <i class="fas fa-file-pdf"></i>
            <h3>Document Upload</h3>
            <p>Upload PDFs, Word docs, and text files. Your chatbot learns from product manuals, FAQs, and support guides.</p>
          </div>
          
          <div class="feature-card">
            <i class="fas fa-microphone"></i>
            <h3>Audio Transcription</h3>
            <p>Convert training videos and audio recordings into searchable knowledge using AI transcription.</p>
          </div>
          
          <div class="feature-card">
            <i class="fas fa-globe"></i>
            <h3>Website Scraping</h3>
            <p>Import content directly from your website. Keep your chatbot updated with your latest information.</p>
          </div>
          
          <div class="feature-card">
            <i class="fas fa-edit"></i>
            <h3>Manual Entry</h3>
            <p>Add custom information, policies, and procedures directly through our editor.</p>
          </div>
        </div>
      </section>

      <section class="feature-section">
        <h2>Smart Content Processing</h2>
        <p>Our RAG (Retrieval-Augmented Generation) technology ensures accurate, context-aware responses.</p>
        
        <ul class="benefit-list">
          <li><i class="fas fa-check-circle"></i> Automatic content chunking and indexing</li>
          <li><i class="fas fa-check-circle"></i> Vector embeddings for semantic search</li>
          <li><i class="fas fa-check-circle"></i> Real-time content updates</li>
          <li><i class="fas fa-check-circle"></i> Multi-format support (PDF, DOCX, TXT, MP3, WAV)</li>
          <li><i class="fas fa-check-circle"></i> Duplicate detection and management</li>
        </ul>
      </section>

      <section class="feature-section">
        <h2>Easy Management</h2>
        <div class="steps">
          <div class="step">
            <div class="step-number">1</div>
            <h3>Upload Content</h3>
            <p>Drag and drop your files or paste URLs</p>
          </div>
          <div class="step">
            <div class="step-number">2</div>
            <h3>Auto-Processing</h3>
            <p>AI extracts and indexes information</p>
          </div>
          <div class="step">
            <div class="step-number">3</div>
            <h3>Instant Availability</h3>
            <p>Your chatbot can answer questions immediately</p>
          </div>
        </div>
      </section>

      <section class="cta-section">
        <h2>Ready to Centralize Your Knowledge?</h2>
        <p>Start organizing your company information today</p>
        <button class="cta-button" @click="$router.push('/signup')">Get Started Free</button>
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

.steps {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.step {
  text-align: center;
}

.step-number {
  width: 60px;
  height: 60px;
  background: #2ED0E6;
  color: white;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 1.5rem;
  font-weight: 700;
  margin: 0 auto 1rem;
}

.step h3 {
  font-size: 1.25rem;
  color: #1e293b;
  margin-bottom: 0.5rem;
}

.step p {
  color: #64748b;
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
  
  .feature-grid, .steps {
    grid-template-columns: 1fr;
  }
}
</style>
