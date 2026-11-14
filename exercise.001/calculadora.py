
import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def exibir_interface(num1=None, num2=None, resultado=None, operacao=""):
    limpar_tela()
    print("+--------------------------------------------------------------------+")
    print("|               CALCULADORA DE OPERAÇÕES BÁSICAS                      |")
    print("+--------------------------------------------------------------------+")
    
    txt_num1 = f"{num1:.2f}" if num1 is not None else "_"
    txt_num2 = f"{num2:.2f}" if num2 is not None else "_"
    txt_res  = f"{resultado:.2f}" if resultado is not None else "_"
    
    print(f"|  Primeiro Número: {txt_num1:<49} |")
    print(f"|  Segundo Número:  {txt_num2:<49} |")
    print(f"|  Operação:        {operacao:<49} |")
    print("+--------------------------------------------------------------------+")
    print(f"|  RESULTADO:       {txt_res:<49} |")
    print("+--------------------------------------------------------------------+")

exibir_interface()

n1 = float(input("\nDigite o primeiro número: "))
exibir_interface(num1=n1)

n2 = float(input("Digite o segundo número: "))
exibir_interface(num1=n1, num2=n2)

print("\nEscolha a operação:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
opcao = input("Opção: ")

res = None
op_nome = ""

if opcao == '1':
    res = n1 + n2
    op_nome = "Soma (+)"
elif opcao == '2':
    res = n1 - n2
    op_nome = "Subtração (-)"
elif opcao == '3':
    res = n1 * n2
    op_nome = "Multiplicação (*)"
elif opcao == '4':
    if n2 != 0:
        res = n1 / n2
        op_nome = "Divisão (/)"
    else:
        op_nome = "Divisão por zero (Erro)"

# Atualiza o painel final com o resultado
exibir_interface(num1=n1, num2=n2, resultado=res, operacao=op_nome)