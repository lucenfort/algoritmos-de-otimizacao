import time
import random
import math


def gerar_solucao_aleatoria(dominio):
    """
    Gera uma solução aleatória dentro do domínio fornecido.

    Args:
        dominio (list): Uma lista de tuplas, onde cada tupla representa o intervalo de valores possíveis para uma posição da solução.

    Returns:
        list: Uma lista de números inteiros aleatórios, onde cada número está dentro do intervalo especificado pela posição correspondente no domínio.
    """
    return [random.randint(dominio[i][0], dominio[i][1]) for i in range(len(dominio))]


# Algoritmo 1: Pesquisa Randômica
def pesquisa_randomica(dominio, funcao_custo):
    """
    Implementa um algoritmo de pesquisa randômica para encontrar a solução ótima para um problema.

    Args:
        dominio (list): Uma lista de tuplas, onde cada tupla representa o intervalo de valores possíveis para uma posição da solução.
        funcao_custo (function): Função para calcular o custo de uma solução.

    Returns:
        list: A melhor solução encontrada pelo algoritmo.
    """
    # Inicializa o melhor custo como infinito
    melhor_custo = float("inf")
    # Inicializa a melhor solução como None
    melhor_solucao = None

    # Itera 100000 vezes
    for _ in range(100000):
        # Gera uma solução aleatória
        solucao = gerar_solucao_aleatoria(dominio)
        # Calcula o custo da solução
        custo = funcao_custo(solucao)

        # Se o custo da solução for menor que o melhor custo encontrado até agora
        if custo < melhor_custo:
            # Atualiza o melhor custo
            melhor_custo = custo
            # Atualiza a melhor solução
            melhor_solucao = solucao

    # Retorna a melhor solução encontrada
    return melhor_solucao


# Algoritmo 2: Subida de Encosta
def subida_encosta(dominio, funcao_custo):
    """
    Implementa o algoritmo de subida de encosta para encontrar uma solução ótima para um problema.

    Args:
        dominio (list): Uma lista de tuplas, onde cada tupla representa o intervalo de valores possíveis para uma posição da solução.
        funcao_custo (function): Função para calcular o custo de uma solução.

    Returns:
        list: A melhor solução encontrada pelo algoritmo.
    """
    # Gera uma solução aleatória para iniciar
    solucao = gerar_solucao_aleatoria(dominio)

    # Loop principal do algoritmo
    while True:
        # Lista para armazenar os vizinhos da solução atual
        vizinhos = []

        # Gera os vizinhos da solução atual
        for i in range(len(dominio)):
            if solucao[i] > dominio[i][0]:
                # Adiciona um vizinho com o valor decrementado em 1 na posição i
                vizinhos.append(solucao[:i] + [solucao[i] - 1] + solucao[i + 1 :])
            if solucao[i] < dominio[i][1]:
                # Adiciona um vizinho com o valor incrementado em 1 na posição i
                vizinhos.append(solucao[:i] + [solucao[i] + 1] + solucao[i + 1 :])

        # Calcula o custo da solução atual
        atual = funcao_custo(solucao)

        # Encontra o vizinho com o menor custo
        melhor = min((funcao_custo(v), v) for v in vizinhos)

        # Se o custo do melhor vizinho for maior ou igual ao custo atual, interrompe o loop
        if melhor[0] >= atual:
            break

        # Atualiza a solução para o melhor vizinho encontrado
        solucao = melhor[1]

    # Retorna a melhor solução encontrada
    return solucao


# Algoritmo 3: Tempera Simulada
def Tempera_Simulada(
    dominio, funcao_custo, temperatura=99999999.99, resfriamento=0.95, passo=1
):
    """
    Implementa o algoritmo de tempera simulada para encontrar uma solução ótima para um problema.

    Args:
        dominio (list): Uma lista de tuplas, onde cada tupla representa o intervalo de valores possíveis para uma posição da solução.
        funcao_custo (function): Função para calcular o custo de uma solução.
        temperatura (float): A temperatura inicial do algoritmo (opcional, padrão é 99999999.99).
        resfriamento (float): O fator de resfriamento no intervalo [0, 1] (opcional, padrão é 0.95).
        passo (float): O tamanho do passo para gerar vizinhos (opcional, padrão é 1).

    Returns:
        list: A melhor solução encontrada pelo algoritmo.
    """
    # Gera uma solução aleatória para iniciar
    solucao = gerar_solucao_aleatoria(dominio)

    # Loop principal do algoritmo
    while temperatura > 0.1:
        # Escolhe uma posição aleatória na solução
        i = random.randint(0, len(dominio) - 1)
        # Define uma direção aleatória para o passo
        direcao = random.randint(-passo, passo)
        # Gera uma solução temporária modificando a posição escolhida
        solucao_temp = solucao[:]
        solucao_temp[i] += direcao
        # Garante que a solução temporária esteja dentro dos limites definidos pelo domínio
        solucao_temp[i] = max(min(solucao_temp[i], dominio[i][1]), dominio[i][0])
        # Calcula o custo da solução atual e da solução temporária
        custo_solucao = funcao_custo(solucao)
        custo_solucao_temp = funcao_custo(solucao_temp)
        # Calcula a probabilidade de aceitar uma solução pior
        probabilidade = pow(math.e, (-custo_solucao_temp - custo_solucao) / temperatura)
        # Verifica se a solução temporária é melhor ou se deve ser aceita com uma probabilidade
        if custo_solucao_temp < custo_solucao or random.random() < probabilidade:
            solucao = solucao_temp
        # Reduz a temperatura multiplicando pelo fator de resfriamento
        temperatura *= resfriamento

    # Retorna a melhor solução encontrada
    return solucao


# Algoritmo 4: Algoritmo Genético
def mutacao(dominio, passo, solucao):
    """
    Performs mutation on a given solution.

    Args:
        dominio (list): The domain of the solution.
        passo (float): The step size for mutation.
        solucao (list): The original solution.

    Returns:
        list: The mutated solution.
    """
    i = random.randint(0, len(dominio) - 1)
    mutante = solucao.copy()  # Create a copy of the original solution

    if random.random() < 0.5:
        if solucao[i] != dominio[i][0]:
            mutante[i] -= passo  # Update the value at index i by subtracting the passo
        elif solucao[i] != dominio[i][1]:
            mutante[i] += passo  # Update the value at index i by adding the passo

    return mutante


def crossover(dominio, individuo1, individuo2):
    """
    Performs crossover between two individuals.

    Args:
        dominio (list): The domain of the individuals.
        individuo1 (list): The first individual.
        individuo2 (list): The second individual.

    Returns:
        list: The new individual after crossover.
    """
    i = random.randint(0, len(dominio) - 2)
    return (
        individuo1[:i] + individuo2[i:]
    )  # Combine the first part of individuo1 with the second part of individuo2


def genetico(
    dominio,
    funcao_custo,
    tamanho_populacao=500,
    passo=1,
    probabilidade_mutacao=0.2,
    elitismo=0.15,
    numero_geracoes=1000,
):
    """
    Implementa um algoritmo genético para encontrar a solução ótima para um problema.

    Args:
        dominio (list): Lista de possíveis valores para cada posição da solução.
        funcao_custo (function): Função para calcular o custo de uma solução.
        tamanho_populacao (int, optional): Número de indivíduos na população. Defaults to 500.
        passo (int, optional): Passo usado na mutação. Defaults to 1.
        probabilidade_mutacao (float, optional): Probabilidade de ocorrer uma mutação. Defaults to 0.2.
        elitismo (float, optional): Proporção de indivíduos que são mantidos de uma geração para a próxima. Defaults to 0.15.
        numero_geracoes (int, optional): Número de gerações que o algoritmo deve executar. Defaults to 1000.

    Returns:
        list: A melhor solução encontrada pelo algoritmo.
    """
    # Gera a população inicial
    populacao = [gerar_solucao_aleatoria(dominio) for _ in range(tamanho_populacao)]
    # Define quantos indivíduos serão mantidos de uma geração para a próxima
    numero_elitismo = int(elitismo * tamanho_populacao)

    # Itera sobre o número de gerações
    for _ in range(numero_geracoes):
        # Calcula o custo para cada indivíduo da população
        # Ordena a população pelo custo (em ordem crescente)
        custos = sorted((funcao_custo(individuo), individuo) for individuo in populacao)
        # Mantém os melhores indivíduos para a próxima geração (elitismo)
        populacao = [individuo for (custo, individuo) in custos[:numero_elitismo]]

        # Enquanto a população não for repopulada
        while len(populacao) < tamanho_populacao:
            # Se a mutação ocorrer
            if random.random() < probabilidade_mutacao:
                # Seleciona um indivíduo aleatório da elite
                m = random.randint(0, numero_elitismo - 1)
                # Adiciona o resultado da mutação à população
                populacao.append(mutacao(dominio, passo, populacao[m]))
            else:
                # Se não ocorrer mutação, faz um crossover
                # Seleciona dois indivíduos aleatórios da elite
                c1 = random.randint(0, numero_elitismo - 1)
                c2 = random.randint(0, numero_elitismo - 1)
                # Adiciona o resultado do crossover à população
                populacao.append(crossover(dominio, populacao[c1], populacao[c2]))

    # Retorna a melhor solução encontrada em todas as gerações
    return min((funcao_custo(individuo), individuo) for individuo in populacao)[1]
