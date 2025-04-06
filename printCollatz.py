N=100
x = 275799822145486508261380

def identify(x):
    n = int((x-4)/6)
    if (n-1)%2 == 0:
        return 'S'
    if (n-2)%4 == 0:
        return 'T'
    if (n)%4 == 0:
        return 'L'

for n in range(0,N):
    if x%2 == 0:
        x = int(x/2)
    else:
        x = 3*x+1
    print(x)
    print(identify(x))