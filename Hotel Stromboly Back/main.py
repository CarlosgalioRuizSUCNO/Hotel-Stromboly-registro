from fastapi import FastAPI, HTTPException
from scoring import evaluar_cliente
from fastapi.middleware.cors import CORSMiddleware
import random
import time

app = FastAPI(
    title="Evaluaciones de clientes - Hotel Stromboly",
    description="API para gestionar petciones de evaluacion de clientes para el alquiler de habitaciones en el Hotel Stromboly",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/evaluaciones/cliente", tags=["Evaluaciones"], summary="Evaluar estado de un cliente")
def evaluar_estado_cliente(edad: int, ingreso: int, n_personas: int, metodo_pago: str, n_dni: str):
    if edad < 0 or ingreso < 0 or n_personas < 0 or metodo_pago not in ["tarjeta", "efectivo", "transferencia"] or len(n_dni) != 8:
        raise HTTPException(status_code=400, detail="Datos inválidos")

    time.sleep(0.4)  # Simula una espera de 400 ms

    resultado = evaluar_cliente(edad, ingreso, n_personas, metodo_pago, n_dni)
    if resultado["califica"]:
        return {
        "status": "APROBADO 😊 👍",
        "mensaje": f"Felicidades, usted puede alquilar una habitación {resultado['habitacion']}",
        "description": resultado['descripcion'],
        "data": resultado
    }
    else:
        return {
        "status": "RECHAZADO",
        "mensaje": "No cumple con los requisitos para alquilar una habitación",
        "data": resultado
    }

@app.post("/clientes", tags=["Clientes"], summary="Crear un nuevo cliente")
def crear_Usuario():
    return {"id": random.randint(1, 10)}

@app.get("/clientes", tags=["Clientes"], summary="Obtener información de un cliente")
def obtener_Usuario(id: int):
    return {
        "id": id
    }

@app.delete("/clientes", tags=["Clientes"], summary="Eliminar un cliente")
def eliminar_Usuario(id: str):
    return {
        "id": id
        }

@app.get("/habitaciones", tags=["Habitaciones"], summary="Obtener información de una habitación")
def obtener_habitacion(edad: int, ingreso: int, n_personas: int, metodo_pago: str, n_dni: str):
    time.sleep(0.4)  # Simula una espera de 400 ms

    resultado = evaluar_cliente(edad, ingreso, n_personas, metodo_pago, n_dni)
    if resultado["califica"]:
        return {
        "description": f"De acuerdo con la informacion brindada, tenemos una {resultado['descripcion']}",
        "data": resultado
    }
    else:
        return {
        "status": "RECHAZADO",
        "mensaje": "No cumple con los requisitos para alquilar una habitación",
        "data": resultado
    }