from constellationFinder import *

def nextNode(n):
    nn = int(n//2)
    while (nn-4)%6 != 0:
        if nn%2 == 1:
            nn = 3*nn+1
        else:
            nn = int(nn//2)
    return nn

def getFirstNode(constellation,b,Solutions_a0):
    firstNode = Node(constellation[0])
    a0 = b * Solutions_a0[0] + Solutions_a0[1]
    n = a0 * firstNode.n1 + firstNode.n2
    return 6*n.intPart+4

def getNode(bead,b,Solutions_a0):
    node = Node(bead)
    a0 = b * Solutions_a0[0] + Solutions_a0[1]
    n = a0 * node.n1 + node.n2
    return 6*n.intPart+4

def testResult(constellation,b,Solutions_a0):
    eachNode = getEachNode(Solutions_a0,b,constellation)
    nodeV1 = getFirstNode(constellation, b, Solutions_a0)
    for node in eachNode:
        print(node)
        print(nodeV1)
        if nodeV1 != node:
            return False
        else:
            nodeV1 = nextNode(nodeV1)
    return True

def classifyNode(node):
    n = (node - 4) // 6
    if (n - 1) % 2 == 0:
        return 'S'
    if (n - 2) % 4 == 0:
        return 'T'
    if n % 4 == 0:
        return 'L'

def constellationTester(n,constellation):
    newConstellation = ''
    while len(newConstellation) < len(constellation):
        newConstellation += classifyNode(n)
        n = nextNode(n)
    return  newConstellation


#constellation = 'LLLLTSTLLTTLLSLLTSLLSSS'
constellation =  'LLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSSLLLLTSTLLTTLLSLLTSLLSSS'
                 #LLLLTSTLLTTLLSLLTSL
                 #LLLLLTSSSSSLLLLSTTST
                 #LLLLTSTLLTTLLSLLT
                 #LLLLTSTLLTTLLSLLTS
                 #LLLLTSTLLTTLLSLLTSL
                 #LLLLLTSSSSSLLLLSTTST
#constellation =  'LLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLLL'
                 #LLLLLLLLLLSSSSSLSLLTSLT
constellation = 'LLLSTTSSS'
b=Fraction(0,1)
constant1,constant2 = Threading(constellation)
Solutions_a0 = findASolutionAlt(constant1,constant2)[0]
Solutions_an = findASolutionAlt(constant1,constant2)[1]

firstNode = getFirstNode(constellation,b,Solutions_a0)

def getCollatzNodes(n,constellation):
    sequence = [n]
    for bead in range(0,len(constellation)-1):
        n = nextNode(n)
        sequence.append(n)
    return sequence

#print(getEachNode(Solutions_a0,b,constellation))
#print(getCollatzNodes(getEachNode(Solutions_a0,b,constellation)[0],constellation))

print(constellation)
print(testResult(constellation,b,Solutions_a0))
print(getEachNode(Solutions_a0,b,constellation)[0])
print(getFirstNode(constellation,b,Solutions_a0))
print(constellationTester(getFirstNode(constellation,b,Solutions_a0),constellation))

print('The equation for the constellation '+constellation+' is a_n = '+str(constant1.print)+' * a_0 + '+str(constant2.print))

print('The solutions are: a_0 = '+str(Solutions_a0[0].print)+' * b + '+str(Solutions_a0[1].print)+', a_n = '+str(Solutions_an[0].print)+' * b + '+str(Solutions_an[1].print))

print('Finally, using b = '+str(b.print)+' we find that one example of this constellation is: '+str(getEachNode(Solutions_a0,b,constellation)))