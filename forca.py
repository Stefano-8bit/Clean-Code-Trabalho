import random
import json

with open('lista_palavras.txt', 'r') as a:
    p = a.read().splitlines()
try:
    with open('vencedores.json', 'r') as f:
        v = json.load(f)
except FileNotFoundError:
    v = []

lc = set()
le = set()
lt = set()
ac = 0
e = 0
d = 0
pal = random.choice(p).upper()

def i():
        print("BEM-VINDO AO JOGO DA FORCA!")
        e = input("DIGITE 1 PARA SEGUIR O JOGO OU 2 PARA VER AS REGRAS OU 3 PARA VER A TABELA DE VENCEDORES: ")
        if e == '1':
            print(f"A PALAVRA TEM {len(pal)} LETRAS👌")
            for i in range(0, len(pal)):
                print("_ ", end="")
            print("\n")
            return
        elif e == '2':
            print("REGRAS DO JOGO: \n 1. VOCÊ TEM 5 CHANCES PARA DESCOBRIR A PALAVRA. \n 2. VOCÊ PODE PEDIR APENAS UMA DICA USANDO (?). \n 3. VOCÊ DEVE DIGITAR APENAS UMA LETRA POR VEZ. \n 4. VOCÊ NÃO PODE REPETIR LETRAS JÁ TENTADAS. \n 5. VOCÊ NÃO PODE DIGITAR NÚMEROS. \n 6. VOCÊ NÃO PODE DIGITAR CARACTERES ESPECIAIS (EXCETO ?). \n 7. VOCÊ NÃO PODE DIGITAR ESPAÇOS. \n 8. VOCÊ NAO PODE DIGITAR MAIS DE UMA LETRA. ")  
            i() 
        elif e == '3':
            print("TABELA DE VENCEDORES:")
            for v in v:
                print(f"Nome: {v['nome']}, Pontuação: {v['pontos']}")
            i()
        else:
            print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
            i()

def f():
    while True:
        global ac, e, d
        l = input("DIGITE UMA LETRA: ").upper()
        if l == '?':
            if d == 0:
                di = random.choice(list(pal))
                while di in lt:
                    di = random.choice(list(pal))
                print(f"A DICA É: {di}")
                d += 1
                continue
            else:
                print("VOCÊ NÃO TEM MAIS CHANCES PARA PEDIR DICAS!")
                continue
        if len(l) > 1 or not l.isalpha():
            print("DIGITE APENAS UMA LETRA POR VEZ")
            continue
        if l in lt:
            print("❌ VOCÊ JÁ TENTOU ESSA LETRA ❌")
            continue
        if l in pal:
            lc.add(l)
            lt.add(l)
            ac += 1
            print("✅ VOCÊ ACERTOU A LETRA! ✅")
            print()
        else:
            le.add(l)
            lt.add(l)
            e += 1 
            print(f"CHANCES RESTANTES: {5 - e}")
            if e == 1:
                print(" O\n")
                print (f"LETRAS ERRADAS: {le}")
            elif e == 2:
                print(" O\n |\n")
                print (f"LETRAS ERRADAS: {le}")
            elif e == 3:
                print(" O\n/|\\\n")
                print (f"LETRAS ERRADAS: {le}")
            elif e == 4:
                print(" O\n/|\\\n/ \\\n")
                print (f"LETRAS ERRADAS: {le}")                 
            if e == 5:
                print(" O\n/|\\\n/ \\\n")
                print("❌ VOCÊ PERDEU! A PALAVRA ERA:", pal)
                break
        for lp in pal:
            if lp in lc:
                print(lp, end=" ")
            else:
                print("_ ", end=" ")
        print("\n")
        if lc == set(pal):
            n = input("🎉PARABÉNS, VOCÊ GANHOU!🎉 DIGITE SEU NOME: ")
            p = 5 - e
            v.append({'nome': n, 'pontos': p})
            with open('vencedores.json', 'w') as f:
                json.dump(v, f)
            break

i()
f()
