
## For subdirectories
import os
import cv2
a='F:\\LPU\\projects\\AI\\Hand-written-text-recognizer\\training_set - Copy\\modify\\0'
l=os.listdir(a)


for count, filename in enumerate(l):
    img=cv2.imread(a+'\\'+filename)
    if count==0:
        cv2.imshow('img',img)
        cv2.waitKey()
    img=cv2.resize(img,(30,30))
    #img=cv2.bitwise_not(img)
    cv2.imwrite(a+'\\'+filename,img)
print('done')
        

#####check your files now

