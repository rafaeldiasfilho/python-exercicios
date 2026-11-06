num1 = 5
num2 = 3.5

a = float(num1)
b = int(num2)

a = int(float("5.3"))
b = "3.5"

print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 // num2)
print(num1 % num2)
print(num1 ** num2)

print(3 + 5 * 7 + 3)
print((3 + 5) * (7 + 3))

print(abs(-15))
print(pow(3,3))
print(max(1,5))
print(min(1,5))
print(round(8.3))
print(round(8.8))

import math

print(math.floor(8.8))
print(math.ceil(8.5))
print(math.sqrt(9))



minha_string = "qualquer texto"

print(minha_string.upper())
print(minha_string.isupper())

print(minha_string.lower())
print(minha_string.islower())

print(minha_string.capitalize())

print(minha_string.strip())

print(minha_string.replace("qualquer", "meu"))

print(len(minha_string))
print(minha_string[2:5])

x = "texto" in minha_string

print(x)

# gustavo é meu pato 

nome = input("Digite seu nome:")
idade = input(f"Qual a sua idade {nome}?")

nascimento = 2024 - idade

print(f"Seu nome é {nome}, e sua idade é: {idade}")
print(f"{nome} você nasceu em {nascimento}")


num1 = int(input("Digite um numero: "))
num1 = int(input("Digite outro numero: "))
resultado = num1 + num2

print(f"O resultado é: {resultado}")


# Criar uma lista
familia = ["Rafa pai", "Juliana", "Rafa filho", "Ana Clara", "Vitoiria", "Natanael"]
#               0            1              2            3            4           5
#              -6           -5             -4           -3           -2          -1

# print(familia[0]) - retorna um indice 
# print(familia[-1]) - retorna um indice de tras pra frente
# print(familia[2:]) - retorna a partir do indice 2 
# print(familia[2:4]) - retorna a partir do indice ate o 4, excluindo o 4

# print(familia)
familia[2] = "rafinha"
familia[3] = "ana"
familia[4] = "vi"
# print(familia)

familia.extend(["Vô","Vó"])

# familia.append("Gato")
familia.insert(1, "cachorro") - adiciona no lugar 
familia.pop()
familia.remove("gato", "cachorro")


print(familia)

