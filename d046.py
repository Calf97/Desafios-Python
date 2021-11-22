# contagem regressiva, indo de 10 até 0 com pausa de 1 seg entre eles.
from time import sleep
for c in range(10, 0, -1):
    print(c)
    if c == 10:
        sleep(1)
    elif c == 9:
        sleep(1)
    elif c == 8:
        sleep(1)
    elif c == 7:
        sleep(1)
    elif c == 6:
        sleep(1)
    elif c == 5:
        sleep(1)
    elif c == 4:
        sleep(1)
    elif c == 3:
        sleep(1)
    elif c == 2:
        sleep(1)
    elif c == 1:
        sleep(1)
print('FOGOS!!!')