import { createRouter, createWebHistory } from 'vue-router'
import ShoppingCart from '../components/ShoppingCart'

const routes = [
  {
    path: '/',
    name: 'ShoppingCart',
    component: ShoppingCart
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
