while True:
    try:
        ent = input()
        ent = ent.split(' ')
        v = float(ent[0])
        m = ent[1]
        n = ent[2]
        if len(m) < 4:
            m = "0" * (4 - len(m)) + m
        if len(n) < 4:
            n = "0" * (4 - len(n)) + n
        
        ac = 0

        if(m[-4:] == n[-4:]):
             ac = v * 3000
        elif(m[-3:] == n[-3:]):
             ac = v * 500
        elif(m[-2:] == n[-2:]):
             ac = v * 50
        else:
            vM = int(m[-2:]) if m[-2:] != '00' else 100
            vN = int(n[-2:]) if n[-2:] != '00' else 100
            for i in range(1, 101, 4):
                if vM in range(i, i + 4) and vN in range(i, i + 4):
                    ac = v * 16

        print("{0:.2f}".format(round(ac,2)))
        
    except:
        break
