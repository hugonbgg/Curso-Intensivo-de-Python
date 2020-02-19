#O método title exibe cada palavra com uma letra maiúscula no início.

name = "ada lovelace"
print(name.title())

# O método upper exibe as letras como maísculas
# O método lower exibe as letras como minúsculas

name = "Ada Lovelace"
print(name.upper())
print(name.lower())

#Concatenando strings

first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)

print("Hello, " + full_name.title() + "!")

message = "Hello, " + full_name.title() + "!"
print(message)

#Acrescentando tabulação ao texto \t

print("Python")
print("\tPython")

#Acrescentando quebras de linhas \n

print("Languages:\nPython\nC\nJavascript")

#Tabulação e quebra de linhas juntos:

print("Languages:\n\tPython\n\tC\n\tJavascript")


#Removendo espaços em branco do lado direito da string:
#método rstrip()

favorite_language = 'python   '
print(favorite_language)

favorite_language.rstrip()
print(favorite_language)

favorite_language = favorite_language.rstrip()
print(favorite_language)

#Removendo espaços em branco do lado esquerdo da string:
#método lstrip()

favorite_language = '   python'
print(favorite_language)

print(favorite_language.lstrip())

#Removendo espaços em branco dos dois lados da string:
#método strip()

favorite_language = '    python    '
print(favorite_language.strip())


#Evitando erros de sintaxe com string

#O apóstrofo está entre aspas duplas, logo não existe erro de interpretação
message = "One of Python's strengths is its diverse community."
print(message)


#O apóstrofo está entre aspas simples, ocorre erro de sintaxe.
message = 'One of Python's strengths is its diverse community.'
print(message)




