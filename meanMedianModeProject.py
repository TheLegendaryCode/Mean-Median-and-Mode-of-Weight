import csv
from collections import Counter
with open("SOCR-HeightWeight.csv",newline="") as d:
    r=csv.reader(d)
    data=list(r)
data.pop(0)
newData=[]
for i in range(len(data)):
    n=data[i][2]
    newData.append(float(n))
num=len(newData)

#mean

total=0
for x in newData:
    total+=x
mean=total/num
print("Mean= ")
print(mean)

#median

newData.sort()
if num%2==0:
    m1=float(newData[num//2])
    m2=float(newData[num//2-1])
    median=(m1+m2)/2
else :
    median=newData[num//2]
print("Median= ")
print(median)

#mode

d=Counter(newData)
rangeForMode={
    "50-60":0,
    "60-70":0,
    "70-80":0
}
for h,o in d.items():
    if 50<float(h)<60:
        rangeForMode["50-60"]+=o
    elif 60<float(h)<70:
        rangeForMode["60-70"]+=o
    elif 70<float(h)<80:
        rangeForMode["70-80"]+=o
modeRange,modeOcc=0,0
for range,occ in rangeForMode.items():
    if occ>modeOcc:
        modeRange=[int(range.split("-")[0]),int(range.split("-")[1])]
        modeOcc=occ
mode=float((modeRange[0]+modeRange[1])/2)
print("Mode= ")
print(mode)



