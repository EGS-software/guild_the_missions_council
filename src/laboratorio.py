import copy
import random
import time
from missao import Missao
from ordenacao import ordenacao_elementar, ordenacao_eficiente

def gerar_massa_dados(quantidade):
    missoes = []
    for i in range(quantidade):
        codigo = random.randint(1, quantidade * 10)
        dificuldade = random.randint(1, 10)
        ouro = random.randint(10, 10000)
        urgencia = random.randint(1, 5)
        missoes.append(Missao(codigo, f"Missao {i}", dificuldade, ouro, urgencia))
    return missoes

def executar_experimento():
    # Tamanhos exigidos: 100, 1.000 e um conjunto maior
    tamanhos = [100, 1000, 5000] 
    
    print("=== LABORATORIO DE COMPARACAO ===")
    for n in tamanhos:
        print(f"\n--- Testando conjunto com N = {n} ---")
        massa = gerar_massa_dados(n)
        
        copia_1 = copy.deepcopy(massa)
        copia_2 = copy.deepcopy(massa)
        
        # Teste Elementar (Selection Sort)
        inicio = time.time()
        _, comp_elem, mov_elem = ordenacao_elementar(copia_1, 'codigo')
        fim = time.time()
        print(f"[Selection Sort] Comp: {comp_elem:10d} | Mov: {mov_elem:10d} | Tempo: {fim - inicio:.4f}s")
        
        # Teste Eficiente (Quick Sort)
        inicio = time.time()
        _, comp_efic, mov_efic = ordenacao_eficiente(copia_2, 'codigo')
        fim = time.time()
        print(f"[Quick Sort]     Comp: {comp_efic:10d} | Mov: {mov_efic:10d} | Tempo: {fim - inicio:.4f}s")

if __name__ == "__main__":
    executar_experimento()