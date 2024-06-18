import random
import json

with open('lista_palavras.txt', 'r') as arquivo:
    palavra = arquivo.read().splitlines()
try:
    with open('vencedores.json', 'r') as f:
        vencedores = json.load(f)
except FileNotFoundError:
    vencedores = []

letras_certas = set()
letras_erradas = set()
letras_tentadas = set()
acertos = 0
erros = 0
dicas = 0
palavra = random.choice(palavra).upper()

def inicio_forca():
        print("BEM-VINDO AO JOGO DA FORCA!")
        escolha = input("DIGITE 1 PARA SEGUIR O JOGO OU 2 PARA VER AS REGRAS OU 3 PARA VER A TABELA DE VENCEDORES: ")
        if escolha == '1':
            print(f"A PALAVRA TEM {len(palavra)} LETRAS👌")
            for i in range(0, len(palavra)):
                print("_ ", end="")
            print("\n")
            return
        elif escolha == '2':
            print("REGRAS DO JOGO: \n 1. VOCÊ TEM 5 CHANCES PARA DESCOBRIR A PALAVRA. \n 2. VOCÊ PODE PEDIR APENAS UMA DICA USANDO (?). \n 3. VOCÊ DEVE DIGITAR APENAS UMA LETRA POR VEZ. \n 4. VOCÊ NÃO PODE REPETIR LETRAS JÁ TENTADAS. \n 5. VOCÊ NÃO PODE DIGITAR NÚMEROS. \n 6. VOCÊ NÃO PODE DIGITAR CARACTERES ESPECIAIS (EXCETO ?). \n 7. VOCÊ NÃO PODE DIGITAR ESPAÇOS. \n 8. VOCÊ NAO PODE DIGITAR MAIS DE UMA LETRA. ")  
            inicio_forca() 
        elif escolha == '3':
            print("TABELA DE VENCEDORES:")
            vencedores_ordenados = sorted(vencedores, key=lambda x: x['pontos'], reverse=True)
            for vencedor in vencedores_ordenados:
                print(f"Nome: {vencedor['nome']}, Pontuação: {vencedor['pontos']}")
            inicio_forca()
        else:
            print("OPÇÃO INVÁLIDA. TENTE NOVAMENTE.")
            inicio_forca()

def forca_logica():
    while True:
        global acertos, erros, dicas
        letra = input("DIGITE UMA LETRA: ").upper()
        if letra == '?':
            if dicas == 0:
                dica = random.choice(list(palavra))
                while dica in letras_tentadas:
                    dica = random.choice(list(palavra))
                print(f"A DICA É: {dica}")
                dicas += 1
                continue
            else:
                print("VOCÊ NÃO TEM MAIS CHANCES PARA PEDIR DICAS!")
                continue
        if len(letra) > 1 or not letra.isalpha():
            print("DIGITE APENAS UMA LETRA POR VEZ")
            continue
        if letra in letras_tentadas:
            print("❌ VOCÊ JÁ TENTOU ESSA LETRA ❌")
            continue
        if letra in palavra:
            letras_certas.add(letra)
            letras_tentadas.add(letra)
            acertos += 1
            print("✅ VOCÊ ACERTOU A LETRA! ✅")
            print()
        else:
            letras_erradas.add(letra)
            letras_tentadas.add(letra)
            erros += 1 
            print(f"CHANCES RESTANTES: {5 - erros}")
            if erros == 1:
                print(" O\n")
                print (f"LETRAS ERRADAS: {letras_erradas}")
            elif erros == 2:
                print(" O\n |\n")
                print (f"LETRAS ERRADAS: {letras_erradas}")
            elif erros == 3:
                print(" O\n/|\\\n")
                print (f"LETRAS ERRADAS: {letras_erradas}")
            elif erros == 4:
                print(" O\n/|\\\n/ \\\n")
                print (f"LETRAS ERRADAS: {letras_erradas}")                 
            if erros == 5:
                print(" O\n/|\\\n/ \\\n")
                print("❌ VOCÊ PERDEU! A PALAVRA ERA:", palavra)
                break
        for letra_palavra in palavra:
            if letra_palavra in letras_certas:
                print(letra_palavra, end=" ")
            else:
                print("_ ", end=" ")
        print("\n")
        if letras_certas == set(palavra):
            nome = input("🎉PARABÉNS, VOCÊ GANHOU!🎉 DIGITE SEU NOME: ")
            pontos = 5 - erros
            vencedores.append({'nome': nome, 'pontos': pontos})
            with open('vencedores.json', 'w') as f:
                json.dump(vencedores, f)
            break

inicio_forca()
forca_logica()
