"""Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro."""

numero = input("Digite um número inteiro: ")

if numero.isdigit():
    numero = int(numero)
    if numero % 2 == 0:
        print(f'{numero} é par')
    else:
        print(f'{numero} é ímpar!')
else:
    print(f'Isso não é um número inteiro!')


numero = input("Digite um número inteiro: ")

if not numero.isdigit():
    print(f'Isso não é um número inteiro')
else:
    numero = int(numero)
    
    if not numero % 2 == 0:
       print(f"{numero} é ímpar!")
    else:
       print(f'{numero} é par!')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
horario = input('Digite o horário atual (entre 0-23hrs) : ')

if horario.isdigit():
    horario=int(horario)

    if horario < 0 or horario >23:
        print('Horário deve estar entre 0 e 23 horas')
    else:
        if horario <= 11:
            print('Bom dia!')
        elif horario <= 17:
            print('Boa tarde!')
        else:
            print('Boa Noite!')

else:
    print('Por favor digite um horário entre 0 e 23 horas')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome_1 = input('Qual o seu nome? ')
tamanho = len(nome_1)

if tamanho <= 4:
    print('Seu nome é pequeno!')
elif tamanho <=6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande!')