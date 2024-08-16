




def set_custom_rates(self):
        try:
            self.paused_rate = float(input("Ingrese la tarifa por segundo cuando el taxi está parado (en euros): "))
            self.moving_rate = float(input("Ingrese la tarifa por segundo cuando el taxi está en movimiento (en euros): "))
            print(f"Tarifas actualizadas: Parado {self.paused_rate}€/s, En movimiento {self.moving_rate}€/s")
        except ValueError:
            print("Entrada inválida. Se usarán las tarifas por defecto.")