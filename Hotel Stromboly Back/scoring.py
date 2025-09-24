def evaluar_cliente(edad, ingreso, n_personas, metodo_pago, n_dni):
    # Edad o ingresos no válidos
    if edad < 18 or ingreso < 25 or n_personas < 1 or metodo_pago not in ["tarjeta", "efectivo", "transferencia"] or len(n_dni) != 8:
        return {"califica": False, "habitacion": None, "descripcion": "No cumple con los requisitos mínimos"} 

    # Simple Premium: Ingreso igual a 30 Soles, edad mayor o igual a 18 y numero de personas 1
    if ingreso == 30 and edad >= 18 and n_personas == 1 and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Simple Premium", "descripcion": "Habitacion con baño privado, TV con cable y cama de 1 plaza y media"}

    # Simple Premium: Ingreso igual a 35 Soles, edad mayor o igual a 18 y numero de personas 2
    if ingreso == 35 and edad >= 18 and n_personas == 2 and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Simple Premium", "descripcion": "Habitacion con baño privado, TV con cable y cama de 1 plaza y media"}

    # Matrimonial: Ingreso igual a 35 Soles, edad mayor o igual a 18 y numero de personas 1
    if ingreso == 35 and edad >= 18 and n_personas == 1 and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Matrimonial Simple", "descripcion": "Habitacion con baño privado, TV con cable y cama de 2 plazas"}

    # Matrimonial: Ingreso igual a 40 Soles, edad mayor o igual a 18 y numero de personas 2
    if ingreso == 40 and edad >= 18 and n_personas == 2 and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Matrimonial Simple", "descripcion": "Habitacion con baño privado, TV con cable y cama de 2 plazas"}

    # Matrimonial Premium: Ingreso igual a 40 Soles, edad mayor o igual a 18 y numero de personas 1
    if ingreso == 40 and edad >= 18 and n_personas == 1 and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Matrimonial Premium", "descripcion": "Habitacion con baño privado, TV con cable, cama de 2 plazas con vista a la calle"}

    # Matrimonial Premium: Ingreso igual a 45 Soles, edad mayor o igual a 18 y numero de personas 2
    if ingreso == 45 and edad >= 18 and n_personas == 2 and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Matrimonial Premium", "descripcion": "Habitacion con baño privado, TV con cable, cama de 2 plazas con vista a la calle"}

    # Doble Simple: Ingreso igual a 50 Soles, edad mayor o igual a 18 y numero de personas 2 o 3
    if ingreso == 50 and edad >= 18 and n_personas in [2, 3] and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Doble Simple", "descripcion": "Habitacion con baño privado, TV con cable y 2 camas de una plaza y media"}
    
    # Doble Simple: Ingreso igual a 55 Soles, edad mayor o igual a 18 y numero de personas 4
    if ingreso == 55 and edad >= 18 and n_personas == 4 and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Doble Simple", "descripcion": "Habitacion con baño privado, TV con cable y 2 camas de una plaza y media"}

    # Doble Premium: Ingreso igual a 55 Soles, edad mayor o igual a 18 y numero de personas 2 o 3
    if ingreso == 55 and edad >= 18 and n_personas in [2, 3] and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Doble Premium", "descripcion": "Habitacion con baño privado, TV con cable, 1 cama de dos plazas y 1 cama de 1 plaza y media con vista a la calle"}

    # Doble Premium: Ingreso igual a 60 Soles, edad mayor o igual a 18 y numero de personas 4
    if ingreso == 60 and edad >= 18 and n_personas == 4 and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Doble Premium", "descripcion": "Habitacion con baño privado, TV con cable y 1 cama de dos plazas y 1 cama de 1 plaza y media con vista a la calle"}
    
    # Triple Simple: Ingreso igual a 70 Soles, edad mayor o igual a 18 y numero de personas 3 o 4
    if ingreso == 70 and edad >= 18 and n_personas in [3, 4] and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Triple Simple", "descripcion": "Habitacion con baño privado, TV con cable y 2 camas de 1 plaza y media y 1 cama de 2 plazas"}

    # Triple Simple: Ingreso igual a 80 Soles, edad mayor o igual a 18 y numero de personas 5 o 6
    if ingreso == 80 and edad >= 18 and n_personas in [5, 6] and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Triple Simple", "descripcion": "Habitacion con baño privado, TV con cable y 2 camas de 1 plaza y media y 1 cama de 2 plazas"}

    # Triple Premium: Ingreso igual a 80 Soles, edad mayor o igual a 18 y numero de personas 3 o 4
    if ingreso == 80 and edad >= 18 and n_personas in [3, 4] and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Triple Premium", "descripcion": "Habitacion con baño privado, TV con cable, 2 camas de 1 plaza y media y 1 cama de 2 plazas con vista a la calle"}
    
    # Triple Premium: Ingreso igual a 90 Soles, edad mayor o igual a 18 y numero de personas 5 o 6
    if ingreso == 90 and edad >= 18 and n_personas in [5, 6] and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Triple Premium", "descripcion": "Habitacion con baño privado, TV con cable, 2 camas de 1 plaza y media y 1 cama de 2 plazas con vista a la calle"}


    # Defecto: Tarjeta OH
    return {"califica": True, "habitacion": "Simple Basica", "descripcion": "Habitacion con baño compartido, TV con cable y cama de 1 plaza y media"}