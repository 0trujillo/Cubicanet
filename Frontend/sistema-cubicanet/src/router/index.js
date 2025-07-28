import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import EmpleadosCrudView from '@/views/EmpleadosCrudView.vue'
import TarjaView from '@/views/TarjaView.vue'

const routes = [
  { path: '/', component: HomeView },
  { path: '/empleados', component: EmpleadosCrudView },
  { path: '/tarja', component: TarjaView }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
