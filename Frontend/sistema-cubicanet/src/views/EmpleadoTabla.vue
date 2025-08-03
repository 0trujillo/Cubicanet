<template>
  <table class="w-full table-auto border border-gray-300">
    <thead>
      <tr class="bg-gray-100">
        <th class="p-2">ID</th>
        <th class="p-2">Nombre</th>
        <th class="p-2">RUT</th>
        <th class="p-2">Correo</th>
        <th class="p-2">Banco</th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="empleado in empleados" :key="empleado.id" class="border-t">
        <td class="p-2">{{ empleado.id }}</td>
        <td class="p-2">{{ empleado.nombre }}</td>
        <td class="p-2">{{ empleado.rut }}</td>
        <td class="p-2">{{ empleado.correo_trabajador }}</td>
        <td class="p-2">{{ empleado.correo_trabajador }}</td>

        <td class="p-2 flex gap-2">
          <button class="bg-yellow-400 px-2 py-1 rounded" @click="$emit('editar', empleado)">Editar</button>
          <button class="bg-red-500 text-white px-2 py-1 rounded" @click="$emit('eliminar', empleado.id)">Eliminar</button>
        </td>
      </tr>
    </tbody>
  </table>
</template>

<script setup>
defineProps(['empleados'])
defineEmits(['editar', 'eliminar'])
</script>
