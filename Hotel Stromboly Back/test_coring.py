from scoring import evaluar_cliente

def test_rechazo_por_edad():
    resultado = evaluar_cliente(edad = 16, ingreso = 10, n_personas = 0, metodo_pago="efectivo", n_dni="12345678")
    assert resultado["califica"] is False

def test_rechazo_por_ingreso():
    resultado = evaluar_cliente(edad = 20, ingreso = 20, n_personas = 1, metodo_pago="efectivo", n_dni="12345678")
    assert resultado["califica"] is False

def test_simple_premium_ingreso_30():
    resultado = evaluar_cliente(edad = 18, ingreso = 30, n_personas = 1, metodo_pago="tarjeta", n_dni="12345678")
    assert resultado["califica"] is True
    assert resultado["habitacion"] == "Simple Premium"
    assert resultado["descripcion"] == "Habitacion con baño privado, TV con cable y cama de 1 plaza y media"

def test_simple_premium_ingreso_35():
    resultado = evaluar_cliente(edad = 18, ingreso = 35, n_personas = 2, metodo_pago="tarjeta", n_dni="12345678")
    assert resultado["califica"] is True
    assert resultado["habitacion"] == "Simple Premium"
    assert resultado["descripcion"] == "Habitacion con baño privado, TV con cable y cama de 1 plaza y media"

def test_matrimonial_simple_ingreso_35():
    resultado = evaluar_cliente(edad = 18, ingreso = 35, n_personas = 1, metodo_pago="tarjeta", n_dni="12345678")
    assert resultado["califica"] is True
    assert resultado["habitacion"] == "Matrimonial Simple"
    assert resultado["descripcion"] == "Habitacion con baño privado, TV con cable y cama de 2 plazas"

def test_matrimonial_simple_ingreso_40():
    resultado = evaluar_cliente(edad = 18, ingreso = 40, n_personas = 2, metodo_pago="tarjeta", n_dni="12345678")
    assert resultado["califica"] is True
    assert resultado["habitacion"] == "Matrimonial Simple"
    assert resultado["descripcion"] == "Habitacion con baño privado, TV con cable y cama de 2 plazas"

def test_matrimonial_premium_ingreso_40():
    resultado = evaluar_cliente(edad = 18, ingreso = 40, n_personas = 1, metodo_pago="tarjeta", n_dni="12345668")
    assert resultado["califica"] is True
    assert resultado["habitacion"] == "Matrimonial Premium"
    assert resultado["descripcion"] == "Habitacion con baño privado, TV con cable, cama de 2 plazas con vista a la calle"

def test_matrimonial_premium_ingreso_45():
    resultado = evaluar_cliente(edad = 18, ingreso = 45, n_personas = 2, metodo_pago="tarjeta", n_dni="12345668")
    assert resultado["califica"] is True
    assert resultado["habitacion"] == "Matrimonial Premium"
    assert resultado["descripcion"] == "Habitacion con baño privado, TV con cable, cama de 2 plazas con vista a la calle"

def test_doble_simple_ingreso_50():
    resultado = evaluar_cliente(edad = 18, ingreso = 50, n_personas = 2, metodo_pago="transferencia", n_dni="12345678")
    assert resultado["califica"] is True
    assert resultado["habitacion"] == "Doble Simple"
    assert resultado["descripcion"] == "Habitacion con baño privado, TV con cable y 2 camas de plaza y media"

def test_doble_simple_ingreso_55():
    resultado = evaluar_cliente(edad = 18, ingreso = 55, n_personas = 4, metodo_pago="transferencia", n_dni="12345678")
    assert resultado["califica"] is True
    assert resultado["habitacion"] == "Doble Simple"
    assert resultado["descripcion"] == "Habitacion con baño privado, TV con cable y 2 camas de una plaza y media"

def test_doble_premium_ingreso_55():
    resultado = evaluar_cliente(edad = 18, ingreso = 55, n_personas = 2, metodo_pago="transferencia", n_dni="12345678")
    assert resultado["califica"] is True
    assert resultado["habitacion"] == "Doble Premium"
    assert resultado["descripcion"] == "Habitacion con baño privado, TV con cable, 1 cama de dos plazas y 1 cama de 1 plaza y media con vista a la calle"

def test_doble_premium_ingreso_60():
    resultado = evaluar_cliente(edad = 18, ingreso = 60, n_personas = 4, metodo_pago="transferencia", n_dni="12345678")
    assert resultado["califica"] is True
    assert resultado["habitacion"] == "Doble Premium"
    assert resultado["descripcion"] == "Habitacion con baño privado, TV con cable y 1 cama de dos plazas y 1 cama de 1 plaza y media con vista a la calle"

def test_triple_simple_ingreso_70():
    resultado = evaluar_cliente(edad = 18, ingreso = 70, n_personas = 3, metodo_pago="transferencia", n_dni="12345628")
    assert resultado["califica"] is True
    assert resultado["habitacion"] == "Triple Simple"
    assert resultado["descripcion"] == "Habitacion con baño privado, TV con cable y 2 camas de 1 plaza y media y 1 cama de 2 plazas"

def test_triple_simple_ingreso_80():
    resultado = evaluar_cliente(edad = 18, ingreso = 80, n_personas = 5, metodo_pago="efectivo", n_dni="12345628")
    assert resultado["califica"] is True
    assert resultado["habitacion"] == "Triple Simple"
    assert resultado["descripcion"] == "Habitacion con baño privado, TV con cable y 2 camas de 1 plaza y media y 1 cama de 2 plazas"

def test_triple_premium_ingreso_80():
    resultado = evaluar_cliente(edad = 18, ingreso = 80, n_personas = 3, metodo_pago="transferencia", n_dni="12345628")
    assert resultado["califica"] is True
    assert resultado["habitacion"] == "Triple Premium"
    assert resultado["descripcion"] == "Habitacion con baño privado, TV con cable, 2 camas de 1 plaza y media y 1 cama de 2 plazas con vista a la calle"

def test_triple_premium_ingreso_90():
    resultado = evaluar_cliente(edad = 18, ingreso = 90, n_personas = 5, metodo_pago="efectivo", n_dni="12345628")
    assert resultado["califica"] is True
    assert resultado["habitacion"] == "Triple Premium"
    assert resultado["descripcion"] == "Habitacion con baño privado, TV con cable, 2 camas de 1 plaza y media y 1 cama de 2 plazas con vista a la calle"

def test_caso_intermedio():
    resultado = evaluar_cliente(edad = 25, ingreso = 25, n_personas = 1, metodo_pago="efectivo", n_dni="12345678")
    assert resultado["califica"] is True
    assert resultado["habitacion"] == "Simple Basica"
    assert resultado["descripcion"] == "Habitacion con baño compartido, TV con cable y cama de 1 plaza y media"
