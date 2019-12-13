lista_numero = [ 1, 5, 3, 2, 6, 9, 4, 10, 7,]
pergunta = int(input('Digite 1 para crescente e 2 para decrescente'))

if pergunta ==1:
        print(sorted(lista_numero, reverse=0))

elif pergunta ==2:
        print(sorted(lista_numero, reverse=1))
