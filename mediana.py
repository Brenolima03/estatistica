def calcular_mediana(lista_de_numeros):
    numeros_ordenados = sorted(lista_de_numeros)
    tamanho_da_lista = len(numeros_ordenados)
    centro = lista_de_numeros[tamanho_da_lista // 2]

    # Verifica se o número de elementos na lista é par ou ímpar.
    # Se for par:
    if tamanho_da_lista % 2 == 0:

        # Encontra os dois elementos do centro da lista.
        esquerda_do_centro = lista_de_numeros[tamanho_da_lista // 2 - 1]

        # Calcula a média entre esses dois elementos do meio.
        mediana = (esquerda_do_centro  + centro) / 2
        print(f"Mediana: {mediana}")

    # Se for ímpar:
    else:
        # O elemento do meio é a mediana.
        print(f"Mediana: {centro}")

def calcular_mediana_com_frequencia(lista_de_numeros, frequencias):

    # Calcula a soma de todas as frequências.
    frequencia_acumulada_total = sum(frequencias)

    # Se a frequência acumulada total for um número par:
    if frequencia_acumulada_total % 2 == 0:
        frequencia_acumulada_atual = 0

        # Encontra as posições centrais da distribuição das frequências.
        posicoes_mediana = (
            frequencia_acumulada_total // 2,
            frequencia_acumulada_total // 2 + 1
        )

        # Itera sobre a distribuição das frequências.
        for i, frequencia in enumerate(frequencias):

            # Calcula a frequência acumulada em cada iteração.
            frequencia_acumulada_atual += frequencia

            # Se a posição esquerda do centro for maior que a frequência
            # acumulada anterior e a posição direita for menor ou igual a
            # frequência acumulada atual, a mediana será o número da lista
            # no índice da iteração.
            if (
                posicoes_mediana[0] > frequencia_acumulada_atual - frequencia
                and posicoes_mediana[1] <= frequencia_acumulada_atual
            ):
                mediana = lista_de_numeros[i]
                print(
                    f"A mediana, {round(mediana, 2)}, está na {i + 1}ª classe."
                )

            # Se a posição esquerda do centro for igual a frequência acumulada
            # anterior, deve-se calcular a média entre os números da lista nos
            # índices da iteração anterior e da atual.
            if posicoes_mediana[0] == frequencia_acumulada_atual - frequencia:
                mediana = (lista_de_numeros[i - 1] + lista_de_numeros[i]) / 2
                print(
                    f"A mediana, {round(mediana, 2)}, está na {i + 1}ª classe."
                )

    # Se a frequência acumulada total for um número ímpar, a mediana será o
    # número do centro da lista.
    else:
        posicao_mediana = (frequencia_acumulada_total + 1) // 2
        frequencia_acumulada_atual = 0

        # Itera sobre a distribuição das frequências.
        for i, frequencia in enumerate(frequencias):
            frequencia_acumulada_atual += frequencia

            # Se a posição da mediana for menor ou igual a frequência acumulada
            # atual, significa que encontramos a classe onde a mediana está.
            if posicao_mediana <= frequencia_acumulada_atual:

                # A mediana será o número da lista no índice da iteração.
                mediana = lista_de_numeros[i]
                print(
                    f"A mediana, {round(mediana, 2)}, está na {i + 1}ª classe."
                )
                break

def calcular_mediana_com_intervalos(lista_de_intervalos, frequencias):
    frequencia_acumulada_atual = 0
    frequencia_acumulada_total = sum(frequencias)

    # Itera sobre os intervalos.
    for i, intervalo in enumerate(lista_de_intervalos):

        frequencia_atual = frequencias[i]

        # Atualiza a frequência acumulada atual
        frequencia_acumulada_atual += frequencia_atual

        # Calcula a frequência acumulada anterior
        frequencia_acumulada_anterior =\
            frequencia_acumulada_atual - frequencia_atual

        # Se a frequência acumulada total for um número par:
        if frequencia_acumulada_total % 2 == 0:
            # Encontra as posições centrais da distribuição das frequências.
            posicoes_mediana = (
                frequencia_acumulada_total // 2,
                frequencia_acumulada_total // 2 + 1
            )

            # Verifica se o intervalo atual contém a mediana
            if posicoes_mediana[1] <= frequencia_acumulada_atual:

                # Fórmula da mediana:
                mediana = (
                    intervalo.start
                    + (
                        frequencia_acumulada_total / 2
                        - frequencia_acumulada_anterior
                    ) * len(intervalo) / frequencia_atual
                )
                print(
                    f"A mediana, {round(mediana, 2)}, está na {i + 1}ª classe."
                )
                break
        else:
            posicao_mediana = (frequencia_acumulada_total + 1) // 2

            if posicao_mediana <= frequencia_acumulada_atual:

                # Fórmula da mediana:
                mediana = (
                    intervalo.start
                    + (
                        frequencia_acumulada_total / 2
                        - frequencia_acumulada_anterior
                    )
                    * len(intervalo) / frequencia_atual
                )
                print(
                    f"A mediana, {round(mediana, 2)}, está na {i + 1}ª classe."
                )
                break

# calcular_mediana([3, 5, 2, 6, 5, 8])
# calcular_mediana([20, 7, 8, 12])

# calcular_mediana_com_frequencia(
#     [500, 1000, 1500, 2000],
#     [10, 4, 2, 14]
# )
# calcular_mediana_com_frequencia(
#     [500, 1000, 1500, 1500],
#     [10, 5, 6, 9]
# )

# calcular_mediana_com_intervalos(
#     [
#         range(0, 2), range(2, 4), range(4, 6),range(6, 8),range(8, 10)
#     ],
#     [5, 2, 4, 2, 8]
# )
# calcular_mediana_com_intervalos(
#     [
#         range(150, 160), range(160, 170), range(170, 180),
#         range(180, 190),range(190, 200)
#     ],
#     [2, 8, 8, 10, 3]
# )

calcular_mediana_com_intervalos(
    [
        range(159, 166), range(166, 172), range(172, 178),
        range(178, 184), range(184, 190),
    ],
    [1, 2, 10, 4, 1]
)
calcular_mediana_com_intervalos(
    [
        range(23, 27), range(29, 32), range(33, 37),
        range(38, 42), range(43, 47), range(48, 52),
        range(53, 55),
    ],
    [13, 10, 19, 15, 17, 11, 11]
)
