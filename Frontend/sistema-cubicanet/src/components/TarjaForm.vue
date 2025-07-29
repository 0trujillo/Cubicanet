<template>
  <form class="form-box" @submit.prevent="onSubmit">
    <div class="form-group">
      <label>RUT</label>
      <input v-model="form.rut" required />
    </div>
    <button class="btn-primary" type="submit">Marcar Entrada/Salida</button>
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

<style scoped>
.form-box {
  max-width: 400px;
  margin: 0 auto 1.5rem auto;
  padding: 1.5rem;
  border: 1px solid #ccc;
  border-radius: 8px;
  background: #fff;
  box-shadow: 0 2px 8px rgba(0,0,0,0.07);
}
.form-group {
  margin-bottom: 1rem;
  display: flex;
  flex-direction: column;
}
.form-group label {
  font-weight: 500;
  margin-bottom: 0.3rem;
}
.form-group input {
  padding: 0.5rem;
  border: 1px solid #bbb;
  border-radius: 4px;
  font-size: 1rem;
}
.btn-primary {
  background: #22c55e;
  color: #fff;
  border: none;
  padding: 0.6rem 1.2rem;
  border-radius: 4px;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.2s;
}
.btn-primary:hover {
  background: #16a34a;
}
</style>
