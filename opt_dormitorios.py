from opt2 import *

dormitorios = ["Mercurio", "Venus", "Terra", "Marte", "Jupiter"]

preferencias = [
    ("Thais", ("Mercurio", "Marte")),
    ("Bruno", ("Mercurio", "Venus")),
    ("Amanda", ("Mercurio", "Marte")),
    ("Carlos", ("Venus", "Marte")),
    ("Francisco", ("Venus", "Jupiter")),
    ("Wellington", ("Venus", "Terra")),
    ("Gabriela", ("Terra", "Marte")),
    ("Thayane", ("Terra", "Jupiter")),
    ("Romênia", ("Terra", "Jupiter")),
    ("Larissa", ("Terra", "Jupiter")),
]

dominio = [(0, (len(dormitorios) * 2) - i - 1) for i in range(0, len(dormitorios) * 2)]


def imprimir_solucao(solucao):
    vagas = []
    for i in range(len(dormitorios)):
        vagas += [i, i]
    for i in range(len(solucao)):
        atual = solucao[i]
        dormitorio = dormitorios[vagas[atual]]
        print(preferencias[i][0], dormitorio)
        del vagas[atual]


# imprimir_solucao([6, 1, 2, 1, 2, 0, 2, 2, 0, 0])


def Funcao_Custo(solucao):
    custo = 0
    vagas = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4]
    for i in range(len(solucao)):
        atual = solucao[i]
        dormitorio = dormitorios[vagas[atual]]
        preferencia = preferencias[i][1]
        if preferencia[0] == dormitorio:
            custo = custo + 0
        elif preferencia[1] == dormitorio:
            custo = custo + 1
        else:
            custo = custo + 3
        del vagas[atual]
    return custo


Funcao_Custo([6, 1, 2, 1, 2, 0, 2, 2, 0, 0])

print("\nPesquisa Randomica: ")
solucao_randomica = pesquisa_randomica(dominio, Funcao_Custo)
custo_randomica = Funcao_Custo(solucao_randomica)
imprimir_solucao(solucao_randomica)

print("\nSubida de Encosta: ")
solucao_subida_encosta = subida_encosta(dominio, Funcao_Custo)
custo_subida_encosta = Funcao_Custo(solucao_subida_encosta)
imprimir_solucao(solucao_subida_encosta)

print("\nTempera Simulada: ")
solucao_tempera = Tempera_Simulada(dominio, Funcao_Custo)
custo_tempera = Funcao_Custo(solucao_tempera)
imprimir_solucao(solucao_tempera)

print("\nAlgoritmo Genético: ")
solucao_genetico = genetico(dominio, Funcao_Custo)
custo_genetico = Funcao_Custo(solucao_genetico)
imprimir_solucao(solucao_genetico)
