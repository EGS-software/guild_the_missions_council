import copy
from missao import Missao
from ordenacao import ordenacao_elementar, ordenacao_eficiente
from busca import busca_linear, busca_binaria

def carregar_missoes():
    return [
        Missao(105, "Derrotar o Dragao", 9, 5000, 5),
        Missao(101, "Coletar Ervas", 2, 100, 1),
        Missao(110, "Escolta da Caravana", 5, 800, 3),
        Missao(108, "Decifrar Runas", 7, 2000, 4),
        Missao(102, "Limpar o Porao", 1, 50, 1),
        Missao(115, "Cacar Lobos", 4, 300, 2),
        Missao(112, "Encontrar Artefato", 8, 3500, 4),
        Missao(103, "Entregar Mensagem", 1, 30, 1),
        Missao(120, "Infiltracao na Base", 9, 6000, 5),
        Missao(107, "Proteger Fazenda", 3, 200, 2),
        Missao(102, "Caçar Ursos", 2, 4000, 4)
    ]

def main():
    print("=== O CONSELHO DE MISSOES - BRASILANDIA ===")
    mural = carregar_missoes()
    
    # GUARDA UMA CÓPIA PURA E DESORDENADA PARA O PASSO 5
    mural_desordenado_original = copy.deepcopy(mural)
    
    # 1. Mostrar mural desordenado
    print("\n1. Mural Desordenado Atual:")
    for m in mural: print(m)
        
    # 2. Executar sobre cópias idênticas
    mural_copia_1 = copy.deepcopy(mural)
    mural_copia_2 = copy.deepcopy(mural)
    
    # 3. Apresentar os resultados e contadores (Ordenando por Urgência)
    print("\n2 e 3. Organizando por Urgencia...")
    mural_ord_simples, comp_simples, mov_simples = ordenacao_elementar(mural_copia_1, 'urgencia')
    print(f"[Selection Sort] Comparacoes: {comp_simples} | Movimentacoes: {mov_simples}")
    
    mural_ord_eficiente, comp_eficiente, mov_eficiente = ordenacao_eficiente(mural_copia_2, 'urgencia')
    print(f"[Quick Sort]     Comparacoes: {comp_eficiente} | Movimentacoes: {mov_eficiente}")
    
    # 4. Inserir nova missão e reorganizar
    print("\n4. Nova ameaca! Inserindo e reorganizando pelo Quick Sort...")
    mural.append(Missao(199, "Invasao de NullPointer", 10, 10000, 5))
    mural_atualizado, _, _ = ordenacao_eficiente(mural, 'urgencia')
    for m in mural_atualizado: print(m)
    
    # 5. Busca linear por código (exatamente no VETOR DESORDENADO, como pede a rubrica)
    print("\n5. Busca Linear pelo codigo 110 no vetor desordenado...")
    pos_lin, obj_lin = busca_linear(mural_desordenado_original, 110)
    print(f"Encontrado no indice {pos_lin}: {obj_lin}")
    
    # 6. Ordenar por código e realizar Busca Binária
    print("\n6. Ordenando por CODIGO e executando Busca Binaria pelo codigo 110...")
    mural_por_codigo, _, _ = ordenacao_eficiente(mural_atualizado, 'codigo')
    pos_bin, obj_bin = busca_binaria(mural_por_codigo, 110)
    print(f"Encontrado no indice {pos_bin}: {obj_bin}")
    
    # 7. Procurar código inexistente
    print("\n7. Procurando codigo fantasma (999)...")
    pos_err, _ = busca_binaria(mural_por_codigo, 999)
    if pos_err == -1:
        print("Missao 999 nao consta nos registros do Conselho.")

if __name__ == "__main__":
    main()