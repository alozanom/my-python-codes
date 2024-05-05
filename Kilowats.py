import os
os.system ('cls')

def calcular_tarifa(estrato, consumo):
    tarifa = 0
    if estrato in [1, 2, 3]:
        tarifa = 2742
    elif estrato in [4, 5]:
        tarifa = 3468
    elif estrato in [6, 7, 8]:
        tarifa = 4964

    if consumo <= 104:
        return 54000
    elif consumo <= 1876:
        return consumo * tarifa
    else:
        return consumo * tarifa * 1.14

def procesar_cliente():
    nic = input("NIC: ")
    titular_pago = input("Titular del pago: ")
    direccion = input("Dirección: ")
    ciudad = input("Ciudad: ")
    estrato = int(input("Estrato: "))
    numero_medidor = input("Número del Medidor: ")
    fecha_actual = input("Fecha Lectura Actual (YYYY-MM-DD): ")
    lectura_actual = float(input("Lectura Actual (KWh): "))
    fecha_anterior = input("Fecha Lectura Anterior (YYYY-MM-DD): ")
    lectura_anterior = float(input("Lectura Anterior (KWh): "))

    consumo_mes = lectura_actual - lectura_anterior
    valor_consumo_mes = calcular_tarifa(estrato, consumo_mes)

    print("\nDatos del Cliente:")
    print("NIC:", nic)
    print("Titular del pago:", titular_pago)
    print("Dirección:", direccion)
    print("Ciudad:", ciudad)
    print("Estrato:", estrato)
    print("Número del Medidor:", numero_medidor)
    print("Fecha Lectura Actual:", fecha_actual)
    print("Lectura Actual (KWh):", lectura_actual)
    print("Fecha Lectura Anterior:", fecha_anterior)
    print("Lectura Anterior (KWh):", lectura_anterior)
    print("Consumo del Mes (KWh):", consumo_mes)
    print("Valor del Consumo del Mes:", valor_consumo_mes)

# Procesar clientes hasta que el usuario decida salir
while True:
    # procesar_cliente()
    respuesta = input("\n¿Desea procesar otro cliente? (s/n): ")
    print(respuesta)
    print(respuesta.lower()) 
    if respuesta.lower() != 's':
        break
