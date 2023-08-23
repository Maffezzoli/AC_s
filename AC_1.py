def bhaskara():
    a = float(input("Insira o valor de A: "))
    b = float(input("Insira o valor de B: "))
    c = float(input("Insira o valor de C: "))
    delta = float((b ** 2) -4 * a * c)
    x1 = float(-b + (delta**(1/2)))/(2*a)
    x2 = float(-b - (delta**(1/2)))/(2*a)
    print(f"X1: {x1} e X2: {x2}")

def ano_bissexto():
    ano = int(input("Insira o ano a ser verificado: "))
    x = 0
    print((x == ano % 4 and x != ano % 100) or  (x == ano % 400 and x == ano % 100))
ano_bissexto()
bhaskara()