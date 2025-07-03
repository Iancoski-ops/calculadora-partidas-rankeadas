def calcular_saldo_vitorias(vitorias, derrotas):
    return vitorias - derrotas

def obter_ranking(saldo):
    if saldo <= 10:
        return "Ferro"
    elif saldo <= 20:
        return "Bronze"
    elif saldo <= 50:
        return "Prata"
    elif saldo <= 80:
        return "Ouro"
    elif saldo <= 90:
        return "Diamante"
    elif saldo <= 100:
        return "Lendário"
    else:
        return "Imortal"


saldoVitorias = calcular_saldo_vitorias(64, 2)
nivel = obter_ranking(saldoVitorias)

print(f'O saldo do Herói é {saldoVitorias} e ele está no nível {nivel}!')