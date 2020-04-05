T=int(input())
N=int(input())
P=int(input())
a=[]
b=[]
c=0
for i in range(N):
    l=int(input())
    a.append(l)
for i in range(len(a)):
    b.append(a[i])
    c+=1
    if(c==P):
        break
    else:
        pass
sum=0
for i in range(0,len(b)):
    if(b[i]<=max(b)):
        sum=sum+(max(b)-b[i])
        
    else:
        sum=0
print(sum)
        
        
    
