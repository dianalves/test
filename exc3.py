import json


def ler_faturamento_json(arquivo):
    with open(arquivo) as file:
        dados = json.load(file)
    return dados


def calcular_min_max_faturamento(faturamento_diario):
    menor = min(faturamento_diario)
    maior = max(faturamento_diario)
    return menor, maior


def calcular_media_mensal(faturamento_diario):
    dias_com_faturamento = [dia for dia in faturamento_diario if dia > 0]
    media = sum(dias_com_faturamento) / len(dias_com_faturamento)
    return media


def contar_dias_acima_da_media(faturamento_diario, media_mensal):
    dias_acima_da_media = sum(1 for dia in faturamento_diario if dia > media_mensal)
    return dias_acima_da_media


def main():
    arquivo_json = "faturamento.json"
    dados_faturamento = ler_faturamento_json(arquivo_json)
    faturamento_diario = dados_faturamento["faturamento_diario"]

    menor, maior = calcular_min_max_faturamento(faturamento_diario)
    print(f"Menor valor de faturamento: R${menor}")
    print(f"Maior valor de faturamento: R${maior}")

    media_mensal = calcular_media_mensal(faturamento_diario)
    print(f"Média mensal de faturamento: R${media_mensal}")

    dias_acima_da_media = contar_dias_acima_da_media(faturamento_diario, media_mensal)
    print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")

if __name__ == "__main__":
    main()