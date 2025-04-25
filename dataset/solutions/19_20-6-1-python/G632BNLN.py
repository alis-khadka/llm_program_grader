def editDistance(a, b):
    if len(a)==0:
        return(len(b))
    if len(b)==0:
        return(len(a))
    ed=[[None for i in range(len(b)+1)] for j in range(len(a)+1)]
    for i in range(len(a)+1):
        for j in range(len(b)+1):
            if a[i-1]==b[j-1]:
                x=0
            else:
                x=1
            if i==0:
                ed[i][j]=j
            elif j==0:
                ed[i][j]=i
            else:
                ed[i][j]=min(ed[i-1][j]+1,ed[i][j-1]+1,ed[i-1][j-1]+x)
    return ed[len(a)][len(b)]