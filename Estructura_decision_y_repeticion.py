opcion = 0
while opcion != 5:  
    print("(1) para sumar")
    print("(2) para restar")
    print("(3) para multiplicar")
    print("(4) para dividir")
    print("(5) TERMINAR")
    opcion = int(input("Seleccione una opcion "))
    if opcion != 5:
        primer_numero = int(input("Ingrese el primer numero "))
        segundo_numero = int(input("Ingrese el segundo numero "))
        if opcion == 1: 
            print("El resultado de la suma es " + str(primer_numero + segundo_numero))
        else:
            if opcion == 2:
                print("El resultado de la resta es " + str(primer_numero - segundo_numero))
            else:
                if opcion == 3:
                    print("El resultado de la multiplicacion es " + str(primer_numero * segundo_numero))
                else:
                    print("El resultado de la division es "  + str(primer_numero / segundo_numero))
            
        
