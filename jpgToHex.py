def imageToHex(image_path):
    with open(image_path, 'rb') as image_file:
        return image_file.read().hex()

def hexToImage(binary_string, output_path):
    hexData = bytes.fromhex(binary_string)  # Convert hex string back to bytes
    with open(output_path, 'wb') as image_file:
        image_file.write(hexData)

#png
#print(imageToBinary('/Users/fer/leaningManim/awesomeEncryption/pngTest.png'))
#jpeg
#print(imageToHex('/Users/fer/leaningManim/awesomeEncryption/padoru.jpeg'))

hexToImage(imageToHex('/Users/fer/leaningManim/awesomeEncryption/padoru.jpeg'),'/Users/fer/leaningManim/awesomeEncryption/padoruRecovered.jpeg')