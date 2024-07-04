from os import system
system ("cls")

pedidos = []

def entero_positivo(valor):
    return valor.isdigit() and int(valor) >=0

def registrar_pedido():
    print("\Registro de nuevo pedido")

idpedido=input("Ingrese ID del pedido: ")
nombrecliente=input("Ingrese el nombre del cliente: ")
apellidocliente=input("Ingrese el apellido del cliente: ")
direccion=input("Ingrese la direccion del cliente: ")
comuna=input("Ingrese la comuna del cliente: ")

while True:
    dis6lt=input("Ingrese cantidad de dispensadores de 6 litros: ")
    dis10lt=input("Ingrese cantidad de dispensadores de 10 litros: ")
    dis20lt=input("Ingrese cantidad de dispensadores de 20 litros: ")

    if entero_positivo(dis6lt) and entero_positivo(dis10lt) and entero_positivo(dis20lt):
        dis6lt=int(dis6lt)
        dis10lt=int(dis10lt)
        dis20lt=int(dis20lt)

        if dis6lt>0 or dis10lt>0 or dis20lt>0:
            detallepedido=(f"Disponible 6lts: {dis6lt} Disponible 10lts: {dis10lt} Disponible 20lts: {dis20lt}")
            break
        else:
            print("La cantidad ingresada no es posible.")
    else:
        print("Error en cantidad pedida.")

pedidos.append({
    "idpedido": idpedido,
    "nombrecliente": nombrecliente,
    "apellidocliente": apellidocliente,
    "direccion": direccion,
    "comuna": comuna,
    "detallepedido": detallepedido,
    })
print("Pedido registrado correctamente")

def listarpedidos():
    print("\Lista de pedidos")
    if len(pedidos)==0:
        print("No hay pedidos registrados")
    else:
        for pedido in pedidos:
            print(f"ID pedido: {pedido[idpedido]}")
            print(f"Cliente: {pedido[nombrecliente]}")
            print(f"Apellido: {pedido[apellidocliente]}")
            print(f"Comuna: {pedido[comuna]}")
            print(f"Direccion: {pedido[direccion]}")
            print(f"Detalle pedido: {pedido[detallepedido]}")

def imprimirhojaruta():
    print("\Seleccionar sector disponible para realizar ruta:")

def main():
    while True:
        print("\Bienvenido a CleanWasser ahora selecciona una opcion a seguir")
        print("1- Registrar pedido")
        print("2- Lista de los pedidos")
        print("3- Imprimir hoja de ruta")
        print("4- Buscar un pedido por ID")
        print("5- Salir del programa")
        opcion=input("Seleccionar una opcion:")

        if opcion=="1":
            registrar_pedido
        elif opcion=="2":
            listarpedidos
        elif opcion=="3":
            imprimirhojaruta
        elif opcion=="4":
            pass
        elif opcion=="5":
            print("Gracias por utilizarnos, vuelva pronto.")
        else:
            print("Opcion no valida.")

if __name__=="__main__":
    main()


