##funciones 

# def saludar():
#     print("hola")

# saludar()

# def sumarNumero(num1, num2):
#     suma = num1 + num2
#     return suma

# def multiNumero(num1, num2):
#     suma = num1 * num2
#     return suma

# def diviNumero(num1, num2):
#     suma = num1 / num2
#     return suma

# def restaNumero(num1, num2):
#     suma = num1 - num2
#     return suma

# def esNumero(num1):
#     try:
#         return float(num1)
#     except :
#         return False

# while True:
#     while True:
#         numero1 = esNumero(input("ingrese un numero:"))
#         numero2 = esNumero(input("ingrese otro numero:"))
#         if numero1 and numero2:
#             break
#         else:
#             print("ingrese un un numero valido")
    
#     ope = input("que operacion quieres hacer suma, multiplicacion, divicion o resta si deseas salir pon salir").lower()
#     if  ope == "salir": 
#         break
#     elif ope == "multiplicacion":
#         resultado = multiNumero(numero1, numero2)
#         print("el resultado de la multiplicacion es:", resultado)
#     elif ope == "suma":
#         resultado = sumarNumero(numero1, numero2)
#         print("el resultado de la suma es:", resultado)
#     elif ope == "resta":
#         resultado = restaNumero(numero1, numero2)
#         print("el resultado de la resta es:", resultado)
#     elif ope == "divicion":
#         resultado = diviNumero(numero1, numero2)
#         print("el resultado de la divi es:", resultado)
#     else:
#         print("operacion no valida")

#https://www.w3schools.com/ 
#freeCodeCamp
# hacer una division una resta y un multiplicacion 

## elabore un programa que calcule el area del cuadrado, rectangulo el area del circulo el area del trapecio
# triangulo el usuiario debe tener la opocion cual de las areas debe calcular inplemente las funciones 
#necesarias 

def areaCuadrado(num1):
    area = num1 * num1
    return area

def areaRectangulo(num1, num2):
    area = num1 * num2
    return area

def areaCirculo(num1):
    area = 3.14159 * num1**2
    return area

def areaTrapecio(num1, num2, num3):
    area = num1 + num2 * num3 / 2
    return area

def areaTriangulo(num1, num2):
    area =  num1 * num2 / 2
    return area

def esNumero(num1):
    try:
        return float(num1)
    except :
        return False

continuar = True

while continuar != False:
    verficar = True
    ope = input("Cual es el area que deseas calular 1=cuadrado 2=rectangulo 3=circulo 4=trapecio 5=triangulo 6=salir").lower()
    if  ope == "6": 
        continuar = False
    elif ope == "1":
        while verficar != False :
            numero1 = esNumero(input("ingrese la longitud de un lado"))
            if numero1:
                verficar = False
                break
            else:
                print("ingrese un un numero valido")
        resultado = areaCuadrado(numero1)
        print("el area del cuadrado es:", resultado)
    elif ope == "2":
        while verficar != False:
            numero1 = esNumero(input("ingrese la longuitud del largo"))
            numero2 = esNumero(input("ingrese la longuitud del ancho"))
            if numero1 and numero2: 
                verficar = False
            else:
                print("ingrese un un numero valido")
        resultado = areaRectangulo(numero1,numero2)
        print("el area del rectangulo es:", resultado)
    elif ope == "3":
        while verficar != False:
            numero1 = esNumero(input("ingrese el radio del circulo"))
            if numero1:
                verficar = False
            else:
                print("ingrese un un numero valido")
        resultado = areaCirculo(numero1)
        print("el area del circulo es:", resultado)
    elif ope == "4":
        while verficar != False:
            numero1 = esNumero(input("ingrese la longuitud de la base mayor"))
            numero2 = esNumero(input("ingrese la longuitud de la base menor"))
            numero3 = esNumero(input("ingrese la longuitud de la altura"))
            if numero1 and numero2 and numero3:
                verficar = False
            else:
                print("ingrese un un numero valido")
        resultado = areaTrapecio(numero1,numero2,numero3)
        print("el area del trapecio es:", resultado)
    elif ope == "5":
        while verficar != False:
            numero1 = esNumero(input("ingrese la longuitud de la base"))
            numero2 = esNumero(input("ingrese la longuitud de la altura"))
            if numero1 and numero2:
                verficar = False
            else:
                print("ingrese un un numero valido")
        resultado = areaTriangulo(numero1,numero2)
        print("el area del  es de:", resultado)
    else:
        print("operacion no valida")