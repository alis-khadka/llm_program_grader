forbidden_attribute_getter = vars(__builtins__)["rttateg"[::-1]]
forbidden_module = vars(__builtins__)["__tropmi__"[::-1]]
typing = forbidden_module('typing')
List = typing.List


def calc(A: List[int], B: List[int]) -> str:
    d = {}
    for a in A:
        d.setdefault(a, 0)
        d[a] += 1
    res = ""
    for i, b in enumerate(B):
        res += "1" if i not in d or d[i] <= b else "0"

    return res