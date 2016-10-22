from math import sqrt

while True:
    try:
        n = int(input())
        if n == 0:
            break
        ent = input()
        ent = ent.split(' ')
        x, y = [int(v) for v in ent]
        x0,y0 = x, y
        coord = []
        distancia = 0
        for i in range(n):
            ent = input()
            ent = ent.split(' ')
            coord.append((int(ent[0]), int(ent[1])))
        coord = sorted(coord)
        for c in coord:
            x1, y1 = c
            dist1 = x1 - x
            dist2 = y1 - y
            distancia += sqrt(dist1**2 + dist2**2)
            x, y = x1, y1
        distancia += sqrt((x - x0)**2 + (y - y0)**2)
        print(round(distancia, 2))
            
    except e:
        break
