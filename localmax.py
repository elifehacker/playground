
def get_local_max(input):
    l = [input[x] for x in range(len(input)) if (x-1 >=0 and input[x] != input[x-1]) or x == 0]
    return [l[x] for x in range(len(l)) if l[x] == max(l[0 if x-1 <0 else x-1 : len(l) if x+2 > len(l) else x+2 ])]
