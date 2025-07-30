from pydantic import BaseModel, validator
from typing import Optional
from datetime import date
import re

class EmpleadoCreate(BaseModel):
    nombre: str
    rut: str
    correo_trabajador: Optional[str] = None
    fecha_nacimiento: date
    estado_civil_id: int

    @validator('rut')
    def validar_rut(cls, v):
        # Validar formato básico de RUT chileno
        if not re.match(r'^\d{7,8}-[0-9Kk]$', v):
            raise ValueError('RUT debe tener formato XXXXXXXX-X')
        return v.upper()

    @validator('nombre')
    def validar_nombre(cls, v):
        if len(v.strip()) < 2:
            raise ValueError('Nombre debe tener al menos 2 caracteres')
        return v.strip()

    @validator('correo_trabajador')
    def validar_correo(cls, v):
        if v and '@' not in v:
            raise ValueError('Correo debe tener formato válido')
        return v

    @validator('estado_civil_id')
    def validar_estado_civil(cls, v):
        if v < 1 or v > 5:  # Basado en los datos que insertamos
            raise ValueError('Estado civil debe estar entre 1 y 5')
        return v

class EmpleadoOut(BaseModel):
    id: int
    nombre: str
    rut: str
    correo_trabajador: Optional[str]
    fecha_nacimiento: date
    estado_civil_id: int

    class Config:
        orm_mode = True