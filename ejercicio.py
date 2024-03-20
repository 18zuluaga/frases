# sueldo = float(input("ingrese su salario"))
# continua = True
# alimentos = []
# transporte = []
# vivienda = []
# entretenimiento = []

# while continua != False:
#     categoria = input("ingrese en que categoria quieres ingresar el gasto 1=alimentos 2=transporte 3=vivienda 4=entretenimiento 5=para no agregar mas gastos")
#     if categoria == "5":
#         continua = False
#     elif categoria == "1":
#         gasto = float(input("ingrese el gasto que tuvo en alimentos"))
#         alimentos.append(gasto)
#     elif categoria == "2":
#         gasto = float(input("ingrese el gasto que tuvo en trasporte"))
#         transporte.append(gasto)    
#     elif categoria == "3":
#         gasto = float(input("ingrese el gasto que tuvo en vivienda"))
#         vivienda.append(gasto)
#     elif categoria == "4":
#         gasto = float(input("ingrese el gasto que tuvo en entretenimiento"))
#         entretenimiento.append(gasto)

# sumaTotal = sum(alimentos)+sum(transporte)+sum(vivienda)+sum(entretenimiento)
# saldoRestante = sueldo-sumaTotal

# if saldoRestante < 0:
#     print("stás gastando más de lo que ganas.")
#     print(f"tu saldo restante es de {saldoRestante}, tu total de los gastos es de {sumaTotal}, los gastos en aliementos es de {sum(alimentos)}, los gastos en trasporte son de {sum(transporte)}, los gastos en vivienda son de {sum(vivienda)} y los gastos en entretenimiento son {sum(entretenimiento)} ")
# else:
#     print(f"tu saldo restante es de {saldoRestante}, tu total de los gastos es de {sumaTotal}, los gastos en aliementos es de {sum(alimentos)}, los gastos en trasporte son de {sum(transporte)}, los gastos en vivienda son de {sum(vivienda)} y los gastos en entretenimiento son {sum(entretenimiento)} ")
    
    
#ejercicio dos

import random

continua = True
print("Bienvenido al laberinto")
while continua:
    op = int(input("deseas girar ala derecha o ala izquierda \n para girara derecha =1 \n para girara ala izquierda =2 \n 0 salir "))
    numero_aleatorio1 = random.randint(1, 2)
    numero_aleatorio2 = random.randint(1, 4)
    numero_aleatorio3 = random.randint(1, 10)
    if op ==0:
        break
    if op == 1:
        if numero_aleatorio1 == 1:
            if numero_aleatorio3 == 5:
                print("Encontaste la llave ¡Felicidades, has escapado del laberinto!")
                continua = False
            elif numero_aleatorio2 == 1:
                print("te encontraste un objeto sombrero")
            elif numero_aleatorio2 == 2:
                print("te encontraste un objeto cuerda")
            elif numero_aleatorio2 == 3:
                print("te encontraste un objeto piel")
            elif numero_aleatorio2 == 4:
                print("te encontraste un objeto piedra")
        elif numero_aleatorio1 == 2:
            if numero_aleatorio3 == 5:
                print("Te encontrate con el jefe  Game Over")
                continua = False
            elif numero_aleatorio2 == 1:
                print("te encontraste un enano pero lo venciste")
            elif numero_aleatorio2 == 2:
                print("te atrapo un Narizon pero te lograste escabullir")
            elif numero_aleatorio2 == 3:
                print("Casi caes en una trampa")
            elif numero_aleatorio2 == 4:
                print("una rapiabispula casi te pica pero sigues con vida")
    if op == 2:
        if numero_aleatorio1 == 1:
            if numero_aleatorio3 == 5:
                print("Encontaste la llave ¡Felicidades, has escapado del laberinto!")
                continua = False
            elif numero_aleatorio2 == 1:
                print("te encontraste un objeto sombrero")
            elif numero_aleatorio2 == 2:
                print("te encontraste un objeto cuerda")
            elif numero_aleatorio2 == 3:
                print("te encontraste un objeto piel")
            elif numero_aleatorio2 == 4:
                print("te encontraste un objeto piedra")
        elif numero_aleatorio1 == 2:
            if numero_aleatorio3 == 5:
                print("Te encontrate con el jefe  Game Over")
                continua = False
            elif numero_aleatorio2 == 1:
                print("te encontraste un enano pero lo venciste")
            elif numero_aleatorio2 == 2:
                print("te atrapo un Narizon pero te lograste escabullir")
            elif numero_aleatorio2 == 3:
                print("Casi caes en una trampa")
            elif numero_aleatorio2 == 4:
                print("una rapiabispula casi te pica pero sigues con vida")

# productos = {}
# op = 0 

# while op != 0:
#     op = int(input("1=para ingresar un nuevo producto 2=para mostra un producto 3=para gastar un producto 4=para ver cuantos productos faltan 5=calcular cunato inventario tienes"))
    
#     if op == 1:
#         producto = input("ingrese el nombre del producto").lower()
#         cantidad = int(input("ingrese la cantidad del producto"))
#         producto.update({producto: cantidad})
#     elif op == 2:
#         producto = input("que producto deseas ver").lower()
#         print(productos[producto])