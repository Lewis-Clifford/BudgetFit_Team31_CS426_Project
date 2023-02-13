import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import About from '../views/AboutView.vue'
import Diet from '../views/DietView.vue'
import Shop from '../views/ShopView.vue'
import Exercise from '../views/ExerciseView.vue'
import Login from '../views/LoginView.vue'
import Signup from '../views/SignupView.vue'
import Exercise1View from '../views/Exercise1View.vue'


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
    component: Shop
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
    path: '/signup',
    name: 'signup',
    component: Signup
  },
  {
    path: '/exercise/exercise1',
    name: 'exercise1',
    component: Exercise1View

  }

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
