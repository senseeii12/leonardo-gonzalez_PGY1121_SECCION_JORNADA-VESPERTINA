import random

vehiculos = []

def grabar_vehiculo():
    print("\n--- Grabar Vehículo ---")
    tipo = input("Tipo de vehículo: ")
    patente = input("Patente: ")
    marca = input("Marca (entre 2 y 15 caracteres): ")

    while not (2 <= len(marca) <= 15):
        print("La marca debe tener entre 2 y 15 caracteres.")
        marca = input("Marca (entre 2 y 15 caracteres): ")

    precio = float(input("Precio (mayor a $5.000.000): "))

    while precio <= 5000000:
        print("El precio debe ser mayor a $5.000.000.")
        precio = float(input("Precio (mayor a $5.000.000): "))

    multas = {"monto": float(input("Monto de multas: ")), "fecha": input("Fecha de multas: ")}
    fecha_registro = input("Fecha de registro del vehículo: ")
    nombre_dueno = input("Nombre del dueño: ")

    vehiculo = {"Tipo": tipo, "Patente": patente, "Marca": marca, "Precio": precio,
                "Multas": multas, "Fecha de Registro": fecha_registro, "Dueño": nombre_dueno}

    vehiculos.append(vehiculo)
    print("Vehículo registrado exitosamente.")

def buscar_vehiculo():
    print("\n--- Buscar Vehículo ---")
    patente_buscar = input("Ingrese la patente a buscar: ")
    encontrado = False

    for vehiculo in vehiculos:
        if vehiculo["Patente"] == patente_buscar:
            print("\nInformación del vehículo encontrado:")
            for clave, valor in vehiculo.items():
                print(f"{clave}: {valor}")
            encontrado = True
            break

    if not encontrado:
        print("Vehículo no encontrado.")

def imprimir_certificados():
    print("\n--- Imprimir Certificados ---")
    for vehiculo in vehiculos:
        cert_emision = random.uniform(1500, 3500)
        cert_anotaciones = random.uniform(1500, 3500)
        cert_multas = random.uniform(1500, 3500)

        certificados = {
            "Emisión de contaminantes": cert_emision,
            "Anotaciones vigentes": cert_anotaciones,
            "Multas": cert_multas
        }

        for certificado, valor in certificados.items():
            print(f"\nCertificado de {certificado}:")
            print(f"Patente del auto: {vehiculo['Patente']}")
            print(f"Datos del dueño: {vehiculo['Dueño']}")
            print(f"Valor del certificado: ${valor:.2f}")

def main():
    print("Bienvenido a Auto Seguro - Registro de Vehículos")

    while True:
        print("""\n--- Menú ---
        1. Grabar Vehículo
        2. Buscar Vehículo
        3. Imprimir Certificados
        4. Salir""")

        opcion = input("Ingrese la opción deseada (1-4): ")

        if opcion == "1":
            grabar_vehiculo()
        elif opcion == "2":
            buscar_vehiculo()
        elif opcion == "3":
            imprimir_certificados()
        elif opcion == "4":
            print("\nGracias por utilizar Auto Seguro. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese una opción válida (1-4).")

if __name__ == "__main__":
    main()