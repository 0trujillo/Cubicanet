import { createRouter, createWebHistory } from 'vue-router'

import InicioView from '@/views/InicioView.vue'
import TarjaView from '@/views/TarjaView.vue'

const routes = [
  { path: '/', name: 'Inicio', component: InicioView },
  { path: '/tarja', name: 'Tarja', component: TarjaView },
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
