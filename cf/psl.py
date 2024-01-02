t=int(input())
while t>0:
    n=int(input())
    s=input()
    ar = [0] * 26

    for i in range(n):
        ar[ord(s[i])-ord('A')]+=1
    
    cnt = 0
    for i in range(26):
        if(ar[i]>i):
            cnt+=1
    print(cnt)
    t-=1
        