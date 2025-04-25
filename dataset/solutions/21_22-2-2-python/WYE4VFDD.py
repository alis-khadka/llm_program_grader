def calc(a,b):
    part_sum = [0]
    for i, x in enumerate(a):
        part_sum.append(part_sum[i] + x)
    work = []
    for days in b:
        work.append(part_sum[days[1] + 1] - part_sum[days[0]])
    return work