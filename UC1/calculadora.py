#Autor: Enzo Garcia Braz Rocha
#Data da Ultima Atualiação: 05/10/26
#Descrição código: Calculadora 4 funções com uso de IF

#Código de Apoio (GAbarito comentado)
# Recebendo dados do usuario e convertendo para numero inteiro

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
operação = input("Digite a operação desejada: ")

if operação == "soma":
 soma = num1 + num2
 print("\n--- RESULTADOS DAS OPERAÇÃO--")
 print(f"Soma: {num1} + {num2} = {soma}")
if operação == "subtração":
  subtracao = num1 - num2
  print("\n--- RESULTADOS DAS OPERAÇÃO--")
  print(f"Subtração: {num1} - {num2} = {subtracao}")
elif operação == "multiplicação":
  multiplicacao = num1 * num2
  print("\n--- RESULTADOS DAS OPERAÇÃO--")
  print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")
elif operação == "divisão":
  divisao = num1 / num2
  print("\n--- RESULTADOS DAS OPERAÇÃO--")
  print(f"Divisão: {num1} / {num2} = {divisao}")
else:
  print(f"\n -- Alguma informação foi digitado errada por favor verifique. ")


'''
print("\n--- RESULTADOS DAS OPERAÇÕES ---")
print(f"Soma: {num1} + {num2} = {soma}")
print(f"Subtração: {num1} - {num2} = {subtracao}")
print(f"Multiplicação: {num1} * {num2} = {multiplicacao}")
print(f"Divisão Real: {num1} / {num2} = {divisao}")
print(f"Divisão Inteira: {num1} // {num2} = {divisao_inteira}")
'''