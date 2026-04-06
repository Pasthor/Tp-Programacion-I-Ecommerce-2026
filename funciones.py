def mostrarLogo():
    print("  ______  _____ ____  __  __ __  __ ______ _____   _____ ______ ")
    print(" |  ____|/ ____/ __ \\|  \\/  |  \\/  |  ____|  __ \\ / ____|  ____|")
    print(" | |__  | |   | |  | | \\  / | \\  / | |__  | |__) | |    | |__   ")
    print(" |  __| | |   | |  | | |\\/| | |\\/| |  __| |  _  /| |    |  __|  ")
    print(" | |____| |___| |__| | |  | | |  | | |____| | \\ \\| |____| |____ ")
    print(" |______|\\_____\\____/|_|  |_|_|  |_|______|_|  \\_\\\\_____|______|")


def crearUsuario():
    nombre = input("Ingrese su nombre: ")
    correo = input("Ingrese su correo electrónico: ")
    contrasenia = input("Ingrese su contraseña: ")
    print(f"Usuario creado exitosamente: {nombre}, {correo}")

def iniciarSesion():
    correo = input("Ingrese su correo electrónico: ")
    contrasenia = input("Ingrese su contraseña: ")
    print(f"Inicio de sesión exitoso para: {correo}")

def mostrar(msj):
    print(msj)

def loginSignUp():
    print("1. Iniciar Sesión")
    print("2. Crear Usuario")
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        iniciarSesion()
    elif opcion == "2":
        crearUsuario()
    else:
        print("No existe esa opción. Por favor, intentá nuevamente.")