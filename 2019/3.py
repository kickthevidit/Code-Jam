from sys import stdin
from fractions import Fraction

def indtochr(ind):
    return chr(65+ind)

T = int(input())

for case in range(T):
    N,L = map(int,stdin.readline().strip().split())

    ct = stdin.readline().strip().split()

    primel=set()
    fracl=[]
    for i in range(L-1):
        frac = tuple(map(int,str(Fraction(ct[i]+'/'+ct[i+1])).split('/')))
        fracl.append(frac)
        for pr in frac:
            if pr not in primel:
                primel.add(pr)
    primel = sorted(list(primel))

    ans = indtochr(primel.index(fracl[0][0])) + indtochr(primel.index(fracl[1][0]))

    for prs in fracl:
        ans+=indtochr(primel.index(prs[1]))

    print(f"Case #{case+1}: {ans}")

exit()
