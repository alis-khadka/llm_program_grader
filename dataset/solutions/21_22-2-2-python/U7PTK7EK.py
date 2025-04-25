def calc(a, b):
    summed_list_a = []
    output_list = []

    for i in range(len(a)):
        if i == 0:
            summed_list_a.append(a[0])
        else:
            summed_list_a.append(summed_list_a[0 - 1] + a[i])

    for i in range(len(b)):

        l_i = b[i][0]
        r_i = b[i][1]

        if l_i == 0:
            output = summed_list_a[r_i]
        else:
            output = summed_list_a[r_i] - summed_list_a[l_i - 1]

        output_list.append(output)

    return output_list