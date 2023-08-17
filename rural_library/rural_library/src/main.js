import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import eventBus from 'vue3-eventbus'
 
const app = createApp(App)
app.use(eventBus)

app.use(router).mount('#app')