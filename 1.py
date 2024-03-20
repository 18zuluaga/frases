#ejemplos

#elabore un algoritmo que capture el sexo de una persona y la salude deacuerdo a dicho sexo


# nombre = input("ingrese su nombre")
# sexo = input("ingrese 'M' o 'm' para masculino o 'F' o 'f' para femenino")

# match(sexo):
#     case "F":
#         print(f"Hola {nombre} ")
#     case "f":
#         print(f"Hola {nombre} ")
#     case "m":
#         print(f"Hola señor!! {nombre}")
#     case "M": 
#         print(f"Hola señor!! {nombre}")
#     case _:
#         print(f"señor usuario error en el ingreso de datos")
        

#una empresa decide otorgar un bono de temporada pero desea hacerlo deacuerdo al estrato de los trabajadores 
# de la siguiente manera si el tabajador es 
# si es estrato uno dara un bono del 35%
# si es estrato 2 el bono sera del 25%
# si es estrato 3 el bono sera del 20%
# si es estrato 4 el bono sera del 15%
# los demas estratos tendran un bono del 10%
# haga un programa que calcule el estrato y el valor a pagar


# sueldo = float(input("ingrese su salario"))
# estrato = int(input("ingrese su estrato"))


# match(estrato):
#     case 1:
#          print(f"el valor a pagar es de {sueldo*0.35+sueldo} y el bono fue de {sueldo*0.35}")
#     case 2:
#          print(f"el valor a pagar es de{sueldo*0.25+sueldo} y el bono fue de {sueldo*0.25}")
#     case 3:
#          print(f"el valor a pagar es de{sueldo*0.20+sueldo} y el bono fue de {sueldo*0.20}")
#     case 4:
#          print(f"el valor a pagar es de{sueldo*0.15+sueldo} y el bono fue de {sueldo*0.15}")
#     case 5:
#          print(f"el valor a pagar es de{sueldo*0.10+sueldo} y el bono fue de {sueldo*0.10}")
#     case 6:
#          print(f"el valor a pagar es de{sueldo*0.10+sueldo} y el bono fue de {sueldo*0.10}")
#     case _:
#          print(f"has ingresado un dato erronio"


##while

# i = 1

# while i <= 5:
#       print(i)
#       i += 1
# print("fin programa")


#mostrar los numeros pares que hay entre 1 y 10

# i = 1 

# while i <= 10:
#      if i % 2 == 0:
#           print(i)
#      i += 1
# print("fin del algoritmo")


# muestre los valores multiplos entre 5 y 7 que hay entre 1 y  100

# i = 1 
# cont = 0

# while i <= 100:
#      if i % 5 == 0 and i % 7 == 0:
#           cont += 1
#           print(i)
#      i += 1
# print(f"hay {cont} numero multiplos de 5 y 7")
# print("fin del algoritmo")

#muestre los valores pares o multiplos de 7 que hay entre 20 y 50

# i = 20 

# while i <= 50 :
#      if i % 2 == 0 or i % 7 == 0:
#           print(i)
#      i += 1
# print("fin del algoritmo")

# i = 1
# suma = 0
# while i <= 5:
#       print(i)
#       suma = suma + i 
#       i += 1
# print("el valor de la suma es: "+ str(suma))
# print("fin programa")

#sumar de 10 hasta 20 
#ejercicio 1

# i = 10
# suma = 0
# while i <= 20:
#       print(i)
#       suma = suma + i 
#       i += 1
# print("el valor de la suma es: "+ str(suma))
# print("fin programa")

# #ejercicio 2

# i = 3
# suma = 0
# while i <= 20:
#       print(i)
#       suma = suma + i 
#       i += 3
# print("el valor de la suma es: "+ str(suma))
# print("fin programa")

# #ejercicio 3

# i = 200 
# cont = 0

# while i <= 432:
#      if i % 2 == 0 and i % 7 == 0:
#           cont += 1
#           print(i)
#      i += 1
# print(f"hay {cont} numeros pares multiplos de 7 entre 200 y 432")
# print("fin del algoritmo")

# #ejercicio4

# i = 100
# suma = 0
# while i <= 330:
#      if i % 2 == 0:
#           suma = suma + i 
#      i += 1
# print("el valor de la suma es: "+ str(suma))
# print("fin programa")

# #ejercicio5

# i = 100
# suma = 0
# cont = 0
# while i <= 330:
#      if i % 2 == 0:
#           cont += 1    
#           suma = suma + i 
#      i += 1
# print("el promedio del punto 3 es de ", suma/cont)
# print("fin programa")



# i = 200 
# suma = 0
# cont = 0

# while i <= 432:
#      if i % 2 == 0 and i % 7 == 0:
#           cont += 1
#           suma = suma + i 
#      i += 1
# print("el promedio del punto 4 es de ", suma/cont)
# print("fin del algoritmo")

# #ejercicio6

# i = 1
# cont = 0
# suma = 0

# while i <=5:
#      numeros = int(input("ingrese un numero"))
#      cont += 1
#      suma += numeros
#      i += 1

# print(f"el promedio es de {suma/cont}")

# #ejercicio7

# i = 1
# cont = 0
# suma = 0

# while i <=5:
#      numeros = int(input("ingrese sus notas"))
#      cont += 1
#      suma += numeros
#      i += 1

# print(f"el promedio es de {suma/cont}")

# numero = int(input("ingrese un numero natural"))
# i = 1
# suma = 0
# while i <= numero:
#      suma += i
#      i += 1
# print("la suma es de",suma)


# numero = int(input("ingrese un numero natural"))
# suma = 0
# while numero>0:
#      suma += numero
#      numero = int(input("ingrese un numero natural"))
# print("la suma es de",suma)

# i = 1
# cont = 0
# suma = 0

# while i <=7:
#      numeros = int(input("ingrese un numero"))
#      if numeros % 2 == 0:
#           cont += 1
#           suma += numeros
#      i += 1
# print(f"el promedio es de {suma/cont}")

# i = 1
# cont = 0

# while i <=7:
#      numeros = int(input("ingrese un numero"))
#      if numeros % 2 == 0:
#           cont += 1
#      i += 1
# print(f"los numeros pares son {cont}")

# i = 1
# suma = 0
# while i <= 10:
#      numeros = int(input("ingrese una edad"))
#      suma += numeros 
#      i += 1
# print("el valor de la suma es: "+ str(suma))
# print("fin programa")

# i = 1
# cont = 0
# suma = 0

# while i <=5:
#      numeros = float(input("ingrese la altura"))
#      cont += 1
#      suma += numeros
#      i += 1

# print(f"el promedio es de {suma/cont}")

# i = 1
# cont = 0

# while i <=10:
#      numeros = int(input("ingrese un numero"))
#      if numeros>100:
#           cont += 1
#      i += 1
# print(f"los numeros mayores que 100 son {cont}")

# while i <=7:
#      numeros = int(input("ingrese un numero"))
#      if numeros % 3 == 0:
#           cont += 1
#      i += 1
# print(f"los numeros divisibles en 3 son {cont}")

# numero = int(input("ingrese un numero natural"))
# i = 1
# suma = 0
# while i <= numero:
#      if numero % 2 == 0: 
#           suma += i
#      i += 1
# print("la suma es de",suma)


# i = 1
# suma = 0
# while i <= 10:
#      numero = int(input("ingrese un numero "))
#      if numero <0: 
#           suma += numero
#      i += 1
# print("la suma es de",suma)

# i = 1
# cont = 0

# while i <=7:
#      numeros = int(input("ingrese un numero"))
#      if numeros % 5 == 0:
#           cont += 1
#      i += 1
# print(f"los numeros multiplos de 5 son {cont}")

# suma = 0
# i = 1
# print(suma)
# print(i)

# while i <= 100:
#      suma += i 
#      print(suma)
#      i += suma
#      print(i)
     

import random

numero_aleatorio = random.randint(1, 10)  # Genera un número aleatorio entre 1 y 10 (inclusive)
print(numero_aleatorio)
while True:
     import random
     numero_aleatorio = random.randint(1, 3)  # Genera un número aleatorio entre 1 y 10 (inclusive)
     va = input("escoja piedra, papel o tijera") .lower()
     puntos = 0
     if va == "piedra":
          if 1 == numero_aleatorio:
               puntos += 1
               print("la maquina saco piedra sumas un punto")
          elif numero_aleatorio == 2:
               puntos += -3
               print("la maquina saco papel pierdes 3 puntos")
          elif numero_aleatorio == 3:
               puntos += 3
               print("ganaste la maquina saco tijera sumas 3 puntos")
     elif va == "papel":
          
          if 2 == numero_aleatorio:
               puntos += 1
               print("empate la maquina saco papel sumas 1 punto")
          elif numero_aleatorio == 3:
               puntos += -3
               print("perdiste la maquina saco tijeras pierdes 3 puntos")
          elif numero_aleatorio == 1:
               puntos += 3
               print("ganaste la maquina saco piedra sumas 3 puntos")
     elif va == "tijera":
          
          if 3 == numero_aleatorio:
               puntos += 1
               print("empate la maquina saco tijera sumas 1 punto")
          elif numero_aleatorio == 1:
               puntos += -3
               print("perdiste la maquina saco piedra pierdes 3 puntos")
          elif numero_aleatorio == 2:
               puntos += 3
               print("ganaste la maquina saco papel sumas 3 puntos")
     elif va == "puntos":
          print(puntos)
     elif va == "salir":
          break

if va == "puntos":
          print(puntos)
          
