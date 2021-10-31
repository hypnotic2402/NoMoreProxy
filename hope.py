import face_recognition
import cv2 
import os 
import pickle
import numpy as np

class Image:
    def __init__(self, path , name):
        self.path = path
        self.image = face_recognition.load_image_file(path)
        self.image = cv2.cvtColor(self.image , cv2.COLOR_BGR2RGB)
        self.name = name
        self.loc = face_recognition.face_locations(self.image)[0]
        self.encoding = face_recognition.face_encodings(self.image)[0]
        cv2.rectangle(self.image,(self.loc[3] , self.loc[0]) , (self.loc[1] , self.loc[2]) , (255,0,255) , 2)




def check_present(imgPaths , testimgPath , nameList , superPath):#put superPath = "" if exact path specified
    reference_images=[]
    i = 0
    for name in imgPaths:
        print(name)
        reference_images.append(Image(superPath + name, nameList[i]))
        i+= 1

    testImage = Image(testimgPath , 'test')
    flag = 0
    j = 0

    for f in reference_images:
        r = face_recognition.compare_faces([f.encoding] , testImage.encoding)
        if r[0]:
            return nameList[j]
        j+= 1

    return "-1"
    


#test driver code


# p1 = "sample_img/"
# rip = os.listdir(p1)

# tpi = input("enter test img path : ")
# tp = tpi

# nl = [ "pappu" , "Mudizi"]

# print(check_present(rip , tp , nl,p1))


# cv2.waitKey(0)
