def validar_contrasena(password):
    if len(password) < 8:
        return False

    if " " in password:
        return False

    tiene_numero = False
    tiene_letra = False

    for caracter in password:
        if caracter.isdigit():
            tiene_numero = True
        if caracter.isalpha():
            tiene_letra = True

    return tiene_numero and tiene_letra


def ingresar_usuario(usuarios):
    while True:
        nombre = input("Ingrese nombre de usuario: ")

        if nombre in usuarios:
            print("Usuario ya existe. Intente otro.")
        else:
            break

    while True:
        sexo = input("Ingrese sexo: ").upper()

        if sexo == "M" or sexo == "F":
            break
        else:
            print("Debe ingresar M o F solamente. Intente de nuevo.")

    while True:
        password = input("Ingrese contraseña: ")

        if validar_contrasena(password):
            print("Contraseña valida.")
            break
        else:
            print("Contraseña no valida. Intente otra.")

    usuarios[nombre] = {
        "sexo": sexo,
        "password": password
    }

    print("Usuario ingresado con exito!!")


def buscar_usuario(usuarios):
    nombre = input("Ingrese usuario a buscar: ")

    if nombre in usuarios:
        print(
            f"El sexo del usuario es: {usuarios[nombre]['sexo']} "
            f"y la contraseña es: {usuarios[nombre]['password']}"
        )
    else:
        print("El usuario no se encuentra.")


def eliminar_usuario(usuarios):
    nombre = input("Ingrese usuario a eliminar: ")

    if nombre in usuarios:
        del usuarios[nombre]
        print("Usuario eliminado con éxito!")
    else:
        print("No se pudo eliminar usuario!")


def mostrar_menu():
    print("\nMENU PRINCIPAL")
    print("1.- Ingresar usuario.")
    print("2.- Buscar usuario.")
    print("3.- Eliminar usuario.")
    print("4.- Salir.")


def main():
    usuarios = {}

    while True:
        mostrar_menu()

        opcion = input("Ingrese opción: ")

        if opcion == "1":
            ingresar_usuario(usuarios)

        elif opcion == "2":
            buscar_usuario(usuarios)

        elif opcion == "3":
            eliminar_usuario(usuarios)

        elif opcion == "4":
            print("Programa terminado...")
            break

        else:
            print("Debe ingresar una opción válida!!")


main()