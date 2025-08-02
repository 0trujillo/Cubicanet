
<template>
  <div class="view-box">
    <h1 class="titulo">Tarja de Empleados</h1>
    <div class="tabla-box">
      <TarjaTabla :registros="registros" />
    </div>
  </div>
</template>

<script setup>
import TarjaTabla from '@/components/TarjaTabla.vue'
import { ref } from 'vue'

// Datos de ejemplo, reemplaza por datos reales de la API si es necesario
const registros = ref([
  { id: 1, nombre: 'Juan Pérez', rut: '28223064-k', entrada: '08:00', salida: '17:00', fecha: '2025-08-01', faltas_mes: 0, asistencias_mes: 20 },
  { id: 2, nombre: 'Ana Gómez', rut: '28223064-k', entrada: '08:10', salida: '17:05', fecha: '2025-08-01', faltas_mes: 1, asistencias_mes: 19 },
])
</script>

<style scoped>
.view-box {
  max-width: 2000px;
  margin: 2rem auto;
  background: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
  padding: 2rem;
}
.tabla-box {
  overflow-x: auto;
  margin-top: 2rem;
}
.titulo {
  font-size: 2rem;
  font-weight: bold;
  margin-bottom: 1.5rem;
}
</style>
