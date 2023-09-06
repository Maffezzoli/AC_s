def pula_linha(): 
    print("\n")
def mensagem(salario, porcentagem, percentual):
        salario_aumentado = salario * porcentagem
        print(f"Salário antes do reajuste = {salario}")
        print(f"Percentual de aumento = {percentual} ")
        print(f"Salário foi aumentado em: {round((salario_aumentado) - (salario),2)}")
        print(f"Novo salário = {round(salario_aumentado , 2)}")
def aumento_salario(salario):
    if salario <= 280:
        mensagem(salario, 1.2, "20%")
    elif salario <= 780:
        mensagem(salario, 1.15, "15%")
    elif salario < 1500:
        mensagem(salario, 1.10, "10%")
    else:
        mensagem(salario, 1.05, "5%")
aumento_salario(280)
pula_linha()
aumento_salario(700)
pula_linha()
aumento_salario(1499)
pula_linha()
aumento_salario(2000)
pula_linha()

def dia_semana(dia):
    match str(dia):
        case "1":
            print("Domingo")
        case "2":
            print("Segunda")
        case "3":
            print("Terça-Feira")
        case "4":
            print("Quarta-Feira")
        case "5":
            print("Quinta-Feira")
        case "6":
            print("Sexta-Feira")
        case "7":
            print("Sábado")
        case _:
            print("Input inválido!")
i = 1
while i <= 8:
    dia_semana(i)
    pula_linha()
    i += 1

def bhaskara(a, b, c):
    if a == 0:
        return print("A = 0, equação não é de 2 grau!")
    delta = int((b ** 2) -4 * a * c)
    x1 = (-b + (delta**(1/2)))/(2*a)
    x2 = (-b - (delta**(1/2)))/(2*a)
    if delta < 0:
        print("Delta negativo! Equação não possuí raízes reais!")
    elif delta == 0:
        print(f"Delta = 0, Equação possui apenas uma raiz real! x1 = {x1}")
    else:
        print(f"Equação possui duas raízes reais, x1 = {x1}, x2 = {x2}")
bhaskara(0,1,1)
pula_linha()
bhaskara(1,-6, 8)
pula_linha()
bhaskara(4,2,4)
pula_linha()
bhaskara(4,4,1)