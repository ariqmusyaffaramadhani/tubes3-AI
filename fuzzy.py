import csv
import numpy

def readCSV():
    big_array = []
    with open('/home/ariq/Documents/AI/tubes3-AI/influencers.csv', 'r') as dat:
        data = csv.reader(dat)
        idx = 0
        for row in data:
            if idx != 0:
                big_array.append([int(row[0]),int(row[1]),float(row[2])])
            idx += 1
    return big_array

def fol_acceptence(dat):
    # -------------------high--------------------------

    if dat > 60000 :
        h = 1
    elif dat <=51000:
        h = 0
    elif (dat > 51000) and (dat <=60000):
        x = dat - 51000
        y = 60000 - 51000
        h = x/y

    # -------------------avg--------------------------

    if dat > 30000 :
        a = 1
    elif dat <=21000:
        a = 0
    elif (dat > 21000) and (dat <=30000):
        x = dat - 21000
        y = 30000 - 21000
        a = x/y

    # -------------------low--------------------------
    if dat > 5000 :
        l = 1
    elif dat <=2000:
        l = 0
    elif (dat > 2000) and (dat <=5000):
        x = dat - 2000
        y = 5000 - 2000
        l = x/y


    return [h,a,l]

def eng_acceptence(dat):
    # -------------------high--------------------------

    if dat > 10 :
        h = 1
    elif dat <=7:
        h = 0
    elif (dat > 7) and (dat <=10):
        x = dat - 7
        y = 10 - 7
        h = x/y

    # -------------------avg--------------------------

    if dat > 6 :
        a = 1
    elif dat <=4:
        a = 0
    elif (dat > 4) and (dat <=6):
        x = dat - 4
        y = 6 - 4
        a = x/y

    # -------------------low--------------------------
    if dat > 3 :
        l = 1
    elif dat <=0.5:
        l = 0
    elif (dat > 0.5) and (dat <=3):
        x = dat - 0.5
        y = 3 - 0.5
        l = x/y


    return [h,a,l]

def inference_prop(fol,eng):
    prop1 = min(fol[0],eng[0])
    prop2 = min(fol[0],eng[1])
    prop3 = min(fol[1],eng[0])
    inf = max([prop1,prop2,prop3])
    return inf 

def inference_so(fol,eng):
    so1 = min(fol[1],eng[1])
    so2 = min(fol[2],eng[1])
    so3 = min(fol[2],eng[0])
    inf = max([so1,so2,so3])
    return inf

def inference_meh(fol,eng):
    meh1 = min(fol[0],eng[2])
    meh2 = min(fol[1],eng[2])
    meh3 = min(fol[2],eng[2])
    inf = max([meh1,meh2,meh3])
    return inf

def defuzzyfication(prop,so,meh):
    x = (prop*100) + (so*60) + (meh*30)
    y = prop + so + meh
    return x/(y+0.00000000000000001)



def mergefunc(data):
    fac = fol_acceptence(data[1])
    engac = eng_acceptence(data[2])
    prop = inference_prop(fac,engac)
    so = inference_so(fac,engac)
    meh = inference_meh(fac,engac)
    defuz = defuzzyfication(prop,so,meh)
    return defuz



def catch_defuz(data):
    arr_defuz = []
    for i in data :
        x = mergefunc(i)
        arr_defuz.append(x)
    return arr_defuz    

def printdat(data,defz):
    for i in range(len(data)) :
        print("ini data ke ",i+1, " = ",data[i])
        print("defuz = ", defz[i])
        print("------------------------------------------")
        print()

def reversearray(x):
    revs = []
    for i in reversed(x):
        revs.append(i)
    return revs

def top_twenty(defz):
    arr =  sorted(range(len(defz)), key=lambda k: defz[k])
    arr2 = reversearray(arr)[:20]

    for i in range(len(arr2)):
        arr2[i]+=1
    
    return arr2


def savetocsv(toptwenty):
    with open('chosen.csv','w') as file:
        writer = csv.writer(file, lineterminator='\n')
        for i in toptwenty:
            writer.writerow([i])

# -------------------------------------------------------------MAIN PROGRAM-------------------------------------------------------------

data = readCSV()
defz = catch_defuz(data)

print (defz)
printdat(data,defz)
srt = top_twenty(defz)
print ("top twenty : ",srt)
savetocsv(srt)