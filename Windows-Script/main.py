from PIL import Image
import os
import itertools

t = []

"""

To add more layers, you'll need to add more directory variables, 
more Image open layers variables and know how to use a bit of the PIL library

Ex 1: Layers 6


    directory1 = r"...\Layer1"
    directory2 = r"...\Layer2"
    directory3 = r"...\Layer3"
    directory4 = r"...\Layer4"
    directory5 = r"...\Layer5"
    directory6 = r"...\Layer6"

    layer1 = Image.open(os.path.join(directory1, i[0]))
    layer2 = Image.open(os.path.join(directory2, i[1]))
    layer3 = Image.open(os.path.join(directory3, i[2]))
    layer4 = Image.open(os.path.join(directory4, i[3]))
    layer5 = Image.open(os.path.join(directory5, i[4]))
    layer6 = Image.open(os.path.join(directory6, i[5]))

    base = Image.alpha_composite(layer1, layer2)
    base1 = Image.alpha_composite(base, layer3)
    base2 = Image.alpha_composite(base1, layer4)
    base3 = Image.alpha_composite(base2, layer5)
    final = Image.alpha_composite(base3, layer6)

"""

def generate_nfts():
    print("Generating NFTs...")

    directory1 = r"NFT Scripts\images\Layer1"
    directory2 = r"NFT Scripts\images\Layer2"
    directory3 = r"NFT Scripts\images\Layer3"
    directoryf = r"NFT Scripts\images\Generated NFTs"

    t = [os.listdir(directory1), os.listdir(directory2), os.listdir(directory3)]
    
    e = list(itertools.product(*t))

    z = 0

    for i in e:
        z+=1
        layer1 = Image.open(os.path.join(directory1, i[0]))
        layer2 = Image.open(os.path.join(directory2, i[1]))
        layer3 = Image.open(os.path.join(directory3, i[2]))

        base = Image.alpha_composite(layer1, layer2)

        final = Image.alpha_composite(base, layer3)

        final.save(os.path.join(directoryf, f'final{z}.png'))
    
    print("Generating NFTs Complete!")

generate_nfts()