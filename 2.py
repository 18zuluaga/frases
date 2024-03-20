"""
# palabra = input("ingrese una palabra:")
# palabra = palabra.lower()

# while palabra != "fin":
#     palabra = input("ingrese OTRA palabra:")
#     palabra = palabra.lower()
# print("fin programa")


# #capture n numeros y calcule la sumatoria de ellos el programa debe terminar cuando 
# # el usuario ingrese un 0
# numero = int(input("ingrese un numero"))
# suma= 0 
# cont = 0
# while 0 != numero:
#     suma += numero
#     numero = int(input("ingrese un numero:"))
#     cont += 1
# print(f"la sumatoria de los numeros es de {suma}")
# print(f"el promedio es de {suma/cont}")

#capturar n numeros y calcular el promedio de los numeros pares e inpares por separado y finaliza con 0
# numero = int(input("ingrese un numero"))
# suma= 0 
# cont = 0
# suma1=0
# cont1=0
# while 0 != numero:
#     if numero % 2 == 0 :
#         suma += numero
#         numero = int(input("ingrese un numero:"))
#         cont += 1
#     else :
#         suma1 += numero
#         numero = int(input("ingrese un numero:"))
#         cont1 += 1
# print(f"el promedio de los numeros pares es de {suma/cont}")
# print(f"el promedio de los numeros inpares es de {suma1/cont1}")

#########FOR###########

#mostar del 1 al 5 con para.....add()


# i = 1
# while i <= 5:
#     print(i)
#     i += 1
# print("fin programa")

# for i in range(10,20,2):
#     print(i)
# print("fin programa")


#capturar un numero y mostrar los divisores exactos de dicho numero

# num = int(input("ingresar numero:"))
# cont=0

# for i in range(1, num + 1):
#     if num  % i == 0:
#         print(i)
#         cont += 1
# print(f"hay {cont} divisores exactos de {num}")

# if cont == 2:
#     print(f"el numero {num} es primo")
# else:
#     print(f"el numero {num} no es primo")
    
    
# # se desea determinar el promedio de numeros que hay entre 5 y 25

# #ejercicio1
# cont=0
# suma = 0 

# for i in range(5,26):
#     suma+=i
#     cont+=1
# print(f"el promedio de numeros que hay entre 5 y 25 es de {suma/cont}")

#ejercicio 2 
# se desea capturar n numeros clacular el promedio que unuicamente seas multiplos de 7 

salir = input("desea poner otro numero").lower()
suma = 0
cont = 0

while salir != "no":
    numero = int(input("ingrese un numero"))
    if numero % 7 == 0 :
        suma+=numero
        cont+=1
    salir = input("desea poner otro numero").lower()
print(f"el promedio de los numeros que son multiplos de 7 es de {suma/cont}")

#ejercicio3
# # calcular el factorial de un numero ingresado por el usuario

num = int(input("ingresar numero:"))


for i in range(1,num):
    num *= i
print(F"el factorial es de {num}")

#ejercicio4
# #calculara la multiplicaion de dos numeros n y m con sumas 

n = int(input("ingresar numero:"))
m = int(input("ingresar numero:"))
suma = 0

for i in range (1,m+1):
    suma += n
print(f"el resultado de la multiplicacion es de {suma}")


#ejercicio 5
# # de un grupo de personas se desea determinar cuantos son hombres y cuantos son mujeres ingrese los datos  necesarios 
# #para calcular este dato y encuentre el porcentaje
personas = input("deseas agregar un hombre o una mujer, si deseas agregar un hombre 1 y una mujer 2").lower()
contm=0
cont=0
conth=0

while personas != "no":
    if personas == "1":
       conth += 1
    elif personas == "2":
        contm += 1 
    cont+=1
    personas = input("deseas agregar un hombre o una mujer, si deseas agregar un hombre 1 y una mujer 2").lower()
print(f"el porsentaje de hombres es de {conth*100/cont}% y el de las mujeres es de {contm*100/cont}% ")
"""

#ejercicio 6
# #calcular el promedio de 5 notas que tiene una materia  ademas determinar cual es la nota mas baja y la nota mas alta

# cont = 0
# suma = 0
# alta = 0
# baja = 5


# for i in range(1,6):
#     notas = float(input("ingrese las notas"))
#     if notas < baja:
#         baja = notas
#     if notas > alta:
#         alta = notas
#     suma += notas
#     cont += 1
# print(f"el promedio de las notas es de {suma/cont} la nota mas baja es de {baja} y la nota mas grande es de {alta}")

def prom(notas):
    
    promedio = sum(notas) / len(notas)
    
    alta = max(notas)
    baja = min(notas)
    
    resul = (promedio,alta,baja)
    
    return resul

nota = []
for i in range(1,6):
    nota.append(int(input("ingrese sus notas: ")))
    resultado = prom(nota)

print(f"Promedio: {resultado[0]}")
print(f"Nota más baja: {resultado[1]}")
print(f"Nota más alta: {resultado[2]}")



#ejercicio 7
# #leer n numeros cuantos son positivos cuantos son negativos y cuantos 0


# p= input("quieres agregar un numero")

# contp = 0
# cont=0
# contn = 0

# while "no" != p:
#     numero = int(input("ingrese un numero "))
#     if numero > 0 :
#         contp += 1
#     elif numero < 0 :
#         contn += 1
#     else:
#         cont += 1
#     p= input("quieres agregar un numero")
# print(f"los numeros positivos son {contp}")
# print(f"los numeros negativos son {contn}")
# print(f"los numeros cero son {cont}")
