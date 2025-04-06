def extended_gcd(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1
    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return a, x0, y0

class Fraction:
    def __init__(self,numerator,denominator):
        if denominator != 0:
            gcd, x, y = extended_gcd(numerator, denominator)
            self.numerator = numerator // gcd
            self.denominator = denominator // gcd
            self.actualValue = self.numerator / self.denominator
            self.intPart = self.numerator // self.denominator
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

#n1 multiplies a1 when the node the second
#-s1 multiplies a0 when the node is the first

class Vertex: #I needed to access all of thee constants dynamically and this is the best I came up with
    def __init__(self,symbol):
        if symbol == 'S':
            self.symbol = 'S'
            self.n1 = 2
            self.n2 = 1
            self.s1 = 3
            self.s2 = 2
        elif symbol == 'L':
            self.symbol = 'L'
            self.n1 = 4
            self.n2 = 0
            self.s1 = 3
            self.s2 = 0
        elif symbol == 'T':
            self.symbol = 'T'
            self.n1 = 4
            self.n2 = 2
            self.s1 = 1
            self.s2 = 0

def Threading(constellation):
    [alpha, beta, gamma] = [1, 1, 0]
    for n in range(1, len(constellation)):
        prevNode = Vertex(constellation[n - 1])
        currentNode = Vertex(constellation[n])
        if n == 1:
            gamma = prevNode.s1 * gamma + (prevNode.s2-currentNode.n2)
        else:
            gamma = prevNode.s1 * gamma + alpha * (prevNode.s2 - currentNode.n2)
        alpha = currentNode.n1*alpha
        beta = prevNode.s1 * beta
    return alpha, -beta, gamma

def getEachNode(Solutions_a_0,b,constellation):
    nodes = []
    a0 = b*Solutions_a_0[0] + Solutions_a_0[1]
    for element in range(0, len(constellation)-1):
        nextNode = Node(constellation[element + 1])
        currentNode = Node(constellation[element])
        n = a0 * currentNode.n1 + currentNode.n2
        nodes.append(6*n+4)
        a0 = (a0 * currentNode.s1 + currentNode.s2 - nextNode.n2)/nextNode.n1
    lastNode = Node(constellation[len(constellation)-1])
    n = lastNode.n1 * a0 + lastNode.n2
    nodes.append(6 * n + 4)
    return nodes

def getNextNode(solutions_a0,b,symbol):
    a0 = b*solutions_a0[0] + solutions_a0[1]
    currentNode = Node(symbol)
    n = a0 * currentNode.n1 + currentNode.n2
    node = 6*n+4
    return node

def getFirstNodeDeprecated(Solutions_a_0,b,constellation):
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

def findSolution(alpha, beta, gamma):
    z, x, y = extended_gcd(alpha, beta)
    solutions_a0 = [alpha // z, y * gamma // z]
    solutions_an = [-beta // z, x * gamma // z]
    return solutions_a0, solutions_an

#constellation = 'LLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSS'
#alpha, beta, gamma = Threading(constellation)
#solutions_a0, solutions_an = findSolution(alpha, beta, gamma)
#print(alpha, beta, gamma)
#print(solutions_a0,solutions_an)