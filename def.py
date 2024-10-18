def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) -1
    while baixo <= alto:
        #Problema nessa linha. O código do livro foi feita na versão 2.7. 
        #Python trata as divisões de forma diferente "/" é automaticamente número 
        #int ou float, se os números são int ou float. Depois da 3.0 é preciso especícifar.
        meio = (baixo + alto ) // 2 
        chute = lista[meio]
        if chute == item:
            return meio        
        if chute > item: 
            alto = meio - 1 
        else: 
            baixo = meio + 1
    return None    

minha_lista = [1,3,5,7,9]

print (pesquisa_binaria(minha_lista,3))
print (pesquisa_binaria(minha_lista, -1))

