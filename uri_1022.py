def  simplifica(n, d):
    m = n if n < d else d
    m = abs(m)
    for i in range(m, 1, -1):
        while n % i == 0 and d % i == 0:
            n, d = n / i, d /i          
    return (int(n), int(d))

             
while True:
    try:
        n = int(input())
        if not n:
            break
        for i in range(n):
            ent = input()
            ent = ent.split(' ')
            n1, d1, n2, d2 = [int(v) for v in ent[::2]]
            op = ent[3]
            num, den = 0, 0
            if op == '/':
                num, den = n1 * d2, n2 * d1     
            elif op == '*':
                num, den = n1 * n2, d1 * d2
            elif op == '-':
                num, den = n1 * d2 - n2 * d1, d1 * d2
            elif op == '+':
                num, den = n1 * d2 + n2 * d1, d1 * d2
            n, d = simplifica(num, den)
            print("{}/{} = {}/{}".format(num,den,n, d))
    except e:
        break
