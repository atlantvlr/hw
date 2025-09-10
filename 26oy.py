f=open("26_59852.txt")
s=list(map(int,f.readlines()))
n=s[0]
k=s[1]
d=s[2:n+2]
p=s[n+2:]
count=0
v=0
for i in range(n):
    for j in range(k):
        if d[i]<=p[j]:
            count+=1
            v=max(v, d[i])
            p[j]-=d[i]
            break
print(count,v)
