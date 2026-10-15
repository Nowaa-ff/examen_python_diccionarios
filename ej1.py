menu = {
    1 : "Tienda",
    2 : "Jugar a un juego",
    3 : "Salir"
}
tienda = {
    "Acción": ["Mono enojado I", "Mono enojado II: La venganza"],
    "Ciencia Ficción": ["RoboBob"],
    "Terror": ["La maldición de la escuela técnica"]
}
biblioteca = {  
}

while True:
    print(" ————————————————————————————")
    print("|        ETec Station        |")
    print(" ————————————————————————————")
    
    for key, values in menu.items():
        print(key,":",values)
        print(" ")
       
    op = int(input("Ingrese la opción que desee: "))
        
    if op == 1:
        print("¡¡Bienvenido a la — Tienda — !!")
        desi = input("¿Desea comprar un juego? si/no: ")
        if desi == "si":
            print("Juegos disponibles según género:")
            print("  ——————————————————————————————  ")
            for elemento in tienda:
                print(f"{cont}: {""}")
            comp=""
            comp=input("Escriba el juego: ")
            
            if comp in tienda:
                print("¡Juego comprado!")
                cont=cont+1
                biblioteca[cont]=comp
                for key, values in biblioteca.items():
                    print(key,": ",values)
                    print(" ")
            else:
                print("Juego no encontrado")
                print(" ———————————————————————————")
        else:
            print("Ok chau")
            break
        