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

#The extended Euclid algorithm gets us a solution, but it doesn't correspond to the solution with b=0. Granted, b=0 is not
#special objectively speaking, but it is convenient, so we find that solution using this
def find_solution(constant1, constant2):
    alpha, beta = constant1.denominator, constant1.numerator
    gamma = constant2.numerator
    gcd, x, y = extended_gcd(alpha, beta)
    # Adjust for constant2
    scale = gamma // gcd
    a0_base = y * scale
    an_base = x * scale
    return [alpha, a0_base], [beta, an_base]

def getEachNode(solutions_a0, b, constellation):
    nodes = []
    a0 = Fraction(solutions_a0[0], 1) * b + Fraction(solutions_a0[1], 1)
    for i in range(len(constellation) - 1):
        curr_node = Node(constellation[i])
        next_node = Node(constellation[i + 1])
        n = a0 * curr_node.n1 + curr_node.n2
        nodes.append(6 * n.intPart + 4)
        a0 = (a0 * curr_node.s1 + curr_node.s2 - next_node.n2) / next_node.n1
    last_node = Node(constellation[-1])
    n = a0 * last_node.n1 + last_node.n2
    nodes.append(6 * n.intPart + 4)
    return nodes

# Example usage
constellation = 'TLST'
b = Fraction(0, 1)
constant1, constant2 = Threading(constellation)
solutions_a0, solutions_an = find_solution(constant1, constant2)

print(f'The equation for {constellation} is a_n = {constant1.print} * a_0 + {constant2.print}')
print(f'Solutions: a_0 = {solutions_a0[0]} * b + {solutions_a0[1]}, a_n = {solutions_an[0]} * b + {solutions_an[1]}')
print(f'With b = {b.print}, nodes are: {getEachNode(solutions_a0, b, constellation)}')