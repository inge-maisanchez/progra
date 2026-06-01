cupos = 75
historial = 0

print("¡Bienvenido al sistema de gestión de cupos del Gimnasio Titan!")

opc = 0

while opc != 5:
    try:
        print("*** MENU PRINCIPAL ***")
        print("1.- Cupos disponibles.")
        print("2.- Realizar reservas.")
        print("3.- Cancelar reservas.")
        print("4.- Historial de reservas.")
        print("5.- Salir.")

        opc = int(input("Seleccione una opción: "))

        if opc == 1:
            print(f"Actualmente hay {cupos} cupos disponibles!")
        elif opc == 2:
            reserva = 0
            while reserva <= 0 or reserva > cupos:
                try:
                    reserva = int(input("Cuantos cupos desea reservar?: "))
                    if reserva > 0 and reserva < cupos:
                        print(f"Se han reservado {reserva} cupos")
                    else:
                        print("Datos invalidos")
                except:
                    print("Error!! Datos invalidos")
            cupos -= reserva
            historial += reserva
        elif opc == 3:
            cancelar = 0
            while cancelar <= 0 or cancelar > historial:
                try:
                    cancelar = int(input("Cuantos reservas desea cancelar?: "))
                    if cancelar > historial:
                        print("Imposible!! Datos incorrectos")
                    else:
                        print(f"Se han cancelado {cancelar} reservas exitosamente")
                except:
                    print("Datos invalidos")
            cupos += cancelar
            historial -= cancelar        
        elif opc == 4:
            print(f"Hoy se han hecho {historial} reservas")
        elif opc == 5:
            print("Gracias por utilizar nuestro software, hasta la próxima.")
            break
        else:
            print("Opcion invalida!!")
    except ValueError:
        print("Datos incorrectos")