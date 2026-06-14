# Lista principal
registros = []

# ---------------- VALIDACIONES ----------------

def validar_campo_texto(texto): #cambiar nombre de función y parámetros según el contexto, por ejemplo validar_modelo(modelo) o validar_nombre(nombre)
    return texto.strip() != ""

def validar_numero(numero): #cambiar nombre de función y parámetros según el contexto, por ejemplo validar_anio(anio) o validar_precio(precio)
    return numero > 0

# ---------------- MENU ----------------

def mostrar_menu():
    print("\n===== MENÚ PRINCIPAL =====")
    print("1. Agregar")
    print("2. Buscar")
    print("3. Eliminar")
    print("4. Actualizar")
    print("5. Mostrar")
    print("6. Salir")

def leer_opcion(): #leer la opción del menú, validar que sea un número entre 1 y 6, y devolver la opción seleccionada
    while True:
        try:
            opcion = int(input("Ingrese una opción: "))
            if 1 <= opcion <= 6:
                return opcion
            else:
                print("Debe ingresar un número entre 1 y 6.")
        except:
            print("Ingrese un número válido.")

# ---------------- FUNCIONES ----------------

def agregar_registro(lista): #cambiar nombre de función y parámetros según el contexto, por ejemplo agregar_vehiculo(lista) o agregar_producto(lista)

    campo1 = input("Ingrese dato 1: ") #cambiar texto de "Ingrese dato 1" por el nombre del dato que se va a ingresar, como "Ingrese modelo" o "Ingrese nombre"
    try:
        campo2 = int(input("Ingrese año: ")) 
        campo3 = float(input("Ingrese precio: "))
    except:
        print("Año o precio inválido.")
        return

    # Validaciones
    if not validar_campo_texto(campo1):

        print("Dato inválido")
        return

    # Crear diccionario
    registro = {
        "campo1": campo1,
        "campo2": campo2,
        "campo3": campo3,
        "estado": False
    }

    lista.append(registro)
    print("Registro agregado")

def buscar_registro(lista, valor_buscado):

    for i in range(len(lista)):
        if lista[i]["campo1"] == valor_buscado:
            return i

    return -1

def eliminar_registro(lista):

    valor = input("Ingrese dato a eliminar: ")

    posicion = buscar_registro(lista, valor)

    if posicion != -1:
        lista.pop(posicion)
        print("Registro eliminado")
    else:
        print("Registro no encontrado")

def actualizar_estado(lista):

    for elemento in lista:

        # AQUÍ VA LA REGLA DE LA PRUEBA
        if True:
            elemento["estado"] = True
        else:
            elemento["estado"] = False

def mostrar_registros(lista):

    actualizar_estado(lista)

    for elemento in lista:
        print("------------------")
        print(elemento)

# ---------------- PROGRAMA PRINCIPAL ----------------

while True:

    mostrar_menu()
    opcion = leer_opcion()

    if opcion == 1:
        agregar_registro(registros)

    elif opcion == 2:

        valor = input("Ingrese dato a buscar: ")

        posicion = buscar_registro(registros, valor)

        if posicion != -1:
            print(registros[posicion])
        else:
            print("No encontrado")

    elif opcion == 3:
        eliminar_registro(registros)

    elif opcion == 4:
        actualizar_estado(registros)

    elif opcion == 5:
        mostrar_registros(registros)

    elif opcion == 6:
        print("Fin del programa")
        break