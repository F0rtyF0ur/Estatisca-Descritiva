
#### OPERADORES LÓGICOS

# MAIOR -- >
# MENOR -- <
# IGUAL -- =
# DIFERENTE -- !=

# E -- and
# OU -- OR
# NÃO -- NOT

# Exercicio operador
numero_1 = 10
numero_2 = 5

maior = (10 > 5)
print("Resultado usando operador > onde 10 > 5: ", maior)
###
numero_1 = 10
numero_2 = 5
numero_3 = 30

resultado = (numero_1 > numero_2)
print("Resultado usando operador > onde 10 > 5, mas usando variáveis: ", resultado)

resultado = (numero_1 < numero_2 and numero_1 < numero_3)
print("Resultado usando operador < e and onde 10 < 5 and 10 < 30: ", resultado)

resultado_1 = (numero_1 > numero_2 and numero_3 > numero_2) # true
resultado_2 = (numero_2 > numero_1 and numero_2 > numero_3) # false
resultado_3 = (numero_1 > numero_2 or numero_3 > numero_2) # true
resultado_4 = (numero_1 < numero_2 or numero_3 < numero_2) # false
resultado_5 = (not numero_1 < numero_2)
print("Resultado 1 usando 10 > 2 and 30 > 5: ", resultado_1)
print("Resultado 2 usando 5 > 10 and 5 > 30: ", resultado_2)
print("Resultado 3 usando 10 > 5 or 30 > 5: ", resultado_3)
print("Resultado 4 usando 10 < 5 or 30 < 5: ", resultado_4)
print("Resultado 5 usando not 10 < 5: ", resultado_5)

print("*"*50)

nome = "Maria"
idade = 18
nota = 7.5
status = "aprovado"

print("Resultado da consulta do tipo de dado do nome Maria: ", type(nome))
print("Resultado da consulta do tipo de dado da idade 18: ", type(idade))
print("Resultado da consulta do tipo de dado da nota 7.5: ", type(nota))
print("Resultado da consulta do tipo de dado do status aprovado: ", type(status))

print("Tipos de dados: ", type(nome), type(idade), type(nota), type(status))

print("*"*50)

# valide se a idade é maior que 18 e nota maior ou igual a 7
# valida se a idade é maior e igual 18 e nota maior ou igual a 8
# valida se a pessoa é a Maria e status é aprovado

validação_1 = (idade > 18 and nota >= 7)
print("Validei se a idade >18 e nota >=7 o resultado foi: ", validação_1)

validação_2 = (idade >= 18 and nota >= 8)
print("Validei se a idade >= 18 and nota >= 8 o resultado foi: ", validação_2)

validação_3 = (nome == "Maria" and status == "aprovado") # O == é o operador de comparação de igualdade, usado para verificar se dois valores são iguais
print("Validei se o nome = Maria e status = aprovado o resultado foi: ", validação_3)

print("*"*50)

# Condicionais Simples #



##18Forma ruim de fazer esse código
if idade >= 18:
    print("A pessoa é adulta")
if idade < 18:
    print("A pessoa é menor de idade")


if idade >= 18:
    print("A pessoa é adulta")
else:
    print("A pessoa é menor de idade")

# Interação com o usuário pedindo a idade dele e ver se é maior ou não

idade = int(input("Digite sua idade: ")) # usei o int para converter numero
if idade >= 18:
    print("Você é maior de idade")
else:
    print("Você é menor de idade")

nota_al = float(input("Digite sua nota"))
if nota_al >= 8:
    print("VocÊ foi aprovado com Louvor")
elif nota_al >= 6:
    print("Você foi para Conselho de Classe")
elif nota_al >= 4:
    print("Você esta de recuperação")
else:
    print("Você foi Reprovado")

print("*"+50)


# Condicional com o Operador And ##
nota_al = float(input("Digite sua nota: "))
usuário= input("Digite seu nome: ")

if nota_al >= nota or usuário == nome:
    print("Você pode participar do curso Avançado.")
else:
    print("Você não pode participar.")

print("*"*50)

#Condicional com Operador Or ## 
if nota_al >= nota or usuário == nome:
    print("Você pode participar do curso Avançado.")
else:
    print("Você não pode participar.")

## Condicinal Aninhada ( If dentro de IF)

if idade >= 18:
    if nota >= 7:
        print("Você passou para a próxima fase.")
    else:
        print("Você tem idade o suficiente e não tem nota para participar.")
else:
    print("Você não tem idade para participar")