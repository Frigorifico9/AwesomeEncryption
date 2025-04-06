import newConstellationFinder as ncf
import random

def textToBinary(text):
    return ' '.join(format(ord(c),'b') for c in text)

def binaryToText(binaryString):
    return ''.join(chr(int(c,2)) for c in binaryString.split(' '))

def imageToBinary(imagePath):
    with open(imagePath, 'rb') as imageFile:
        binaryData = imageFile.read()
    return ''.join(format(byte, '08b') for byte in binaryData)  # Convert to binary string

# Convert binary string back to image
def binaryToImage(binaryString, outputPath):
    binaryData = bytes(int(binaryString[i:i+8], 2) for i in range(0, len(binaryString), 8))
    with open(outputPath, 'wb') as imageFile:
        imageFile.write(binaryData)

def binaryToConstellation(binaryString):
    binaryString = binaryString.replace(' ', '')
    global added
    if len(binaryString)%3 == 1:
        binaryString += '00'
        added = 2
    elif len(binaryString)%3 == 2:
        binaryString += '0'
        added = 1
    elif len(binaryString)%3 == 0:
        added = 0
    conversionDictionary = {0: 'TT', 1: 'TL', 2: 'TS', 3: 'LT', 4: 'LL', 5: 'LS', 6: 'ST',
                            7: 'SL'}
    constellation = []
    chunks = [binaryString[i:i + 3] for i in range(0, len(binaryString), 3)]
    for chunk in chunks:
        constellation.append(conversionDictionary[int(chunk,2)])
    constellation.append('SSS') #this serves to indicate the end of the message, since it will never arise naturally
    return constellation

def constellationToBinary(constellation):
    conversionDictionary = {'TT':0, 'TL':1, 'TS':2, 'LT':3, 'LL':4, 'LS':5, 'ST':6,
                            'SL':7}
    binaryString = ''
    for bead in constellation:
        initialString = bin(conversionDictionary[bead])[2:]
        if len(initialString) == 1:
            initialString = '00' + initialString
        elif len(initialString) == 2:
            initialString = '0' + initialString
        binaryString += initialString
    return binaryString[:len(binaryString)-added]

def findVertex(constellation,b):
    constellationString = ''.join(constellation)
    alpha, beta, gamma = ncf.Threading(constellationString)
    solution_a0, solution_an = ncf.findSolution(alpha, beta, gamma)
    currentNode = ncf.Vertex(constellationString[0])
    a0 = b * solution_a0[0] + solution_a0[1]
    return 6*(a0 * currentNode.n1 + currentNode.n2)+4

def nextVertex(n):
    nn = int(n//2)
    while (nn-4)%6 != 0:
        if nn%2 == 1:
            nn = 3*nn+1
        else:
            nn = int(nn//2)
    return nn

def vertexToBinary(vertex):
    constellationString = ''
    sStrikeCounter = 0
    #while (constellationString[::-1][0:3] != 'SSS'): #find stop signal
    while (sStrikeCounter != 3):  # find stop signal
        n = (vertex - 4) // 6
        if (n-1)%2 == 0:
            constellationString += 'S'
            sStrikeCounter += 1
        elif (n-2)%4 == 0:
            constellationString += 'T'
            sStrikeCounter = 0
        elif n%4 == 0:
            constellationString += 'L'
            sStrikeCounter = 0
        vertex = nextVertex(vertex)
    if len(constellationString)%2 == 0: #we avoid removing a legitimate final S
        constellationString = constellationString[0:len(constellationString) - 2]  # remove stop signal
    elif len(constellationString)%2 == 1:
        constellationString = constellationString[0:len(constellationString) - 3] #remove stop signal
    constellationList = [constellationString[i:i + 2] for i in range(0, len(constellationString), 2)]
    #print(len(constellationList))
    rawBinary = constellationToBinary(constellationList)
    return ''.join(rawBinary[i] for i in range(0, len(rawBinary)))

def decrypt(key,encrypted):
    alpha, beta, gamma = ncf.Threading(key[0])
    solution_a0K, solution_anK = ncf.findSolution(alpha, beta, gamma)
    firstVertex = ncf.Vertex(key[0][0])
    a0 = solution_a0K[0]*encrypted+solution_a0K[1]
    vertex = 6*(a0 * firstVertex.n1 + firstVertex.n2)+4
    galaxyString = ''
    sStrikeCounter = 0
    while (sStrikeCounter != 3):  # find stop signal
        n = (vertex - 4) // 6
        if (n-1)%2 == 0:
            galaxyString += 'S'
            sStrikeCounter += 1
        elif (n-2)%4 == 0:
            galaxyString += 'T'
            sStrikeCounter = 0
        elif n%4 == 0:
            galaxyString += 'L'
            sStrikeCounter = 0
        vertex = nextVertex(vertex)
    constellationString = galaxyString[len(key[0])+2*key[1]:]
    if len(constellationString)%2 == 0: #we avoid removing a legitimate final S
        constellationString = constellationString[0:len(constellationString) - 2]  # remove stop signal
    elif len(constellationString)%2 == 1:
        constellationString = constellationString[0:len(constellationString) - 3] #remove stop signal
    constellationList = [constellationString[i:i + 2] for i in range(0, len(constellationString), 2)]
    rawBinary = constellationToBinary(constellationList)
    return ''.join(rawBinary[i] for i in range(0, len(rawBinary)))

def generateDecoy(size):
    conversionDictionary = {0: 'TT', 1: 'TL', 2: 'TS', 3: 'LT', 4: 'LL', 5: 'LS', 6: 'ST',
                            7: 'SL'}
    decoy = ''
    for n in range(0,size):
        decoy += conversionDictionary[random.randint(0,7)]
    return decoy

def chunkify(string,chunkSize):
    chunkified = []
    for n in range(0,chunkSize-1):
        chunkified.append(string[n*chunkSize:(n+1)*chunkSize])
    return chunkified

key = ['STL',1,0]
b = key[2]
decoy = generateDecoy(key[1])

#step 1: image to binary
print('Image to biary')
binaryString = imageToBinary('/Users/fer/leaningManim/awesomeEncryption/newSmall_pict_test.JPG')
print(len(binaryString))

#step 1.5: split image into manageable chunks
binaryImage = chunkify(binaryString,9336)

#step 2: binary to constellation
print('binary to constellation')
constellations = []
for chunk in binaryImage:
    constellations.append(binaryToConstellation(chunk))

#step 2.5: constellation to galaxy
galaxies = []
for constellation in constellations:
    galaxies.append(key[0]+decoy+''.join(constellation))

#step 3.-1: get solution for a0 of key
print('get solution for a0 of key')
alpha, beta, gamma = ncf.Threading(key[0])
solution_a0K, solution_anK = ncf.findSolution(alpha, beta, gamma)

print('get solution for a0 of galaxy')
encryptedChunks = []
for galaxy in galaxies:
    #step 3: get solution for a0 of galaxy
    alpha, beta, gamma = ncf.Threading(galaxy)
    solution_a0G, solution_anG = ncf.findSolution(alpha, beta, gamma)
    #step 4: encrypt
    encryptedChunks.append((solution_a0G[0]*b + solution_a0G[1] - solution_a0K[1])//solution_a0K[0])

#wait, we have to deal with the bits we added to make them divisible by 3... I guess... if all the chunks are already
#divisible by 3 only the last chunk will have anything added to it... but if it does, it will affect the added variable

#step 5: decrypt
print('decrypt')

for gibberish in encryptedChunks:
    decrypted = decrypt(key,gibberish)


binaryToImage(decrypted,'/Users/fer/leaningManim/awesomeEncryption/newwachamacallit.JPG')
