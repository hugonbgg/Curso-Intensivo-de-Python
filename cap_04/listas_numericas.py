#Função range()

for value in range(1,5):
    print(value)

#convertendo a série de números em uma lista
numbers = list(range(1,6))
print(numbers)

#Ignorando alguns números no intervalo

even_numbers = list(range(0, 11, 2))
print(even_numbers)

#Criando uma lista com o quadrados dos números de 0 a 10
squares = []
for value in range (1,11):
    square = value ** 2
    squares.append(square)

print(squares)

#Mesmo código escrito de um jeito mais conciso

squares = []
for value in range (1,11):
    squares.append(value ** 2)

print(squares)

#Estatísticas simples com lista de números

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

min(digits)
max(digits)
sum(digits)

#List comprehension (abrangência da lista)

squares = [value ** 2 for value in range (1,11)]
print (squares)

#Exercicios

numeros = [print (numero) for numero in range (1,21)]

milhao = [print (numero) for numero in range (1, 1000001)]
milhao = list(range(1,1000001))
min(milhao)
max(milhao)
sum(milhao)

impares = [print (impar) for impar in range (1,21,2)]

multiplos_de_tres = [print(multiplo) for multiplo in range (3, 30,3)]

ao_cubo = []
for value in range(1,11):
    ao_cubo.append(value**3)

print(ao_cubo)

ao_cubo = print([(value**3) for value in range(1,11)])
