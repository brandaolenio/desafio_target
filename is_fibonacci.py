'''Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.'''

def is_fibonacci (num):
    lista_fibonacci = [0, 1, 1]
    soma = 0
    while soma < num:
        soma = lista_fibonacci[-1] + lista_fibonacci[-2]
        lista_fibonacci.append(soma)
    
    if num in lista_fibonacci:
        return 'O número informado pertence a Sequência de Fibonacci'
    else:
        return 'O número informado NÃO pertecente a Sequência de Fibonacci'

print(is_fibonacci(89))