<template>
  <form class="mb-4 p-4 border rounded bg-white shadow" @submit.prevent="onSubmit">
    <div class="mb-2">
      <label class="block text-sm font-medium">Nombre</label>
      <input v-model="form.nombre" class="border p-2 w-full rounded" required />
    </div>
    <div class="mb-2">
      <label class="block text-sm font-medium">RUT</label>
      <input v-model="form.rut" class="border p-2 w-full rounded" required />
    </div>
    <div class="mb-2">
      <label class="block text-sm font-medium">Correo</label>
      <input v-model="form.correo_trabajador" class="border p-2 w-full rounded" type="email" required />
    </div>
    <button class="bg-blue-500 text-white px-4 py-2 rounded" type="submit">Agregar</button>
  </form>
</template>

<script setup>
import { ref } from 'vue'
const emit = defineEmits(['agregar'])
const form = ref({ nombre: '', rut: '', correo_trabajador: '' })

function onSubmit() {
  emit('agregar', { ...form.value })
  form.value = { nombre: '', rut: '', correo_trabajador: '' }
}
</script>
