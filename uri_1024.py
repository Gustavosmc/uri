n = int(input())
for i in range(n):
    palavra = input()
    palavra = list(palavra)
    for i in range(len(palavra)):
        if palavra[i].isalpha():
          palavra[i] = chr(ord(palavra[i]) + 3)
    palavra = palavra[::-1]
    for l in range(int(len(palavra) / 2), len(palavra)):
        palavra[l]  = chr(ord(palavra[l]) - 1)   
    palavra = ''.join(palavra)
    print(palavra)
