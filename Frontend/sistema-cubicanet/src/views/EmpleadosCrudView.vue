

<template>
  <div class="view-box">
    <h1 class="titulo">CRUD de Empleados</h1>
    <section>
      <h2 class="subtitulo">Agregar Empleado</h2>
      <!-- Mostrar el formulario siempre, sin lógica -->
      <EmpleadoForm />
      <div class="edit-section" style="margin-top:2rem;">
        <h2 class="subtitulo">Editar Empleado (demo)</h2>
        <EmpleadoForm :empleado="{nombre:'Ejemplo',rut:'1-9',correo_trabajador:'ejemplo@mail.com',fecha_nacimiento:'2000-01-01',estado_civil_id:1}" />
        <button class="btn-cancelar" disabled>Cancelar</button>
      </div>
    </section>
    <section>
      <h2 class="subtitulo">Lista de Empleados</h2>
      <!-- Tabla con datos de ejemplo y botones -->
      <EmpleadoTabla :empleados="empleadosDemo" />
    </section>
  </div>
</template>

onMounted(async () => {
<script setup>
import EmpleadoTabla from '@/components/EmpleadoTabla.vue'
import EmpleadoForm from '@/components/EmpleadoForm.vue'

// Datos de ejemplo para mostrar la UI
const empleadosDemo = [
  { id: 1, nombre: 'Juan Pérez', rut: '11.111.111-1', correo_trabajador: 'juan@mail.com' },
  { id: 2, nombre: 'Ana Gómez', rut: '22.222.222-2', correo_trabajador: 'ana@mail.com' },
];
</script>

<style scoped>
.view-box {
  max-width: 700px;
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
.subtitulo {
  font-size: 1.2rem;
  font-weight: 600;
  margin: 1.2rem 0 0.7rem 0;
}
.edit-section {
  background: #f3f3f3;
  padding: 1rem;
  border-radius: 6px;
  margin-bottom: 1.5rem;
}
.btn-cancelar {
  background: #ef4444;
  color: #fff;
  border: none;
  padding: 0.4rem 1rem;
  border-radius: 4px;
  margin-top: 0.7rem;
  cursor: pointer;
}
.btn-cancelar:hover {
  background: #b91c1c;
}
</style>
