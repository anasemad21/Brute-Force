#Problem 1

def Remove(L,dy):
    for i in range(len(dy)):
        if dy[i] in L:
            L.remove(dy[i])
    return L

def Check(L,dy):
    flag= False
    for i in range(len(dy)):
        if dy[i] in L:
            flag=True
        else:
            flag =False
            break
    return flag

def PartialDigest(L):
    Dx=[0]
    width=max(L)
    L.remove(width)
    #print("L:",L)
    Dx.append(width)
    #print("DX:",Dx)
    return Place(L,Dx,width)


def Place(L,Dx,width):
    Dy=[]
    DyI=[]
    if len(L)==0:
        #print("yes")
        return  Dx
    else:
        y=max(L)
        #print("y",y)
        for j in range(len(Dx)):
            Dy.append(abs(y-Dx[j]))
            DyI.append(abs(width-y-Dx[j]))
        #print("DY:",Dy)
        #print("DyI:",DyI)
        #for i in range(len(Dy)):
        if Check(L,Dy):
             #print("ah")
             Dx.append(y)
             #print("bDx:",Dx)
             Remove(L,Dy)
             #L.remove(Dy[i])
             Place(L, Dx,width)
             Remove(L, Dy)
             #Dx.remove(Dy[i])
             L.append(y)
        else:
             #print("ah")
             Dx.append(width-y)
             Remove(L, DyI)
            # L.remove(width--DyI[i])
             Place(L, Dx,width)
             Remove(L,DyI)
             #Dx.remove(width--DyI[i])
             L.append(width-y)
    return Dx
    #print("final:", Dx)


print(PartialDigest([2,2,3,3,4,5,6,7,8,10]))
#print(PartialDigest([1,1,1,2,2,3,3,3,4,4,5,5,6,6,6,9,9,10,11,12,15]))


#Problem 2

def partial_Digest_Brute_Force (listt):
    returned_list=[]
    counter_1=0

    while counter_1 != len(listt):
        counter_2 = counter_1+1
        while counter_2 !=len(listt):
            returned_list.append(abs(listt[counter_1]-listt[counter_2]))
            counter_2+=1
        counter_1+=1
    return returned_list



def Complete_Digest(listt):
    returned_list = []
    for i in range(1,len(listt)):
        returned_list.append(abs(listt[i]-listt[i-1]))
    return returned_list



print(partial_Digest_Brute_Force([0,2,4,7,10]))
print(Complete_Digest([0,2,4,7,10]))
