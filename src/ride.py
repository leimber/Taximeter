import time 
from datetime import datetime
import pytz
from fares import Fare 
#import logging


class Ride:
    def __init__(self, fares):
        self.fares = fares
        self.in_ride = False
        self.in_movement = False
        self.in_pause = False 
        self.time_in_pause = 0 #tiempo en pausa
        self.time_in_movement = 0 #tiempo total en movimiento
        self.time_start_ride = None
        self.last_change = 0 #tiempo desde el ultimo cambio      
        
      
        
        '''self.inicio_carrera_info = datetime.datetime.now(pytz.timezone('Europe/Madrid')) # Solo se usa para generar_informes
        self.fin_carrera_info = datetime.datetime.now(pytz.timezone('Europe/Madrid')) # Solo se usa para generar_informes
'''
        #logs
    
    def start_ride(self):
        if not self.in_ride:
            self.time_start_ride = datetime.datetime.now(pytz.timezone('Europe/Madrid'))
            self.in_ride = True
            self.in_movement = False
            #self.in_pause = True
            self.time_in_pause = 0
            self.time_in_movement = 0
            self.time_last_state_change = self.time_start_ride
            #logs
            print("Carrera iniciada. En breve salimos")
        else:
            print("Ya hay una carrera iniciada")
            '''try: 
                user_input = input("Ya hay una carrera iniciada. ¿Desea finalizarla y empezar una nueva? (S/N): ")
                if user_input == 'S':
                    self.finish_ride()
                    self.start_ride()
                    print("Carrera finalizada. Iniciando nueva carrera")
                    return #precio de la carrera anterior
                elif user_input == 'N':
                    print("La carrera continua")
            except:
                    print("Entrada inválida. la carrera continua") #poner cuenta atrás para iniciar una nueva
          '''

    def start_movement(self):
        if not self.in_ride:
            print("Inicie la carrera antes de moverse")
        elif not self.in_movement:
            self.in_movement = True
            self._update_times()
            print("En movimiento")
        else:
            print("Ya estaba en movimiento")
    
    def pause_ride(self):
        if not self.in_ride:
            print("Carrera no iniciada. Inicie la carrera")
        elif self.in_movement:
            self.in_movement = False
            self._update_times()
            print("Detenido")
        else:
            print("Ya detenido. ¿Desea reanudar la marcha o finalizar la carrera?")a reanudar la marcha o finalizar la carrera?")
    
    def _update_times(self):
        now = datetime.datetime.now(pytz.timezone('Europe/Madrid'))
        time_elapsed = (now - self.time_last_state_change).total_seconds()
        if self.in_movement:
            self.time_in_movement += time_elapsed
        else:
            self.time_in_pause += time_elapsed
        self.time_last_state_change = now
        
    def finish_ride(self):
        if self.in_ride:
            self._update_times()
            self.in_ride = False
            self.in_movement = False
            return self.calculate_total_fare()
        else:
            print("No hay carrera iniciada")
            return None
    
    def calculate_total_fare(self):
          
        movement_price = self.time_in_movement * self.fares['moving']
        pause_price = self.time_in_pause * self.fares['paused']
        total_price = (self.time_in_movement * self.fares['moving']) + (self.time_in_pause * self.fares['paused'])
        print(f"Carrera Finalizada. Tiempo total en movimiento: {self.time_in_movement:.2f} segundos. "
              f"Tiempo total en pausa: {self.time_in_pause:.2f} segundos. "
              f"Precio total: {total_price:.2f} euros.")
        return movement_price, pause_price, total_price
        
    
    
    
    