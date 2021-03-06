# Colchetes indicam que é uma lista e os elementos são separados por vírgulas.

bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print (bicycles)
type (bicycles)

#Acessando elementos da lista
#A posição dos índices começa em 0 e não em 1
print(bicycles[0])


#Métodos de string podem ser usados com elementos da lista
print(bicycles[0].title())

#Acessando o último elemento da lista
print(bicycles[-1])

#Usando valores individuais de uma lista

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)

nomes = ['João', 'Maria', 'Ana', 'Pedro']
print ("Olá " + nomes[0] + " !!!")

#Alterando, acrescentando e removendo elementos da lista

#Alterando/substituindo

motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

motorcycles [0] = 'ducati'
print(motorcycles)

#Acrescentando

motorcycles = ['honda', 'yamaha', 'suzuki']

#método append()

motorcycles.append('ducati')
print(motorcycles)

#Criando uma lista vazia e adicionando os elementos

motorcycles = []
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')

print(motorcycles)

#método insert

motorcycles = ['honda', 'yamaha', 'suzuki']
motorcycles.insert(0, 'ducati')
print(motorcycles)

#removendo

#método del() - Quando se sabe a posição do item que quer remover.
#Não permite mais acessar o valor que foi removido da lista.
motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

#método pop() Remove o último item de uma lista. Permite acessar o valor que foi removido da lista.

motorcycles = ['honda', 'yamaha', 'suzuki']
print (motorcycles)

popped_motorcycle = motorcycles.pop()
print (popped_motorcycle)
print (motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop()

print("The last motorcyce I owned was a " + last_owned.title() + ".")


#Removendo itens de qualquer posição usando o método pop()
motorcycles = ['honda', 'yamaha', 'suzuki']
first_owned = motorcycles.pop(0)
print ('The first motorcycle I owned was a ' + first_owned.title() + '.')

#Removendo um item de acordo com o valor com o método remove()

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
print (motorcycles)

motorcycles.remove('ducati')
print (motorcycles)

motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati']
too_expensive = 'ducati'

motorcycles.remove(too_expensive)
print(motorcycles)
print("\n A " + too_expensive.title() + " is a too expensive for me.")


###################
#Exercícios

convidados =['João','Maria','José']
print('Sejam muito bem-vindos ' + convidados[0] +', ' + convidados[1] + ' e ' + convidados[2] + '!')

print(convidados[0] + ' não poderá comparecer!')
#Substituindo João por Mariana

convidados[0] = 'Mariana'
print('Sejam muito bem-vindos ' + convidados[0] +', ' + convidados[1] + ' e ' + convidados[2] + '!')

#Adicionando três pessoas a lista
convidados.insert(0,'Ana Paula')
convidados.insert(2, 'Pedro Paulo')
convidados.append('Clara')

#Exibindo um bem vindo para cada um dos convidados
#Esse for é ensinado mais pra frente no livro, estou treinando com coisas que já sei
for convidado in convidados:
    print('Seja bem-vindo '+ convidado + '!')


#Removendo uma das pessoas da lista, vai ficar apenas dois:
##Esse while / else é ensinado mais pra frente no livro, estou treinando com coisas que já sei
 
len(convidados)

while len(convidados) > 2:
    removido = convidados.pop()
    print('Sinto muito por cancelar o convite ' + removido + '!')

else:
    print('Te espero no jantar '+ convidados[0] + '!')
    print('Te espero no jantar '+ convidados[1] + '!')


#limpando a lista:
del(convidados[0])
print(convidados)

print()


#######################################
#Organizando uma lista usando método sort()

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse = True)
print(cars)

#Ordenando temporariamente com a função sorted()

cars = ['bmw', 'audi', 'toyota', 'subaru']

print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)


#Exibindo a lista em ordem inversa usando o método reverse(). É permanente.
#não organiza em ordem alfabética, apenas inverte a lista.

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)

#Descobrindo o tamanho de uma lista

cars = ['bmw', 'audi', 'toyota', 'subaru']
len(cars)

###########################
#Exercícios

locais = ['Antártida', 'Chicago', 'Moscou', 'Londres', 'Nova Iorque']
print(locais)

print(sorted(locais))
print(sorted(locais, reverse=True))

locais = ['Antártida', 'Chicago', 'Moscou', 'Londres', 'Nova Iorque']
locais.reverse()
print(locais)
locais.reverse()
print(locais)

locais.sort()
print(locais)

locais.sort(reverse = True)
print(locais)

print(len(locais))

############################################






























