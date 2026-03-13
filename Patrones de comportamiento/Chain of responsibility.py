class ManejadorSoporte:
    def __init__(self, sucesor=None):
        self.sucesor = sucesor

    def procesar_ticket(self, nivel_gravedad, descripcion):
        pass

class PasanteSoporte(ManejadorSoporte):
    def procesar_ticket(self, nivel_gravedad, descripcion):
        if nivel_gravedad == "Bajo":
            print(f" Pasante resolvió el ticket: '{descripcion}' (Reinicio de equipo)")
        elif self.sucesor:
            print(" Pasante: 'Esto es muy complejo, escalando al técnico...'")
            self.sucesor.procesar_ticket(nivel_gravedad, descripcion)

class TecnicoSoporte(ManejadorSoporte):
    def procesar_ticket(self, nivel_gravedad, descripcion):
        if nivel_gravedad == "Medio":
            print(f" Técnico resolvió el ticket: '{descripcion}' (Configuración de red)")
        elif self.sucesor:
            print(" Técnico: 'Se requiere acceso de administrador, escalando al jefe...'")
            self.sucesor.procesar_ticket(nivel_gravedad, descripcion)

class JefeSoporte(ManejadorSoporte):
    def procesar_ticket(self, nivel_gravedad, descripcion):
        if nivel_gravedad == "Alto":
            print(f" Jefe de Soporte resolvió el ticket crítico: '{descripcion}' (Caída de servidor)")
        else:
            print(f" Nadie pudo resolver el ticket: '{descripcion}'")

jefe = JefeSoporte()
tecnico = TecnicoSoporte(sucesor=jefe)
pasante = PasanteSoporte(sucesor=tecnico)

print("--- Ticket 1 ---")
pasante.procesar_ticket("Bajo", "Mi ratón no funciona")

print("\n--- Ticket 2 ---")
pasante.procesar_ticket("Medio", "No hay conexión a la base de datos local")

print("\n--- Ticket 3 ---")
pasante.procesar_ticket("Alto", "El servidor principal de producción está caído")