## Definir una función max() que tome como argumento dos números y devuelva el mayor de ellos.
## (Es cierto que python tiene una función max() incorporada, pero hacerla nosotros mismos es un muy buen ejercicio.

# def maxdn(n1,n2):
#     if n1>n2:
#         print(f"{n1} es mayo que {n2}")
#     if n1==n2:
#         print("son números iguales")
#     if n2>n1:
#         print(f"{n2} es mayor que {n1}")


# numero1 = int(input("Ingrese el primer número: "))
# numero2 = int(input("Ingrese el segundo número: "))

# ejercicio1 = maxdn(numero1, numero2)



## Definir una función max_de_tres(), que tome tres números como argumentos y devuelva el mayor de ellos.

# def max_tres(n1,n2,n3):
#     if n1>n2 and n1>n3:
#         print(f"{n1} es mayor que {n2} y {n3}")
#     if n2>n1 and n2>n3:
#         print(f"{n2} es mayo que {n1} y {n3}")
#     if n3>n1 and n3>n2:
#         print(f"{n3} es mayor que {n1} y {n2}")
#     else:
#         print(f"los numeros son iguales")

# nums = []
# for n in list(range(3)):
#     nums.append(int(input("ingrese el numero: ")))

# validar = max_tres(nums[0],nums[1],nums[2])

## Definir una función que calcule la longitud de una lista o una cadena dada. (Es cierto que python tiene la función len() 
## incorporada, pero escribirla por nosotros mismos resulta un muy buen ejercicio.

# def largo_cadena(cadena):
#     cant = 0
#     for i in cadena:
#         cant += 1
#     return cant

# my_string = input("Ingrese un texto: ")
# largo_cad = largo_cadena(my_string)
# print(largo_cad)


##Escribir una función que tome un carácter y devuelva True si es una vocal, de lo contrario devuelve False.

# vocales = ['a','e','i','o','u']
# vocal = input("ingrese la letra: ")

# def valida_vocal(vocal):
#     #for vocal in vocales:
#     if vocal in vocales:
#         print(f"{vocal} es una vocal")
#     else:
#         print(f"{vocal} No es una vocal")

# valida = valida_vocal(vocal)


## Escribir una función sum() y una función multip() que sumen y multipliquen 
## respectivamente todos los números de una lista. Por ejemplo: sum([1,2,3,4]) debería devolver 10 y multip([1,2,3,4]) debería devolver 24.

## listado funciones

# 1. suma
# 2. resta
# 3. Multiplicacion
# 4. Division

# lista_numeros = [1,2,3,4,5,6,7]
# oper = int(input("Ingrese la operación a realizar: "))

# def operacion(oper):
#     if oper == 1:
#         resultado = 0
#         for i in lista_numeros:
#             resultado = resultado + i

#     if oper == 2:
#         resultado = 0
#         for i in lista_numeros:
#             resultado = resultado - i

#     if oper == 3:
#         resultado = 1
#         for i in lista_numeros:
#             resultado = resultado * i

#     if oper == 4:
#         resultado = 1
#         for i in lista_numeros:
#             resultado = resultado / i

#     return resultado

# operacion_ejemplo = operacion(oper)
# print(operacion_ejemplo)

##Definir una función inversa() que calcule la inversión de una cadena. 
##Por ejemplo la cadena "estoy probando" debería devolver la cadena "odnaborp yotse"

# cadena = input("Ingrese la cadena de texto: ")

# def revertir(cadena):
#     invertida = ""
#     cont = len(cadena)
#     indice = -1
#     while cont >=1:
#         invertida += cadena[indice]
#         indice = indice + (-1)
#         cont -=1
#     return invertida

# mi_cadena = revertir(cadena)
# print(mi_cadena)

##  Definir una función es_palindromo() que reconoce palíndromos 
## (es decir, palabras que tienen el mismo aspecto escritas invertidas), ejemplo: es_palindromo ("radar") tendría que devolver True.
# palabra = input("Ingresa la palabra: ")

# def espalindrome(palabra):
#     if palabra == palabra[::-1]:
#         print("Es palindrome")
#     else:
#         print("No es palindorme")

# palabrin = espalindrome(palabra)


##Definir una función superposicion() que tome dos listas y devuelva 
## True si tienen al menos 1 miembro en común o devuelva False de lo contrario. Escribir la función usando el bucle for anidado.

# list1 = [1,5,8,7,46,9]
# list2 = [5,7,8,9,6,3,2]
# list3 = []
# def superposicion(list1, list2):
#     for i in list1:
#         for x in list2:
#             if i == x:
#                 list3.append(i)
#     return list3

# resultado = list(superposicion(list1,list2))
# print(resultado)


