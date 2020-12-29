## For subdirectories
import os
a='F:\\LPU\\projects\\AI\\Hand-written-text-recognizer\\training_set - Copy\\modify'
l=os.listdir(a)
print(l)
for foldername in l:
    for count, filename in enumerate(os.listdir(a+'\\'+foldername)):
        #print(filename)
        dst =str(count) + ".jpg"
        src = a+'\\'+foldername+'\\'+filename 
        dst =a+'\\'+foldername+'\\'+dst
          
        os.rename(src, dst) 

#####check your files now
