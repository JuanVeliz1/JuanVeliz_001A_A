import funciones as fn

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

while True:

    print("""
    ------menu------
    1.- asignar sueldos
    2.- clasificar sueldos
    3.- ver estadisticas
    4.- reporte sueldo
    5.- salir programa
    """)

    opc = int(input(" ingrese la opcion que desea utilizar (desde la opc 1 a la 5)\n "))    

    if opc == 1:
        asignarSueldos = fn.asignarSueldos(trabajadores)
        print("se han generado los sueldos de 10 trabajadores")
        
    elif opc == 2:
        fn.clasificarSueldos(trabajadores)
        if not asignarSueldos:
            print("primero genere los sueldos ")


    elif opc == 3:1
    sueldoMAX, sueldoMin, promSueldo, mediaAritmetica = fn.verEstadisticas(asignarSueldos)
    if promSueldo is not None:
        print("el sueldo maximo entre los trabajadores fue de $", sueldoMAX)
        print("el sueldo minimo entre los trabajadores fue de $", sueldoMin)
        print("el sueldo promediado entre los trabajadores fue de $", promSueldo)
        print("la media aritmetica entre los trabajadores fue de $", mediaAritmetica)


    elif opc == 4:
        fn.reporteSueldos(asignarSueldos)

    elif opc == 5:
        print("""
              finalizando programa, hasta luego... 
              Desarrollado por Carlos Vergara
              RUT 12.345.678-9
              """)
        break
    else:
        print("opcion ingresada de forma erronea, prueba de la opcion 1 a la 5")    
