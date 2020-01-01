import random
from PIL import Image

rd = str(random.randint(1,5))

imageA = Image.open('/home/pi/autophoto/humanface.png')
imageA = imageA.convert('RGBA')
widthA , heightA = imageA.size


imageB = Image.open('/home/pi/autophoto/frame'+rd[:1]+'.png')
imageB = imageB.convert('RGBA')
widthB , heightB = imageB.size


newWidthB = int(widthA)
newHeightB = int(heightB/widthB*newWidthB)
imageB_resize = imageB.resize((newWidthB, newHeightB))


resultPicture = Image.new('RGBA', imageA.size, (0, 0, 0, 0))

resultPicture.paste(imageA,(0,0))


right_bottom = (widthA - newWidthB, heightA - newHeightB)


resultPicture.paste(imageB_resize, right_bottom, imageB_resize)


resultPicture.save("/home/pi/autophoto/merge.png")
