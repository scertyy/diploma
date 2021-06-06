import { createApp } from 'vue'
import app from './app/app.vue'
import router from './router'
import store from './store'


createApp(app).use(store).use(router).mount('#app')

let vh = window.innerHeight * 0.01;
document.documentElement.style.setProperty('--vh', `${vh}px`);