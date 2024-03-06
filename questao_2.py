"""
2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência. 
"""

numero = int(input('Digite o número de termos da sequência que deseja visualizar: '))

sequencia = []
atipicos = [1, 2, 3, 5]

n1, n2 = 0, 1
i = 0

while i < numero:
    sequencia.append(n1)
    n = n1 + n2
    n1 = n2
    n2 = n
    i += 1

print(f'A sequência de Fibonacci com {numero} número(s) é {sequencia}.')

if numero in atipicos:
    print(f'O número {numero} pertence à sequência e se encontra à frente.')
elif (numero == 0) or (numero in sequencia):
    print(f'O número {numero} pertence à sequência de Fibonacci') 
else:
    print(f'O número {numero} não pertence à sequência de Fibonacci')