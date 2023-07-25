

def decorator_imprimir(funcao):
    def imprimir(capital, taxa, tempo):
        print(f'CAPITAL:{capital}, TAXA:{taxa}, TEMPO:{tempo}')
        resultado = funcao(capital, taxa, tempo)
        print(f'RESULTADO:{resultado}')
        return resultado
    return imprimir

@decorator_imprimir
def juros_simples(capital, taxa, tempo):

    return capital * (taxa / 100) * tempo

capital = int(input())
taxa = int(input())
tempo = int(input())

juros_simples(capital, taxa, tempo)