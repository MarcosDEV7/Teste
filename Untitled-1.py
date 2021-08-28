import time

#============Testanto time============
print('Teste de Delay')
time.sleep(5)
print('Ok, teste funcionando')
time.sleep(2)
#=====================================

#============Solicitando entrada de dados============
print('Digite um numero')
n1 = int(input())
print('Digite outro numero')
n2 = int(input())
#====================================================


#============Somda dos dados============
print('Deseja Somar os numeros')
res = input()
    #Função Aguarde...
def mensagem(x):
    print(x)
    time.sleep(2)
mensagem('Aguarde...')
    #Verifica opção digitada
if res == ('Sim'):
    mensagem
    print (n1 + n2)
elif res == ('Não'):
    mensagem
    print('Ok, Obrigado por utilizar o programa')
else:
    mensagem
    print('Digite apenas Sim ou Não')
#========================================
