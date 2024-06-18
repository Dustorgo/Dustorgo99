aprobados=0
cantidad=0
sumaAprobados=0
a=input("¿Analizar calificaciones? 'S' para 'sí':")
while a == "S":
    calificacion=int(input("Calificación de un alumno:"))
    if calificacion > 4:
        aprobados=aprobados+1
        sumaAprobados=sumaAprobados+calificacion
    cantidad=cantidad+1
    a=input("¿Continuar? 'S' para 'sí':")
print("Porcentaje de alumnos aprobados:", (aprobados*100)/cantidad, "%")
print("Promedio de los aprobados:", sumaAprobados/aprobados)