import re

# Funcao do exercicio 1:
def funcao_exer1_inverter_ordem_palavras(frase):
    lista_palavras = frase.split()
    palavras_invertidas = lista_palavras[::-1]
    nova_frase = " ".join(palavras_invertidas)
    
    return nova_frase

# Funcao do exercicio 2:
def funcao_exer2_remover_duplicadas(frase):
    frase_final = ""
    for cada_letra in frase:
        if (cada_letra not in frase_final) or (cada_letra == " "):
            frase_final += cada_letra   

    return frase_final

# Funcao do exercicio 4
def funcao_exer4_colocar_maiuscula(texto):
    frases = re.split(r'(?<=[.?!])\s', texto)
    lista_frases = ""

    for frase in frases:
        if frase[-1] not in '.?!':
            lista_frases += frase[0].title() + frase[1:] + frase[-1] + " "
        else:
            lista_frases += frase[0].title() + frase[1:] + " "

    return lista_frases.rstrip()


# Funcao do exercicio 5:
def funcao_exer5_verificar_anagrama_palindromo(palavra):
    contador = {}
    for letra in palavra:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    
    valores_impares = 0
    for valor in contador.values():
        if valor % 2 != 0:
            valores_impares += 1

    if valores_impares <= 1:
        resposta = "true"
    else:
        resposta = "false"

    return resposta


# Enunciado do desafio 1:
print('='*10 + ' DESAFIO 1 ' + '='*10)
print('Reverter a ordem das palavras em um frase, mantendo a ordem das palavras.\n')

# Algoritmo do desafio 1 - Exemplo 1
frase_exer1 = 'Hello, World! OpenAI is amazing.'
resposta_exer1 = funcao_exer1_inverter_ordem_palavras(frase_exer1)
print(frase_exer1)
print(resposta_exer1)

# Algoritmo do desafio 1 - Exemplo 2
frase_exer1_exemplo2 = "PwC no Brasil ha mais de 100 anos no país."
print('\nTeste 2:\n')
resposta_exer1_exemplo2 = funcao_exer1_inverter_ordem_palavras(frase_exer1_exemplo2)
print(frase_exer1_exemplo2)
print(resposta_exer1_exemplo2)


# Enunciado do desafio 2:
print('\n' + '='*10 + ' DESAFIO 2 ' + '='*10)
print('Remover todos os caracteres duplicados da string.\n')

# Algoritmo do desafio 2 - Exemplo 1
frase_exer2 = "Hello, World!"
print(frase_exer2)
resposta_exer2 = funcao_exer2_remover_duplicadas(frase_exer2)
print(resposta_exer2)

# Algoritmo do desafio 2 - Exemplo 2
frase_exer2_exemplo2 = "Desafios de codigos"
print('\nTeste 2:\n')
print(frase_exer2_exemplo2)
resposta_exer2_exemplo2 = funcao_exer2_remover_duplicadas(frase_exer2_exemplo2)
print(resposta_exer2_exemplo2)

# Enunciado do desafio 4
print('\n' + '='*10 + ' DESAFIO 4 ' + '='*10)
print('Colocar em maiúscula a primeira letra de cada frase na string.\n')

# Algoritmo do desafio 4 - Exemplo 1
texto = "hello. how are you? i'm fine, thank you."
print(texto)
nova_frase = funcao_exer4_colocar_maiuscula(texto)
print(nova_frase)

# Algoritmo do desafio 4 - Exemplo 2
texto = "um segundo texto de teste. será que funciona? funciona! excelente."
print('\nTeste 2:\n')
print(texto)
nova_frase = funcao_exer4_colocar_maiuscula(texto)
print(nova_frase)


# Enunciado do desafio 5:
print('\n' + '='*10 + ' DESAFIO 5 ' + '='*10)
print('Verificar se a string e um anagrama de um palindromo.\n')

# Algoritmo do desafio 5 - Exemplo 1
palavra = 'racecar'
print(palavra)
resposta_exer5 = funcao_exer5_verificar_anagrama_palindromo(palavra)
print(resposta_exer5)

# Algoritmo do desafio 5 - Exemplo 2
palavra = 'amor'
print('\nTeste 2:\n')
print(palavra)
resposta_exer5_exemplo2 = funcao_exer5_verificar_anagrama_palindromo(palavra)
print(resposta_exer5_exemplo2)
