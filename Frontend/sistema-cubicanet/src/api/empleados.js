import axios from 'axios';


// Detecta entorno automáticamente
// Usar el proxy /api configurado en nginx para acceder al backend
const API_URL = '/api';


export function crearEmpleado(empleado) {
  return axios.post(`${API_URL}/empleado`, empleado);
}

export function obtenerEmpleados() {
  return axios.get(`${API_URL}/empleado`);
}



// Actualizar empleado (PUT o PATCH según tu backend)
export function actualizarEmpleado(empleado) {
  // Suponiendo que el backend espera el id en la URL
  return axios.put(`${API_URL}/empleado/${empleado.id}`, empleado);
}

// Eliminar empleado
export function eliminarEmpleado(id) {
  return axios.delete(`${API_URL}/empleado/${id}`);
}
