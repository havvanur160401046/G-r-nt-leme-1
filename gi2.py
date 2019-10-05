import os
print(os.getcwd())

my_list=[9,3,5,6,2,3,6]
print(my_list)

for i in my_list:
    print(i)


def my_function_1(my_list=[9,3,5,6,2,3,6]):
    #my_list=[9,3,5,6,2,3,6]
    for i in range(len(my_list)):
        print(i,my_list[i])
        my_list[i]+=1
    print(my_list)

my_function_1(my_list=[9,3,55,6,2,34,61])
#my_function_1(my_list=["dokuz",3,55,6,2,34,61]) # hata


import numpy as np
my_list_1=np.array([[9,3,55,6,2,34,61]])#ndarray
print(my_list_1)
print(my_list_1+1)



def my_function_2(my_array=np.array([[9,3,55,6,2,34,61]])):
    return my_array-10

print(my_function_2())
#my_function_1(my_list=["dokuz",3,55,6,2,34,61]) # hata



import matplotlib.pyplot as plt
im_1=plt.imread("istanbul.jpg")
plt.imshow(im_1)
plt.show()

print(im_1.ndim)

print(im_1.shape)

im_2=np.zeros(im_1.shape,dtype=int)
for m in range(im_1.shape[0]):
    for n in range(im_1.shape[1]):
        im_2[m,n,0]=im_1[m,n,0]+100
        im_2[m,n,1]=im_1[m,n,0]
        im_2[m,n,2]=im_1[m,n,0]
plt.imshow(im_2)
#plt.imshow((im_2 * 255).astype(np.uint8))
plt.show()

m,n,p=im_1.shape
im_3=np.zeros((int(m/2),int(n/2)),dtype=int)
for m in range(int(im_1.shape[0]/2)):
    for n in range(int(im_1.shape[1]/2)):
        #s0=(im_1[m*2,n*2,0]+im_1[m*2,n*2,1]+im_1[m*2,n*2,2])/3
        s0=(im_1[m*2,n*2,0]/3+im_1[m*2,n*2,1]/3+im_1[m*2,n*2,2]/3)
        s1=(im_1[m*2,n*2+1,0]/3+im_1[m*2,n*2+1,1]/3+im_1[m*2,n*2+1,2]/3)
        s2=(im_1[m*2+1,n*2,0]/3+im_1[m*2+1,n*2,1]/3+im_1[m*2+1,n*2,2]/3)
        s3=(im_1[m*2+1,n*2+1,0]/3+im_1[m*2+1,n*2+1,1]/3+im_1[m*2+1,n*2+1,2]/3)
        s=(s0+s1+s2+s3)/4
        im_3[m,n]=int(s0)
plt.imshow(im_3)
plt.show()



def my_f_4(im_20):
    m,n,p=im_20.shape
    new_m=int(m/2)
    new_n=int(n/2)
    im_30=np.zeros((new_m,new_n,3),dtype=int)
    for m in range(new_m):
        for n in range(new_n):
            im_30[m,n,0]=int(im_20[m*2,n*2,0])
            im_30[m,n,1]=int(im_20[m*2,n*2,1])
            im_30[m,n,2]=int(im_20[m*2,n*2,2])
    return(im_30)
im_10=my_f_4(im_1)
im_20=my_f_4(im_10)
plt.imshow(im_20)
plt.show()





