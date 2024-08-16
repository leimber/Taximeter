class Fare: 
         
    def __init__(self):
        self.rates = {
            'moving': 0.05,  # 5 céntimos por segundo por defecto
            'paused': 0.02   # 2 céntimos por segundo por defecto
        }

    def get_rate(self, state):
        return self.rates.get(state, 0)

    def set_rate(self, state, rate):
        if state in self.rates:
            self.rates[state] = rate
        else:
            raise ValueError(f"Estado de tarifa no reconocido: {state}")

    def get_all_rates(self):
        return self.rates.copy()