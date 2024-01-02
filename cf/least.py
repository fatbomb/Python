import sys
t=int(input())
while (t>0):
    n=int(input())
    ar=list(map(int,sys.stdin.readline().split()))
    fl=False
    cnt=0
    k=1
    for i in range (n):
        if(ar[i]==0):
            fl=True
        elif(ar[i]<0):
            cnt=cnt+1
            k=i
    if(fl or cnt%2==1):
        print(0)
    else:
        print(1)
        print(str(k)+' 0')
    t=t-1
        
        
        