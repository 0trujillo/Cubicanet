<template>
  <form class="form-box" @submit.prevent="onSubmit">
    <div class="form-group">
      <label>Nombre</label>
      <input v-model="form.nombre" required />
    </div>
    <div class="form-group">
      <label>RUT</label>
      <input v-model="form.rut" required />
    </div>
    <div class="form-group">
      <label>Correo</label>
      <input v-model="form.correo_trabajador" type="email" />
    </div>
    <div class="form-group">
      <label>Fecha de nacimiento</label>
      <input v-model="form.fecha_nacimiento" type="date" required />
    </div>
    <div class="form-group">
      <label>Estado civil (ID)</label>
      <input v-model.number="form.estado_civil_id" type="number" min="1" required />
    </div>
    <button class="btn-primary" type="submit">Agregar</button>
  </form>
</template>

<script setup>
import { ref } from 'vue'
const emit = defineEmits(['agregar'])
const form = ref({
  nombre: '',
  rut: '',
  correo_trabajador: '',
  fecha_nacimiento: '',
  estado_civil_id: 1
})

function onSubmit() {
  // Formatear fecha_nacimiento a YYYY-MM-DD si es necesario
  emit('agregar', { ...form.value })
  form.value = {
    nombre: '',
    rut: '',
    correo_trabajador: '',
    fecha_nacimiento: '',
    estado_civil_id: 1
  }
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
  background: #2563eb;
  color: #fff;
  border: none;
  padding: 0.6rem 1.2rem;
  border-radius: 4px;
  font-weight: bold;
  cursor: pointer;
  transition: background 0.2s;
}
.btn-primary:hover {
  background: #1d4ed8;
}
</style>
