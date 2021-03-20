def Pch(P,i):
    if P[i]=='S':
        return 'E'
    return 'S'

def ansch(ans):
    if ans[-1]=='E':
        return 'S'
    return 'E'


T = int(input())

for lm in range(T):
    N = int(input())
    P = input()

    ly = {'E':0,'S':0} # Number of Easts and Souths Lydia Took
    me = {'E':0,'S':0} # Number of Easts and Souths that I have taken
    ans=''

    l = len(P)
    for i in range(l):
        if ly['E']==me['E'] and ly['S']==me['S']: # When both Lydia and my number of Easts and Souths are equal, our paths have intersected. Now, we should take the opposite turn of Lydia's Path
            n = Pch(P,i)
            ans+=n
            ly[P[i]]+=1
            me[ans[-1]]+=1
            continue
        n = ansch(ans)
        ans+=n
        ly[P[i]]+=1
        me[ans[-1]]+=1

    print(f'Case #{lm+1}: {ans}')
