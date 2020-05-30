from PIL import Image, ImageOps
from sys import argv
try:
    image = argv[2]
    number = int(argv[1])
    output = argv[3]
    im = Image.open(image)
    (width, height) = im.size
    if (width + number) > 11000:
        print('Too many pixels')
        raise SystemExit()
    if (height + number) > 11000:
        print('Too many pixels')
        raise SystemExit()
    if number < 0:
        print('Bad pixel number')
        raise SystemExit()
    ImageOps.expand(im,border=number,fill='black').save(output)
except IndexError:
    print('No arguments')
except FileNotFoundError:
    print('File not found')
except MemoryError:
    print('Not enough memory')
