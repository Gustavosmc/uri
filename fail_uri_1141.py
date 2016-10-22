
while True:
    try:
        n = int(input())
        if n == 0:
            break
        cont = 0
        last_s = ' '
        ctrl = 0
        for i in range(n):
            s = input()
            if last_s not in s:
                cont += 1
            last_s = s

        print(cont)

    except:
        break
