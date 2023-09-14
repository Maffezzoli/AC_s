def numPrimo(num):
    primo = True
    for div in range(2,num):
        if num % div == 0:
            print(div," - " ,end="")
            primo = False
    if primo == False:
        print("Não é primo!")
    else:
        print("É primo!")
        
numPrimo(100)

print()

def quantidade_indeterminada():
    cont1 = cont2 = cont3 = cont4 = 0
    while True:
        pergunta = int(input("Insira um número : "))
        
        if pergunta < 0:
            break
        if pergunta <= 25:
            cont1 += 1
        elif pergunta <= 50:
            cont2 += 1
        elif pergunta <= 75:
            cont3 += 1
        elif pergunta <= 100:
            cont4 += 1
            
    print()

    print("Quantidade de números no intervalo [0,25]:", cont1,"\nQuantidade de números no intervalo [26,50]:", cont2,
          "\nQuantidade de números no intervalo [51,75]:", cont3, "\nQuantidade de números no intervalo [76,100]:",cont4)
    print()

quantidade_indeterminada()

print()

def calcula_juros (num_parcelas):
    if num_parcelas == 1:
        return 0
    else:
        calcula = (num_parcelas / 3) * 5 
        return calcula + 5
def mostra(parcelas, valor):
    juros = calcula_juros(parcelas)
    valor_juros = round((juros/100) * valor,2)
    valor_tot = round(valor_juros + valor,2)
    valor_parcela = round(valor_tot / parcelas)
    print("Valor dos juros: ",valor_juros,", Valor total: ",valor_tot,", Quantidade de parcelas: ", parcelas, "Valor da parcela: ",valor_parcela)
def funcao_principal(valor):
    for parcelas in range(1, 13, 3):
        if parcelas > 1:
            parcelas -= 1
            mostra(parcelas, valor)
        else:
            mostra(parcelas, valor)

funcao_principal(1000)