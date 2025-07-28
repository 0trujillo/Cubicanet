<template>
  <form class="mb-4 p-4 border rounded bg-white shadow" @submit.prevent="onSubmit">
    <div class="mb-2">
      <label class="block text-sm font-medium">RUT</label>
      <input v-model="form.rut" class="border p-2 w-full rounded" required />
    </div>
    <button class="bg-green-500 text-white px-4 py-2 rounded" type="submit">Marcar Entrada/Salida</button>
  </form>
</template>

<script setup>
import { ref } from 'vue'
const form = ref({ rut: '' })

function onSubmit() {
  // Aquí deberías llamar a la API para marcar entrada/salida
  alert(`Marcado para RUT: ${form.value.rut}`)
  form.value = { rut: '' }
}
</script>
