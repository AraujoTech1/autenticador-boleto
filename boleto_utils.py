def validar_boleto(codigo: str) -> bool:
    return codigo.isdigit() and (len(codigo) == 47 or len(codigo) == 48)

def extrair_info(codigo: str):
    banco = codigo[:3]

    # Banco fictício (poderia usar dicionário de códigos)
    bancos = {
        "001": "Banco do Brasil",
        "033": "Santander",
        "104": "Caixa Econômica",
        "237": "Bradesco",
        "341": "Itaú",
        "748": "Sicredi",
        "341": "Itaú"
    }
    banco_nome = bancos.get(banco, "Banco Desconhecido")

    # Valor está nas últimas 10 posições (simulação)
    valor_raw = codigo[-10:]
    try:
        valor = f"{int(valor_raw) / 100:.2f}"
    except:
        valor = "0.00"

    # Vencimento simulado (fictício com base em posição)
    vencimento = "20/12/2025"  # Só exemplo, sem cálculo real aqui

    return banco_nome, valor, vencimento
