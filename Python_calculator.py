import math


# In[6]:


def adição(x, y):
    return x+y

def subtração(x, y):
    return x-y

def multiplicação(x, y):
    return x*y

def divisão(x, y):
    return x/y

def potencia(x, y):
    return x**y

def raiz(x, y):
    return math.sqrt(x)

print("\n***** Python Calculator *****")
print('Escolha uma operação (1/2/3/4/5/6):\n')
print('1 - Soma')
print('2 - Subtração')
print('3 - Multiplicação')
print('4 - Divisão')
print('5 - Potência')
print('6 - Raiz quadrada')



operacao = input('Digite sua opção: 1/2/3/4/5/6\n')
num1 = float(input('Insira um número: '))
num2 = float(input('Insira um segundo número: '))

if operacao == '1':
    print(num1, '+', num2, '=', adição(num1, num2))

elif operacao == '2':
    print(num1, '-', num2, '=', subtração(num1, num2))

elif operacao == '3':
    print(num1, 'x', num2, '=', multiplicação(num1, num2))

elif operacao == '4':
    print(num1, '/', num2, '=', divisão(num1, num2))

elif operacao == '5':
    print(potencia(num1, num2))
    
else:
    print(raiz(num1, num2))

