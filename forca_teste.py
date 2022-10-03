# Trabalho 3º Bimestre - Forca
# Brenda Ziviani
# Gianlucca Fadiga
# Yasmin Souza

import pandas as pd
import os
import re

def main():
    
    # Inicialização de classes e métodos
    
    # Classe para colorir código no terminal
    class bcolors:
        HEADER = '\033[95m'
        OKBLUE = '\033[94m'
        OKCYAN = '\033[96m'
        OKGREEN = '\033[92m'
        WARNING = '\033[93m'
        FAIL = '\033[91m'
        ENDC = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
    
    # Classe jogador para armazenar dados do jogador
    class Jogador:
        def __init__(self, nome, pontuacao, jogadas):
            self.nome = nome
            self.pontuacao = pontuacao
            self.jogadas = jogadas

        def add_jogada(self, jogada_feita):
            self.jogadas += jogada_feita
    
    # Carregamento de dados do arquivo csv de palavras
    df = pd.read_csv('palavras.csv', index_col = False)
    
    # Criação de cada ficha de jogador
    nomes_jogadores = []
    n_jogadores = int(input(bcolors.WARNING + 'Digite a quantia de jogadores: ' + bcolors.ENDC))
    for i in range (n_jogadores):
        nome = input(bcolors.WARNING + 'Digite o nome do jogador: ' + bcolors.ENDC)
        nomes_jogadores += [nome]
        pontuacao = 0
        jogadas = ''
        nomes_jogadores[i] = Jogador(nome, pontuacao, jogadas)
    
    # Input para receber número de rodadas do jogo
    n_rodadas = int(input(bcolors.WARNING + 'Digite a quantia de rodadas a serem jogadas: ' + bcolors.ENDC))
    
    # Criação de cada rodada com as palavras e dicas aleatórias
    vetor_palavraA = []
    vetor_dicaA = []
    
    # Seleção de uma palavra aleatória
    for i in range (n_rodadas):
        # Usa sample para selecionar uma linha aleatória do dataframe
        # axis significa que é a linha, palavra significa o que queremos escolher
        palavra_aleatoria = str(df.sample(axis = 0)['Palavra'])
        # Limpa a palavra, ficamos com a palavra em si que é o index 1 (começando em 0)
        palavra_escolhida = palavra_aleatoria.split()[1]
        # Cria a dica da palavra pesquisando a sua linha toda no dataframe
        dica_palavra = str(df[df['Palavra'].str.contains(palavra_escolhida)])
        dica_palavra = dica_palavra.split()[4]
        
        repetida = True
        
        while repetida == True:
            if re.compile(palavra_escolhida, flags=re.IGNORECASE).search in vetor_palavraA:
                palavra_aleatoria = str(df.sample(axis = 0)['Palavra'])
                palavra_escolhida = palavra_aleatoria.split()[1]
                dica_palavra = str(df[df['Palavra'].str.contains(palavra_escolhida)])
                dica_palavra = dica_palavra.split()[4]
            else:
                vetor_palavraA.append(palavra_escolhida)
                vetor_dicaA.append(dica_palavra)
                repetida = False
    
    # Inicio do jogo
    for rodadas in range(n_rodadas):
        
        # Inicialização das variáveis
        acertos = 0
        erros = 0
        letras_acertadas = ''
        letras_erradas = ''
        termino_rodada = False
        total_letras = set(vetor_palavraA[rodadas])
        jogadores_eliminados = []
        
        # Inicio do jogo
        print(os.system('clear'))
        print(bcolors.WARNING + 'Rodada ' + str(rodadas + 1) + bcolors.ENDC)
        
        while termino_rodada == False:
            
            while erros <= 5:
                if termino_rodada == True:
                    break
                
                for x in range(len(nomes_jogadores)):
                    if termino_rodada == True:
                        break
                    
                    elif nomes_jogadores[x] in jogadores_eliminados:
                        x += 1
                    
                    elif x <= len(nomes_jogadores):
                        
                        mensagem = ''
                        for letra in vetor_palavraA[rodadas]:
                            if letra in letras_acertadas:
                                mensagem += letra + ''
                            else:
                                mensagem += '_ '     
                        
                        if mensagem == vetor_palavraA[rodadas]:
                            print(bcolors.HEADER + 'Parabéns, você(s) acertou(aram) todas as letras da palavra!' + bcolors.ENDC)
                            for jogador in range(len(nomes_jogadores)):
                                nomes_jogadores[jogador].pontuacao += 1
                            termino_rodada = True
                            break
                        
                        print(os.system('clear'))
                        print(bcolors.HEADER + 'Vez de ' + nomes_jogadores[x].nome + bcolors.ENDC)
                        print(bcolors.BOLD + mensagem + bcolors.ENDC)
                        print(bcolors.OKCYAN + 'A palavra possui {} letras'.format(str(len(vetor_palavraA[rodadas]))) + bcolors.ENDC)
                        print('A dica é: ' + vetor_dicaA[rodadas])
                        print(bcolors.OKGREEN + 'Letras corretas: ' + letras_acertadas + bcolors.ENDC)
                        print(bcolors.FAIL + 'Letras incorretas: ' + letras_erradas + bcolors.ENDC)
                        print(bcolors.HEADER + 'Total de erros: ' + str(erros) + '/5' + bcolors.ENDC)
                        
                        letra = input(bcolors.WARNING + 'Digite a letra ou chute a palavra completa: ' + bcolors.ENDC).upper()
                        
                        if len(letra) == 1:
                            
                            if letras_acertadas == len(total_letras):
                                print(bcolors.OKGREEN + 'Parabéns, você(s) acertou(aram) todas as letras da palavra!' + bcolors.ENDC)
                                # nomes_jogadores[x].pontuacao += 1
                                termino_rodada = True
                                break
                            
                            elif letra in vetor_palavraA[rodadas]: 
                                print(bcolors.OKGREEN + 'Você acertou!\n' + bcolors.ENDC)
                                letras_acertadas += letra
                                nomes_jogadores[x].add_jogada('[' + letra + '] ')
                                acertos += 1
                            
                            else:
                                print(bcolors.FAIL + 'Errou trouxa!\n' + bcolors.ENDC)
                                letras_erradas += letra
                                nomes_jogadores[x].add_jogada('[' + letra + '] ')
                                erros += 1
                    
                        elif len(letra) > 1:
                            if letra == vetor_palavraA[rodadas]:
                                print(bcolors.OKGREEN + 'Parabéns {}, você acertou a palavra!'.format(nomes_jogadores[x].nome) + bcolors.ENDC)
                                nomes_jogadores[x].pontuacao += 1
                                letras_acertadas += ' *' + letra + '* '
                                nomes_jogadores[x].add_jogada('[' + letra + '] ')
                                termino_rodada = True
                                break   
                            else:
                                print(bcolors.WARNING + 'Você não pode digitar mais de uma letra por vez ou errou a palavra!' + bcolors.ENDC)
                                if len(nomes_jogadores) <= 1:
                                    print(bcolors.FAIL + 'Você errou a palavra e perdeu o jogo!' + bcolors.ENDC)
                                    termino_rodada = True
                                    break
                                else:
                                    print(bcolors.FAIL + 'Você errou a palavra e foi eliminado!' + bcolors.ENDC)
                                    letras_erradas += ' *' + letra + '* ' 
                                    nomes_jogadores[x].add_jogada('[' + letra + '] ')
                                    erros += 1
                                    jogadores_eliminados.append(nomes_jogadores[x])            
                    else:
                        x = 0
                    
            termino_rodada = True
            
            # Verifica se possui mais de uma rodada e propõe adicionar jogador
            resposta_dada = False
            if n_rodadas > 1:
                while resposta_dada == False:
                    print(os.system('clear'))
                    resposta = input(bcolors.WARNING + 'Deseja adicionar um novo jogador? (S/N): ' + bcolors.ENDC).upper()
                    if resposta == 'S':
                        nome = input(bcolors.HEADER + 'Digite o nome do jogador: ' + bcolors.ENDC)
                        nomes_jogadores += [nome]
                        pontuacao = 0
                        jogadas = ''
                        nomes_jogadores[i] = Jogador(nome, pontuacao, jogadas)
                        resposta_dada = True
                        
        # Finalização do jogo e prints finais
        print(os.system('clear'))
        print(bcolors.OKCYAN + 'Palavra da rodada: ' + palavra_escolhida + bcolors.ENDC)
        for jogador in range(len(nomes_jogadores)):
            print(bcolors.HEADER + 'Jogador: ' + nomes_jogadores[jogador].nome + bcolors.ENDC)
            print(bcolors.HEADER + 'Pontuação: ' + str(nomes_jogadores[jogador].pontuacao) + bcolors.ENDC)
            print(bcolors.HEADER + 'Jogadas: ' + str(nomes_jogadores[jogador].jogadas) + bcolors.ENDC)
            print('\n')
        print(bcolors.OKGREEN + 'Jogadas corretas da rodada: ' + letras_acertadas + bcolors.ENDC)
        print(bcolors.FAIL + 'Jogadas incorretas da rodada: ' + letras_erradas + bcolors.ENDC)
        print(bcolors.OKGREEN + 'Total de acertos: ' + str(acertos) + bcolors.ENDC)
        print(bcolors.FAIL + 'Total de erros: ' + str(erros) + bcolors.ENDC)
        
        # Verificação de empate e rodada extra
        empate = False
        nomes_empate = []
        if len(nomes_jogadores) > 1:
            for x in range(len(nomes_jogadores)):
                if nomes_jogadores[x].pontuacao == nomes_jogadores[x-1].pontuacao:
                    nomes_empate.append(nomes_jogadores[x].nome)
                    empate = True
                else:
                    break
        if len(nomes_empate) > 1:
            print(bcolors.WARNING + 'Houve um empate!' + bcolors.ENDC)
            print(bcolors.WARNING + 'Jogadores que empataram: ' + str(nomes_empate) + bcolors.ENDC)
        
        if empate == True:
            # Inicialização das variáveis
            acertos = 0
            erros = 0
            letras_acertadas = ''
            letras_erradas = ''
            termino_rodada = False
            total_letras = set(vetor_palavraA[rodadas])
            jogadores_eliminados = []
            nomes_jogadores = []
            
            # Criação da ficha do jogador (empate)
            for i in range (len(nomes_empate)):
                nome = nomes_empate[i]
                nomes_jogadores += [nome]
                pontuacao = 0
                jogadas = ''
                nomes_jogadores[i] = Jogador(nome, pontuacao, jogadas)
            
            # Criação de palavra aleatória (empate pode repetir do original e é única)
            # Usa sample para selecionar uma linha aleatória do dataframe
            # axis significa que é a linha, palavra significa o que queremos escolher
            palavra_aleatoria = str(df.sample(axis = 0)['Palavra'])
            # Limpa a palavra, ficamos com a palavra em si que é o index 1 (começando em 0)
            palavra_escolhida = palavra_aleatoria.split()[1]
            # Cria a dica da palavra pesquisando a sua linha toda no dataframe
            dica_palavra = str(df[df['Palavra'].str.contains(palavra_escolhida)])
            dica_palavra = dica_palavra.split()[4]
            
            while repetida == True:
                if re.compile(palavra_escolhida, flags=re.IGNORECASE).search in vetor_palavraA:
                    palavra_aleatoria = str(df.sample(axis = 0)['Palavra'])
                    palavra_escolhida = palavra_aleatoria.split()[1]
                    dica_palavra = str(df[df['Palavra'].str.contains(palavra_escolhida)])
                    dica_palavra = dica_palavra.split()[4]
            else:
                vetor_palavraA.append(palavra_escolhida)
                vetor_dicaA.append(dica_palavra)
                repetida = False
            
            # Inicio da rodada de empate
            print(os.system('clear'))
            print(bcolors.WARNING + 'Rodada desempate' + bcolors.ENDC)
            print(bcolors.WARNING + 'Jogadores que empataram: ' + str(nomes_empate) + bcolors.ENDC)
            
            while termino_rodada == False:
                
                while erros <= 5:
                    if termino_rodada == True:
                        break
                    
                    for x in range(len(nomes_jogadores)):
                        if termino_rodada == True:
                            break
                        
                        elif nomes_jogadores[x] in jogadores_eliminados:
                            x += 1
                        
                        elif x <= len(nomes_jogadores):
                            
                            mensagem = ''
                            for letra in vetor_palavraA[-1]:
                                if letra in letras_acertadas:
                                    mensagem += letra + ''
                                else:
                                    mensagem += '_ '     
                            
                            if mensagem == vetor_palavraA[-1]:
                                print(bcolors.HEADER + 'Parabéns, você(s) acertou(aram) todas as letras da palavra!' + bcolors.ENDC)
                                for jogador in range(len(nomes_jogadores)):
                                    nomes_jogadores[jogador].pontuacao += 1
                                termino_rodada = True
                                break
                            
                            print(os.system('clear'))
                            print(bcolors.WARNING + 'Rodada desempate' + bcolors.ENDC)
                            print(bcolors.HEADER + 'Vez de ' + nomes_jogadores[x].nome + bcolors.ENDC)
                            print(bcolors.BOLD + mensagem + bcolors.ENDC)
                            print(bcolors.OKCYAN + 'A palavra possui {} letras'.format(str(len(vetor_palavraA[-1]))) + bcolors.ENDC)
                            print('A dica é: ' + vetor_dicaA[-1])
                            print(bcolors.OKGREEN + 'Letras corretas: ' + letras_acertadas + bcolors.ENDC)
                            print(bcolors.FAIL + 'Letras incorretas: ' + letras_erradas + bcolors.ENDC)
                            print(bcolors.HEADER + 'Total de erros: ' + str(erros) + '/5' + bcolors.ENDC)
                            
                            letra = input(bcolors.WARNING + 'Digite a letra ou chute a palavra completa: ' + bcolors.ENDC).upper()
                            
                            if len(letra) == 1:
                                
                                if letras_acertadas == len(total_letras):
                                    print(bcolors.OKGREEN + 'Parabéns, você(s) acertou(aram) todas as letras da palavra!' + bcolors.ENDC)
                                    # nomes_jogadores[x].pontuacao += 1
                                    termino_rodada = True
                                    break
                                
                                elif letra in vetor_palavraA[-1]: 
                                    print(bcolors.OKGREEN + 'Você acertou!\n' + bcolors.ENDC)
                                    letras_acertadas += letra
                                    nomes_jogadores[x].add_jogada('[' + letra + '] ')
                                    acertos += 1
                                
                                else:
                                    print(bcolors.FAIL + 'Errou trouxa!\n' + bcolors.ENDC)
                                    letras_erradas += letra
                                    nomes_jogadores[x].add_jogada('[' + letra + '] ')
                                    erros += 1
                        
                            elif len(letra) > 1:
                                if letra == vetor_palavraA[-1]:
                                    print(bcolors.OKGREEN + 'Parabéns {}, você acertou a palavra!'.format(nomes_jogadores[x].nome) + bcolors.ENDC)
                                    nomes_jogadores[x].pontuacao += 1
                                    letras_acertadas += ' *' + letra + '* '
                                    nomes_jogadores[x].add_jogada('[' + letra + '] ')
                                    termino_rodada = True
                                    break   
                                else:
                                    print(bcolors.WARNING + 'Você não pode digitar mais de uma letra por vez ou errou a palavra!' + bcolors.ENDC)
                                    if len(nomes_jogadores) <= 1:
                                        print(bcolors.FAIL + 'Você errou a palavra e perdeu o jogo!' + bcolors.ENDC)
                                        termino_rodada = True
                                        break
                                    else:
                                        print(bcolors.FAIL + 'Você errou a palavra e foi eliminado!' + bcolors.ENDC)
                                        letras_erradas += ' *' + letra + '* ' 
                                        nomes_jogadores[x].add_jogada('[' + letra + '] ')
                                        erros += 1
                                        jogadores_eliminados.append(nomes_jogadores[x])            
                        else:
                            x = 0
                        
            # Finalização da rodada de empate e prints finais
            print(os.system('clear'))
            print(bcolors.OKCYAN + 'Palavra do desempate: ' + palavra_escolhida + bcolors.ENDC)
            for jogador in range(len(nomes_empate)):
                print(bcolors.HEADER + 'Jogador: ' + nomes_jogadores[jogador].nome + bcolors.ENDC)
                print(bcolors.HEADER + 'Pontuação: ' + str(nomes_jogadores[jogador].pontuacao) + bcolors.ENDC)
                print(bcolors.HEADER + 'Jogadas: ' + str(nomes_jogadores[jogador].jogadas) + bcolors.ENDC)
                print('\n')
            print(bcolors.OKGREEN + 'Jogadas corretas da rodada de desempate: ' + letras_acertadas + bcolors.ENDC)
            print(bcolors.FAIL + 'Jogadas incorretas da rodada de desempate: ' + letras_erradas + bcolors.ENDC)
            print(bcolors.OKGREEN + 'Total de acertos do desempate: ' + str(acertos) + bcolors.ENDC)
            print(bcolors.FAIL + 'Total de erros do desempate: ' + str(erros) + bcolors.ENDC)
        
        # Verificação de ganhador
        for i, j in enumerate(nomes_jogadores):
            if j == max(nomes_jogadores, key=lambda x: x.pontuacao):
                if nomes_jogadores[i].pontuacao == 0:
                    print(bcolors.FAIL + 'Ninguém ganhou!' + bcolors.ENDC)
                    break
                else:
                    if n_jogadores > 1:
                        print(bcolors.OKGREEN + 'O vencedor foi: ' + nomes_jogadores[i].nome + bcolors.ENDC)
                        break
                    elif n_jogadores == 1:
                        print(bcolors.OKGREEN + 'Parabéns, você ganhou o jogo!' + bcolors.ENDC)
                        break

if __name__ == '__main__':
    main()