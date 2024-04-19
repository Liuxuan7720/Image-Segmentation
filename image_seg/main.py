import cv2
import numpy as np

img = cv2.imread('hehua.jpg')
cv2.imshow("img",img)
mask = np.zeros(img.shape[:2],np.uint8)#定义与原图大小相同的掩模
bg = np.zeros((1,65),np.float64)
fg = np.zeros((1,65),np.float64)
# rect = (50,50,400,300)
#在input图像中框选出要分割的目标图像，按回车
r = cv2.selectROI('input', img, True)

x1 = int(r[0])
y1 = int(r[1])
x2 = int(r[0]+r[2])
y2 = int(r[1]+r[3])
rect = (x1,y1,x2,y2) #根据原图设置包含前景的矩形大小
mask2,_,_=cv2.grabCut(img,mask,rect,bg,fg,5,cv2.GC_INIT_WITH_RECT)#提取前景

#将返回的掩模中像数值为0或2像素设置为0（确认为背景），
#所有1或3的像素设置为1（确认为前景）
mask2 = np.where((mask2==2)|(mask2==0),0,1).astype('uint8') 
mask2=mask2[:,:,np.newaxis] #使mask2增加一个维度，由二维变成三维
img2 = img*mask2#将掩模与原图像相乘获得分割出来的前景图像
cv2.imshow("img2",img2)
cv2.waitKey(0)
cv2.destroyAllWindows()