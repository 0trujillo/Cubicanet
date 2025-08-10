<template>
  <div class="view-box">
    <h1 class="titulo">Vista General de Empleados</h1>
    <button class="btn-actualizar" @click="actualizarEmpleados">Actualizar</button>
    <EmpleadoTabla :empleados="empleados" />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { obtenerEmpleados } from '@/api/empleados'
import EmpleadoTabla from '@/components/EmpleadoTabla.vue'

const empleados = ref([])

async function actualizarEmpleados() {
  const res = await obtenerEmpleados()
  empleados.value = res.data
}

onMounted(() => {
  actualizarEmpleados()
})
</script>

<style scoped>
.view-box {
  max-width: 700px;
  max-width: 2000px;
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
.btn-actualizar {
  background: #2d3748;
  color: #fff;
  border: none;
  padding: 0.5rem 1.2rem;
  border-radius: 4px;
  font-weight: 500;
  margin-bottom: 1.5rem;
  cursor: pointer;
  transition: background 0.2s;
}
.btn-actualizar:hover {
  background: #1a202c;
}
</style>
