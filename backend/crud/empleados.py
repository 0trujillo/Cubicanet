from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from schemas.empleados import EmpleadoCreate
from db.models import Empleado

def crear_empleado(db: Session, empleado: EmpleadoCreate):
    try:
        db_empleado = Empleado(**empleado.dict())
        db.add(db_empleado)
        db.commit()
        db.refresh(db_empleado)
        return db_empleado
    except IntegrityError as e:
        db.rollback()
        if "rut" in str(e.orig):
            raise HTTPException(status_code=400, detail="El RUT ya existe")
        elif "correo_trabajador" in str(e.orig):
            raise HTTPException(status_code=400, detail="El correo ya existe")
        elif "estado_civil_id" in str(e.orig):
            raise HTTPException(status_code=400, detail="Estado civil inválido")
        else:
            raise HTTPException(status_code=400, detail="Error de integridad de datos")

def obtener_empleados(db: Session):
    return db.query(Empleado).all()

def obtener_empleado_por_id(db: Session, empleado_id: int):
    return db.query(Empleado).filter(Empleado.id == empleado_id).first()

def actualizar_empleado(db: Session, empleado_id: int, empleado: EmpleadoCreate):
    try:
        db_empleado = db.query(Empleado).filter(Empleado.id == empleado_id).first()
        if not db_empleado:
            return None
        for key, value in empleado.dict().items():
            setattr(db_empleado, key, value)
        db.commit()
        db.refresh(db_empleado)
        return db_empleado
    except IntegrityError as e:
        db.rollback()
        if "rut" in str(e.orig):
            raise HTTPException(status_code=400, detail="El RUT ya existe")
        elif "correo_trabajador" in str(e.orig):
            raise HTTPException(status_code=400, detail="El correo ya existe")
        elif "estado_civil_id" in str(e.orig):
            raise HTTPException(status_code=400, detail="Estado civil inválido")
        else:
            raise HTTPException(status_code=400, detail="Error de integridad de datos")

def eliminar_empleado(db: Session, empleado_id: int):
    try:
        db_empleado = db.query(Empleado).filter(Empleado.id == empleado_id).first()
        if not db_empleado:
            return None
        db.delete(db_empleado)
        db.commit()
        return True
    except IntegrityError as e:
        db.rollback()
        raise HTTPException(status_code=400, detail="No se puede eliminar: empleado tiene datos relacionados")