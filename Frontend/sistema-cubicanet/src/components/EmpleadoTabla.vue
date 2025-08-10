<template>
  <table class="tabla-empleados">
    <thead>
      <tr>
        <th>ID</th>
        <th>Nombre</th>
        <th>RUT</th>
        <th>Correo</th>
        <th>Fecha Nacimiento</th>
        <th>Estado Civil</th>
        <th>Acciones</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="empleado in empleados" :key="empleado.id">
        <td>{{ empleado.id }}</td>
        <td>{{ empleado.nombre }}</td>
        <td>{{ empleado.rut }}</td>
        <td>{{ empleado.correo_trabajador }}</td>
        <td>{{ empleado.fecha_nacimiento }}</td>
        <td>{{ estadoCivilNombre(empleado.estado_civil_id) }}</td>
        <td>
          <button class="btn-edit" @click="$emit('editar', empleado)">Editar</button>
          <button class="btn-delete" @click="$emit('eliminar', empleado.id)">Eliminar</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
import { defineProps, defineEmits } from 'vue'
const estadoCivilMap = {
  1: 'Soltero',
  2: 'Casado',
  3: 'Divorciado',
  4: 'Viudo',
  5: 'Conviviente',
}
function estadoCivilNombre(id) {
  return estadoCivilMap[id] || id
}
defineProps({
  empleados: {
    type: Array,
    required: true,
  },
})
defineEmits(['editar', 'eliminar'])
</script>

<style scoped>
/* Estilo más cuadrado y formal */
.tabla-empleados {
  width: 100%;
  border-collapse: separate;
  border-spacing: 0;
  margin-bottom: 1.5rem;
  background: #f8f9fa;
  box-shadow: 0 2px 8px rgba(0,0,0,0.04);
  border: 1px solid #b0b0b0;
  font-family: 'Segoe UI', Arial, sans-serif;
}
.tabla-empleados th, .tabla-empleados td {
  border: 1px solid #b0b0b0;
  padding: 0.5rem 0.7rem;
  text-align: center;
  vertical-align: middle;
}
.tabla-empleados th {
  background: #e9ecef;
  font-weight: 600;
  color: #222;
  letter-spacing: 0.5px;
}
.tabla-empleados tr:nth-child(even) td {
  background: #f4f6f8;
}
.tabla-empleados tr:hover td {
  background: #e2e6ea;
}
.btn-edit {
  background: #facc15;
  color: #333;
  border: none;
  padding: 0.3rem 0.8rem;
  border-radius: 4px;
  margin-right: 0.5rem;
  cursor: pointer;
}
.btn-delete {
  background: #ef4444;
  color: #fff;
  border: none;
  padding: 0.3rem 0.8rem;
  border-radius: 4px;
  cursor: pointer;
}
.btn-edit:hover {
  background: #eab308;
}
.btn-delete:hover {
  background: #b91c1c;
}
</style>

