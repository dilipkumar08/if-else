m,n=map(int,input().split())
li1=list(map(int,input().split()))
li1.sort()
li2=list(map(int,input().split()))
li2.sort(reverse=True)
print(*li1,*li2)
