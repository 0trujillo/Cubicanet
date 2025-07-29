<template>
  <table class="tabla-empleados">
    <thead>
      <tr>
        <th>ID</th>
        <th>Nombre</th>
        <th>RUT</th>
        <th>Correo</th>
        <th>Acciones</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="empleado in empleados" :key="empleado.id">
        <td>{{ empleado.id }}</td>
        <td>{{ empleado.nombre }}</td>
        <td>{{ empleado.rut }}</td>
        <td>{{ empleado.correo_trabajador }}</td>
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
defineProps({
  empleados: {
    type: Array,
    required: true,
  },
})

defineEmits(['editar', 'eliminar'])
</script>

<style scoped>
.tabla-empleados {
  width: 100%;
  border-collapse: collapse;
  margin-bottom: 1.5rem;
  background: #fff;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
}
.tabla-empleados th, .tabla-empleados td {
  border: 1px solid #ccc;
  padding: 0.6rem 0.8rem;
  text-align: left;
}
.tabla-empleados th {
  background: #f3f3f3;
  font-weight: bold;
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
