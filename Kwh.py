import os
os.system ('cls')

def calcular_consumo(valor_estrato, consumo_actual, consumo_anterior):
    consumo_mes = consumo_actual - consumo_anterior
    if consumo_mes <= 104:
        return 54000, consumo_mes
    elif 105 <= consumo_mes <= 1876:
        return valor_estrato * consumo_mes, consumo_mes
    else:
        return (valor_estrato * consumo_mes) * 1.14, consumo_mes

while True:
    try:
        NIC = input("NIC: ")
        titular_pago = input("Titular del pago: ")
        direccion = input("Dirección: ")
        ciudad = input("Ciudad: ")
        estrato = int(input("Estrato: "))
        num_medidor = input("Número del Medidor: ")
        fecha_lectura_actual = input("Fecha Lectura Actual (yyyy-mm-dd): ")
        lectura_actual = float(input("Lectura Actual (KWh): "))
        fecha_lectura_anterior = input("Fecha Lectura Anterior (yyyy-mm-dd): ")
        lectura_anterior = float(input("Lectura Anterior (KWh): "))

        if 1 <= estrato <= 3:
            valor_estrato = 2742
        elif 4 <= estrato <= 5:
            valor_estrato = 3468
        elif 6 <= estrato <= 8:
            valor_estrato = 4964
        else:
            print("Estrato no válido.")
            continue

        valor_consumo, consumo_mes = calcular_consumo(valor_estrato, lectura_actual, lectura_anterior)

        print("\nDatos del Cliente:")
        print("NIC:", NIC)
        print("Titular del pago:", titular_pago)
        print("Dirección:", direccion)
        print("Ciudad:", ciudad)
        print("Estrato:", estrato)
        print("Número del Medidor:", num_medidor)
        print("Fecha Lectura Actual:", fecha_lectura_actual)
        print("Lectura Actual (KWh):", lectura_actual)
        print("Fecha Lectura Anterior:", fecha_lectura_anterior)
        print("Lectura Anterior (KWh):", lectura_anterior)
