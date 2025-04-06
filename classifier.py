def nextNode(n):
    nn = int(n//2)
    while (nn-4)%6 != 0:
        if nn%2 == 1:
            nn = 3*nn+1
        else:
            nn = int(nn//2)
    return nn

def classifyNode(node):
    n = (node - 4) // 6
    if (n - 1) % 2 == 0:
        return 'S'
    if (n - 2) % 4 == 0:
        return 'T'
    if n % 4 == 0:
        return 'L'

n=5927771957113003238404
constellation = constellation =  'LLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSS'
                 #LLLTSTLLTTLLSLLTSLLSSS

recoveredConstellation = ''
for i in range(0,len(constellation)-1):
    n = nextNode(n)
    symbol = classifyNode(n)
    recoveredConstellation += symbol
print(recoveredConstellation)



