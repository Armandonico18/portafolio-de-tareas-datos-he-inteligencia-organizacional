def binario_a_decimal(binario):
    return int(binario, 2)

def decimal_a_binario(decimal):
    return bin(decimal)[2:]

while True:
    print("Menú:")
    print("1. Convertir de binario a decimal")
    print("2. Convertir de decimal a binario")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Sumar")
    print("6. Restar")
    print("7. Salir")
    
    opcion = input("Elija una opción (1/2/3/4/5/6/7): ")
    
    if opcion == "1":
        binario = input("Introduce un número binario: ")
        try:
            decimal = binario_a_decimal(binario)
            print(f"El valor en decimal es: {decimal}")
        except ValueError:
            print("Entrada no válida. Debe ser un número binario válido.")
    
    elif opcion == "2":
        decimal = int(input("Introduce un número decimal: "))
        if decimal < 0:
            print("El número decimal debe ser positivo.")
        else:
            binario = decimal_a_binario(decimal)
            print(f"El valor en binario es: {binario}")
    
    elif opcion == "3":
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        resultado = num1 * num2
        print(f"El resultado de la multiplicación es: {resultado}")
    
    elif opcion == "4":
        num1 = float(input("Introduce el dividendo: "))
        num2 = float(input("Introduce el divisor: "))
        if num2 == 0:
            print("No se puede dividir entre cero.")
        else:
            resultado = num1 / num2
            print(f"El resultado de la división es: {resultado}")
    
    elif opcion == "5":
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))
        resultado = num1 + num2
        print(f"El resultado de la suma es: {resultado}")
    
    elif opcion == "6":
        num1 = float(input("Introduce el minuendo: "))
        num2 = float(input("Introduce el sustraendo: "))
        resultado = num1 - num2
        print(f"El resultado de la resta es: {resultado}")
    
    elif opcion == "7":
        print("¡Hasta luego!")
        break
    
    else:
        print("Opción no válida. Por favor, elija una opción válida (1/2/3/4/5/6/7).")