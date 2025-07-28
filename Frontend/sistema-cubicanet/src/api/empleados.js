import axios from 'axios';

// Usa 'http://backend:8000' si usas Docker Compose, 'http://localhost:8000' si corres local
const API_URL = process.env.VUE_APP_API_URL || 'http://backend:8000';

export function crearEmpleado(empleado) {
  return axios.post(`${API_URL}/empleados`, empleado);
}

export function obtenerEmpleados() {
  return axios.get(`${API_URL}/empleados`);
}

// Puedes agregar más funciones para editar/eliminar empleados según tu backend
