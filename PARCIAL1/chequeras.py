import random

class Chequera:
    def _init_(self):
        self.fecha_adquisicion = "29 de septiembre de 2024"
        self.fecha_vencimiento = "29 de septiembre de 2027"
        self.cheques = self.generar_cheques()

    def generar_cheques(self):
        cheques = {}
        for i in range(1, 26):
            cheque_id = self.generar_numero_unico()
            cheques[cheque_id] = f"Cheque #{i}"
        return cheques

    def generar_numero_unico(self):
        return random.randint(100000, 999999)

    def mostrar_informacion(self):
        print(f"Fecha de adquisición: {self.fecha_adquisicion}")
        print(f"Fecha de vencimiento: {self.fecha_vencimiento}")
        print(f"Número de cheques: {len(self.cheques)}")
        print("Detalles de los cheques:")
        for cheque_id, cheque_info in self.cheques.items():
            print(f"{cheque_info} - ID: {cheque_id}")