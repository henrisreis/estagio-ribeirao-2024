"""
1) Observe o trecho de código abaixo: 

int INDICE = 13, SOMA = 0, K = 0; 

enquanto K < INDICE faça 

{ 

    K = K + 1; 

    SOMA = SOMA + K; 

} 

imprimir(SOMA); 

Ao final do processamento, qual será o valor da variável SOMA? 
"""

INDICE, SOMA, K = 13, 0, 0

while K < INDICE:
    K += 1
    SOMA += K

print(f'A variável SOMA terá valor {SOMA}.')

