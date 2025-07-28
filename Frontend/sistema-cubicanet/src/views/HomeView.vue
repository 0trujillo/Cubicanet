<template>
  <div class="p-4">
    <h1 class="text-2xl font-bold mb-4">Vista General de Empleados</h1>
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
