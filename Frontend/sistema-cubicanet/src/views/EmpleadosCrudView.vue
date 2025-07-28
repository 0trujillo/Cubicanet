<template>
  <div class="p-4 max-w-xl mx-auto">
    <h1 class="text-2xl font-bold mb-4">CRUD de Empleados</h1>
    <EmpleadoForm @agregar="agregarEmpleado" />
    <EmpleadoTabla :empleados="empleados" @editar="editarEmpleado" @eliminar="eliminarEmpleado" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { obtenerEmpleados, crearEmpleado } from '@/api/empleados'
import EmpleadoTabla from '@/components/EmpleadoTabla.vue'
import EmpleadoForm from '@/components/EmpleadoForm.vue'

const empleados = ref([])

onMounted(async () => {
  const res = await obtenerEmpleados()
  empleados.value = res.data
})

function agregarEmpleado(nuevoEmpleado) {
  crearEmpleado(nuevoEmpleado).then(() => {
    // Recargar empleados
    obtenerEmpleados().then(res => empleados.value = res.data)
  })
}

function editarEmpleado(empleado) {
  // Implementar lógica de edición
}

function eliminarEmpleado(id) {
  // Implementar lógica de eliminación
}
</script>
