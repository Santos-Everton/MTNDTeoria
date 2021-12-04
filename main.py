import time

estados = input().split() 
alfabetoEntrada=input().split() 
alfabetoFita = input().split()
delimitador = input()  
simboloBranco = input() 
quantTransicoes=int(input())
transicoes=dict()

for i in range(quantTransicoes):
    quintupla = input().split() 
    chave = (quintupla[0], quintupla[1])
    if chave not in transicoes:
        transicoes[chave]=([[quintupla[2], quintupla[3], quintupla[4]]])
    else:
        transicoes[chave].append([quintupla[2], quintupla[3], quintupla[4]])
estadoInicial = input()
estadosFinais = input().split()
palavras = input().split()
aux = 1
for palavra in palavras:
    tempo_inicial = time.time()
    fita=list((delimitador+palavra+simboloBranco))
    pilha=[(estadoInicial, aux, fita)]
    aceita=False
    while len(pilha)>0:
        p=pilha.pop()
        estadoAtual=p[0]
        indice_p=p[1]
        fita_p=p[2][:]
        chave_p=(estadoAtual,fita_p[indice_p])
        if chave_p not in transicoes and estadoAtual in estadosFinais:
            aceita=True
            break
        if chave_p in transicoes:          
            for a in transicoes[(chave_p)]:               
                estadoAtual = a[0] 
                fita_p[indice_p] = a[1]
                direcao = a[2]    
                if direcao == 'E':                   
                    pilha.append((estadoAtual, indice_p-1, fita_p))
                elif direcao == 'D':
                    if (indice_p+1)==len(fita):
                        fita_p.append(simboloBranco)
                    pilha.append((estadoAtual, indice_p+1, fita_p))
                elif direcao == 'I':
                    pilha.append((estadoAtual, indice_p, fita_p))
    tempo_final = time.time()     
    tempo_total=tempo_final-tempo_inicial
    if aceita:
        print("S")
        print(tempo_total)
    else:
        print("N")
        print(tempo_total)