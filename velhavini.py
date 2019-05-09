import random #importando o comando 'random' para fazer o jogo contra o computador
sorteio = random.randrange(1, 10) #apenas utilizada para onde o computador jogar for um lugar aleatorio entre 1 e 9.
vez =  'X' #atribui a vez para quem esta jogando
j =''
c1 = '1' # todos esses c1,c2,c3,c4... Sao as casas do jogo
c2 = '2'
c3 = '3'
c4 = '4'
c5 = '5'
c6 = '6'
c7 = '7'
c8 = '8'
c9 = '9'
def tabuleiro(): #imprimindo o tabuleiro
    print (c1, '|', c2,'|', c3)
    print ('--+---+--')
    print (c4, '|', c5, '|', c6)
    print ('--+---+--')
    print (c7, '|', c8, '|', c9)
    
def ganhador(c1, c2, c3, c4, c5, c6, c7, c8, c9): #esta comparando se as casas sao iguais para ter o ganhador
    return c1 == c2 == c3 or c4 == c5 == c6 or c7 == c8 == c9 or \
       c1 == c4 == c7 or c2 == c5 == c8 or c3 == c6 == c9 or \
       c1 == c5 == c9 or c3 == c5 == c7 
        


def deu_velha(c1, c2, c3, c4, c5, c6, c7, c8, c9): #esta comparando se as casas sao diferentes para ver se deu velha.
      return c1 != '1' and c2 != '2' and c3 != '3' and \
        c4 != '4' and c5 != '5' and c6 != '6' and \
        c7 != '7' and c8 != '8' and c9 != '9' 

def valida_casa(c,c1, c2, c3, c4, c5, c6, c7, c8, c9):  #está vendo se as casas que o player ou computador jogou foi correta.
    if c == '1':
        if c1 == '1':
            return True
    elif c =='2':
        if c2 == '2':
            return True
    elif c == '3':
        if c3 =='3':
            return True
    elif c =='4':
        if c4=='4':
            return True
    elif c == '5':
        if c5 == '5' :
            return True
    elif c=='6':
        if c6 == '6':
            return True
    elif c == '7':
        if c7 == '7':
            return True
    elif c == '8':
        if c8 == '8':
            return True
    elif c == '9':
        if c9 == '9':
            return True
    return False        


def jogar():

    global vez, c1, c2, c3, c4, c5, c6, c7, c8, c9, CONTRA_COMPUTADOR

    if CONTRA_COMPUTADOR and vez == 'O':
        jogo = str(random.randrange(1, 10))
        while  not valida_casa(jogo ,c1, c2, c3, c4, c5, c6, c7, c8, c9):
           jogo = str(random.randrange(1, 10))
        print('O computador jogou na casa', jogo) #essa função determinou aonde o computador jogou
    else:
        jogo = str(input('Digite a casa que voce quer jogar: ')) 
        while  not valida_casa(jogo ,c1, c2, c3, c4, c5, c6, c7, c8, c9): # se a casa nao for valida, a jogada é invalidada.
            print('Jogada invalida') #invalidou a jogada
            jogo = str(input('Digite a casa que voce quer jogar: '))
       

    if jogo == c1: #irá ver de quem é a vez de jogar,e tambem imprimara de quem é a vez.
        c1 = vez
        if vez == 'X':
            vez = 'O'
        else:
            vez = 'X'
    elif jogo == c2:
        c2 = vez
        if vez == 'X':
            vez = 'O'
        else:
            vez = 'X'
    elif jogo == c3:
        c3 = vez
        if vez == 'X':
            vez = 'O'
        else:
            vez = 'X'
    elif jogo == c4:
        c4 = vez
        if vez == 'X':
            vez = 'O'
        else:
            vez = 'X'
    elif jogo == c5:
        c5 = vez
        if vez == 'X':
            vez = 'O'
        else:
            vez = 'X'
    elif jogo == c6:
        c6 = vez
        if vez == 'X':
            vez = 'O'
        else:
            vez = 'X'
    elif jogo == c7:
        c7 = vez
        if vez == 'X':
            vez = 'O'
        else:
            vez = 'X'
    elif jogo == c8:
        c8 = vez
        if vez == 'X':
            vez = 'O'
        else:
            vez = 'X'
    elif jogo == c9:
        c9 = vez
        if vez == 'X':
            vez = 'O'
        else:
            vez = 'X'
    print('Agora é a vez de', vez) 

jogando = True
CONTRA_COMPUTADOR = False
while jogando:
    CONTRA_COMPUTADOR = str(input('Quer jogar contra computador? (Y/N): ')) == 'Y' #está pedindo no começo do jogo se o user quer jogar contra o computador ou nao
    if CONTRA_COMPUTADOR:
        print ('Informe o nome dos jogadores') #pedindo nome dos jogadores
        jogador01= input('Digite o nome do jogador(x): ') 
    else:
        print ('Informe o nome dos jogadores')
        jogador01= input('Digite o nome do jogador 1(x): ') #está pedindo o nome dos jogadores
        jogador02 = input('Digite o nome do jogador 2(O): ')

    while not deu_velha(c1, c2, c3, c4, c5, c6, c7, c8, c9) and \
     not ganhador(c1, c2, c3, c4, c5, c6, c7, c8, c9):
        tabuleiro()
        jogar()
    else: #se nao,teremos um ganhador ou deu velha
        tabuleiro()
        if ganhador(c1, c2, c3, c4, c5, c6, c7, c8, c9):
            if vez == 'X':
                vez = 'O'
            else:
                vez = 'X'
            print('Parabens', vez, 'voce ganhou!') #definiu o ganhador
        else:
            print("Deu velha...") #deu velha,ou seja todas as casas estao diferentes.

        jogando  = input('Quer continuar jogando? (Y/N): ') == 'Y' #está pedindo se o jogador vai querer continuar ou nao.
        if jogando:
            vez =  'X'
            j =''
            c1 = '1'
            c2 = '2'
            c3 = '3'
            c4 = '4'
            c5 = '5'
            c6 = '6'
            c7 = '7'
            c8 = '8'
            c9 = '9'
        else:
            print('Obrigado por jogar!!') #se o jogador digitou 'N' printou esta mensagem.
