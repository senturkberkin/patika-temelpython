input=[[1,'a',['cat'],2],[[[3]],'dog'],4,5]

def flat(x):
    for i in x:
        if type(i) is list:
            for deger in flat(i):
                yield deger
        else:
            yield i
    
print(list(flat(input)))
