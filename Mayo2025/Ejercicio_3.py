usuarios = {
    "iperurena": {
        "nombre": "Iñaki",
        "apellido": "Perurena",
        "password": "123123"
    },
    "fmuguruza": {
        "nombre": "Fermín",
        "apellido": "Muguruza",
        "password": "654321"
    },
    "aolaizola": {
        "nombre": "Aimar",
        "apellido": "Olaizola",
        "password": "123456"
    }
}

intentos_maximos = 3
intentos_realizados = 0

while intentos_realizados < intentos_maximos:
    usuario_ingresado = input("Introduce tu nombre de usuario: ")  # <--- Pedimos el nombre de usuario
    print(f"Usuario ingresado: '{usuario_ingresado}'")
    contrasena_ingresada = input("Introduce tu contraseña: ")

    if usuario_ingresado in usuarios:  # <--- Verificamos si el usuario existe
        if usuarios[usuario_ingresado]["password"] == contrasena_ingresada:
            print(f"\n¡Bienvenido, {usuarios[usuario_ingresado]['nombre']}!")
            break
        else:
            intentos_realizados += 1
            print("Contraseña incorrecta.")
    else:
        intentos_realizados += 1
        print("Usuario no encontrado.")

    if intentos_realizados < intentos_maximos:
        print(f"Te quedan {intentos_maximos - intentos_realizados} intentos.\n")
    else:
        print("\nNúmero máximo de intentos alcanzado. El acceso ha sido bloqueado.")