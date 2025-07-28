<template>
  <div class="max-w-2xl mx-auto p-4">
    <h1 class="text-2xl font-bold mb-4">Registrar nuevo empleado</h1>
    <form @submit.prevent="registrarEmpleado">
      <input v-model="form.nombre" type="text" placeholder="Nombre" class="input" required />
      <input v-model="form.rut" type="text" placeholder="RUT" class="input" required />
      <input v-model="form.correo_trabajador" type="email" placeholder="Correo" class="input" />
      <input v-model="form.fecha_nacimiento" type="date" class="input" required />
      <select v-model="form.estado_civil_id" class="input">
        <option disabled value="">Estado civil</option>
        <option v-for="estado in estadosCiviles" :key="estado.id" :value="estado.id">{{ estado.nombre }}</option>
      </select>
      <button type="submit" class="bg-blue-500 text-white px-4 py-2 rounded mt-4">Registrar</button>
    </form>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

const form = ref({
  nombre: '',
  rut: '',
  correo_trabajador: '',
  fecha_nacimiento: '',
  estado_civil_id: ''
})

const estadosCiviles = ref([])

const obtenerEstadosCiviles = async () => {
  const res = await axios.get('http://localhost:8000/estados_civil')
  estadosCiviles.value = res.data
}

const registrarEmpleado = async () => {
  try {
    await axios.post('http://localhost:8000/empleados', form.value)
    alert('Empleado registrado')
  } catch (error) {
    console.error(error)
    alert('Error al registrar')
  }
}

onMounted(() => {
  obtenerEstadosCiviles()
})
</script>

<style scoped>
.input {
  @apply w-full border p-2 mb-2 rounded;
}
</style>
