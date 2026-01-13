# Um programa com uma função fatorial() que receba dois parâmetros.
# O primeiro que indique o número a calcular e 
# O segundo chamado show(), que será um valor lógico
# indicando se será mostrado ou não na tela o processo de cálculo.

def fatorial(n, show=False):
    '''
    -> Calcula o fatorial de um número.
    :param n: O número a ser fatorado.
    :param show: Se será exibido na tela o cálculo.
    :return: Retorna o resultado do cálculo.
    '''
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(f' x ', end='')
            else:
                print(f' = ', end='')
        f *= c
    return f

# Programa principal
print(fatorial(5, show=True))


    
    
    
    
    
    