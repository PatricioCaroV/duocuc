# Lista donde se guardarán los vehículos
vehiculos = []


def mostrar_menu():
    print("\n===== MENU PRINCIPAL =====")
    print("1. Agregar vehículo")
    print("2. Buscar vehículo")
    print("3. Eliminar vehículo")
    print("4. Actualizar disponibilidad")
    print("5. Mostrar vehículos")
    print("6. Salir")


def leer_opcion():
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe ingresar un número entre 1 y 6.")
        except:
            print("Ingrese un número válido.")


def validar_modelo(modelo):
    return modelo.strip() != ""


def validar_anio(anio):
    return anio > 1900


def validar_precio(precio):
    return precio > 0


def agregar_vehiculo(lista):
    modelo = input("Ingrese modelo: ")

    try:
        anio = int(input("Ingrese año: "))
        precio = float(input("Ingrese precio: "))
    except:
        print("Año o precio inválido.")
        return

    if not validar_modelo(modelo):
        print("El modelo no puede estar vacío.")
        return

    if not validar_anio(anio):
        print("El año debe ser mayor a 1900.")
        return

    if not validar_precio(precio):
        print("El precio debe ser mayor que 0.")
        return

    vehiculo = {
        "modelo": modelo,
        "anio": anio,
        "precio": precio,
        "disponible": False
    }

    lista.append(vehiculo)
    print("Vehículo agregado correctamente.")


def buscar_vehiculo(lista, modelo):
    for i in range(len(lista)):
        if lista[i]["modelo"] == modelo:
            return i
    return -1


def eliminar_vehiculo(lista):
    modelo = input("Ingrese el modelo a eliminar: ")

    posicion = buscar_vehiculo(lista, modelo)

    if posicion != -1:
        lista.pop(posicion)
        print("Vehículo eliminado.")
    else:
        print(f"El vehículo '{modelo}' no se encuentra registrado.")


def actualizar_disponibilidad(lista):
    for vehiculo in lista:
        if vehiculo["anio"] >= 2020:
            vehiculo["disponible"] = True
        else:
            vehiculo["disponible"] = False


def mostrar_vehiculos(lista):
    actualizar_disponibilidad(lista)

    print("\n=== LISTA DE VEHICULOS ===")

    if len(lista) == 0:
        print("No hay vehículos registrados.")
        return

    for vehiculo in lista:

        if vehiculo["disponible"]:
            estado = "DISPONIBLE"
        else:
            estado = "NO DISPONIBLE"

        print("Modelo:", vehiculo["modelo"])
        print("Año:", vehiculo["anio"])
        print("Precio:", vehiculo["precio"])
        print("Estado:", estado)
        print("*" * 40)


# Programa principal
while True:

    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_vehiculo(vehiculos)

    elif opcion == 2:
        modelo = input("Ingrese modelo a buscar: ")

        posicion = buscar_vehiculo(vehiculos, modelo)

        if posicion != -1:
            print("Vehículo encontrado:")
            print(vehiculos[posicion])
        else:
            print("Vehículo no encontrado.")

    elif opcion == 3:
        eliminar_vehiculo(vehiculos)

    elif opcion == 4:
        actualizar_disponibilidad(vehiculos)
        print("Disponibilidad actualizada.")

    elif opcion == 5:
        mostrar_vehiculos(vehiculos)

    elif opcion == 6:
        print("Gracias por usar el sistema. Vuelva pronto.")
        break