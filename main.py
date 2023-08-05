print('\033[1;34;45mVamos começar!\033[0m')

# nome=input('Qual é o seu nome?')
# sobrenome=input('Qual é o seu sobrenome?')
# message='Seja bem vindo, '
# print(message, nome, sobrenome + '!')

# n1 =int(input('Digite um número: '))
# n2 =int(input('Digite outro número: '))
# soma = n1 + n2
# print('A soma de {} e {} resulta em {}'.format(n1, n2, soma))

# nome = str(input('Qual é o seu nome? '))
# if nome == 'Gustavo':
#     print('Que nome bonito!')
# elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
#     print('Seu nome é muito popular no Brasil.')
# elif nome in 'Ana Cláudia Jéssica Juliana':
#     print('Belo nome feminino!')    
# print('Tenha um bom dia, {}!'.format(nome))

# number = int(input('Digite um número: '))
# for c in range(0, number+1):
#     print (c)
# print('Fim.')    

# sum = 0
# for c in range(0, 4):
#     n = int(input('Digite um valor: '))
#     sum += n
# print('O somatório de todos os valores foi {}'.format(sum))    

# c = 1
# while c < 10:
#     print(c)
#     c += 1
# print('Fim')    

count = 0
sum = 0
while True:
    number = int(input('Digite um número: '))
    if number == 999:
        break
    count += 1
    sum += number

print(f'A soma dos {count} valores é {sum}')