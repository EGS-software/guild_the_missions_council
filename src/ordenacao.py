def ordenacao_elementar(lista, atributo):
    """
    Implementação completa do SELECTION SORT.
    Complexidade: O(n²) em todos os casos.
    """
    comparacoes = 0
    movimentacoes = 0
    n = len(lista)
    
    for i in range(n):
        indice_menor = i
        for j in range(i + 1, n):
            comparacoes += 1
            if getattr(lista[j], atributo) < getattr(lista[indice_menor], atributo):
                indice_menor = j
                
        if indice_menor != i:
            movimentacoes += 1
            lista[i], lista[indice_menor] = lista[indice_menor], lista[i]
            
    return lista, comparacoes, movimentacoes

def ordenacao_eficiente(lista, atributo):
    """
    Implementação completa do QUICK SORT.
    Complexidade: O(n log n) no caso médio, O(n²) no pior caso.
    """
    # Usamos uma lista para manter a referência dos contadores nas chamadas recursivas
    contadores = [0, 0] # [comparacoes, movimentacoes]

    def particao(arr, baixo, alto):
        pivo = getattr(arr[alto], atributo)
        i = baixo - 1
        
        for j in range(baixo, alto):
            contadores[0] += 1
            if getattr(arr[j], atributo) <= pivo:
                i += 1
                contadores[1] += 1
                arr[i], arr[j] = arr[j], arr[i]
                
        contadores[1] += 1
        arr[i + 1], arr[alto] = arr[alto], arr[i + 1]
        return i + 1

    def quick_sort_recursivo(arr, baixo, alto):
        if baixo < alto:
            pi = particao(arr, baixo, alto)
            quick_sort_recursivo(arr, baixo, pi - 1)
            quick_sort_recursivo(arr, pi + 1, alto)

    quick_sort_recursivo(lista, 0, len(lista) - 1)
    
    return lista, contadores[0], contadores[1]