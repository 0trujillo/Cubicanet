<template>
  <div class="tabla-tarja-wrapper">
    <table class="tabla-tarja">
      <thead>
        <tr>
          <th>Nombre</th>
          <th>RUT</th>
          <th>Entrada</th>
          <th>Salida</th>
          <th>Fecha</th>
          <th>Faltas del mes</th>
          <th>Asistencias del mes</th>
          <th>Acciones</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="registro in registros" :key="registro.id">
          <td>{{ registro.nombre }}</td>
          <td>
            <input v-model="registro.rut" />
          </td>
          <td>
            <input v-model="registro.entrada" />
          </td>
          <td>
            <input v-model="registro.salida" />
          </td>
          <td>
            <input v-model="registro.fecha" />
          </td>
          <td>
            <input v-model="registro.faltas_mes" type="number" min="0" />
          </td>
          <td>
            <input v-model="registro.asistencias_mes" type="number" min="0" />
          </td>
          <td>
            <button class="btn-edit" @click="$emit('editar', registro)">Guardar</button>
          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { defineProps } from 'vue'
defineProps({
  registros: {
    type: Array,
    required: true
  }
})
</script>

<style scoped>
.btn-edit {
  background: #facc15;
  color: #333;
  border: none;
  padding: 0.3rem 0.8rem;
  border-radius: 4px;
  margin-right: 0.5rem;
  cursor: pointer;
}
.btn-edit:hover {
  background: #eab308;
}
/* Wrapper para hacer la tabla responsiva y centrada */
.tabla-tarja-wrapper {
  width: 100%;
  overflow-x: auto;
  margin: 0 auto;
}
.tabla-tarja {
  min-width: 900px;
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1.5rem;
  background: #fff;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
}
.tabla-tarja th, .tabla-tarja td {
  border: 1px solid #ccc;
  padding: 0.6rem 0.8rem;
  text-align: left;
}
.tabla-tarja th {
  background: #f3f3f3;
  font-weight: bold;
}
</style>
