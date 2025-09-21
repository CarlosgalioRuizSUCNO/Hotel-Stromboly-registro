from locust import HttpUser, task, between
import random

class EvaluacionesUser(HttpUser):
    wait_time = between(1, 3.5)         # Cada usuario del test de carga espera entre 2 y 3 segundos
    # host = "https://financieraoh.com"

    @task
    def evaluar_rechazo(self):
        edad = random.randint(0, 17)  # Entero aleatorio entre 0 y 17
        self.client.get("/evaluaciones/cliente", params={
            "edad": edad,
            "ingreso": 10,
            "n_personas": 1
        })

    @task
    def evaluar_simple_premium_ingreso_30(self):
        edad = random.randint(18, 65)  # Entero aleatorio entre 18 y 65
        self.client.get("/evaluaciones/cliente", params={
            "edad": edad,
            "ingreso": 30,
            "n_personas": 1
        })

    @task
    def evaluar_simple_premium_ingreso_35(self):
        edad = random.randint(18, 65)  # Entero aleatorio entre 18 y 65
        self.client.get("/evaluaciones/cliente", params={
            "edad": edad,
            "ingreso": 35,
            "n_personas": 2
        }) 
    
    @task
    def evaluar_matrimonial_simple_ingreso_35(self):
        edad = random.randint(18, 65)  # Entero aleatorio entre 18 y 65
        self.client.get("/evaluaciones/cliente", params={
            "edad": edad,
            "ingreso": 35,
            "n_personas": 1
        })

    @task
    def evaluar_matrimonial_simple_ingreso_40(self):
        edad = random.randint(18, 65)  # Entero aleatorio entre 18 y 65
        self.client.get("/evaluaciones/cliente", params={
            "edad": edad,
            "ingreso": 40,
            "n_personas": 2
        })

    @task
    def evaluar_matrimonial_premium_ingreso_40(self):
        edad = random.randint(18, 65)  # Entero aleatorio entre 18 y 65
        self.client.get("/evaluaciones/cliente", params={
            "edad": edad,
            "ingreso": 40,
            "n_personas": 1
        }) 

    @task
    def evaluar_matrimonial_premium_ingreso_45(self):
        edad = random.randint(18, 65)  # Entero aleatorio entre 18 y 65
        self.client.get("/evaluaciones/cliente", params={
            "edad": edad,
            "ingreso": 45,
            "n_personas": 2
        })
    
    @task
    def evaluar_doble_simple_ingreso_50(self):
        edad = random.randint(18, 65)  # Entero aleatorio entre 18 y 65
        self.client.get("/evaluaciones/cliente", params={
            "edad": edad,
            "ingreso": 50,
            "n_personas": 2
        })

    @task
    def evaluar_doble_simple_ingreso_55(self):
        edad = random.randint(18, 65)  # Entero aleatorio entre 18 y 65
        self.client.get("/evaluaciones/cliente", params={
            "edad": edad,
            "ingreso": 55,
            "n_personas": 4
        })
    
    @task
    def evaluar_doble_premium_ingreso_55(self):
        edad = random.randint(18, 65)  # Entero aleatorio entre 18 y 65
        self.client.get("/evaluaciones/cliente", params={
            "edad": edad,
            "ingreso": 55,
            "n_personas": 2
        })

    @task
    def evaluar_doble_premium_ingreso_60(self):
        edad = random.randint(18, 65)  # Entero aleatorio entre 18 y 65
        self.client.get("/evaluaciones/cliente", params={
            "edad": edad,
            "ingreso": 60,
            "n_personas": 4
        })

    @task
    def evaluar_doble_premium_ingreso_65(self):
        edad = random.randint(18, 65)  # Entero aleatorio entre 18 y 65
        self.client.get("/evaluaciones/cliente", params={
            "edad": edad,
            "ingreso": 65,
            "n_personas": 4
        })

    @task
    def evaluar_doble_premium_ingreso_70(self):
        edad = random.randint(18, 65)  # Entero aleatorio entre 18 y 65
        self.client.get("/evaluaciones/cliente", params={
            "edad": edad,
            "ingreso": 70,
            "n_personas": 4
        })

    @task
    def evaluar_triple_simple_ingreso_70(self):
        edad = random.randint(18, 65)  # Entero aleatorio entre 18 y 65
        self.client.get("/evaluaciones/cliente", params={
            "edad": edad,
            "ingreso": 70,
            "n_personas": 6
        })

    @task
    def evaluar_triple_premium_ingreso_70(self):
        edad = random.randint(18, 65)  # Entero aleatorio entre 18 y 65
        self.client.get("/evaluaciones/cliente", params={
            "edad": edad,
            "ingreso": 70,
            "n_personas": 3
        })

    @task
    def evaluar_triple_premium_ingreso_80(self):
        edad = random.randint(18, 65)  # Entero aleatorio entre 18 y 65
        self.client.get("/evaluaciones/cliente", params={
            "edad": edad,
            "ingreso": 80,
            "n_personas": 3
        })

    @task
    def evaluar_triple_premium_ingreso_90(self):
        edad = random.randint(18, 65)  # Entero aleatorio entre 18 y 65
        self.client.get("/evaluaciones/cliente", params={
            "edad": edad,
            "ingreso": 90,
            "n_personas": 3
        })

    @task
    def evaluar_CRUDClientes(self):
        # Mandar peticion POST a cliente para crear uno
        response = self.client.post("/clientes")
        if response.status_code == 200:

            # Del cliente creado obtener su id
            id_cliente = response.json().get("id")

            # Obtner datos del cliente creado
            self.client.get("/clientes", params={
                "id": id_cliente
            })

            # Eliminar el cliente creado
            self.client.delete("/clientes", params={
                "id": id_cliente
            })

