def contador_letras(lista_palavras):
    contador = []
    for x in lista_palavras:
        quantidade = len(x)
        contador.append(quantidade)
    return contador

def teste():
    return 'teste'

if __name__ == '__main__':
    lista = ['cachorro', 'gato']
    print(contador_letras(lista))
