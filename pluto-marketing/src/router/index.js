import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import FeatureDetail from '../views/FeatureDetail.vue'
import StepDetail from '../views/StepDetail.vue'
import Demo from '../views/Demo.vue'
import Signup from '../views/Signup.vue'
import SignupSuccess from '../views/SignupSuccess.vue'
import { updateMetaTags, routeMeta } from '../utils/seo'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home,
    meta: {
      title: 'Pluto - AI-Powered Customer Support with RAG Technology | Reduce Costs 80%',
      description: 'Transform customer support with Pluto\'s AI chatbot using RAG technology. Get 95% accurate responses in <0.5s. Reduce support costs by 80%. Start free trial today.',
      keywords: 'AI customer support, RAG chatbot, automated customer service, AI support platform'
    }
  },
  {
    path: '/demo',
    name: 'Demo',
    component: Demo,
    meta: {
      title: 'Schedule a Demo | Pluto AI Customer Support',
      description: 'Book a personalized demo of Pluto AI customer support platform'
    }
  },
  {
    path: '/signup',
    name: 'Signup',
    component: Signup,
    meta: {
      title: 'Start Free Trial | Pluto AI Customer Support',
      description: 'Start your 14-day free trial. No credit card required.'
    }
  },
  {
    path: '/signup-success',
    name: 'SignupSuccess',
    component: SignupSuccess,
    meta: {
      title: 'Welcome to Pluto | Get Your Widget Code',
      description: 'Your free trial has started. Get your widget code.'
    }
  },
  {
    path: '/feature/:id',
    name: 'FeatureDetail',
    component: FeatureDetail,
    meta: {
      title: 'Feature Details | Pluto AI Customer Support',
      description: 'Explore Pluto\'s advanced AI customer support features'
    }
  },
  {
    path: '/step/:id',
    name: 'StepDetail',
    component: StepDetail,
    meta: {
      title: 'How It Works | Pluto AI Customer Support',
      description: 'Learn how to get started with Pluto AI customer support platform'
    }
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to, from, savedPosition) {
    return savedPosition || { top: 0 }
  }
})

router.afterEach((to) => {
  const metaKey = to.params.id ? `feature-${to.params.id}` : 'home'
  const meta = routeMeta[metaKey] || to.meta
  if (meta) updateMetaTags(meta)
})

export default router
