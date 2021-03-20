def splitter(l,f):
    return 10**(l-int(f)-1)

def summer(N,l):
    a=0
    f=-1
    while True:
        f = N.find('4',f+1)
        if f==-1:
            break
        a+=splitter(l,f)
    return a

t = int(input())

for i in range(t):
    N = str(input())
    l = len(N)
    a = summer(N,l)
    print(f'Case #{i+1}: {int(N)-a} {a}')

# I am not actively thinking about how the algorithm would not work.
