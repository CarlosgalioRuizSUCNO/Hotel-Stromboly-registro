from fastapi import FastAPI, HTTPException
from scoring import evaluar_cliente
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/evaluaciones/cliente")
def evaluar_estado_cliente(edad: int, ingreso: int, n_personas: int):
    if edad < 0 or ingreso < 0 or n_personas < 0:
        raise HTTPException(status_code=400, detail="Datos inválidos")

    resultado = evaluar_cliente(edad, ingreso, n_personas)
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