def calc(A: list, B: list) -> str:
    count_of_a_elements = {}

    for element in A:
        if element in count_of_a_elements:
            count_of_a_elements[element] += 1
        else:
            count_of_a_elements[element] = 1

    result = ""

    for b_idx, element in enumerate(B):
        if b_idx in count_of_a_elements:
            if count_of_a_elements[b_idx] > element:
                result += "0"
            else:
                result += "1"
        else:
            result += "1"
    return result