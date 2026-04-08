msjSeleccione = "Seleccione una opción: "
msjNoExiste = "Opción no válida. Por favor, intente de nuevo."

def mostrarLogo():
    print("  ______  _____ ____  __  __ __  __ ______ _____   _____ ______ ")
    print(" |  ____|/ ____/ __ \\|  \\/  |  \\/  |  ____|  __ \\ / ____|  ____|")
    print(" | |__  | |   | |  | | \\  / | \\  / | |__  | |__) | |    | |__   ")
    print(" |  __| | |   | |  | | |\\/| | |\\/| |  __| |  _  /| |    |  __|  ")
    print(" | |____| |___| |__| | |  | | |  | | |____| | \\ \\| |____| |____ ")
    print(" |______|\\_____\\____/|_|  |_|_|  |_|______|_|  \\_\\\\_____|______|")

def verificarCorreo (nomFuncion):
    correo = input("Ingrese su correo electrónico: ")
    if "@" not in correo or "." not in correo:
        print("Correo electrónico inválido. Por favor, intente de nuevo.")
        return nomFuncion()
    return correo

def verificarContrasenia (nomFuncion):
    contrasenia = input("Ingrese su contraseña (mínimo 6 caracteres): ")
    if len(contrasenia) < 6:
        print("La contraseña debe tener al menos 6 caracteres. Por favor, intente de nuevo.")
        return nomFuncion()
    return contrasenia

def crearUsuario():
    nombre = input("Ingrese su nombre: ")
    correo = verificarCorreo(crearUsuario)
    contrasenia = verificarContrasenia(crearUsuario)
    print(f"Bienvenid@ {nombre}, {correo}! Tu cuenta se creó exitosamente.")

def iniciarSesion():
    correo = verificarCorreo(iniciarSesion)
    contrasenia = verificarContrasenia(iniciarSesion)
    print(f"Bienvenid@ de nuevo {correo}!")

def mostrar(msj):
    print(msj)

# Función para el proceso de login o creación de usuario
def loginSignUp():
    print("1. Iniciar Sesión")
    print("2. Crear Usuario")
    opcion = input(msjSeleccione)
    if opcion == "1":
        iniciarSesion()
    elif opcion == "2":
        crearUsuario()
    else:
        while opcion not in ["1", "2"]:
            print(msjNoExiste)
            opcion = input(msjSeleccione)

# Función para elegir método de envío
def elegirEnvio():
    print("Seleccione el método de envío:")
    print("1. Envío estándar de 5 a 7 días hábiles")
    print("2. Envío express de 1 a 2 días hábiles")
    print("3. Retiro en el local")
    opcion = input(msjSeleccione)
    if opcion == "1":
        print("Seleccionaste envío estándar.")
    elif opcion == "2":
        print("Seleccionaste envío express.")
    elif opcion == "3":
        print("Seleccionaste retiro en el local.")
    else:
        while opcion not in ["1", "2", "3"]:
            print(msjNoExiste)
            opcion = input(msjSeleccione)
    return int(opcion)

# Generador de código de seguimiento random
def randomNumber():
    import random
    return str(random.randint(10000000000, 99999999999))

# Resumen compra
def mostrarMensajeFinal(tipoEnvio):
    if tipoEnvio == 1:
        mostrar("Seleccionaste envío estándar. Tu pedido llegará dentro de 5 a 7 días hábiles.")
        mostrar(f"El código de seguimiento de tu pedido es: {randomNumber()}")
    elif tipoEnvio == 2:
        mostrar("Seleccionaste envío express. Tu pedido llegará dentro de 1 a 2 días hábiles.")
        mostrar(f"El código de seguimiento de tu pedido es: {randomNumber()}")
    elif tipoEnvio == 3:
        mostrar("A partir de mañana vas a poder retirar tu pedido en nuestro local.")
        mostrar("Nuestro horario de atención es de lunes a viernes de 9 a 18 horas. Te esperamos!")

# Mostrar productos disponibles
def verProductos(productos, productosPrecio):
    print("Productos disponibles:")
    for i in range(len(productos)):
        print(f"{i + 1}. {productos[i]} - Precio: ${productosPrecio[i]}")


def mostrarPrompt(titulo, opciones):
    """
    Funcion de utilidad para mostrar un prompt multiple choice en pantalla y devolver opcion elegida \n
    Entrada: titulo de prompt, lista de opciones \n
    Salida: numero de opcion elegida
    """

    print(titulo)
    for i in range(len(opciones)):
        print(f"{i+1} - {opciones[i]}")
    return int(input(msjSeleccione))

def buscarProducto(productos, productosCategoria, productosPrecio):
    """
    Imprime todos los productos que coinciden con el nombre, la categoria o el precio definido por el usuario \n
    Entrada: listas paralelas de productos, productosCategoria y productosPrecio \n
    Salida: N/A, hace un print en pantalla
    """

    tipo = mostrarPrompt("Seleccione tipo de busqueda:",["Nombre","Categoria","Precio"])
    prodNums = []

    if tipo == 1:
        nom = input("Ingrese el nombre del producto: ").lower()
        for i in range(len(productos)):
            if nom in productos[i].lower():
                prodNums.append(i)
    
    print("Productos disponibles:")
    for i in range(len(prodNums)):
        print(f"{i + 1}. {productos[prodNums[i]]} - Precio: ${productosPrecio[prodNums[i]]}")