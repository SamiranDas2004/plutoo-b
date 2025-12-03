// SEO utility functions
export const updateMetaTags = (meta) => {
  if (meta.title) document.title = meta.title
  
  const tags = {
    description: meta.description,
    keywords: meta.keywords,
    'og:title': meta.title,
    'og:description': meta.description,
    'og:url': meta.url || window.location.href,
    'twitter:title': meta.title,
    'twitter:description': meta.description
  }
  
  Object.entries(tags).forEach(([name, content]) => {
    if (!content) return
    const attr = name.startsWith('og:') || name.startsWith('twitter:') ? 'property' : 'name'
    let tag = document.querySelector(`meta[${attr}="${name}"]`)
    if (!tag) {
      tag = document.createElement('meta')
      tag.setAttribute(attr, name)
      document.head.appendChild(tag)
    }
    tag.setAttribute('content', content)
  })
}

export const routeMeta = {
  home: {
    title: 'Pluto - AI-Powered Customer Support with RAG Technology | Reduce Costs 80%',
    description: 'Transform customer support with Pluto\'s AI chatbot using RAG technology. Get 95% accurate responses in <0.5s. Reduce support costs by 80%. Start free trial today.',
    keywords: 'AI customer support, RAG chatbot, automated customer service, AI support platform, customer support automation, AI chatbot, intelligent customer service'
  },
  'feature-ai-rag': {
    title: 'AI-Powered RAG Technology | Pluto Customer Support',
    description: 'Advanced Retrieval-Augmented Generation for 95% accurate customer support responses. Learn how Pluto\'s RAG technology transforms support.',
    keywords: 'RAG technology, retrieval augmented generation, AI accuracy, customer support AI'
  },
  'feature-knowledge-base': {
    title: 'Smart Knowledge Base | AI-Powered Documentation | Pluto',
    description: 'Upload documents, PDFs, and websites. Pluto\'s AI automatically organizes and indexes content for instant retrieval. 10x faster setup.',
    keywords: 'knowledge base, AI documentation, document indexing, smart knowledge management'
  },
  'feature-instant-responses': {
    title: 'Instant AI Responses <0.5s | Real-Time Customer Support | Pluto',
    description: 'Sub-second response times with 95% accuracy. Deliver instant, relevant answers to customers 24/7 with Pluto\'s AI support.',
    keywords: 'instant responses, real-time support, fast customer service, AI response time'
  },
  'feature-enterprise-security': {
    title: 'Enterprise Security | SOC2 & GDPR Compliant | Pluto',
    description: 'Bank-level encryption, SOC2 compliance, and GDPR ready. Your customer data stays secure and private with Pluto.',
    keywords: 'enterprise security, SOC2 compliance, GDPR, data security, secure AI'
  },
  'feature-analytics': {
    title: 'Advanced Analytics & Insights | Customer Support Metrics | Pluto',
    description: 'Real-time insights into customer satisfaction, response accuracy, and support performance. 360° visibility into your support operations.',
    keywords: 'support analytics, customer insights, performance metrics, AI analytics'
  },
  'feature-easy-integration': {
    title: 'Easy Integration | 5-Minute Setup | Pluto AI Support',
    description: 'Deploy in minutes with simple widget or robust API. Integrate Pluto with your existing tools. 5-minute setup guaranteed.',
    keywords: 'easy integration, API integration, widget setup, quick deployment'
  }
}
