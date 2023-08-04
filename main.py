print('\033[1;34;45mHello World!\033[0m')

# nome=input('Qual é o seu nome?')
# sobrenome=input('Qual é o seu sobrenome?')
# message='Seja bem vindo, '
# print(message, nome, sobrenome + '!')

# n1 =int(input('Digite um número: '))
# n2 =int(input('Digite outro número: '))
# soma = n1 + n2
# print('A soma de {} e {} resulta em {}'.format(n1, n2, soma))

nome = str(input('Qual é o seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é muito popular no Brasil.')
elif nome in 'Ana Cláudia Jéssica Juliana':
    print('Belo nome feminino!')    
print('Tenha um bom dia, {}!'.format(nome))

