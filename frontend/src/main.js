import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import { plugin, defaultConfig } from '@formkit/vue'
import '@formkit/themes/genesis' 
import { createAutoAnimatePlugin, createFloatingLabelsPlugin } from '@formkit/addons'
import '@formkit/addons/css/floatingLabels'


createApp(App).use(router).use(plugin, defaultConfig({
    plugins: [
        createAutoAnimatePlugin({
            useAsDefault: true
        }),
        createFloatingLabelsPlugin({
            useAsDefault: true
        })
    ]
})).mount('#app')
