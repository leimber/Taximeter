import datetime
import pytz
from ride import Ride
from fares import Fare

def get_user_fares():
    try:
        moving_fare = float(input("Ingrese la tarifa por segundo en movimiento (default 0.05): ") or 0.05)
        paused_fare = float(input("Ingrese la tarifa por segundo en pausa (default 0.02): ") or 0.02)
        return Fare(moving_rate=moving_fare, paused_rate=paused_fare)
    except ValueError:
        print("Entrada inválida. Usando tarifas por defecto.")
        return Fare()

def main():
    fare = Fare()
    ride = None
    print("Bienvenida al sistema de taxímetro.")
    print(f"Las tarifas por defecto son: Movimiento: {fare.get_rate('moving')} por segundo, Pausa: {fare.get_rate('paused')} por segundo. Elige una opción")

    while True:
        print("\nOpciones:")
        print("1. Cambiar tarifas")
        print("2. Iniciar carrera")
        print("3. Iniciar movimiento")
        print("4. Pausar carrera")
        print("5. Finalizar carrera")
        print("6. Salir")
        
        choice = input("Seleccione una opción: ")

        if choice == '1':
            fare = get_user_fares()
        elif choice == '2':
            ride = Ride(fare.get_all_rates())
            ride.start_ride()
        elif choice == '3':
            if ride:
                ride.start_movement()
            else:
                print("Primero debe iniciar una carrera.")
        elif choice == '4':
            if ride:
                ride.pause_ride()
            else:
                print("Primero debe iniciar una carrera.")
        elif choice == '5':
            if ride:
                fare_details = ride.finish_ride()
                if fare_details:
                    print(f"Detalles de la tarifa: {fare_details}")
            else:
                print("Primero debe iniciar una carrera.")
        elif choice == '6':
            print("Saliendo del sistema de taxímetro.")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")


if __name__ == "__main__":
    main()