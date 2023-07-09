import re

# Funcao do exercicio 1:
def funcao_exer1_inverter_ordem_palavras(frase):
    # metodo split - dividir uma string em uma lista de substrings 
    lista_palavras = frase.split()
    # criar uma cópia invertida da lista
    palavras_invertidas = lista_palavras[::-1]
    # metodo " ".join - juntar os elementos da lista em uma única string, separados por um espaço em branco
    nova_frase = " ".join(palavras_invertidas)
    
    return nova_frase


# Funcao do exercicio 2:
def funcao_exer2_remover_duplicadas(frase):
    frase_final = ""
    for cada_letra in frase:
        # condicional de validacao se uma letra/caracter já está na lista ou nao
        if (cada_letra not in frase_final) or (cada_letra == " "):
            frase_final += cada_letra   

    return frase_final

# Funcao do exercicio 3:
def funcao_exer3_palindromo_longo(palavra):
    combinacoes_original = set()
    combinacoes_invertidas = set()
    # utilizar conjuntos para evitar duplicacao de elementos - cada elemnto é unico
    
    # lacos aninhados - gerar todas as combinações possíveis de substrings de tamanho 3 ou mais
    # a partir da palavra fornecida
    for i in range(3, len(palavra) + 1):
        for j in range(len(palavra) - i + 1):
            sub = palavra[j:j+i]
            if len(sub) >= 3:
                combinacoes_original.add(sub)
    
    palavra_invertida = palavra[::-1]
 
    # fazer o mesmo que o comando anterior só que com a palavra invertida
    for i in range(3, len(palavra_invertida) + 1):
        for j in range(len(palavra_invertida) - i + 1):
            sub = palavra_invertida[j:j+i]
            if len(sub) >= 3:
                combinacoes_invertidas.add(sub)
    

    # trecho de código responsável por encontrar a substring mais longa que está presente tanto nas
    # combinações originais quanto nas combinações invertidas
    substring_mais_longa = ''
    for combinacao in combinacoes_original:
        if combinacao in combinacoes_invertidas and len(combinacao) > len(substring_mais_longa):
            substring_mais_longa = combinacao

    return substring_mais_longa


# Funcao do exercicio 4
def funcao_exer4_colocar_maiuscula(texto):
    frases = re.split(r'(?<=[.?!])\s', texto)
    # re.split(r'(?<=[.?!])\s') - dividir o texto em frases com base em um padrão definido pela expressão
    # regular - r'(?<=[.?!])\s' - Verifica se a posição atual é precedida por um ponto final, ponto
    # de interrogação ou ponto de exclamação
    # \s: É um caractere de espaço em branco. Usei para verificar se a posição atual é seguida por um espaço em branco
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

    # contar a frequência de ocorrência de cada letra em uma palavra
    for letra in palavra:
        if letra in contador:
            contador[letra] += 1
        else:
            contador[letra] = 1
    
    # contar a quantidade de valores ímpares presentes em um dicionário
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
print(f'Frase: {frase_exer1}')
print(f'Respo: {resposta_exer1}')

# Algoritmo do desafio 1 - Exemplo 2
frase_exer1_exemplo2 = "PwC no Brasil há mais de 100 anos no país."
print('\nTeste 2:\n')
resposta_exer1_exemplo2 = funcao_exer1_inverter_ordem_palavras(frase_exer1_exemplo2)
print(f'Frase: {frase_exer1_exemplo2}')
print(f'Respo: {resposta_exer1_exemplo2}')


# Enunciado do desafio 2:
print('\n' + '='*10 + ' DESAFIO 2 ' + '='*10)
print('Remover todos os caracteres duplicados da string.\n')

# Algoritmo do desafio 2 - Exemplo 1
frase_exer2 = "Hello, World!"
print(f'Frase: {frase_exer2}')
resposta_exer2 = funcao_exer2_remover_duplicadas(frase_exer2)
print(f'Respo: {resposta_exer2}')

# Algoritmo do desafio 2 - Exemplo 2
frase_exer2_exemplo2 = "Desafios de codigos"
print('\nTeste 2:\n')
print(f'Frase: {frase_exer2_exemplo2}')
resposta_exer2_exemplo2 = funcao_exer2_remover_duplicadas(frase_exer2_exemplo2)
print(f'Respo: {resposta_exer2_exemplo2}')


# Enunciado do desafio 3
print('\n' + '='*10 + ' DESAFIO 3 ' + '='*10)
print('Encontrar a substring palindroma mais longa na string.\n')

# Algoritmo do desafio 3 - Exemplo 1
palavra = "babad"
print(f'Palavra: {palavra}')
resposta_exer3_exemplo2 = funcao_exer3_palindromo_longo(palavra)
print(f'Respost: {resposta_exer3_exemplo2}')

# Algoritmo do desafio 3 - Exemplo 2
palavra_exer3_exemplo2 = 'bananada'
print('\nTeste 2:\n')
print(f'Palavra: {palavra_exer3_exemplo2}')
resposta_exer3_exemplo2 = funcao_exer3_palindromo_longo(palavra_exer3_exemplo2)
print(f'Respost: {resposta_exer3_exemplo2}')


# Enunciado do desafio 4
print('\n' + '='*10 + ' DESAFIO 4 ' + '='*10)
print('Colocar em maiúscula a primeira letra de cada frase na string.\n')

# Algoritmo do desafio 4 - Exemplo 1
texto = "hello. how are you? i'm fine, thank you."
print(f'Texto: {texto}')
nova_frase = funcao_exer4_colocar_maiuscula(texto)
print(f'Respo: {nova_frase}')

# Algoritmo do desafio 4 - Exemplo 2
texto = "um segundo texto de teste. será que funciona? funciona! excelente."
print('\nTeste 2:\n')
print(f'Texto: {texto}')
nova_frase = funcao_exer4_colocar_maiuscula(texto)
print(f'Respo: {nova_frase}')


# Enunciado do desafio 5:
print('\n' + '='*10 + ' DESAFIO 5 ' + '='*10)
print('Verificar se a string e um anagrama de um palindromo.\n')

# Algoritmo do desafio 5 - Exemplo 1
palavra = 'racecar'
print(f'Palavra: {palavra}')
resposta_exer5 = funcao_exer5_verificar_anagrama_palindromo(palavra)
print(f'Respost: {resposta_exer5}')

# Algoritmo do desafio 5 - Exemplo 2
palavra = 'amor'
print('\nTeste 2:\n')
print(f'Palavra: {palavra}')
resposta_exer5_exemplo2 = funcao_exer5_verificar_anagrama_palindromo(palavra)
print(f'Respost: {resposta_exer5_exemplo2}')
