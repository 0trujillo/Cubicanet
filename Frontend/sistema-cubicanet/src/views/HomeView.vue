<template>
  <div class="view-box">
    <h1 class="titulo">Vista General de Empleados</h1>
    <EmpleadoTabla :empleados="empleados" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { obtenerEmpleados } from '@/api/empleados'
import EmpleadoTabla from '@/components/EmpleadoTabla.vue'

const empleados = ref([])

onMounted(async () => {
  const res = await obtenerEmpleados()
  empleados.value = res.data
})
</script>

<style scoped>
.view-box {
  max-width: 700px;
  margin: 2rem auto;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
  padding: 2rem;
}
.titulo {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 1.5rem;
}
</style>
