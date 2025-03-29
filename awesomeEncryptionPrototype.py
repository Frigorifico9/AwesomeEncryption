# Convert image to binary string
import constellationFinder as cf

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
    print(constellation)
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

def findNode(constellation,b):
    constellationString = ''.join(constellation)
    constant1,constant2 = cf.Threading(constellationString)
    Solutions_a0 = cf.findASolution(constant1, constant2)
    currentNode = cf.Node(constellationString[0])
    a0 = b * Solutions_a0[0] + Solutions_a0[1]
    return 6*(a0 * currentNode.n1 + currentNode.n2).intPart+4

def nextNode(n):
    nn = int(n//2)
    while (nn-4)%6 != 0:
        if nn%2 == 1:
            nn = 3*nn+1
        else:
            nn = int(nn//2)
    return nn

def nodeToBinary(node):
    constellationString = ''
    while (constellationString[::-1][0:3] != 'SSS'): #find stop signal
        n = (node - 4) // 6
        if (n-1)%2 == 0:
            constellationString += 'S'
        if (n-2)%4 == 0:
            constellationString += 'T'
        if n%4 == 0:
            constellationString += 'L'
        node = nextNode(node)
    if len(constellationString)%2 == 0: #we avoid removing a legitimate final S
        constellationString = constellationString[0:len(constellationString) - 2]  # remove stop signal
    elif len(constellationString)%2 == 1:
        constellationString = constellationString[0:len(constellationString) - 3] #remove stop signal
    constellationList = [constellationString[i:i + 2] for i in range(0, len(constellationString), 2)]
    rawBinary = constellationToBinary(constellationList)
    return ' '.join(rawBinary[i:i+7] for i in range(0, len(rawBinary), 7))

def encrypt(node,sharedSecret):
    sign = int(node / abs(node))
    message = str(abs(node))
    encrypted=''
    for i in range(0,len(message)):
        encrypted += str((int(message[i])+int(sharedSecret[i]))%10)
    return sign*int(encrypted)

def decrypt(node,sharedSecret):
    sign = int(node/abs(node))
    message = str(abs(node))
    decrypted=''
    for i in range(0,len(message)):
        if sharedSecret[i] != '0':
            decrypted += str((10+int(message[i])-int(sharedSecret[i]))%10)
        else:
            decrypted += message[i]
    return sign*int(decrypted)

#step 1: text to binary
print('textToBinary')
binaryString = textToBinary('Hel')
print(binaryString)

#step 2: Binary to Constellation
#binaryString = '00111101 00110011'
print('binaryToConstellation')
constellation = binaryToConstellation(binaryString)
print(constellation)

#step 3: Constellation to number
print('findNode')
node = findNode(constellation,cf.Fraction(0,1))
print(node)

#step 3.5: Encrpt node
sharedSecret = '458976895467894500000000000000000000000000000000000000000000'
print('encrypt')
encrypted = encrypt(node,sharedSecret)
print(encrypted)

#step 3.6: Decrypt node
print('decrypt')
decrypted = decrypt(encrypted,sharedSecret)
print(decrypted)

#step 4: Number to binary
print('nodeToBinary')
binaryString = nodeToBinary(decrypted)
print(binaryString)

#step 5: Binary to string
text = binaryToText(binaryString)
print(text)