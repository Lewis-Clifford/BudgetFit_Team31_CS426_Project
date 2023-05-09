// Author: Kaden Nesch
// This page allows me to set the routes for each page as well as enable history so users can use the back arrow to go back to previous pages

import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import About from '../views/AboutView.vue'
import Diet from '../views/DietView.vue'
import ShopView from '../views/ShopView.vue'
import Exercise from '../views/ExerciseView.vue'
import Login from '../views/LoginView.vue'
import Register from '../views/RegisterView.vue'
import Exercise1View from '../views/Exercise1View.vue'
import EditView from '../views/EditProfileView.vue'
import ViewShopView from '../views/ViewShopView'
import CartView from '../views/CartView'
import FinalListView from '../views/FinalListView'
import StatsView from '../views/StatsView'


const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    component: About
  },
  {
    path: '/diet',
    name: 'diet',
    component: Diet
  },
  {
    path: '/shop',
    name: 'shop',
    component: ShopView,
    props: true
  },
  {
    path: '/exercise',
    name: 'exercise',
    component: Exercise
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  },
  {
    path: '/exercise1',
    name: 'exercise1',
    component: Exercise1View

  },
  {
    path: '/edit',
    name: 'edit',
    component: EditView,
    props: true
    },
  
  {
    path: '/viewshop',
    name: 'viewshop',
    component: ViewShopView,
    props: true
  },

  {
    path: '/cart',
    name: 'cart',
    component: CartView,
    props: true
  },

  {
    path: '/finallist',
    name: 'finallist',
    component: FinalListView,
    props: true
  },

  {
    path: '/stats',
    name: 'stats',
    component: StatsView,
    props: true
  }
     

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
