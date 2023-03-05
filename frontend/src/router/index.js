import { createRouter, createWebHashHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'
import About from '../views/AboutView.vue'
import Diet from '../views/DietView.vue'
import ShopView from '../views/ShopView.vue'
import Exercise from '../views/ExerciseView.vue'
import Login from '../views/LoginView.vue'
import Signup from '../views/SignupView.vue'
import Exercise1View from '../views/Exercise1View.vue'
import EditView from '../views/EditProfileView.vue'
import ViewShopView from '../views/ViewShopView'
import CartView from '../views/CartView'
import FinalListView from '../views/FinalListView'



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
    path: '/signup',
    name: 'signup',
    component: Signup
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
  }
     

]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
