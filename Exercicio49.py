import time
n1 = int(input('Insira um numero: '))

for t in range (1, 11, ):
   print('{} X {} = {}'.format(n1, t, n1*t))
   time.sleep(0.7)

