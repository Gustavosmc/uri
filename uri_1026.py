while True:
    try:
        ent = input()
        ent = ent.split(' ')
        a, b = [int(e) for e in ent]
        print(a ^ b)
    except:
        break




