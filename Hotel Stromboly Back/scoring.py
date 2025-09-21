def evaluar_cliente(edad, ingreso, n_personas, metodo_pago, n_dni):
    # Edad o ingresos no válidos
    if edad < 18 or ingreso < 25 or n_personas < 1 or metodo_pago not in ["tarjeta", "efectivo", "transferencia"] or len(n_dni) != 8:
        return {"califica": False, "habitacion": None} 

    # Simple Premium: Ingreso igual a 30 Soles, edad mayor o igual a 18 y numero de personas 1
    if ingreso == 30 and edad >= 18 and n_personas == 1 and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Simple Premium"}

    # Simple Premium: Ingreso igual a 35 Soles, edad mayor o igual a 18 y numero de personas 2
    if ingreso == 35 and edad >= 18 and n_personas == 2 and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Simple Premium"}

    # Matrimonial: Ingreso igual a 35 Soles, edad mayor o igual a 18 y numero de personas 1
    if ingreso == 35 and edad >= 18 and n_personas == 1 and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Matrimonial Simple"}

    # Matrimonial: Ingreso igual a 40 Soles, edad mayor o igual a 18 y numero de personas 2
    if ingreso == 40 and edad >= 18 and n_personas == 2 and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Matrimonial Simple"}

    # Matrimonial Premium: Ingreso igual a 40 Soles, edad mayor o igual a 18 y numero de personas 1
    if ingreso == 40 and edad >= 18 and n_personas == 1 and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Matrimonial Premium"}
    
    # Matrimonial Premium: Ingreso igual a 45 Soles, edad mayor o igual a 18 y numero de personas 2
    if ingreso == 45 and edad >= 18 and n_personas == 2 and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Matrimonial Premium"}

    # Doble Simple: Ingreso igual a 50 Soles, edad mayor o igual a 18 y numero de personas 2 o 3
    if ingreso == 50 and edad >= 18 and n_personas in [2, 3] and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Doble Simple"}
    
    # Doble Simple: Ingreso igual a 55 Soles, edad mayor o igual a 18 y numero de personas 4
    if ingreso == 55 and edad >= 18 and n_personas == 4 and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Doble Simple"}

    # Doble Premium: Ingreso igual a 55 Soles, edad mayor o igual a 18 y numero de personas 2 o 3
    if ingreso == 55 and edad >= 18 and n_personas in [2, 3] and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Doble Premium"}
    
    # Doble Premium: Ingreso igual a 60 Soles, edad mayor o igual a 18 y numero de personas 4
    if ingreso == 60 and edad >= 18 and n_personas == 4 and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Doble Premium"}
    
    # Triple Simple: Ingreso igual a 70 Soles, edad mayor o igual a 18 y numero de personas 3 o 4
    if ingreso == 70 and edad >= 18 and n_personas in [3, 4] and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Triple Simple"}
    
    # Triple Simple: Ingreso igual a 80 Soles, edad mayor o igual a 18 y numero de personas 5 o 6
    if ingreso == 80 and edad >= 18 and n_personas in [5, 6] and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Triple Simple"}
    
    # Triple Premium: Ingreso igual a 80 Soles, edad mayor o igual a 18 y numero de personas 3 o 4
    if ingreso == 80 and edad >= 18 and n_personas in [3, 4] and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Triple Premium"}
    
    # Triple Premium: Ingreso igual a 90 Soles, edad mayor o igual a 18 y numero de personas 5 o 6
    if ingreso == 90 and edad >= 18 and n_personas in [5, 6] and metodo_pago in ["tarjeta", "efectivo", "transferencia"] and len(n_dni) == 8:
        return {"califica": True, "habitacion": "Triple Premium"}


    # Defecto: Tarjeta OH
    return {"califica": True, "habitacion": "Simple Basica"}