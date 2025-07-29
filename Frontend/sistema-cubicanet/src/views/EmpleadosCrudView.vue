
<template>
  <div class="view-box">
    <h1 class="titulo">CRUD de Empleados</h1>
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
