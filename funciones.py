import random
import csv
import statistics

trabajadores = ["Juan Pérez", "María García", "Carlos López", "Ana Martínez", "Pedro Rodríguez", "Laura Hernández", "Miguel Sánchez", "Isabel Gómez", "Francisco Díaz", "Elena Fernández"]

def asignarSueldos(trabajadores):
    sueldosA = {}
    for trabajador in trabajadores:
        sueldos = random.randint(300000,2500000)
        sueldosA [trabajador] = sueldos
        print("los sueldos de los trabajadores creado de manera satisfactora")
    print(sueldosA)
    return asignarSueldos


def clasificarSueldos(sueldosA):
    mayorA300 = {}
    igual800y2m = {}
    sueldos2m = {} 

    for trabajadores, sueldos in sueldosA.item():
        if sueldos >= 300000:
            mayorA300[trabajadores] = sueldos
        elif sueldos >= 800000 < 2000000:
            igual800y2m[trabajadores] = sueldos
        elif sueldos >=2000000:
            sueldos2m[trabajadores] = sueldos  
    return clasificarSueldos

def verEstadisticas(sueldosA):
    sueldos = list(sueldosA.values())
    if not sueldos:
        print("no se puede imprimir las estadisticas de sueldos ")
        return None,None,None
    
    sueldoMAX = max(sueldos)
    sueldosMin = min(sueldos)
    promSueldos = sum(sueldos)/ len(sueldos)
    mediaAritmetica = statistics.geometric_mean(sueldos)
    return sueldoMAX, sueldosMin, promSueldos, mediaAritmetica




def reporteSueldos (sueldosA):

    with open("reporteSueldo.csv","w",newline="") as archivo:        
        escritor= csv.writer(archivo)           
        escritor.writerow(["trabajadores", "sueldosA"])    
        for trabajadores in sueldos:                        
            for trabajadores, sueldos in trabajadores.items():    
                escritor.writerow([trabajadores, sueldos])        
    print("Se ha generado el reporte satisfactoriamiente")
    
