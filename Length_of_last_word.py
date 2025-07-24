def builtin(s):
    #requires extra space cuz split()
    st = s.split(" ")

    # print(st)
    return len(st[-1])


def iteration(s):
    # start from last character in a string, reverse loop
    i = len(s) - 1
    length = 0

    while s[i] == ' ':
        i = i - 1
    while i >= 0 and s[i] != ' ':
        length = length + 1
        i = i - 1
    return length


s = 'Joey doesnt share food'
print(builtin(s))
print(iteration(s))