class ComponenteSistema:
    def mostrar(self, sangria=""):
        pass

class Archivo(ComponenteSistema):
    def __init__(self, nombre):
        self.nombre = nombre

    def mostrar(self, sangria=""):
        print(f"{sangria}📄 Archivo: {self.nombre}")

class Carpeta(ComponenteSistema):
    def __init__(self, nombre):
        self.nombre = nombre
        self.hijos = []

    def agregar(self, componente: ComponenteSistema):
        self.hijos.append(componente)

    def mostrar(self, sangria=""):
        print(f"{sangria}📁 Carpeta: {self.nombre}")
        for hijo in self.hijos:
            hijo.mostrar(sangria + "    ")


archivo1 = Archivo("foto_perfil.jpg")
archivo2 = Archivo("reporte_mensual.pdf")
archivo3 = Archivo("script_base_datos.py")

carpeta_imagenes = Carpeta("Mis Imágenes")
carpeta_imagenes.agregar(archivo1)

carpeta_raiz = Carpeta("Directorio Principal")
carpeta_raiz.agregar(carpeta_imagenes)
carpeta_raiz.agregar(archivo2)
carpeta_raiz.agregar(archivo3)

carpeta_raiz.mostrar()