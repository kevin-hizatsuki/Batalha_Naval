#-*-coding: utf-8 -*-
import re
resultado=open('resultado.txt','w')
def TABULEIRO():
    posicionamento = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'L', 'M', 'N', 'O', 'P']
    pos = []
    n = []
    x = 0
    while x < len(posicionamento):
        for i in range(1, 16):
            pos = posicionamento[x] + str(i)
            n.append(pos)
            pos = []
        x += 1
    return n
def POSICONAMENTO_DOS_BARCOS_J1():
    arquivo_barco = open('jogador1.txt', 'r')
    l = []
    dicpos = []
    l2,jogada = [],[]
    for i in arquivo_barco.readlines():
        l.append(re.split('\r|;|[|]', i))
    for d in l:
        if d[-1]=='' or d[-1]=='\n' or d[-1]=='\r':
            d.pop(-1)
        for b in d:
            if 'T' in d or '#Jogada' in d:
                jogada.append(b)
            elif 'T' not in d:
                dicpos = b[0] + b[1:]
                l2.append(dicpos)
    arquivo_barco.close()
    return [l2,jogada[2:]]
def POSICONAMENTO_DOS_BARCOS_J2():
    arquivo_barco = open('jogador2.txt', 'r')
    l = []
    dicpos = []
    l2,jogada = [],[]
    for i in arquivo_barco.readlines():
        l.append(re.split('\r|;|[|]', i))
    for d in l:
        if d[-1]=='' or d[-1]=='\n' or d[-1]=='\r':
            d.pop(-1)
        for b in d:
            if 'T' in d or '#Jogada' in d:
                jogada.append(b)
            elif 'T' not in d:
                dicpos = b[0] + b[1:]
                l2.append(dicpos)
    arquivo_barco.close()
    return [l2,jogada[2:]]
def CLASSE_J1():
    val=[]
    cont=1
    encouracados,portaavioes,submarinos,cruzadores= [],[],[],[]
    for i in POSICONAMENTO_DOS_BARCOS_J1()[0]:
        if cont==1:
            encouracados.append(i)
            if i=='2':
                cont+=1
        if cont==2:
            portaavioes.append(i)
            if i=='3':
                cont+=1
        if cont==3:
            submarinos.append(i)
            if i=='4':
                cont+=1
        elif cont==4:
            cruzadores.append(i)
    x=1
    while x<4:
        if x==1:
            encouracados.pop(0)
            encouracados.pop(-1)
        elif x==2:
            portaavioes.pop(0)
            portaavioes.pop(-1)
        elif x==3:
            submarinos.pop(0)
            submarinos.pop(-1)
        x+=1
    return encouracados,portaavioes,submarinos,cruzadores
def CLASSE_J2():
    val=[]
    cont=1
    encouracados,portaavioes,submarinos,cruzadores=[],[],[],[]
    for i in POSICONAMENTO_DOS_BARCOS_J2()[0]:
        if cont==1:
            encouracados.append(i)
            if i=='2':
                cont+=1
        if cont==2:
            portaavioes.append(i)
            if i=='3':
                cont+=1
        if cont==3:
            submarinos.append(i)
            if i=='4':
                cont+=1
        elif cont==4:
            cruzadores.append(i)
    x=1
    while x<4:
        if x==1:
            encouracados.pop(0)
            encouracados.pop(-1)
        elif x==2:
            portaavioes.pop(0)
            portaavioes.pop(-1)
        elif x==3:
            submarinos.pop(0)
            submarinos.pop(-1)
        x+=1
    return encouracados,portaavioes,submarinos,cruzadores
def ENCOURACADO_J1():
    x,y=0,1
    error=False
    encouracado1,encouracado2,aux=[],[],[]
    for i in CLASSE_J1()[0]:
        if i[:-1] not in TABULEIRO():
            error=True
            #break
        if i[-1]=='V':
            while x<len(TABULEIRO()):
                if TABULEIRO()[x]==i[:-1]:
                    while y<=4:
                        if x>=len(TABULEIRO()):
                            error=True
                            break
                        else:
                            encouracado1.append(TABULEIRO()[x])
                            x+=15
                            y+=1
                x+=1
        if i[-1]=='H':
            while x <len(TABULEIRO()):
                if TABULEIRO()[x]==i[:-1]:
                    while y<=4:
                        if x>=len(TABULEIRO()):
                            error = True
                            break
                        else:
                            encouracado2.append(TABULEIRO()[x])
                            aux.append(TABULEIRO()[x])
                            x+=1
                            y+=1

                for v in aux:
                    if v[0]!=i[0]:
                        error=True
                        break
                x += 1
        x=0
        y=1
        encouracado=encouracado1+encouracado2
        aux=[]
    return encouracado,error
def ENCOURACADO_J2():
    x, y = 0, 1
    error = False
    encouracado1, encouracado2,aux = [], [],[]
    for i in CLASSE_J2()[0]:
        if i[:-1] not in TABULEIRO():
            error = True
            # break
        if i[-1] == 'V':
            while x < len(TABULEIRO()):
                if TABULEIRO()[x] == i[:-1]:
                    while y <= 4:
                        if x >= len(TABULEIRO()):
                            error = True
                            break
                        else:
                            encouracado1.append(TABULEIRO()[x])
                            x += 15
                            y += 1
                x += 1
        if i[-1] == 'H':
            while x < len(TABULEIRO()):
                if TABULEIRO()[x] == i[:-1]:
                    while y <= 4:
                        if x >= len(TABULEIRO()):
                            error = True
                            break
                        else:
                            encouracado2.append(TABULEIRO()[x])
                            aux.append(TABULEIRO()[x])
                            x += 1
                            y += 1

                for v in aux:
                    if v[0] != i[0]:
                        error = True
                        break
                x += 1
        x = 0
        y = 1
        encouracado = encouracado1 + encouracado2
        aux=[]
    return encouracado,error
def PORTA_AV_J1():
    x,y=0,1
    error=False
    porta_av,porta_av1,porta_av2,aux=[],[],[],[]
    for i in CLASSE_J1()[1]:
        if i[:-1] not in TABULEIRO():
            error = True
        if i[-1]=='V':
            while x<len(TABULEIRO()):
                if TABULEIRO()[x]==i[:-1]:
                    while y<=5:
                        if x>=len(TABULEIRO()):
                            error=True
                            break
                        else:
                            porta_av1.append(TABULEIRO()[x])
                            x+=15
                            y+=1
                x+=1
        if i[-1]=='H':
            if i[:-1] not in TABULEIRO():
                error = True
            else:
                while x <len(TABULEIRO()):
                    if TABULEIRO()[x]==i[:-1]:
                        while y<=5:
                            if x>=len(TABULEIRO()):
                                error=True
                                break
                            else:
                                porta_av2.append(TABULEIRO()[x])
                                aux.append(TABULEIRO()[x])
                                x+=1
                                y+=1
                    for v in aux:
                        if v[0]!=i[0]:
                            error=True
                            break
                    x+=1
        x=0
        y=1
        porta_av=porta_av1+porta_av2
        aux=[]
    return porta_av,error
def PORTA_AV_J2():
    x, y = 0, 1
    error = False
    porta_av, porta_av1, porta_av2,aux = [], [], [],[]
    for i in CLASSE_J2()[1]:
        if i[-1] == 'V':
            while x < len(TABULEIRO()):
                if TABULEIRO()[x] == i[:-1]:
                    while y <= 5:
                        if x >= len(TABULEIRO()):
                            error = True
                            break
                        else:
                            porta_av1.append(TABULEIRO()[x])
                            x += 15
                            y += 1
                x += 1
        if i[-1]=='H':
            if i[:-1] not in TABULEIRO():
                error = True
            else:
                while x <len(TABULEIRO()):
                    if TABULEIRO()[x]==i[:-1]:
                        while y<=5:
                            if x>=len(TABULEIRO()):
                                error=True
                                break

                            else:
                                porta_av2.append(TABULEIRO()[x])
                                aux.append(TABULEIRO()[x])
                                x+=1
                                y+=1
                    for v in aux:
                        if v[0]!=i[0]:
                            error=True
                            break
                    x+=1
        x=0
        y=1
        porta_av=porta_av1+porta_av2
        aux=[]
    return porta_av,error
def CRUZADORES_J1():
    x,y=0,1
    error=False
    cruzadores,cruzadores1,cruzadores2,aux=[],[],[],[]
    for i in CLASSE_J1()[3]:
        if i[-1]=='V':
            while x<len(TABULEIRO()):
                if TABULEIRO()[x]==i[:-1]:
                    while y<=2:
                        if x >= len(TABULEIRO()):
                            error = True
                            break
                        else:
                            cruzadores1.append(TABULEIRO()[x])
                            x+=15
                            y+=1
                x+=1
        if i[-1]=='H':
            if i[:-1] not in TABULEIRO():
                error = True
            else:
                while x <len(TABULEIRO()):
                    if TABULEIRO()[x]==i[:-1]:
                        while y<=2:
                            if x >= len(TABULEIRO()):
                                error = True
                                break
                            else:
                                cruzadores2.append(TABULEIRO()[x])
                                aux.append(TABULEIRO()[x])
                                x+=1
                                y+=1
                    for v in aux:
                        if v[0] != i[0]:
                            error = True
                            break
                    x+=1
        x=0
        y=1
        cruzadores=cruzadores1+cruzadores2
        aux=[]
    return cruzadores,error
def CRUZADORES_J2():
    x, y = 0, 1
    error = False
    cruzadores, cruzadores1, cruzadores2,aux = [], [], [],[]
    for i in CLASSE_J2()[3]:
        if i[-1] == 'V':
            while x < len(TABULEIRO()):
                if TABULEIRO()[x] == i[:-1]:
                    while y <= 2:
                        if x >= len(TABULEIRO()):
                            error = True
                            break
                        else:
                            cruzadores1.append(TABULEIRO()[x])
                            x += 15
                            y += 1
                x += 1
        if i[-1]=='H':
            if i[:-1] not in TABULEIRO():
                error = True
            else:
                while x <len(TABULEIRO()):
                    if TABULEIRO()[x]==i[:-1]:
                        while y<=2:
                            if x >= len(TABULEIRO()):
                                error = True
                                break
                            else:
                                cruzadores2.append(TABULEIRO()[x])
                                aux.append(TABULEIRO()[x])
                                x+=1
                                y+=1
                    for v in aux:
                        if v[0] != i[0]:
                            error = True
                            break
                    x+=1
        x=0
        y=1
        cruzadores=cruzadores1+cruzadores2
        aux=[]
    return cruzadores, error
def ALVOS_ACERTADOS_J1():
    total=ENCOURACADO_J1()[0]+PORTA_AV_J1()[0]+CLASSE_J1()[2]+CRUZADORES_J1()[0]
    ponto=0
    for i in POSICONAMENTO_DOS_BARCOS_J1()[1]:
        if i in total:
            ponto+=1
    return ponto
def ALVOS_ACERTADOS_J2():
    total=ENCOURACADO_J2()[0]+PORTA_AV_J2()[0]+CLASSE_J2()[2]+CRUZADORES_J2()[0]
    ponto=0
    for i in POSICONAMENTO_DOS_BARCOS_J2()[1]:
        if i in total:
            ponto+=1
    return ponto
def SUB_J1():
    error=False
    for i in CLASSE_J1()[2]:
        if i not in TABULEIRO():
            error=True
    return error
def SUB_J2():
    error=False
    for i in CLASSE_J2()[2]:
        if i not in TABULEIRO():
            error=True
    return error
def ATAQUE_ENCOURACADO_J1():
    x = 1
    cont = 0
    abatido = 0
    lista_enco, enco = [], []
    for i in ENCOURACADO_J2()[0]:
        if cont != 4:
            lista_enco.append(i)
            cont += 1
            if cont == 4:
                enco.append(lista_enco)
                for i in lista_enco:
                    if i in POSICONAMENTO_DOS_BARCOS_J1()[1]:
                        abatido+=1
                        break
                cont = 0
                lista_enco = []
    l = []
    ponto = 0
    for i in enco:
        for e in i:
            if e in POSICONAMENTO_DOS_BARCOS_J1()[1]:
                e = '*'
                l.append(e)
        if len(l) < 4:
            aux = len(l) * 3
        elif len(l) == 4:
            aux = ((len(l) - 1) * 3) + 5
        l = []
        ponto = ponto + aux
    return ponto,abatido
def ATAQUE_ENCOURACADO_J2():
    x = 1
    cont = 0
    abatido=0
    lista_enco, enco = [], []
    for i in ENCOURACADO_J1()[0]:
        if cont != 4:
            lista_enco.append(i)
            cont += 1
            if cont == 4:
                enco.append(lista_enco)
                for i in lista_enco:
                    if i in POSICONAMENTO_DOS_BARCOS_J2()[1]:
                        abatido+=1
                        break
                cont = 0
                lista_enco = []
    l = []
    ponto = 0
    for i in enco:
        for e in i:
            if e in POSICONAMENTO_DOS_BARCOS_J2()[1]:
                e = '*'
                l.append(e)
        if len(l) < 4:
            aux = len(l) * 3
        elif len(l) == 4:
            aux = ((len(l) - 1) * 3) + 5
            #abatido+=1
        l = []
        ponto = ponto + aux
    return ponto,abatido
def ATAQUE_PORTA_AV_J1():
    x = 1
    cont = 0
    abatido=0
    lista_port, port = [], []
    for i in PORTA_AV_J2()[0]:
        if cont != 5:
            lista_port.append(i)
            cont += 1
            if cont == 5:
                port.append(lista_port)
                for i in lista_port:
                    if i in POSICONAMENTO_DOS_BARCOS_J1()[1]:
                        abatido+=1
                        break
                cont = 0
                lista_port = []
    l = []
    ponto = 0
    for i in port:
        for e in i:
            if e in POSICONAMENTO_DOS_BARCOS_J1()[1]:
                e = '*'
                l.append(e)
        if len(l) < 5:
            aux = len(l) * 3
            #abatido += 1
        elif len(l) == 5:
            aux = ((len(l) - 1) * 3) + 5
            #abatido+=1
        l = []
        ponto = ponto + aux
    return ponto,abatido
def ATAQUE_PORTA_AV_J2():
    x = 1
    cont = 0
    abatido=0
    lista_port, port = [], []
    for i in PORTA_AV_J1()[0]:
        if cont != 5:
            lista_port.append(i)
            cont += 1
            if cont == 5:
                port.append(lista_port)
                for i in lista_port:
                    if i in POSICONAMENTO_DOS_BARCOS_J2()[1]:
                        abatido+=1
                        break
                cont = 0
                lista_port = []
    ponto = 0
    l=[]
    for i in port:
        for e in i:
            if e in POSICONAMENTO_DOS_BARCOS_J2()[1]:
                e = '*'
                l.append(e)
        if len(l) < 5:
            aux = len(l) * 3
            #abatido += 1
        elif len(l) == 5:
            aux = ((len(l) - 1) * 3) + 5
            #abatido+=1
        l = []
        ponto = ponto + aux
    return ponto,abatido
def ATAQUE_CRUZADORES_J1():
    x = 1
    cont = 0
    abatido=0
    lista_cruz, cruz = [], []
    for i in CRUZADORES_J2()[0]:
        if cont != 2:
            lista_cruz.append(i)
            cont += 1
            if cont == 2:
                cruz.append(lista_cruz)
                for i in lista_cruz:
                    if i in POSICONAMENTO_DOS_BARCOS_J1()[1]:
                        abatido+=1
                        break
                cont = 0
                lista_cruz = []
    l = []
    ponto = 0
    for i in cruz:
        for e in i:
            if e in POSICONAMENTO_DOS_BARCOS_J1()[1]:
                e = '*'
                l.append(e)
        if len(l) < 2:
            aux = len(l) * 3
            #abatido += 1
        elif len(l) == 2:
            aux = ((len(l) - 1) * 3) + 5
            #abatido+=1
        l = []
        ponto = ponto + aux
    return ponto,abatido
def ATAQUE_CRUZADORES_J2():
    x = 1
    cont = 0
    abatido=0
    lista_cruz, cruz = [], []
    for i in CRUZADORES_J1()[0]:
        if cont != 2:
            lista_cruz.append(i)
            cont += 1
            if cont == 2:
                cruz.append(lista_cruz)
                for i in lista_cruz:
                    if i in POSICONAMENTO_DOS_BARCOS_J2()[1]:
                        abatido+=1
                        break
                cont = 0
                lista_cruz = []
    l = []
    ponto = 0
    for i in cruz:
        for e in i:
            if e in POSICONAMENTO_DOS_BARCOS_J2()[1]:
                e = '*'
                l.append(e)
        if len(l) < 2:
            aux = len(l) * 3
        elif len(l) == 2:
            aux = ((len(l) - 1) * 3) + 5
            #abatido+=1
        l = []
        ponto = ponto + aux
    return ponto,abatido
def ATAQUE_SUB_J1():
    l = []
    ponto = 0
    abatido=0
    for e in CLASSE_J2()[2]:
        if e in POSICONAMENTO_DOS_BARCOS_J1()[1]:
            ponto += 5
            abatido+=1
    return ponto,abatido
def ATAQUE_SUB_J2():
    l = []
    abatido=0
    ponto = 0
    for e in CLASSE_J1()[2]:
        if e in POSICONAMENTO_DOS_BARCOS_J2()[1]:
            ponto += 5
            abatido+=1
    return ponto,abatido
def ERRO_POSICAO():
    error1=False
    error2=False
    if ENCOURACADO_J1()[1]==True or  PORTA_AV_J1()[1]==True or  CRUZADORES_J1()[1]==True or  SUB_J1()==True:
        error1=True
    elif ENCOURACADO_J2()[1]==True or PORTA_AV_J2()[1]==True or CRUZADORES_J2()[1]==True or SUB_J2()==True:
        error2=True
    return error1,error2
def ERRO_POS_TOTAL():
    erro=False
    if ERRO_POSICAO()[0]==True or ERRO_POSICAO()[1]==True:
        erro=True
    return erro
def PONTUACAO():
    J1=ATAQUE_ENCOURACADO_J1()[0]+ATAQUE_PORTA_AV_J1()[0]+ATAQUE_SUB_J1()[0]+ATAQUE_CRUZADORES_J1()[0]
    J2=ATAQUE_ENCOURACADO_J2()[0]+ATAQUE_PORTA_AV_J2()[0]+ATAQUE_SUB_J2()[0]+ATAQUE_CRUZADORES_J2()[0]
    return J1,J2
def ABATIDO():
    J1 = ATAQUE_ENCOURACADO_J1()[1] + ATAQUE_PORTA_AV_J1()[1] + ATAQUE_SUB_J1()[1] + ATAQUE_CRUZADORES_J1()[1]
    J2 = ATAQUE_ENCOURACADO_J2()[1] + ATAQUE_PORTA_AV_J2()[1] + ATAQUE_SUB_J2()[1] + ATAQUE_CRUZADORES_J2()[1]
    return J1,J2
def GANHAADOR():
    if PONTUACAO()[0]>PONTUACAO()[1]:
        ganhador=resultado.write('J1 %dAA %dAE %dPT'%(ALVOS_ACERTADOS_J1(),13-ABATIDO()[0],PONTUACAO()[0]))
    elif PONTUACAO()[0]<PONTUACAO()[1]:
        ganhador = resultado.write('J2 %dAA %dAE %dPT'%(ALVOS_ACERTADOS_J2(),13-ABATIDO()[1],PONTUACAO()[1]))
    elif PONTUACAO()[0]==PONTUACAO()[1]:
        ganhador = resultado.write('J1 %dAA %dAE %dPT\nJ2 %dAA %dAE %dPT'%(ALVOS_ACERTADOS_J1(),13-ABATIDO()[0],PONTUACAO()[0],ALVOS_ACERTADOS_J2(),13-ABATIDO()[1],PONTUACAO()[1]))
    return ganhador
def JOGADAS_J1():
    res=False
    if len(POSICONAMENTO_DOS_BARCOS_J1()[1])!=20 or len(POSICONAMENTO_DOS_BARCOS_J1()[1]) != 20:
        res=True
    return res
def JOGADAS_J2():
    res=False
    if len(POSICONAMENTO_DOS_BARCOS_J2()[1])!=20 or len(POSICONAMENTO_DOS_BARCOS_J2()[1]) != 20:
        res=True
    return res
def NAO_ENCONTRADO_J1():
    igual = False
    for i in POSICONAMENTO_DOS_BARCOS_J1()[1]:
        if i not in TABULEIRO():
            igual = True
    return igual
def NAO_ENCONTRADO_J2():
    igual = False
    for i in POSICONAMENTO_DOS_BARCOS_J2()[1]:
        if i not in TABULEIRO():
            igual = True
    return igual
SOMA_J1=ENCOURACADO_J1()[0]+PORTA_AV_J1()[0]+CLASSE_J1()[2]+CRUZADORES_J1()[0]
SOMA_J2=ENCOURACADO_J2()[0]+PORTA_AV_J2()[0]+CLASSE_J2()[2]+CRUZADORES_J2()[0]
def NAO_POSICAO():
    posicao=False
    for i in SOMA_J1:
        if i not in TABULEIRO():
            posicao=True
    for i in SOMA_J2:
        if i not in TABULEIRO():
            posicao=True
    return posicao
def REPETICAO_PECAS_J1():
    repeticao = False
    for i in SOMA_J1:
        if SOMA_J1.count(i) > 1:
            repeticao = True
    return repeticao
def REPETICAO_PECAS_J2():
    repeticao=False
    for i in SOMA_J2:
        if SOMA_J2.count(i) > 1:
            repeticao = True
    return repeticao
def ERRO_QUA_PEC_J1():
    cont=1
    erro=False
    for i in CLASSE_J1():
        if cont==1:
            if len(i)!=2:
                erro=True
        if cont==2:
            if len(i)!=2:
                erro=True
        if cont==3:
            if len(i)!=5:
                erro=True
        if cont==4:
            if len(i)!=4:
                erro=True
        cont+=1
    return erro
TOTAL=ENCOURACADO_J2()[0]+PORTA_AV_J1()[0]+CLASSE_J2()[2]+CRUZADORES_J2()[0]
def ERRO_QUA_PEC_J2():
    cont=1
    erro=False
    for i in CLASSE_J2():
        if cont==1:
            if len(i)!=2:
                erro=True
        if cont==2:
            if len(i)!=2:
                erro=True
        if cont==3:
            if len(i)!=5:
                erro=True
        if cont==4:
            if len(i)!=4:
                erro=True
        cont+=1
    return erro
def SOBREPOS():
    erro=False
    if REPETICAO_PECAS_J1()==True or REPETICAO_PECAS_J2()==True:
        erro=True
    return erro
def ERRO_QUANTIDADE():
    errro=False
    if JOGADAS_J1() == True or JOGADAS_J2() == True or ERRO_QUA_PEC_J1()==True or ERRO_QUA_PEC_J2()==True:
        errro=True
    return errro
if ERRO_QUANTIDADE()==True :
    if JOGADAS_J1()==True or ERRO_QUA_PEC_J1()==True:
        resultado.write('J1 ERROR_NR_PARTS_VALIDATION')
    else:
        resultado.write('J2 ERROR_NR_PARTS_VALIDATION')
elif SOBREPOS()==True:
    if REPETICAO_PECAS_J1()==True:
        resultado.write('J1 ERROR_OVERWRITE_PIECES_VALIDATION')
    else:
        resultado.write('J2 ERROR_OVERWRITE_PIECES_VALIDATION')
elif ERRO_POS_TOTAL()==True or NAO_ENCONTRADO_J1()==True or NAO_ENCONTRADO_J2()==True:
    if NAO_ENCONTRADO_J1()==True or ERRO_POSICAO()[0]==True:
        resultado.write('J1 ERROR_POSITION_NONEXISTENT_VALIDATION')
    else:
        resultado.write('J2 ERROR_POSITION_NONEXISTENT_VALIDATION')
else:
    GANHAADOR()
resultado.close()