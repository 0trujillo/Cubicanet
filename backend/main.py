from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from db.connection import get_db
from schemas.empleados import EmpleadoCreate, EmpleadoOut
from crud.empleados import (
    crear_empleado,
    obtener_empleados,
    obtener_empleado_por_id,
    actualizar_empleado,
    eliminar_empleado,
)

app = FastAPI(title="Cubicanet API", version="1.0.0")

@app.get("/ping")
def ping(db: Session = Depends(get_db)):
    return {"pong": 1}

@app.post("/empleados", response_model=EmpleadoOut)
def crear_nuevo_empleado(empleado: EmpleadoCreate, db: Session = Depends(get_db)):
    try:
        return crear_empleado(db, empleado)
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

@app.get("/empleados", response_model=list[EmpleadoOut])
def listar_empleados(db: Session = Depends(get_db)):
    try:
        return obtener_empleados(db)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

@app.get("/empleados/{empleado_id}", response_model=EmpleadoOut)
def obtener_empleado(empleado_id: int, db: Session = Depends(get_db)):
    try:
        empleado = obtener_empleado_por_id(db, empleado_id)
        if not empleado:
            raise HTTPException(status_code=404, detail="Empleado no encontrado")
        return empleado
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

@app.put("/empleados/{empleado_id}", response_model=EmpleadoOut)
def editar_empleado(empleado_id: int, empleado: EmpleadoCreate, db: Session = Depends(get_db)):
    try:
        emp = actualizar_empleado(db, empleado_id, empleado)
        if not emp:
            raise HTTPException(status_code=404, detail="Empleado no encontrado")
        return emp
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")

@app.delete("/empleados/{empleado_id}")
def borrar_empleado(empleado_id: int, db: Session = Depends(get_db)):
    try:
        result = eliminar_empleado(db, empleado_id)
        if not result:
            raise HTTPException(status_code=404, detail="Empleado no encontrado")
        return {"detail": "Empleado eliminado"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error interno del servidor: {str(e)}")