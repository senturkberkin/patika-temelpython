input= [[1, 2], [3, 4], [5, 6, 7]]
def terso(x):
    output=[]
    a= list(reversed(x))
    for i in a:
        output.append(list(reversed(i)))
    return output
print(terso(input))
