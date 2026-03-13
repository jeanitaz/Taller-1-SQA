class EstadoEvaluacion:
    def cargar_examen(self):
        pass
    def calificar(self):
        pass

class EstadoPendiente(EstadoEvaluacion):
    def cargar_examen(self):
        print(" Examen de matemáticas cargado exitosamente. Listo para evaluar.")
        return EstadoCalificando()
    
    def calificar(self):
        print(" Error: No puedes calificar porque no se ha cargado ningún examen aún.")
        return self

class EstadoCalificando(EstadoEvaluacion):
    def cargar_examen(self):
        print(" Error: Ya hay un examen en proceso, espera a que termine de calificar.")
        return self
    
    def calificar(self):
        print(" Analizando respuestas y procesando fórmulas matemáticas... ¡Examen calificado!")
        return EstadoFinalizado()

class EstadoFinalizado(EstadoEvaluacion):
    def cargar_examen(self):
        print(" Nuevo examen cargado. Reiniciando el proceso.")
        return EstadoCalificando()
    
    def calificar(self):
        print(" Aviso: El examen ya fue calificado anteriormente. Generando reporte de notas.")
        return self

class EvaluadorAutomatico:
    def __init__(self):
        self.estado_actual = EstadoPendiente()

    def cargar_examen(self):
        self.estado_actual = self.estado_actual.cargar_examen()

    def procesar_calificacion(self):
        self.estado_actual = self.estado_actual.calificar()

evaluador = EvaluadorAutomatico()
evaluador.procesar_calificacion() 

print("---")
evaluador.cargar_examen()
evaluador.procesar_calificacion()

print("---")
evaluador.procesar_calificacion()