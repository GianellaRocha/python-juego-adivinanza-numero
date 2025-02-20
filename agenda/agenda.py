def menu():
    print("\n Agenda de contactos:")
    print("1. Agregar nuevo contacto")
    print("2. Eliminar contato")
    print("3. Buscar contacto")
    print("4. lista de contactos")
    print("5. Salir")
def agregar(agenda):
    nombre= input("nombre")
    telefono= input("telefono")
    email= input("email")
    agenda[nombre]={"telefono":telefono, "email":email}
    print("se ha agregado correctamente")
def eliminar(agenda):
    nombre= input("ingrese el nombre a eliminar")
    if nombre in agenda:
        del agenda[nombre]
        print("contacto eliminado")
    else:
        print("no se ha encontrado el contacto")
def buscar(agenda):
    nombre= input("ingrese el nombre a buscar")
    if nombre in agenda:
        print("nombre:", nombre)
        print("telefono:", agenda[nombre["telefono"]])
        print("email:", agenda[nombre]["email"])
    else:
        print("el contacto no se encuentra ")
def listado(agenda):
    if agenda:
        print("\nLista de contactos:")
        for nombre, info in agenda.items():
            print("nombre:",nombre)
            print("telefono:", info["telefono"])
            print("email", info["email"])
            print("-" * 20)
    else:
        print("la agenda esta vacia ")
def agenda():
    agenda = {}
    while True:
        menu()
        a = input("elija una opcion")
        if a == "1":
            agregar(agenda)
        elif a == "2":
            eliminar(agenda)
        elif a == "3":
            buscar(agenda)
        elif a =="4":
            listado(agenda)
        elif a =="5":
            print("salida")
            break
        else:
            print("por favor elija una opcion dentro de 1 a 5")
agenda()