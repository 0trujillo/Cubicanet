<template>
  <div class="view-box">
    <h1 class="titulo">Lista de empleados</h1>
    <EmpleadoTabla :empleados="empleados" @eliminar="eliminarEmpleado" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'
import EmpleadoTabla from '@/components/EmpleadoTabla.vue'

const empleados = ref([])

const obtenerEmpleados = async () => {
  const res = await axios.get('http://localhost:8000/empleados')
  empleados.value = res.data
}

const eliminarEmpleado = async (id) => {
  if (!confirm('¿Seguro que quieres eliminar este empleado?')) return
  await axios.delete(`http://localhost:8000/empleados/${id}`)
  await obtenerEmpleados()
}

onMounted(() => obtenerEmpleados())
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
