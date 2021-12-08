ran = [
    [1,2,3,4,5],
    [11,22,33,44,55],
    [x for x in range(11,16)]
]

# mean = lambda list : sum(list)/len(list)

def mean(list):
    return sum(list)/len(list)

avg = list(map(mean,ran))

print(avg)