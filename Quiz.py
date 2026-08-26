print('Bem vindo ao quiz!')
answer_user = input("Vamos começar? (sim/não)")

if answer_user != "sim":
    quit()

score = 0

print("Iniciando quiz...")

print(" 1. O que é um algoritmo? \n (A) Uma linguagem de programação \n (B) Um erro no código \n (C) Uma sequência de passos para solucionar um problema" )
answer_1 = input("Resposta:")
if answer_1 == "c":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta incorreta!")


print(" 2. O que é uma variável em programação? \n (A) Um comando usado para repetir códigos \n (B) Um espaço utilizado para armazenar um valor \n (C) Uma instrução utilizada para encerrar o programa")
answer_2 = input("Resposta:")
if answer_2 == "b":
    print("Resposta correta!")
    score = score + 1
else:
    print("Resposta incorreta!")


print(" 3. Qual comando é utilizado para mostrar uma informação na tela em Python? \n (A) Print \n (B) Input \n (C) write")
answer_3 = input("Resposta:")
if answer_3 == "a":
    print("Resposta correta!")
    score = score + 1
else:
        print("Resposta incorreta!")


print(" 4. Qual palavra-chave é utilizada para criar uma função em Python? \n (A) Create \n (B) Function \n (C) Def")
answer_4 = input("Resposta:")
if answer_4 == "c":
    print("Resposta correta!")
    score = score + 1
else:
        print("Resposta incorreta!")


print(" 5. Qual comando pode ser usado para repetir ações percorrendo uma sequência? \n (A) If \n (B) For \n (C) Def")
answer_5 = input("Resposta:")
if answer_5 == "b":
    print("Resposta correta!")
    score = score + 1
else:
        print("Resposta incorreta!")


print("Quiz finalizado")
print(f"Pontuação: {score}/5")