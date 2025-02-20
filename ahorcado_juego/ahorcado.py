import random
def ahorcado ():
    palabras = ["roma", "amor", "ojo", "boca","beso"]
    return random.choice(palabras)
def progreso(palabra, letras_adivinadas):
    adivinado = ""
    for letra in palabra:
        if letra in letras_adivinadas:
             adivinado += letra
        else:
            adivinado += "-"
    return adivinado
def juego():
    palabra = ahorcado()
    letras_adivinadas = []
    intentos = 5
    juego_terminado = False
    print (progreso(palabra, letras_adivinadas))
    while not juego_terminado and intentos > 0:
        a = input("introduce una letras:").lower()
        if len(a) !=1 or not a.isalpha():
            print("ingrese una letra valida")
        elif a  in letras_adivinadas:
            print("ya utilizaste esa letra")
        else:
            letras_adivinadas.append(a)
            if a in palabra:
                print("felicitaciones acertaste")
            else:
                intentos -=1
                print("no has acertado, te quedan", intentos,"intentos")
        progreso_actual= progreso(palabra,letras_adivinadas)
        print(progreso_actual)
        if "-" not in progreso_actual:
            juego_terminado = True
            print("felicitaciones has ganado")
    if intentos == 0:
        print("has perdido, la palabra secreta era",palabra)
            
juego()
