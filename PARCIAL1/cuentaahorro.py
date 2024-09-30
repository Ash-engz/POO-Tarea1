class CuentaDeAhorro:
    def _init_(self):
        self.numero_cuenta = self.generar_numero_cuenta()
        self.fecha_adquisicion = "29 de septiembre de 2024"

    def generar_numero_cuenta(self):
        import random
        return str(random.randint(100000, 999999))

    def mostrar_informacion(self):
        print(f"Número de Cuenta: {self.numero_cuenta}")
        print(f"Fecha de Adquisición: {self.fecha_adquisicion}")