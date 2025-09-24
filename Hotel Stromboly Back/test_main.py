from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_endpoitn_rechazo():
    response = client.get("/evaluaciones/cliente?edad=17&ingreso=10&n_personas=1&metodo_pago=efectivo&n_dni=12345678")
    assert response.status_code == 200
    assert response.json()["status"] == "RECHAZADO"

def test_endpoint_simple_premium_ingreso_30():
    response = client.get("/evaluaciones/cliente?edad=21&ingreso=30&n_personas=1&metodo_pago=tarjeta&n_dni=12345678")
    assert response.status_code == 200
    assert response.json()["status"] == "APROBADO 😊 👍"
    assert response.json()["description"] == "Habitacion con baño privado, TV con cable y cama de 1 plaza y media"

def test_endpoint_simple_premium_ingreso_35():
    response = client.get("/evaluaciones/cliente?edad=21&ingreso=35&n_personas=2&metodo_pago=tarjeta&n_dni=12345672")
    assert response.status_code == 200
    assert response.json()["status"] == "APROBADO 😊 👍"
    assert response.json()["description"] == "Habitacion con baño privado, TV con cable y cama de 1 plaza y media"

def test_endpoint_matrimonial_simple_ingreso_35():
    response = client.get("/evaluaciones/cliente?edad=21&ingreso=35&n_personas=1&metodo_pago=tarjeta&n_dni=12345672")
    assert response.status_code == 200
    assert response.json()["status"] == "APROBADO 😊 👍"
    assert response.json()["description"] == "Habitacion con baño privado, TV con cable y cama de 2 plazas"

def test_endpoint_matrimonial_simple_ingreso_40():
    response = client.get("/evaluaciones/cliente?edad=21&ingreso=40&n_personas=2&metodo_pago=efectivo&n_dni=12345672")
    assert response.status_code == 200
    assert response.json()["status"] == "APROBADO 😊 👍"
    assert response.json()["description"] == "Habitacion con baño privado, TV con cable y cama de 2 plazas"

def test_endpoint_matrimonial_premium_ingreso_40():
    response = client.get("/evaluaciones/cliente?edad=21&ingreso=40&n_personas=1&metodo_pago=efectivo&n_dni=12345672")
    assert response.status_code == 200
    assert response.json()["status"] == "APROBADO 😊 👍"
    assert response.json()["description"] == "Habitacion con baño privado, TV con cable, cama de 2 plazas con vista a la calle"

def test_endpoint_matrimonial_premium_ingreso_45():
    response = client.get("/evaluaciones/cliente?edad=21&ingreso=45&n_personas=2&metodo_pago=efectivo&n_dni=12345172")
    assert response.status_code == 200
    assert response.json()["status"] == "APROBADO 😊 👍"
    assert response.json()["description"] == "Habitacion con baño privado, TV con cable, cama de 2 plazas con vista a la calle"

def test_endpoint_matrimonial_premium_ingreso_45():
    response = client.get("/evaluaciones/cliente?edad=21&ingreso=45&n_personas=2&metodo_pago=efectivo&n_dni=12345172")
    assert response.status_code == 200
    assert response.json()["status"] == "APROBADO 😊 👍"
    assert response.json()["description"] == "Habitacion con baño privado, TV con cable, cama de 2 plazas con vista a la calle"

def test_endpoint_doble_simple_ingreso_50():
    response = client.get("/evaluaciones/cliente?edad=21&ingreso=50&n_personas=2&metodo_pago=transferencia&n_dni=12345672")
    assert response.status_code == 200
    assert response.json()["status"] == "APROBADO 😊 👍"
    assert response.json()["description"] == "Habitacion con baño privado, TV con cable y 2 camas de plaza y media"

def test_endpoint_doble_simple_ingreso_50():
    response = client.get("/evaluaciones/cliente?edad=21&ingreso=50&n_personas=2&metodo_pago=transferencia&n_dni=12345672")
    assert response.status_code == 200
    assert response.json()["status"] == "APROBADO 😊 👍"
    assert response.json()["description"] == "Habitacion con baño privado, TV con cable y 2 camas de una plaza y media"

def test_endpoint_doble_simple_ingreso_55():
    response = client.get("/evaluaciones/cliente?edad=21&ingreso=55&n_personas=4&metodo_pago=efectivo&n_dni=12345672")
    assert response.status_code == 200
    assert response.json()["status"] == "APROBADO 😊 👍"
    assert response.json()["description"] == "Habitacion con baño privado, TV con cable y 2 camas de una plaza y media"

def test_endpoint_doble_premium_ingreso_55():
    response = client.get("/evaluaciones/cliente?edad=21&ingreso=55&n_personas=2&metodo_pago=tarjeta&n_dni=12345672")
    assert response.status_code == 200
    assert response.json()["status"] == "APROBADO 😊 👍"
    assert response.json()["description"] == "Habitacion con baño privado, TV con cable, 1 cama de dos plazas y 1 cama de 1 plaza y media con vista a la calle"

def test_endpoint_doble_premium_ingreso_60():
    response = client.get("/evaluaciones/cliente?edad=21&ingreso=60&n_personas=4&metodo_pago=tarjeta&n_dni=12345672")
    assert response.status_code == 200
    assert response.json()["status"] == "APROBADO 😊 👍"
    assert response.json()["description"] == "Habitacion con baño privado, TV con cable y 1 cama de dos plazas y 1 cama de 1 plaza y media con vista a la calle"

def test_endpoint_triple_simple_ingreso_70():
    response = client.get("/evaluaciones/cliente?edad=21&ingreso=70&n_personas=3&metodo_pago=tarjeta&n_dni=12345672")
    assert response.status_code == 200
    assert response.json()["status"] == "APROBADO 😊 👍"
    assert response.json()["description"] == "Habitacion con baño privado, TV con cable y 2 camas de 1 plaza y media y 1 cama de 2 plazas"

def test_endpoint_triple_simple_ingreso_80():
    response = client.get("/evaluaciones/cliente?edad=21&ingreso=80&n_personas=5&metodo_pago=transferencia&n_dni=12315672")
    assert response.status_code == 200
    assert response.json()["status"] == "APROBADO 😊 👍"
    assert response.json()["description"] == "Habitacion con baño privado, TV con cable y 2 camas de 1 plaza y media y 1 cama de 2 plazas"

def test_endpoint_triple_premium_ingreso_80():
    response = client.get("/evaluaciones/cliente?edad=21&ingreso=80&n_personas=3&metodo_pago=tarjeta&n_dni=12315672")
    assert response.status_code == 200
    assert response.json()["status"] == "APROBADO 😊 👍"
    assert response.json()["description"] == "Habitacion con baño privado, TV con cable, 2 camas de 1 plaza y media y 1 cama de 2 plazas con vista a la calle"

def test_endpoint_triple_premium_ingreso_90():
    response = client.get("/evaluaciones/cliente?edad=21&ingreso=90&n_personas=5&metodo_pago=tarjeta&n_dni=12315672")
    assert response.status_code == 200
    assert response.json()["status"] == "APROBADO 😊 👍"
    assert response.json()["description"] == "Habitacion con baño privado, TV con cable, 2 camas de 1 plaza y media y 1 cama de 2 plazas con vista a la calle"

def test_endpoint_caso_intermedio():
    response = client.get("/evaluaciones/cliente?edad=21&ingreso=25&n_personas=1&metodo_pago=efectivo&n_dni=12345672")
    assert response.status_code == 200
    assert response.json()["status"] == "APROBADO 😊 👍"
    assert response.json()["description"] == "Habitacion con baño compartido, TV con cable y cama de 1 plaza y media"

def test_endpoint_datos_invalido():
    response = client.get("/evaluaciones/cliente?edad=-5&ingreso=30&n_personas=-1&metodo_pago=transferencia&n_dni=12345672")
    assert response.status_code == 400
    assert response.json()["detail"] == "Datos inválidos"