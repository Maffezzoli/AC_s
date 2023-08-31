def separa_linha(): #Função só para chamar um print que separa as funções no prompt, deixando mais organizado
    print("-"*25)
def funcao_calcula_salario():
    valor_hora = float(input("Informe o valor pago por hora: "))
    horas_mes = float(input("Informe quantas horas foram trabalhadas por dia: "))
    def horas_trabalhadas(hora_paga,horas):
        mes = 24 #dias
        salario_final = hora_paga * (horas * mes)
        print(f"{salario_final} Reais")
    horas_trabalhadas(valor_hora,horas_mes)
funcao_calcula_salario()

separa_linha()

a = float(input("Insira número 1: "))
b = float(input("Insira número 2: "))
c = float(input("Insira número 3: "))

separa_linha()

def funcao_tres_numeros(a , b , c):
    op1 = (2 * a) * (b/2)
    op2 = (3 * a) + c
    op3 = c**3
    print(f"Operação 1 = {op1}\nOperação 2 = {op2}\nOperação 3 = {op3}")

funcao_tres_numeros(a, b, c)

def funcao_tres_numeros_retorno(a , b , c):
    op1 = (2 * a) * (b/2)
    op2 = (3 * a) + c
    op3 = c**3
    return op1, op2, op3

op1 , op2, op3 = funcao_tres_numeros_retorno(a, b, c) #Eu não entendi muito bem essa terceira atividade, espero que tenha interpretado certo

separa_linha()

print(f"Operação Retorno 1 = {op1}\nOperação Retorno 2 = {op2}\nOperação Retorno 3 = {op3}")

separa_linha()

def ano_bissexto():
    ano = int(input("Insira o ano a ser verificado: "))
    print((ano % 4 == 0 and ano % 100 != 0) or (ano % 100 == 0 and ano % 400 == 0))
ano_bissexto()