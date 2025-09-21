from fastapi import FastAPI, HTTPException
from scoring import evaluar_cliente
from fastapi.middleware.cors import CORSMiddleware
import random
import time

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/evaluaciones/cliente")
def evaluar_estado_cliente(edad: int, ingreso: int, n_personas: int, metodo_pago: str, n_dni: str):
    if edad < 0 or ingreso < 0 or n_personas < 0 or metodo_pago not in ["tarjeta", "efectivo", "transferencia"] or len(n_dni) != 8:
        raise HTTPException(status_code=400, detail="Datos inválidos")

    time.sleep(0.4)  # Simula una espera de 400 ms

    resultado = evaluar_cliente(edad, ingreso, n_personas, metodo_pago, n_dni)
    if resultado["califica"]:
        return {
        "status": "APROBADO 😊 👍",
        "mensaje": f"Felicidades, usted puede alquilar una habitación {resultado['habitacion']}",
        "data": resultado
    }
    else:
        return {
        "status": "RECHAZADO",
        "mensaje": "No cumple con los requisitos para alquilar una habitación",
        "data": resultado
    }

@app.post("/clientes")
def crearUsuario():
    return {"id": random.randint(1, 10)}

@app.get("/clientes")
def obtenerUsuario(id: int):
    return {
        "id": id
    }

@app.delete("/clientes")
def eliminarUsuario(id: str):
    return {
        "id": id
        }