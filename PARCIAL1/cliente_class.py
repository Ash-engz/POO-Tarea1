from cuentaahorro import CuentaDeAhorro
from terjetacredito import TarjetaDeCredito
from tarjetadebito import TarjetaDeDebito

class Cliente:
    def _init_(self):
        self.nombre = input("Ingrese su nombre completo: ")
        self.edad = int(input("Ingrese su edad: "))
        self.municipio = input("Ingrese su municipio de residencia: ")
        self.dpi = int(input("Ingrese su DPI: "))
        self.cuenta = CuentaDeAhorro()
        self.tarjeta_de_credito = TarjetaDeCredito()
        self.tarjeta_de_debito = TarjetaDeDebito(self.cuenta)

        self.crear_perfil()

    def crear_perfil(self):
        if self.edad >= 18:
            print(f"Usuario creado exitosamente con el número de cuenta: {self.cuenta.numero_cuenta}")
            print(f"Número de tarjeta de crédito: {self.tarjeta_de_credito.numero_tarjeta}")
            print(f"Tipo de tarjeta: {self.tarjeta_de_credito.tipo_tarjeta}")
            print(f"Límite de crédito: Q{self.tarjeta_de_credito.limite_credito} por mes")
            print(f"Fecha de adquisición: {self.tarjeta_de_credito.fecha_adquisicion}")
            print(f"Fecha de vencimiento: {self.tarjeta_de_credito.fecha_vencimiento}")

            print(f"Número de tarjeta de débito: {self.tarjeta_de_debito.numero_tarjeta}")
            print(f"Fecha de adquisición de tarjeta de débito: {self.tarjeta_de_debito.fecha_adquisicion}")
            print(f"Fecha de vencimiento de tarjeta de débito: {self.tarjeta_de_debito.fecha_vencimiento}")
        else:
            print("Solamente se puede crear perfil de usuario siendo mayor de edad.")

    def mostrar_info(self):
        print(f"Nombre: {self.nombre}, Edad: {self.edad}, Municipio: {self.municipio}, DPI: {self.dpi}")