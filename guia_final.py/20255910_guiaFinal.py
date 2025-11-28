cliente = []

def crear_clientes():
   
    dui = input("DUI: ")
    if len(dui)==10:
        if dui.count("-")==1 and dui.index("-")==8:
            if len(cliente) ==0:
                nombre = input("Nombre: ")
                Apellido = input("Apellido: ")
                if len(nombre)>= 2 and len(Apellido)>=2:
                    cliente.append({
                        "DUI":dui,
                        "Nombre":nombre,
                        "Apellido": Apellido
                    })
                else:
                    print("El nombre y el apellido debe contener más de 2 digitos")
            else: 
                nombre = input("Nombre: ")
                Apellido = input("Apellido: ")               
                for x in cliente:
                    for v in x.values():
                        if v == dui:
                            if len(nombre)>= 2 and len(Apellido)>=2:
                                cliente.append({
                                    "DUI":dui,
                                    "Nombre":nombre,
                                    "Apellido": Apellido
                                })
                            else:
                                print("El nombre y el apellido debe contener más de 2 digitos")
                        else:
                            print("El dui ya existe")
        else:
            print("Debe contener '-' y debe ser el antepenultimo digito")
    else:
        print("Debe de tener 10 digitos")




menu = True
while menu:
    opcion = input("Seleccione una opcion:\n•	Crear cliente\n•	Contratar servicio\n•	Listar clientes por servicio\n•	Salir\n")
    if opcion.lower() == "crear cliente":
        crear_clientes()
    elif opcion.lower() == "contratar servicio":
        print("servicio")
    elif opcion.lower() == "listar clientes por servicio":
        print(cliente)
    elif opcion.lower() == "salir":
        menu= False
    else:
        print("No es una opcion")


