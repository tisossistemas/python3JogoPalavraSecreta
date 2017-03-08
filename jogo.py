import random as aleatorio, os as so, datetime as data, time
TELA =[
    '''
    ****************************************************************************************************************
    ***                                          JOGO da PALAVRA SECRETA                                         ***
    ***                                                                                                          ***
    ***************************************************************************************************by-Prince****
    ''',
    '''
    ****************************************************************************************************************
    ***                                          JOGO da PALAVRA SECRETA                                         ***
    ***                                                                                                          ***
    ***                                              FIM DE JOGO                                                 ***
    ***************************************************************************************************by-Prince****
    '''
    ]

def gerar_key_palavraSecreta_pegaPlacar(arquivo):
    '''
    :param arquivo: Nome do arquivo de texto onde esta as palavras para serem sorteadas
    :var lista: lista de dados onde será armazenado os dados sorteados
    :var sorteio: recebe o sorteio, transformando o resultado em uma lista de dados separados pela virgula
    :var arquivo: usado apenas para fazer a junção/concatenação do texto inserido pelo parametro arquivo e a extençao
    do arquivo usado como fonte de dados para sorteio. neste caso usamos o arquivo txt.
    :var arq: recebe todo o conteudo do arquivo aberto
    :var key: recebe o primeiro valor da lista do item sorteado
    :var palavraSecreta: recebe o segundo valor da lista do item sorteado
    :return: lista com duas palavras e a pontuação do redorde, a primeira palvra e a chafe ou palavra de ajuda, a segunda
    a palavra a ser descoberta pelo usuario
    '''
    aleatorio.seed(data.datetime.now())
    lista = []
    lista1 =[]
    arquivo = str(arquivo)+'.txt'
    arq = open(arquivo)

    for x in arq: #inserindo cada linha do arquivo na lista
        lista.append(x)
    arq.close() #fechando a conecçao com o arquivo

    placar = int(lista[0].split(',')[1])

    def sort():
        lista1.clear()
        sorteio = aleatorio.choice(lista).split(',') #realizando um sorteio aleatorio,
        key = sorteio[0]
        palavraSecreta = sorteio[1].strip()
        lista1.append(key)
        lista1.append(palavraSecreta)
        return lista1

    key,palavraSecreta = sort()

    while key == 'placar':
        key, palavraSecreta = sort()

    lista.clear()
    lista.append(key.upper()) #após a lista ser apagada, adcionamos somente a palavra chave sorteado novamente na lista
    lista.append(palavraSecreta.upper()) #após a lista ser apagada, adcionamos somente a palavra secreta sorteado novamente na lista
    lista.append(placar)
    return lista #retornamos a lista com os dois valores
def mostraTela(key,palavraSecreta,placarRecorde,placar,totaAcertos,palpites,ponto,palpitesFeitos):
	'''
	Imprime a tela do jogo com os valores necessarios para compreender e ajudar na resoluçaõ do jogo
    :param key: Dica para resolução da palavra secreta
    :param palavraSecreta: Recebe a palavra secreta do jogo
	:param placarRecorde: Recebe o recorde do jogo
	:param placar: Recebe o placar do jogador
	:param totaAcertos: Recebe o total de acertos
	:param palpites: Recebe os palpites 
	:param pontos: Recebe o pontos que estão em jogo
	:param palpitesFeitos: Recebe todos os palpites que foram usados no jogo
    '''
    so.system('cls')
    print(TELA[0])
    print(' PONTOS EM JOGO: %s \n Seu placar: %s Recorde %s\n Acertos: %s   Palpites Feitos: %s\n Dica: %s \n'
          %(str(ponto),str(placar),str(placarRecorde),str(totaAcertos),str(palpitesFeitos), key))
    print(' Palpites usados: ',end='')
    imprimeEspaco(palpites)
    print()
    imprimeEspaco(ocultaPalavraSecreta(palavraSecreta=palavraSecreta, palpites=totaAcertos))
def imprimeEspaco(texto):
    '''
    :param texto: Texto a ser impresso
    :return: Não retorna nada
    Imprime texto com expaço entre as letras
    '''
    for x in texto:
        print( x , end=' ')
def geraPontuacao():
    '''
    O jogo deve gerar uma pontuação que será atribuida para o acerto ou erro os pontos dever sem os seguinte 3,6,9,
    12,15,18 ou 21 pontos
    :return: ponto selecionado
    '''
    aleatorio.seed(data.datetime.now())
    pontosPossiveis = [3,6,9,12,15,18,21]
    aleatorio.seed(data.datetime.now())
    pontoSelecionado = aleatorio.choice(pontosPossiveis)
    return pontoSelecionado
def ver_Palpites_todosPalpites_placar(palpite, todos_palpites, palavraSecreta, ponto, placar):
	'''
	Retorna os Palpites, todos os palpites e o placar do jogo no formato de lista de dados
    :param palpite:
	:param todos_palpites:
	:param palavraSecreta:
	:param ponto:
	:param placar:
	:return lista:
    '''
    lista =[]
    erro = 0
    acerto = 0
    placar_jogador = placar

    executa = False

    if palpite not in todos_palpites:
        todos_palpites += palpite
        executa = True

    if executa == True:
        for letra in palavraSecreta:
            if letra == palpite:
                acerto += ponto
            else:
                erro =- ponto
        if acerto > 0:
            placar_jogador = placar + acerto
        else:
            placar_jogador = placar + erro
    lista.append(palpite)
    lista.append(todos_palpites)
    lista.append(placar_jogador)
    return lista
def ocultaPalavraSecreta(palavraSecreta,palpites):
    '''
	Ocultar a palavraSecreta se exestir alguma letra desta palavra na variavel palpites a letra sera exebida
    :param palavraSecreta: A palavra que deve ser ocultada
    :param palpites: As letras usadas nos palpites do usuario
    :return: Retorna uma palvra com letras ocultas, se a letra já tiver sido sugerida pelo usuario a letra será apresentada para o usuario
    '''
    palavraSecretaOculta = ''
    for x in palavraSecreta:
        if x in palpites:
            palavraSecretaOculta += x
        else:
            palavraSecretaOculta += ' _ '
    return palavraSecretaOculta
def verificaFim(palavraSecreta,totalAcerto,placar):
    '''
    Verifica se a palavraSecreta possui todas as letras na variavel totaAcertos caso sim deve enviar continuar com valor Falso para encerrar o loop
    :param palavraSecreta: recebe a palavra secreta
    :param totalAcertos:  recebe as letras certas
    :param placar: recebe o placar
    :return: continuar com true ou false para continuar o jogo
    '''
    continuar = True
    verificando = 0
    for letra in palavraSecreta:
        if letra in totalAcerto:
            verificando += 1


    if len(palavraSecreta) == verificando:
        so.system('cls')
        print(TELA[1])
        print('Você acertou a palavra %s Placar final %s pontos' % (palavraSecreta, str(placar)))
        opcao = input('Para continuar a jogar insira a letra S :').upper().startswith('S')
        if opcao == True:
            man()
        else:
            continuar = False
    return continuar
def pegaLetra(palpitesFeitos):
	'''
	Verificar se o palpite possui apenas uma letra, não debe ter outros caracteres nem aceitar palavras com acentuação grafica
	:param palpitesFeitos: recebe todos os palpites ja feitos
    '''
	lista = []
    palpite = input('\n\n Digite um palpite: ').upper()
    if (len(palpite) != 1) or (not 'A' <= palpite <= 'Z'):
        print('\n[ ! ] Insira apenas uma letra\n')
        time.sleep(2)
        palpitesFeitos, palpite = pegaLetra(palpitesFeitos)
    elif palpite in palpitesFeitos:
        print('\n[ ! ] Você já usou este palpite insira outra letra\n')
        time.sleep(2)
        palpitesFeitos, palpite = pegaLetra(palpitesFeitos)
    palpitesFeitos += palpite
    lista.append(palpitesFeitos)
    lista.append(palpite)
    return lista
def man():
	'''
	chamada principal para executar o programa
	'''
    key, palavraSecreta, placarRecorde = gerar_key_palavraSecreta_pegaPlacar('palavras')
    placar = 0
    totalAcerto = ''
    palpites = ''
    palpitesFeitos = ''
    continuar = True

    while continuar:
        ponto = geraPontuacao()
        mostraTela(key,palavraSecreta,placarRecorde,placar,totalAcerto,palpites,ponto,palpitesFeitos)
        palpitesFeitos, letra = pegaLetra(palpitesFeitos)
        palpites,totalAcerto,placar = ver_Palpites_todosPalpites_placar(letra,totalAcerto,palavraSecreta,ponto,placar)
        continuar = verificaFim(palavraSecreta,totalAcerto,placar)
    so.system('exit')
man()













