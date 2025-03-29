def extended_gcd(a, b): #Helps us reduce fractions
    if b == 0:
        return a, 1, 0

    gcd, x1, y1 = extended_gcd(b, a % b)
    x = y1
    y = x1 - (a // b) * y1

    return gcd, x, y
'''
def extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return a, x0, y0
'''

class Fraction:
    def __init__(self,numerator,denominator):
        if denominator != 0:
            gcd, x, y = extended_gcd(numerator, denominator)
            self.numerator = int(numerator / gcd)
            self.denominator = int(denominator / gcd)
            self.actualValue = self.numerator / self.denominator
            self.intPart =int(self.numerator / self.denominator)
            self.print = '(' + str(self.numerator) + '/' + str(self.denominator) + ')'
            self.error = False
        else:
            self.error = True

    def __add__(self, other):
        if type(other) == int:
            fraction2 = Fraction(other,1)
        elif type(other) == type(Fraction(1,1)):
            fraction2 = other
        newNumerator = self.numerator * fraction2.denominator + fraction2.numerator * self.denominator
        return Fraction(newNumerator, self.denominator * fraction2.denominator)

    def __sub__(self, other):
        if type(other) == int:
            fraction2 = Fraction(other,1)
        elif type(other) == type(Fraction(1,1)):
            fraction2 = other
        newNumerator = self.numerator * fraction2.denominator - fraction2.numerator * self.denominator
        return Fraction(newNumerator, self.denominator * fraction2.denominator)

    def __mul__(self, other):
        if type(other) == float:
            fraction2 = Fraction(other,1)
        if type(other) == int:
            fraction2 = Fraction(other,1)
        elif type(other) == type(Fraction(1,1)):
            fraction2 = other
        return Fraction(self.numerator * fraction2.numerator, self.denominator * fraction2.denominator)

    def __truediv__(self, other):
        if type(other) == int:
            fraction2 = Fraction(other,1)
        elif type(other) == type(Fraction(1,1)):
            fraction2 = other
        if fraction2.error:
            print('You are trying to divide by zero idiot')
        return Fraction(self.numerator * fraction2.denominator, self.denominator * fraction2.numerator)

    def __floordiv__(self, other):
        if type(other) == int:
            fraction2 = Fraction(other,1)
        elif type(other) == type(Fraction(1,1)):
            fraction2 = other
        if fraction2.error:
            print('You are trying to divide by zero idiot')
        return Fraction(self.numerator * fraction2.denominator, self.denominator * fraction2.numerator).intPart

class Node: #I needed to access all of thee constants dynamically and this is the best I came up with
    def __init__(self,symbol):
        if symbol == 'S':
            self.n1 = Fraction(2,1)
            self.n2 = Fraction(1,1)
            self.s1 = Fraction(3,1)
            self.s2 = Fraction(2,1)
        elif symbol == 'L':
            self.n1 = Fraction(4,1)
            self.n2 = Fraction(0,1)
            self.s1 = Fraction(3,1)
            self.s2 = Fraction(0,1)
        elif symbol == 'T':
            self.n1 = Fraction(4,1)
            self.n2 = Fraction(2,1)
            self.s1 = Fraction(1,1)
            self.s2 = Fraction(0,1)

def Threading(constellation):
    [constant1, constant2] = [Fraction(1,1), Fraction(0,1)]
    for n in range(1, len(constellation)):
        prevNode = Node(constellation[n - 1])
        currentNode = Node(constellation[n])
        factor1 = prevNode.s1 / currentNode.n1
        constant1 = factor1 * constant1
        factor2 = (prevNode.s2 - currentNode.n2) / currentNode.n1
        constant2 = factor1 * constant2 + factor2
    return constant1,constant2

def getEachNode(Solutions_a_0,b,constellation):
    nodes = []
    a0 = b*Solutions_a_0[0] + Solutions_a_0[1]
    for element in range(0, len(constellation)-1):
        nextNode = Node(constellation[element + 1])
        currentNode = Node(constellation[element])
        n = a0 * currentNode.n1  + currentNode.n2
        nodes.append(6*n.intPart+4)
        a0 = (a0 * currentNode.s1 + currentNode.s2 - nextNode.n2)/nextNode.n1
    lastNode = Node(constellation[len(constellation)-1])
    n = lastNode.n1 * a0 + lastNode.n2
    nodes.append(6 * n.intPart + 4)
    return nodes

def getFirstNode(Solutions_a_0,b,constellation):
    nodes = []
    a0 = b*Solutions_a_0[0] + Solutions_a_0[1]
    for element in range(0, 0):
        nextNode = Node(constellation[element + 1])
        currentNode = Node(constellation[element])
        n = a0 * currentNode.n1  + currentNode.n2
        nodes.append(6*n.intPart+4)
        a0 = (a0 * currentNode.s1 + currentNode.s2 - nextNode.n2)/nextNode.n1
    lastNode = Node(constellation[len(constellation)-1])
    n = lastNode.n1 * a0 + lastNode.n2
    nodes.append(6 * n.intPart + 4)
    return nodes[0]

#The extended Euclid algorithm gets us a solution, but this is to find THE solution, the first time this appears in the tree
#I couldn't think of an elegant way to find it
def findFirstSolution(constant1,constant2): #We find the first solution by brute force, I'm sorry
    for n in range(0,2**30-1):
        k = constant1*n+constant2
        if int(k.actualValue) == k.actualValue:
            return k.actualValue,n

#If you are a free spirit who accepts all solutions equally (or a sick freak who doesn't care) use this
def findASolution(constant1,constant2):
    c1 = constant1.numerator
    c2 = constant1.denominator
    c3 = constant2.numerator
    c4 = constant2.denominator
    gamma, x, y = extended_gcd(c2 * c4, -c4 * c1)
    return [Fraction(int(c2 * c4 / gamma), 1), Fraction(int(y * c3 * c2 / gamma), 1)]


'''
#constellation = 'SSSLSSTTTT'
constellation = 'LLLLLTTLLTLSLLSTSTTTSSS'
b=Fraction(0,1)
constant1,constant2 = Threading(constellation)

#factor1 = constant1.denominator*constant2.denominator
#factor2 = -constant2.denominator*constant1.numerator
#gcd, xPrime, yPrime = extended_gcd(factor1,factor2)
#x0 = xPrime*constant1.denominator*constant2.numerator
#y0 = yPrime*constant1.denominator*constant2.numerator
#gcdSign = gcd/abs(gcd)
#Solutions_a0 = [Fraction(-constant2.denominator*constant1.numerator/gcd,1),Fraction(y0*gcdSign,1)]
#Solutions_an = [Fraction(-constant1.numerator/gcd,1),Fraction(x0*gcdSign,1)]
[k,n] = findFirstSolution(constant1,constant2)
Solutions_a0 = [constant1.denominator,n]
Solutions_an = [constant1.numerator,k]

print(getFirstNode(Solutions_a0,b,constellation))

print('The equation for the constellation '+constellation+' is a_n = '+str(constant1.print)+' * a_0 + '+str(constant2.print))

print('The solutions are: a_0 = '+str(Solutions_a0[0])+' * b + '+str(Solutions_a0[1])+', a_n = '+str(Solutions_an[0])+' * b + '+str(int(Solutions_an[1])))

print('Finally, using b = '+str(b.print)+' we find that one example of this constellation is: '+str(getEachNode(Solutions_a0,b,constellation)))
'''




