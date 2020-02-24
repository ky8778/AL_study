#분해합
N=int(input())
nlist = list(map(int,str(N)))
lenN=len(str(N))
alist=[]
anw= True
n=lenN-1

while True:
    if N <=18 and n == 0:
        if N%2==0:
            alist.append(N//2)
            break
        else:
            anw=False
            break
    else:
        if n == lenN - 1:
            a = nlist[lenN-1-n]
        else:
            a = 9
        while True:
            R = N-(10**n +1)*a
            if R<0:
                a-=1
            else:
                temp=0
                for t in range(n):
                    temp += 9*(10**t +1)
                if R<=temp:
                    a-=1
                else:
                    alist.append(a+1)
                    N -= (10**n +1)*(a+1)
                    n = n-1
                    break
            
if anw:
    alist=map(str, alist)
    anw = ''.join(alist)
    print(anw.lstrip('0'))
    #print(anw)
else:
    print("0")