from PIL import Image
import os
import itertools

t = []


def generate_nfts():
    print("Generating NFTs...")

    directory1 = r"C:\Users\Khaldi PC\Pictures\ColdByte NFTs\NFT Scripts\images\Layer1"
    directory2 = r"C:\Users\Khaldi PC\Pictures\ColdByte NFTs\NFT Scripts\images\Layer2"
    directory3 = r"C:\Users\Khaldi PC\Pictures\ColdByte NFTs\NFT Scripts\images\Layer3"
    directoryf = r"C:\Users\Khaldi PC\Pictures\ColdByte NFTs\NFT Scripts\images\Generated NFTs"

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