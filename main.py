# print('\033[1;34;45mVamos começar!\033[0m')

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

# count = 0
# sum = 0
# while True:
#     number = int(input('Digite um número: '))
#     if number == 999:
#         break
#     count += 1
#     sum += number
# print(f'A soma dos {count} valores é {sum}')

# lanche = ('Hamburguer', 'Batata_frita', 'Pizza', 'Pudim')

# for comida in lanche:
#     print(f'Eu vou comer {comida}')

# for count in range(0, len(lanche)):
#     print(f'eu vou comer {lanche[count]} na posição {count}')    

# for pos, comida in enumerate(lanche):
#     print(f'Eu vou comer {comida} na posição {pos}')

# print('Comi demais!')    

galera = list()
dados = list()
totmai = totmen = 0
for c in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))
    galera.append(dados[:])
    dados.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')

