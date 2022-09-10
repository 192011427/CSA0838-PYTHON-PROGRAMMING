sk= []
n = int(input("Enter the list size "))
for i in range(0, n):
    print("Enter  the element")
    item = int(input())
    sk.append(item)
g=[]
h=[]
for i in sk:
	if i%2==0:
		g.append(i*i)
	else:
		h.append(i*i)		
print(sum(h),sum(g))
