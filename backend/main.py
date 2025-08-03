

from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session
from db.connection import get_db
from schemas.empleados import EmpleadoOut, EmpleadoCreate
from crud.empleados import (
    obtener_empleados,
    crear_empleado,
    obtener_empleado_por_id,
    actualizar_empleado,
    eliminar_empleado
)


app = FastAPI(title="Cubicanet API", version="1.0.0")

# Permitir CORS para cualquier origen (desarrollo)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Listar empleados
@app.get("/empleados", response_model=list[EmpleadoOut])
def listar_empleados(db: Session = Depends(get_db)):
    try:
        return obtener_empleados(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

# Crear empleado
@app.post("/empleados", response_model=EmpleadoOut)
def crear_empleado_endpoint(empleado: EmpleadoCreate, db: Session = Depends(get_db)):
    try:
        return crear_empleado(db, empleado)
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

# Obtener empleado por ID
@app.get("/empleados/{empleado_id}", response_model=EmpleadoOut)
def obtener_empleado_endpoint(empleado_id: int, db: Session = Depends(get_db)):
    empleado = obtener_empleado_por_id(db, empleado_id)
    if not empleado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return empleado

# Actualizar empleado
@app.put("/empleados/{empleado_id}", response_model=EmpleadoOut)
def actualizar_empleado_endpoint(empleado_id: int, empleado: EmpleadoCreate, db: Session = Depends(get_db)):
    actualizado = actualizar_empleado(db, empleado_id, empleado)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return actualizado

# Eliminar empleado
@app.delete("/empleados/{empleado_id}")
def eliminar_empleado_endpoint(empleado_id: int, db: Session = Depends(get_db)):
    eliminado = eliminar_empleado(db, empleado_id)
    if eliminado is None:
        raise HTTPException(status_code=404, detail="Empleado no encontrado")
    return {"ok": True}