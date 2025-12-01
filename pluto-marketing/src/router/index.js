import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import FeatureDetail from '../views/FeatureDetail.vue'
import StepDetail from '../views/StepDetail.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/feature/:id',
    name: 'FeatureDetail',
    component: FeatureDetail
  },
  {
    path: '/step/:id',
    name: 'StepDetail',
    component: StepDetail
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
