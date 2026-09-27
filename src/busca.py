def busca_linear(lista, codigo_procurado):
    """Retorna a tupla (indice, missao) ou (-1, None) se não encontrar."""
    for i in range(len(lista)):
        if getattr(lista[i], 'codigo') == codigo_procurado:
            return i, lista[i]
    return -1, None

def busca_binaria(lista_ordenada, codigo_procurado):
    """Exige que a lista_ordenada esteja classificada pelo atributo 'codigo'."""
    inicio = 0
    fim = len(lista_ordenada) - 1
    
    while inicio <= fim:
        meio = (inicio + fim) // 2
        
        codigo_atual = getattr(lista_ordenada[meio], 'codigo')
        
        if codigo_atual == codigo_procurado:
            return meio, lista_ordenada[meio]
        elif codigo_atual < codigo_procurado:
            inicio = meio + 1
        else:
            fim = meio - 1
            
    return -1, None