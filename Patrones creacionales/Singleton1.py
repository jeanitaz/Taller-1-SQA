class ConfiguracionMeteorologica:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(ConfiguracionMeteorologica, cls).__new__(cls)
            cls._instance.estacion_activa = "Quito-Centro"
            cls._instance.unidad = "Celsius"
        return cls._instance

    def cambiar_estacion(self, nueva_estacion):
        self.estacion_activa = nueva_estacion

    def mostrar_configuracion(self):
        return f"Estación actual: {self.estacion_activa} | Unidad: {self.unidad}"


config1 = ConfiguracionMeteorologica()
print("Módulo 1 lee:", config1.mostrar_configuracion())

config2 = ConfiguracionMeteorologica()
config2.cambiar_estacion("Cotopaxi-Norte")

print("Módulo 1 lee ahora:", config1.mostrar_configuracion())

print("¿Son la misma instancia?", config1 is config2)