#frame sorting
import random

class Frame:
    def __init__ (self,num,data=None):
        self.num=num
        self.data=data

def bubsort(data):
    flag=0
    for i in range (len(data)):
        for j in range (len(data)-i-1):
            if data[j].num > data[j+1].num:
                flag=1
                temp=data[j]
                data[j]=data[j+1]
                data[j+1]=temp
        if flag==0:
            break
        else:
            flag=0
            
n=int(input("Enter the number of frames: "))

seqlist=[]
for _ in range(n):
    x=random.randrange(1,n*1000)
    while x in seqlist:
        x=random.randrange(1,n*1000)
    seqlist.append(x)

frames=[]
for i in seqlist:
    frames.append(Frame(i))

for frame in frames:
    frame.data=int(input(f'Input data for frame number {frame.num}:'))

bubsort(frames)

for frame in frames:
    print(f'Frame number {frame.num}, Frame data {frame.data}')
