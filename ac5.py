def imprimir_n():
    n = int(input("Digite um número inteiro: "))
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

imprimir_n()

def num_tamanho(num):
    if type(num) == int:
        print(len(str(num)))
num_tamanho(10)

def calcula_divisao():
    a = input("Informe o número para A: ")
    b = input("Informe o número para B: ")
    try:
        a = int(a)
        b = int(b)
        c = a/b
    except ValueError:
        c = "Value error!"
    except ZeroDivisionError:
        c = "Impossível dividir pro ZERO!"
    finally:
       print(c)
calcula_divisao()

