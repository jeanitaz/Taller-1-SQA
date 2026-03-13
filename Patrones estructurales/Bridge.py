class CanalEnvio:
    def enviar(self, texto):
        pass

class CorreoElectronico(CanalEnvio):
    def enviar(self, texto):
        print(f"📧 Enviando por Correo: {texto}")

class SMS(CanalEnvio):
    def enviar(self, texto):
        print(f"📱 Enviando por SMS: {texto}")

class Mensaje:
    def __init__(self, canal: CanalEnvio):
        self.canal = canal

    def enviar_mensaje(self):
        pass

class AlertaUrgente(Mensaje):
    def enviar_mensaje(self):
        print("\n[!] PREPARANDO ALERTA URGENTE [!]")
        self.canal.enviar("¡El servidor principal está caído!")

class BoletinInformativo(Mensaje):
    def enviar_mensaje(self):
        print("\n--- Preparando Boletín Mensual ---")
        self.canal.enviar("Nuevas actualizaciones de software disponibles.")

canal_correo = CorreoElectronico()
canal_sms = SMS()

alerta_por_sms = AlertaUrgente(canal_sms)
alerta_por_sms.enviar_mensaje()

boletin_por_correo = BoletinInformativo(canal_correo)
boletin_por_correo.enviar_mensaje()