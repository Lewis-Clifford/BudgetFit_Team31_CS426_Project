import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { plugin, defaultConfig } from '@formkit/vue'
import '@formkit/themes/genesis' 
import { createAutoAnimatePlugin, createFloatingLabelsPlugin } from '@formkit/addons'
import '@formkit/addons/css/floatingLabels'
// Import Bootstrap and BootstrapVue CSS files (order is important)
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'
import { createPopper } from '@popperjs/core'
import { library } from '@fortawesome/fontawesome-svg-core'
import { faArrowLeft, faArrowRight, faMagnifyingGlass, faShoppingCart, faPlus, faArrowUp,
faMinus, faCheck, faTrash, faCircleCheck, faPenToSquare, faFilePdf, faX,
faHeart, faStar, faBookmark  } from '@fortawesome/free-solid-svg-icons'
import { faHeart as farHeart } from '@fortawesome/free-regular-svg-icons'
import { faStar as farStar } from '@fortawesome/free-regular-svg-icons'
import { faBookmark as farBookmark } from '@fortawesome/free-regular-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import 'hover.css/css/hover-min.css';
import store from './store'


library.add(faArrowLeft, faArrowRight, faMagnifyingGlass, faShoppingCart, faPlus, faArrowUp,
    faMinus, faCheck, faTrash, faCircleCheck, faPenToSquare, faFilePdf, faX, faHeart, farHeart, 
    farStar, faStar, farBookmark, faBookmark)

    const app = createApp(App);
const root = document.documentElement;

// Set the initial zoom level based on the screen size
if (window.screen.width <= 1920) {
  root.style.zoom = "0.70";
}


app.use(store).use(router).use(createPopper).use(library).use(plugin, defaultConfig({
    plugins: [
        createAutoAnimatePlugin({
            useAsDefault: true
        }),
        createFloatingLabelsPlugin({
            useAsDefault: true
        })
    ]
})).component('font-awesome-icon', FontAwesomeIcon).mount('#app')
