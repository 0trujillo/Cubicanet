import axios from 'axios';


// Detecta entorno automáticamente
let API_URL = '';
if (process.env.VUE_APP_API_URL) {
  API_URL = process.env.VUE_APP_API_URL;
} else if (
  window.location.hostname === 'localhost' ||
  window.location.hostname === '127.0.0.1'
 ) {
  API_URL = 'http://localhost:8000';
} else {
  API_URL = 'http://backend:8000';
}

export function crearEmpleado(empleado) {
  return axios.post(`${API_URL}/empleados`, empleado);
}

export function obtenerEmpleados() {
  return axios.get(`${API_URL}/empleados`);
}


// Puedes agregar más funciones para editar/eliminar empleados según tu backend
