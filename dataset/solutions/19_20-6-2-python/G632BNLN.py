def knapSack(value, volume, capacity):
    c=capacity
    assert len(value) == len(volume)
    for x in volume:
        assert x == round(x)
    rel=[]
    for i in range(len(value)):
        if volume[i]==0:
            rel.append((value[i],i))
        else:    
            rel.append(((value[i]/volume[i]),i))
        if rel[i-1][0]==rel[i][0]:
            if value[rel[i][1]]>value[rel[i-1][1]]:
                temp=rel[i-1]
                rel[i-1]=rel[i]
                rel[i]=temp
    rel=sorted(rel,key=lambda x:x[0],reverse=True)
    rel=sorted(rel,key=lambda x:value[x[1]],reverse=True)
    v=0
    for i in range(len(rel)):
        if c-volume[rel[i][1]]>=0:
            c=c-volume[rel[i][1]]
            v+=value[rel[i][1]]
    return v