class SistemaLogger:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(SistemaLogger, cls).__new__(cls)
            cls._instance.logs = []
        return cls._instance

    def registrar(self, mensaje):
        self.logs.append(mensaje)

    def mostrar_logs(self):
        print("--- Historial de Eventos ---")
        for log in self.logs:
            print(f"> {log}")


logger_auth = SistemaLogger()
logger_auth.registrar("Usuario 'admin' inició sesión en el dashboard.")

logger_db = SistemaLogger()
logger_db.registrar("Se ejecutó un respaldo de la tabla 'tickets'.")

logger_reportes = SistemaLogger()
logger_reportes.mostrar_logs()

print("¿Son la misma instancia?", logger_auth is logger_reportes)