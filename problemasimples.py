# Parte 1: Repetição de Textos
texto = input("Digite uma string: ")
vezes = int(input("Digite um número inteiro: "))
resultado_texto = texto * vezes
print("\nResultado da repetição:")
print(resultado_texto)

# Parte 2: Operações Matemáticas Simples
print("\nOperações Matemáticas Simples:")
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

print("\nEscolha uma operação:")
print("1 - Adição")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
operacao = int(input("Digite o número da operação desejada: "))

if operacao == 1:
    resultado_operacao = num1 + num2
    print(f"\nResultado da adição: {resultado_operacao}")
elif operacao == 2:
    resultado_operacao = num1 - num2
    print(f"\nResultado da subtração: {resultado_operacao}")
elif operacao == 3:
    resultado_operacao = num1 * num2
    print(f"\nResultado da multiplicação: {resultado_operacao}")
elif operacao == 4:
    if num2 != 0:
        resultado_operacao = num1 / num2
        print(f"\nResultado da divisão: {resultado_operacao}")
    else:
        print("\nErro: Divisão por zero não é permitida!")
else:
    print("\nOperação inválida!")
