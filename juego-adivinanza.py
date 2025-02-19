import random
def juego_adivinanza():
    #generar un numero del 1 al 100 
    numero_sec=random.randint(1,100)
    intentos = 0
    adivinado = False
    
    print("Bienvenido a la adivinanza de numero")
    print("debes adivinar del 1 al 100")
    while adivinado == False:
        a= input("ingrese un numero")
        if a.isdigit():
            a=int(a)
            intentos +=1
            if a < numero_sec:
                print("el num sec es mayor a", a)
            elif a > numero_sec:
                  print("el num sec es menor a",a)
            else:
                print ("FELICITACIONES HAS GANADO y lo has hecho en ", intentos, "intentos")
        else:
            print("porfavor ingrese un numero")
juego_adivinanza()
