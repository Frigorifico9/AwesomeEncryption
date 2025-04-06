def nextNode(n):
    nn = int(n//2)
    while (nn-4)%6 != 0:
        if nn%2 == 1:
            nn = 3*nn+1
        else:
            nn = int(nn//2)
    return nn

node = 5927771957113003180036

target = 'LLLLTSTLLTTLLSLLTSLLSSS'

result = ''
for i in range(0,len(target)-1):
    print(node)
    n = (node - 4) // 6
    if ((n - 1) % 2) == 0:
        result = result + 'S'
        print('S')
    elif ((n - 2) % 4) == 0:
        result = result + 'T'
        print('T')
    elif (n % 4) == 0:
        result = result + 'L'
        print('L')
    node=nextNode(node)

print(result)