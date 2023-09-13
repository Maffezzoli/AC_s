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
#numPrimo(100)

def quantidade_indeterminada():
    pergunta = 1
    while pergunta > 0:
            pergunta = int(input("Insira um número:"))
            if pergunta < 100: #Todos os números a partir de 100 retornam o mesmo resultado
                cont1 = cont2 = cont3 = cont4 = 0
                i = pergunta
                while i >= 0:
                    if i in range(0,25):
                        cont1 += 1
                    elif i in range(26,50):
                        cont2 += 1
                    elif i in range(51,75):
                        cont3 += 1
                    elif i in range(76,100):
                        cont4 += 1
                    i -= 1
            else: 
                cont1 = 25
                cont2 = cont3 = cont4 = 24
            print("Intervalo [0,25]: ",cont1,"/Intervalo [26,50]: "
                  ,cont2,"/Intervalo [51,75]: ",cont3,"Intervalo [76,100]: ",cont4)
#quantidade_indeterminada()

def porcentagem_juros(num_parcelas):
    "fazer em casa"
