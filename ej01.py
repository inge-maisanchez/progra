print("SISTEMA DE REGISTRO DE PILOTOS")

cadete = 0
comandante = 0
pilotos = int(input("Cuantos pilotos desea registrar?: "))
cantidad = pilotos
for b in range(pilotos):
    nombre = ""  
    
    while len(nombre) < 6:
        nombre = input(f"Nombre del piloto {b+1}: ").title().replace(" ", "") #El ".title" convierte la primer letra despues de un espacio en MAYUSCULA y todo lo demas a minuscula
                                                                              #El ".replace(" ", "")" sirve para reemplazar los espacios
        
        if len(nombre) < 6:
            print("¡Error: El nombre formateado debe tener al menos 6 caracteres! Intenta de nuevo.")
    print(f"-> Registrado con éxito como: {nombre}")

#for b in range(cantidad):
    #cantidad = 0
    #nombre = input("Ingrese nombre del piloto: ")
#    if len(nombre) < 6:
#        print("Debe contener al menos 6 caracteres!!")
#    elif len(nombre) >= 6:
#        print("Registrado")  
#        cantidad = b+1
#    else:
#        print("Ta mal")
# Este era mi codigo con el error para los nombres

for i in range(pilotos):
    nivel = 0
    while nivel <= 0:
        try:
            nivel = int(input("Ingrese nivel de piloto: "))
            piloto = i+1
            if nivel >= 40:
                print("Se ha registrado un Comandante Galactico!!")
                comandante += 1
            elif nivel <= 0:
                print("Nivel incorrecto")
            else:
                print("Se ha registrado un Cadete estelar!!")
                cadete += 1
        except:
            print("¡Error de calibración! Ingresa un número entero positivo para el nivel de vuelo.")
print(f"¡La flota estelar cuenta con {comandante} Comandantes Galácticos y {cadete} Cadetes Estelares! ¡Preparense para despegar!")

