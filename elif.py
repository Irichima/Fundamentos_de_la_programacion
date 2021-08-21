opcion = 0
while opcion != 5:  
    print("""
        (1) para sumar
        (2) para restar
        (3) para multiplicar
        (4) para dividir
        (5) TERMINAR""")
    opcion = int(input("Seleccione una opcion "))
    if opcion != 5:
        primer_numero = int(input("Ingrese el primer numero "))
        segundo_numero = int(input("Ingrese el segundo numero "))
    if opcion == 1: 
        print("El resultado de la suma es " + str(primer_numero + segundo_numero))
    elif opcion == 2:
        print("El resultado de la resta es " + str(primer_numero - segundo_numero))
    elif opcion == 3:
        print("El resultado de la multiplicacion es " + str(primer_numero * segundo_numero))
    elif opcion == 4:
        print("El resultado de la division es "  + str(primer_numero / segundo_numero))
            
        
