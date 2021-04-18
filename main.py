# cook your dish here
def func(s):
    d={}
    cnt=0
    add=0
    for i in range(0,len(s)):
        if s[i] not in d.keys():
            d[s[i]]=1
        else:
            d[s[i]]+=1
    for val in d.values():
        if val==1:
            cnt=cnt+1
        else:
            add=add+(val//2)
            if(val%2==1):
                cnt+=1
    #print(cnt,"hi",add)
    if(cnt>add):
        print("NO")
    else:
        print("YES")
t=int(input())
for i in range(0,t):
    s=input()
    func(s)