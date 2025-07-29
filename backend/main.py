from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from db.connection import get_db   # <— ojo, aquí "backend.db"
from schemas.empleados import EmpleadoCreate  # ← con punto   # ✅ <--- ESTA LÍNEA
from crud.empleados import crear_empleado  
from schemas.empleados import EmpleadoCreate
app = FastAPI()

@app.get("/ping")
def ping(db: Session = Depends(get_db)):
    return {"pong": 1}

@app.post("/empleados")
def crear_nuevo_empleado(empleado: EmpleadoCreate, db: Session = Depends(get_db)):
    return crear_empleado(db, empleado)