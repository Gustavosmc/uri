entrada = input()
ns = entrada.split(' ')
a, b, c = [int(n) for n in ns]
r = 0
if(b < a  > c):
    r = a
elif(a < b > c):
    r = b
else:
    r = c
print(r, 'eh o maior')
