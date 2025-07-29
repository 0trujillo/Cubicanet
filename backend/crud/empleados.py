from sqlalchemy.orm import Session
from schemas.empleados import EmpleadoCreate
from db.models import Empleado

def crear_empleado(db: Session, empleado: EmpleadoCreate):
    db_empleado = Empleado(**empleado.dict())
    db.add(db_empleado)
    db.commit()
    db.refresh(db_empleado)
    return db_empleado