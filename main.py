# crie um programa onde o usário vai digital um numero de seguencias Fibonacci a ser calculada

def fifi(n):
    if n <= 1: 
      return n
    else:
      return fifi(n - 1) + fifi(n - 2)

n = int(input('informe até qual sequenvia de Fibonacci: '))

for x in range(n):
    print (fifi(x))