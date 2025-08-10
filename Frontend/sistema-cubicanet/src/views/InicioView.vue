
<template>
  <div class="view-box">
    <h1 class="titulo">Lista de empleados</h1>
    <div class="busqueda-bar">
      <input v-model="busquedaId" type="number" min="1" placeholder="Buscar por ID" class="input-busqueda" @keyup.enter="buscarEmpleado" />
      <button class="btn-buscar" @click="buscarEmpleado">Buscar</button>
      <button v-if="busquedaId" class="btn-limpiar" @click="limpiarBusqueda">Limpiar</button>
    </div>
    <button class="btn-add" @click="mostrarModal = true">Añadir</button>
    <EmpleadoTabla :empleados="empleados" @eliminar="eliminarEmpleado" @editar="abrirEditar" />

    <div v-if="mostrarModal" class="modal-bg">
      <div class="modal">
        <h2>{{ editando ? 'Editar empleado' : 'Añadir empleado' }}</h2>
        <form @submit.prevent="editando ? actualizarEmpleado() : registrarEmpleado()">
          <input v-model="nuevoEmpleado.nombre" type="text" placeholder="Nombre" required class="input" />
          <input v-model="nuevoEmpleado.rut" type="text" placeholder="RUT" required class="input" />
          <input v-model="nuevoEmpleado.correo_trabajador" type="email" placeholder="Correo" class="input" />
          <input v-model="nuevoEmpleado.fecha_nacimiento" type="date" required class="input" />
          <select v-model.number="nuevoEmpleado.estado_civil_id" required class="input">
            <option disabled value="">Selecciona estado civil</option>
            <option v-for="(nombre, id) in estadoCivilMap" :key="id" :value="Number(id)">{{ nombre }}</option>
          </select>
          <div class="modal-actions">
            <button type="submit" class="btn-guardar">{{ editando ? 'Actualizar' : 'Guardar' }}</button>
            <button type="button" class="btn-cancelar" @click="cerrarModal">Cancelar</button>
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
const busquedaId = ref('')
const buscarEmpleado = async () => {
  if (!busquedaId.value) return
  try {
    const res = await axios.get(getApiUrl().replace('/empleados', `/empleados/${busquedaId.value}`))
    empleados.value = [res.data]
  } catch (error) {
    alert('Empleado no encontrado')
    empleados.value = []
  }
}

const limpiarBusqueda = async () => {
  busquedaId.value = ''
  await obtenerEmpleados()
}
import { ref, onMounted } from 'vue'
import axios from 'axios'
import EmpleadoTabla from '@/components/EmpleadoTabla.vue'

const empleados = ref([])
const mostrarModal = ref(false)
const editando = ref(false)
let idEditando = null

const estadoCivilMap = {
  1: 'Soltero',
  2: 'Casado',
  3: 'Divorciado',
  4: 'Viudo',
  5: 'Conviviente',
}

const nuevoEmpleado = ref({
  nombre: '',
  rut: '',
  correo_trabajador: '',
  fecha_nacimiento: '',
  estado_civil_id: ''
})

function getApiUrl() {
  if (window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1') {
    return `http://${window.location.hostname}:8000/empleados`;
  } else {
    return '/api/empleados';
  }
}

const obtenerEmpleados = async () => {
  const res = await axios.get(getApiUrl())
  empleados.value = res.data
}

const eliminarEmpleado = async (id) => {
  if (!confirm('¿Seguro que quieres eliminar este empleado?')) return
  await axios.delete(getApiUrl().replace('/empleados', `/empleados/${id}`))
  await obtenerEmpleados()
}

function cerrarModal() {
  mostrarModal.value = false
  editando.value = false
  idEditando = null
  nuevoEmpleado.value = { nombre: '', rut: '', correo_trabajador: '', fecha_nacimiento: '', estado_civil_id: 1 }
}
function abrirEditar(empleado) {
  editando.value = true
  idEditando = empleado.id
  nuevoEmpleado.value = {
    nombre: empleado.nombre,
    rut: empleado.rut,
    correo_trabajador: empleado.correo_trabajador,
    fecha_nacimiento: empleado.fecha_nacimiento,
    estado_civil_id: empleado.estado_civil_id
  }
  mostrarModal.value = true
}
const actualizarEmpleado = async () => {
  try {
    await axios.put(getApiUrl().replace('/empleados', `/empleados/${idEditando}`), {
      ...nuevoEmpleado.value,
      estado_civil_id: Number(nuevoEmpleado.value.estado_civil_id)
    })
    await obtenerEmpleados()
    cerrarModal()
  } catch (error) {
    alert('Error al actualizar: ' + (error.response?.data?.detail || error.message))
  }
}

const registrarEmpleado = async () => {
  try {
    await axios.post(getApiUrl(), { ...nuevoEmpleado.value, estado_civil_id: Number(nuevoEmpleado.value.estado_civil_id) })
    await obtenerEmpleados()
    cerrarModal()
  } catch (error) {
    alert('Error al registrar: ' + (error.response?.data?.detail || error.message))
  }
}

onMounted(() => obtenerEmpleados())
</script>

<style scoped>
/* Barra de búsqueda */
.busqueda-bar {
  display: flex;
  align-items: center;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}
.input-busqueda {
  border: 1px solid #bbb;
  border-radius: 4px;
  padding: 0.4rem 0.8rem;
  font-size: 1rem;
  width: 180px;
}
.btn-buscar {
  background: #2563eb;
  color: #fff;
  border: none;
  padding: 0.4rem 1rem;
  border-radius: 4px;
  font-weight: 500;
  cursor: pointer;
}
.btn-buscar:hover {
  background: #1d4ed8;
}
.btn-limpiar {
  background: #eab308;
  color: #222;
  border: none;
  padding: 0.4rem 1rem;
  border-radius: 4px;
  font-weight: 500;
  cursor: pointer;
}
.btn-limpiar:hover {
  background: #facc15;
}
/* Estilos originales */
.view-box {
  max-width: 2000px;
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
/* Botón añadir */
.btn-add {
  background: #2563eb;
  color: #fff;
  border: none;
  padding: 0.5rem 1.2rem;
  border-radius: 4px;
  font-weight: 500;
  margin-bottom: 1.5rem;
  cursor: pointer;
  transition: background 0.2s;
}
.btn-add:hover {
  background: #1d4ed8;
}
/* Modal */
.modal-bg {
  position: fixed;
  top: 0; left: 0; right: 0; bottom: 0;
  background: rgba(0,0,0,0.3);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}
.modal {
  background: #fff;
  padding: 2rem;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.13);
  min-width: 320px;
  max-width: 95vw;
}
.input {
  width: 100%;
  border: 1px solid #bbb;
  border-radius: 4px;
  padding: 0.5rem;
  margin-bottom: 1rem;
  font-size: 1rem;
}
.modal-actions {
  display: flex;
  gap: 1rem;
  justify-content: flex-end;
}
.btn-guardar {
  background: #22c55e;
  color: #fff;
  border: none;
  padding: 0.5rem 1.2rem;
  border-radius: 4px;
  font-weight: 500;
  cursor: pointer;
}
.btn-guardar:hover {
  background: #16a34a;
}
.btn-cancelar {
  background: #ef4444;
  color: #fff;
  border: none;
  padding: 0.5rem 1.2rem;
  border-radius: 4px;
  font-weight: 500;
  cursor: pointer;
}
.btn-cancelar:hover {
  background: #b91c1c;
}
</style>
