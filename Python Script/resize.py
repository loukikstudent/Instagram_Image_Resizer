import cv2
import os
im_pth = input("Enter path of jpgs\n")
c=int(input("Enter 0 for black and 255 for white bars\n"))
os.chdir(im_pth)
l=os.listdir()
print(l)
os.chdir('..')
os.mkdir('Instagram')
np=os.getcwd()
def resize(i,c):
    im = cv2.imread(im_pth+"\\"+i)
    og_h,og_w = im.shape[:2] # old_size is in (height, width) format
    b=max(og_h,og_w)
    if og_h==b:
        flag=0
    if flag==0:
        #this mean height is more 4:5 widht:height
        #5/9 x is height
        x=int(og_h*(9/5))
        n_w=int(x*(4/9))
        n_h=b
    else:
        x=int(og_w*(9/4))
        n_h=int(x*(5/9))
        n_w=b
    xtr_w=n_w-og_w
    xtr_h=n_h-og_h
    top,bottom = int(xtr_h/2),int(xtr_h/2)
    left,right=int(xtr_w/2),int(xtr_w/2)
    color=[c,c,c]
    n_im=cv2.copyMakeBorder(im,top,bottom,left,right,cv2.BORDER_CONSTANT,value=color)
    dst=np+"\\"+'Instagram'+"\\"+i
    print(dst)
    cv2.imwrite(dst,n_im)
for i in l:
    resize(i,c)
