class TarjetaDeDebito:
    def _init_(self):
        self.numero_tarjeta = self.generar_numero_tarjeta()
        self.fecha_adquisicion = "29 de septiembre de 2024" 
        self.fecha_vencimiento = "29 de septiembre de 2027"

    def generar_numero_tarjeta(self):
        import random
        return str(random.randint(5000000000000000, 5999999999999999))

    def mostrar_informacion(self):
        print(f"Número de Tarjeta de Débito: {self.numero_tarjeta}")
        print(f"Fecha de Adquisición: {self.fecha_adquisicion}")
        print(f"Fecha de Vencimiento: {self.fecha_vencimiento}")