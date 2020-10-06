import requests

def main():
    print('########################')
    print('###Consulta de CEP\'s###')
    print('########################')

    error = 1
    while(error > 0):

        cep = input('Digite o CEP que deseja consultar: ')

        if(len(cep) != 8):
            print('-----------------------------')
            print('O CEP deve conter 8 dígitos !')
            print('-----------------------------')
            error = error + 1
        else:
            error = 0

    request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep))

    retorno = request.json()

    if('erro' not in retorno):
        print('######################')
        print('### CEP ENCONTRADO ###')        
        print('### CEP: {}'.format(retorno['cep']))
        print('### Localidade: {}'.format(retorno['localidade']))
        print('### UF: {}'.format(retorno['uf']))
        print('### DDD: {}'.format(retorno['ddd']))
        #print(retorno)
    else:
        print('----------------------------')
        print('-{}: CEP é inválido !-'.format(cep))
    
    print('----------------------------')
    option = int(input('Deseja consultar outro CEP ?\n1. Sim\n2. Sair\n'))

    if(option != 1):
        print('Saindo...')
    else:
        main()

if __name__ == '__main__':
    main()