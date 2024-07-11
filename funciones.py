


import random
import csv
import statistics

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

def asignarSueldos(trabajadores):
    sueldosA = {}
    for trabajador in trabajadores:
        sueldos = random.randint(300000, 2500000)
        sueldosA[trabajador] = sueldos
    print("Los sueldos de los trabajadores se han creado de manera satisfactoria")
    print(sueldosA)
    return sueldosA

def clasificarSueldos(sueldosA):
    mayorA300 = {}
    igual800y2m = {}
    sueldos2m = {} 

    for trabajador, sueldo in sueldosA.items():
        if sueldo >= 2000000:
            sueldos2m[trabajador] = sueldo
        elif sueldo >= 800000:
            igual800y2m[trabajador] = sueldo
        elif sueldo >= 300000:
            mayorA300[trabajador] = sueldo
    return mayorA300, igual800y2m, sueldos2m

def verEstadisticas(sueldosA):
    sueldos = list(sueldosA.values())
    if not sueldos:
        print("No se pueden imprimir las estadísticas de sueldos")
        return None, None, None, None
    
    sueldoMAX = max(sueldos)
    sueldoMin = min(sueldos)
    promSueldos = sum(sueldos) / len(sueldos)
    mediaAritmetica = statistics.mean(sueldos)
    return sueldoMAX, sueldoMin, promSueldos, mediaAritmetica

def reporteSueldos(sueldosA):
    with open("reporteSueldo.csv", "w", newline="") as archivo:        
        escritor = csv.writer(archivo)           
        escritor.writerow(["Nombre trabajador", "Sueldo"])    
        for trabajador, sueldo in sueldosA.items():    
            escritor.writerow([trabajador, sueldo])        
    print("Se ha generado el reporte satisfactoriamente")
