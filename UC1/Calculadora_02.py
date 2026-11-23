#Autor: Enzo Garcia Braz Rocha
#Data da Ultima Atualiação: 05/10/26
#Descrição do cdigo: uso do match case

num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
operação = input("Digite a operação desejada: ")

match operação:
  case "soma":
     soma = num1 + num2
     print("\n--- RESULTADOS DAS OPERAÇÃO--")
     print(f"Soma: {num1} + {num2} = {soma}")
  case "subtração":
    subtração = num1 - num2
    print("\n--- RESULTADOS DAS OPERAÇÃO--")
    print(f"Subtração: {num1} - {num2} = {subtração}")
  case "multiplicação":
    multiplicação = num1 * num2
    print("\n--- RESULTADOS DAS OPERAÇÃO--")
    print(f"Multiplicação: {num1} * {num2} = {multiplicação}")
  case "divisão":
    divisão = num1 / num2
    print("\n--- RESULTADOS DAS OPERAÇÃO--")
    print(f"Divisão: {num1} / {num2} = {divisão}")
  case _:
      print(f"\n -- Alguma informação foi digitado errada por favor verifique. ")