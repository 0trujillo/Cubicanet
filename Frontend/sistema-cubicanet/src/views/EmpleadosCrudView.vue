

<template>
  <div class="view-box">
    <h1 class="titulo">CRUD de Empleados</h1>
    <section>
      <h2 class="subtitulo">Agregar Empleado</h2>
      <EmpleadoForm v-if="!editando" @agregar="agregarEmpleado" />
      <div v-if="editando" class="edit-section">
        <h2 class="subtitulo">Editar Empleado</h2>
        <EmpleadoForm :empleado="empleadoEdit" @agregar="actualizarEmpleado" />
        <button class="btn-cancelar" @click="cancelarEdicion">Cancelar</button>
      </div>
    </section>
    <section>
      <h2 class="subtitulo">Lista de Empleados</h2>
      <EmpleadoTabla :empleados="empleados" @editar="editarEmpleado" @eliminar="eliminarEmpleado" />
    </section>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { obtenerEmpleados, crearEmpleado, actualizarEmpleado as apiActualizarEmpleado, eliminarEmpleado as apiEliminarEmpleado } from '@/api/empleados'
import EmpleadoTabla from '@/components/EmpleadoTabla.vue'
import EmpleadoForm from '@/components/EmpleadoForm.vue'


const empleados = ref([])
const editando = ref(false)
const empleadoEdit = ref(null)

onMounted(async () => {
  const res = await obtenerEmpleados()
  empleados.value = res.data
})


function agregarEmpleado(nuevoEmpleado) {
  crearEmpleado(nuevoEmpleado).then(() => {
    obtenerEmpleados().then(res => empleados.value = res.data)
  })
}

function editarEmpleado(empleado) {
  editando.value = true
  empleadoEdit.value = { ...empleado }
}

function actualizarEmpleado(empleadoActualizado) {
  apiActualizarEmpleado(empleadoActualizado).then(() => {
    obtenerEmpleados().then(res => empleados.value = res.data)
    editando.value = false
    empleadoEdit.value = null
  })
}

function cancelarEdicion() {
  editando.value = false
  empleadoEdit.value = null
}

function eliminarEmpleado(id) {
  if (confirm('¿Seguro que deseas eliminar este empleado?')) {
    apiEliminarEmpleado(id).then(() => {
      obtenerEmpleados().then(res => empleados.value = res.data)
    })
  }
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
.subtitulo {
  font-size: 1.2rem;
  font-weight: 600;
  margin: 1.2rem 0 0.7rem 0;
}
.edit-section {
  background: #f3f3f3;
  padding: 1rem;
  border-radius: 6px;
  margin-bottom: 1.5rem;
}
.btn-cancelar {
  background: #ef4444;
  color: #fff;
  border: none;
  padding: 0.4rem 1rem;
  border-radius: 4px;
  margin-top: 0.7rem;
  cursor: pointer;
}
.btn-cancelar:hover {
  background: #b91c1c;
}
</style>
