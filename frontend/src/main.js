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
faMinus, faCheck, faTrash, faCircleCheck, faPenToSquare, faFilePdf  } from '@fortawesome/free-solid-svg-icons'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import 'hover.css/css/hover-min.css';


library.add(faArrowLeft, faArrowRight, faMagnifyingGlass, faShoppingCart, faPlus, faArrowUp,
    faMinus, faCheck, faTrash, faCircleCheck, faPenToSquare, faFilePdf)





createApp(App).use(router).use(createPopper).use(library).use(plugin, defaultConfig({
    plugins: [
        createAutoAnimatePlugin({
            useAsDefault: true
        }),
        createFloatingLabelsPlugin({
            useAsDefault: true
        })
    ]
})).component('font-awesome-icon', FontAwesomeIcon).mount('#app')
