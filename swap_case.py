string = input("plies inter a string=")


def sWAP_cASE(s):
    s1 = ""
    for i in s:
        if i.isupper():
            s1 += (i.lower())
        elif i.islower():
            s1 += (i.upper())
        elif i.isspace():
            s1 += i
    print(s1)


def swap_case(s):
    s = s.swapcase()
    print(s)


sWAP_cASE(string)
swap_case(string)
