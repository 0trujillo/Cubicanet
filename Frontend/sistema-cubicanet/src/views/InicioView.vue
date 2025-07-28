<!-- src/views/InicioView.vue -->
<template>
  <div class="p-6">
    <h1 class="text-2xl font-bold mb-4">Lista de empleados</h1>
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
