
faturamento_por_estado = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}


def calcular_total_mensal(faturamento_por_estado):
    total_mensal = sum(faturamento_por_estado.values())
    return total_mensal


def calcular_percentual_por_estado(faturamento_por_estado, total_mensal):
    percentuais = {}
    for estado, faturamento in faturamento_por_estado.items():
        percentual = (faturamento / total_mensal) * 100
        percentuais[estado] = percentual
    return percentuais


def main():
    total_mensal = calcular_total_mensal(faturamento_por_estado)
    print(f"Valor total mensal da distribuidora: R${total_mensal:.2f}")

    percentuais_por_estado = calcular_percentual_por_estado(faturamento_por_estado, total_mensal)
    print("\nPercentual de representação por estado:")
    for estado, percentual in percentuais_por_estado.items():
        print(f"{estado}: {percentual:.2f}%")

if __name__ == "__main__":
    main()