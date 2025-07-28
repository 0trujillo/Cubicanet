import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from backend.db.connection import SessionLocal
from backend.db.models import Empleado

db = SessionLocal()
nuevo_empleado = Empleado(
    nombre="Juan Pérez",
    rut="12345678-9",
    correo_trabajador="juan.perez@correo.com",
    fecha_nacimiento="1990-01-01",
    estado_civil_id=1  # Debe existir este id en la tabla estados_civil
)
db.add(nuevo_empleado)
db.commit()
db.refresh(nuevo_empleado)
print("Empleado insertado con id:", nuevo_empleado.id)
db.close() 