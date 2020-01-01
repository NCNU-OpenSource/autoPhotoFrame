import cv2
from PIL import Image

casc_path = "/home/pi/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(casc_path)
imagename = cv2.imread("/home/pi/autophoto/human.png")
faces = faceCascade.detectMultiScale(imagename, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), flags = cv2.CASCADE_SCALE_IMAGE)

cv2.rectangle(imagename, (10,imagename.shape[0]-20), (110,imagename.shape[0]), (0,0,0), -1)

#cv2.putText(imagename,"Find " + str(len(faces)) + "face!",(10,imagename.shape[0]-5),cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,255),2)

imagename = cv2.cvtColor(imagename,cv2.COLOR_BGR2RGB)
count = 1
for (x,y,w,h) in faces:
    cv2.rectangle(imagename,(x,y),(x+w,y+h),(128,255,0),2)
    filename = "human" + "face" + ".png"
    image1 = Image.fromarray(imagename)
    #image1 = Image.open(imagename)
    image2 = image1.crop((x,y,x+w,y+h))
    image3 = image2.resize((200,200),Image.ANTIALIAS)
    image3.save('/home/pi/autophoto/'+filename)
    count += 1
