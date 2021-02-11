import csv
from collections import Counter
with open("SOCR-HeightWeight.csv",newline="") as d:
    r=csv.reader(d)
    data=list(r)
data.pop(0)
newData=[]
for i in range(len(data)):
    n=data[i][2] #Here 2 stands for the third row
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
    "75-85":0,
    "85-95":0,
    "95-105":0,
    "105-115":0,
    "115-125":0,
    "125-135":0,
    "135-145":0,
    "145-155":0,
    "155-165":0,
    "165-175":0,
}
for w,o in d.items():
    if 75<float(w)<85:
        rangeForMode["75-85"]+=o
    elif 85<float(w)<95:
        rangeForMode["85-95"]+=o
    elif 95<float(w)<105:
        rangeForMode["95-105"]+=o
    elif 105<float(w)<115:
        rangeForMode["105-115"]+=o
    elif 115<float(w)<125:
        rangeForMode["115-125"]+=o
    elif 125<float(w)<135:
        rangeForMode["125-135"]+=o
    elif 135<float(w)<145:
        rangeForMode["135-145"]+=o
    elif 145<float(w)<155:
        rangeForMode["145-155"]+=o
    elif 155<float(w)<165:
        rangeForMode["155-165"]+=o
    elif 165<float(w)<175:
        rangeForMode["165-175"]+=o

modeRange,modeOcc=0,0
for range,occ in rangeForMode.items():
    if occ>modeOcc:
        modeRange=[int(range.split("-")[0]),int(range.split("-")[1])]
        modeOcc=occ
mode=float((modeRange[0]+modeRange[1])/2)
print("Mode= ")
print(mode)



