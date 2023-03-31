#Função abaixo representa código relativo a questão1:
def question1():
    indice = 13
    soma = 0
    k = 0
    while k < indice:
        k += 1
        soma += k
    print(soma)
#Fim da Questão1...

#Função abaixo representa código relativo a questão2:
def question2(x, y, z):
    if z < 0:
        return print("Números negativos como {} não pertencem a sequencia de Fibonacci!".format(z))
    if z == x or z == y:
        return print("{} pertence a sequencia de Fibonacci!".format(z))
    fib = y + x
    while fib <= z:
        x = y
        y = fib
        fib = y + x
        if fib == z:
            return print("{} pertence a sequencia de Fibonacci!".format(z))
    return print("{} não pertence a sequencia de Fibonacci!".format(z))
#Fim da Questão2...

#Função abaixo representa código relativo a questão4:
def question4():
    carro = 0.0
    caminhao = 100.0
    minutos = 0.0
    pedagio = "Z"
    while pedagio != "S" and pedagio != "N":
        pedagio = input("Caminhão sofre 2 pedágios de 5 minutos? (S / N) ").upper()
    while carro < caminhao:
        minutos += 1.0/10
        carro += 1.83333333333/10
        if pedagio == "S":
            if minutos > 10:
                caminhao -= 1.3333333333/10
        if pedagio == "N":
            caminhao -= 1.3333333333 / 10
        if (carro + 0.5) > caminhao:
            print("{} minutos depois, carro = {} e caminhão = {}".format(minutos, carro, caminhao))
#Fim da Questão4...

#Função abaixo representa código relativo a questão5:
def question5():
    palavra = input("Digite o que será invertido: ")
    inversa = []
    for letra in palavra:
        inversa.insert(0, letra)
    return print(''.join(inversa))
#Fim da Questão5...

#Programa começa aqui... Escolha uma questão:
if(__name__ == "__main__"):
    quest = 0
    while quest != 1 and quest != 2 and quest != 4 and quest != 5:
        quest = int(input("Qual questão gostaria de ver a resposta? (1, 2, 4 ou 5) "))
    if quest == 1:
        question1()
    if quest == 2:
        question2(0, 1, int(input("Escolha um número inteiro para Fibonacci: ")))
    if quest == 4:
        question4()
    if quest == 5:
        question5()
#END
