# -*- coding: utf-8 -*-

from PIL import Image, ImageDraw
import random
img  = Image.open("m3.png") 
width, height = img.size
pixels=img.load()
n=100
d=ImageDraw.Draw(img)
lines_widths=[]
lines_heights=[]
l=0
minimum_distance=5
def line1(y):
    global pixels
    global width
    global d
    global height
    start_y=y
    maxi=[]
    for i in range(n):
        y=start_y
        start_x=random.randint(int(width/2)-int(width/4),int(width/2)+int(width/4))
        while y<height and pixels[start_x,y][0]>=200 and pixels[start_x,y][1]>=200 and pixels[start_x,y][2]>=200:
            #pixels[start_x,y]=(255,3,3)
            y=y+1
            if y==height:
                return 'end'
        maxi.append(y)
    if len(lines_heights)%5==0:
        return max(maxi)
    else:
        while max(maxi,key=maxi.count)<=start_y+2:
            most_freq=max(maxi,key=maxi.count)
            while(maxi.count(most_freq)):
                maxi.remove(most_freq)
        return max(maxi,key=maxi.count)

def line2(y):
    global width
    start_x=int(width/2)
    while start_x>0:
        try:
            if pixels[start_x,y][0]>=200 and pixels[start_x,y][1]>=200 and pixels[start_x,y][2]>=200 and pixels[start_x,y+1][0]>=200 and pixels[start_x,y+1][1]>=200 and pixels[start_x,y+1][2]>=200 and pixels[start_x,y-1][0]>=200 and pixels[start_x,y-1][1]>=200 and pixels[start_x,y-1][2]>=200:
                try:
                    if pixels[start_x,y][0]>=200 and pixels[start_x,y][1]>=200 and pixels[start_x,y][2]>=200 and pixels[start_x,y+1][0]>=200 and pixels[start_x,y+1][1]>=200 and pixels[start_x,y+1][2]>=200 and pixels[start_x,y+2][0]>=200 and pixels[start_x,y+2][1]>=200 and pixels[start_x,y+2][2]>=200 and pixels[start_x,y-1][0]>=200 and pixels[start_x,y-1][1]>=200 and pixels[start_x,y-1][2]>=200:
                        x1=start_x
                        start_x=0
                except:
                    pass
        except:
            pass

        start_x=start_x-2
        
    start_x=int(width/2)
    while start_x<width:
        try:
            if pixels[start_x,y][0]>=200 and pixels[start_x,y][1]>=200 and pixels[start_x,y][2]>=200 and pixels[start_x,y+1][0]>=200 and pixels[start_x,y+1][1]>=200 and pixels[start_x,y+1][2]>=200 and pixels[start_x,y+2][0]>=200 and pixels[start_x,y+2][1]>=200 and pixels[start_x,y+2][2]>=200 and pixels[start_x,y-1][0]>=200 and pixels[start_x,y-1][1]>=200 and pixels[start_x,y-1][2]>=200:
                try:
                    if pixels[start_x,y][0]>=200 and pixels[start_x,y][1]>=200 and pixels[start_x,y][2]>=200 and pixels[start_x,y+1][0]>=200 and pixels[start_x,y+1][1]>=200 and pixels[start_x,y+1][2]>=200 and pixels[start_x,y+2][0]>=200 and pixels[start_x,y+2][1]>=200 and pixels[start_x,y+2][2]>=200 and pixels[start_x,y-1][0]>=200 and pixels[start_x,y-1][1]>=200 and pixels[start_x,y-1][2]>=200:
                        x2=start_x
                        start_x=width
                except:
                    pass
        except:
            pass
            
        start_x=start_x+2
        
    return (x1+2,x2+2)
        
        
def draw(y):
    global d
    global lines
    k=line1(y)
    if k!='end':
        left_right=line2(k)
        lines_widths.append(left_right)
        d.line([(left_right[0],k),(left_right[1],k)],fill=(12,12,247))
        lines_heights.append(k)
        draw(k+2)
draw(0)




def check(L,x):
   # for i in L:
   #     print("now testing pixels[",x,"][",i,"]",sep='')
    t=0
    for i in range(0,len(L)):
        if pixels[x,L[i]][0]<=200 and pixels[x,L[i]][1]<=200 and pixels[x,L[i]][2]<=200: 
            t=t+1
        #pixels[x,L[i]]=(255,200,87)
    return t





def check2(a,b,c):
    #try:
    if b>height:
        b=height
    t=0
    for i in range(a,b):
       t=t+pixels[c,i][0] + pixels[c,i][1] + pixels[c,i][2]
    #d.line(((c,a),(c,b)),fill=(0,128,0))
    return t
   #except:
    #   print("I tried with a=",a," b=",b," c=",c," and it didn't work.",sep='')
        




maxlr=[]
for i in range(0,len(lines_heights),5):
    j=i
    maxl=width/2
    maxr=width/2
    while j<i+5:
        try:
            if lines_widths[j][0]<maxl:
                maxl=lines_widths[j][0]
        except:
            pass
        
        try:
            if lines_widths[j][1]>maxr:
                maxr=lines_widths[j][1]
        except:
            pass
        j=j+1
    maxlr.append((maxl,maxr))
#print(maxlr)
    
test_lines=[]
q=0
vertical_lines=[]
for i in range(4,len(lines_heights),10):
    t=[]
    q=q+1
    try:
        l=maxlr[q][0]
        r=maxlr[q][1]
    except:
        pass
    m=[]
    for j in range(1,10):
        try:
            m.append(int(lines_heights[i]+j*(lines_heights[i+1]-lines_heights[i])/10))
            #d.line([(l,lines_heights[i]+(j*(lines_heights[i+1]-lines_heights[i])/10)),(r,lines_heights[i]+(j*(lines_heights[i+1]-lines_heights[i])/10))],fill=(255,3,3))
        except:
            pass
    m_position=l
    while m_position<r:
        if check(m,m_position)>=9:
            t.append(m_position)
        m_position=m_position+1
    vertical_lines.append(t)



for i in vertical_lines:
    for j in range(0,len(i)):
        try:
            if i[j+1]-i[j]<3*(lines_heights[1]-lines_heights[0]):
                del i[j]
        except:
            pass
print("vertical_lines=",vertical_lines)
    
box1_height=lines_heights[1]-lines_heights[0]
box1_width=box1_height*1.1
#for i in range(0,len(lines_heights)):
#    j=i//5
    #d.line([(maxlr[j][0],lines_heights[i]),(maxlr[j][1],lines_heights[i])],fill=(12,12,247))
#    q=maxlr[j][0]
    #while q+box1_width<maxlr[j][1]:
    #    d.rectangle([(q,lines_heights[i]),(q+box1_width,lines_heights[i]+box1_height)],outline="red")
    #    q=q+box1_width
    #while q<maxlr[j][1]:
    #    d.rectangle([(q,lines_heights[i]),(q+box1_width,lines_heights[i]+box1_height)],outline="red")
    #    q=q+box1_width


k=4
for i in vertical_lines:
    for j in i:
        #d.line([(j,lines_heights[k]-20),(j,lines_heights[k]+20)],fill=(255,200,87))
        pass
    k=k+10
    




background=0
for i in range(vertical_lines[0][0],vertical_lines[0][len(vertical_lines[0])-1]):   # finding the background
    t=check2(lines_heights[0]-4*box1_height,lines_heights[4]+4*box1_height,i)
    if t>background:
        background=t
        t1=i
print("background=",background)
#d.line((t1,lines_heights[0]-8*box1_height-1,t1,lines_heights[4]+8*box1_height-1),fill=(0,128,0))
d.line((t1,lines_heights[0]-8*box1_height,t1,lines_heights[4]+8*box1_height),fill=(0,128,0))
#d.line((t1,lines_heights[0]-8*box1_height+1,t1,lines_heights[4]+8*box1_height+1),fill=(0,128,0))
#d.line((t1,lines_heights[0]-8*box1_height+2,t1,lines_heights[4]+8*box1_height+2),fill=(0,128,0))
#d.line((t1,lines_heights[0]-8*box1_height+3,t1,lines_heights[4]+8*box1_height+3),fill=(0,128,0))
#d.line((20,20,20,40),fill=(0,128,0))





#for i in range(0,len(vertical_lines)):   # finding the symbols
#    for j in range(1,len(vertical_lines[i])):
#        while q<vertical_lines[i][j]:
#            t=check2(lines_heights[i]-8*box1_height,lines_heights[4]+8*box1_height,i)





box1_height=4*box1_height
k=0
p=0
for i in range(0,len(lines_heights),5):
    if i%10==0 and i!=0:
        k=k+1
    q1=maxlr[i//5][0]
    q2=q1
    for j in range(1,len(vertical_lines[k])):
        #box2_width=int((vertical_lines[k][j]-q)/8)
        #box2_width=int((vertical_lines[k][j]-q)/8)
        while q2<vertical_lines[k][j]:
            #try:
            #print(p,"I will now try the 'if' with the values",lines_heights[i]-8*box1_height,lines_heights[i+4]+8*box1_height,q2)
            #p=p+1
            if check2(lines_heights[i]-box1_height,lines_heights[i+4]+box1_height,q2)<0.9*background:
                q1=q2
                while check2(lines_heights[i]-box1_height,lines_heights[i+4]+box1_height,q2)<0.9*background and q2<vertical_lines[k][j]:
                    q2=q2+1
                if lines_heights[i+4]+box1_height>height:
                    d.rectangle((q1,lines_heights[i]-box1_height,q2,height-3),outline="red")
                else:
                    d.rectangle((q1,lines_heights[i]-box1_height,q2,lines_heights[i+4]+box1_height),outline="red")
            #except:
                #print("I had an error when trying the 'if' with the values",lines_heights[i]-8*box1_height,lines_heights[i+4]+8*box1_height,q2)
            q2=q2+1
print(width,height)

img.show()
