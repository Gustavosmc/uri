from math import sqrt
while True:
    try:
        ent = input()
        ent = ent.split(' ')
        r1, x1, y1, r2, x2, y2 = [int(v) for v in ent]
        cateto1 = x1 - x2
        cateto2 = y1 - y2
        distancia = sqrt(cateto1**2 + cateto2**2)
        if r1 < r2:
            print('MORTO')
        elif distancia + r2 <= r1:
            print('RICO')
        else:
            print('MORTO')
    except:
        break
