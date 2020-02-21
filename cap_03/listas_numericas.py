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
