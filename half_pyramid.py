def half_pyramid_right(number):
    for item in range(number):
        print("*" * (item + 1))


def half_pyramid_left(number):
    # for item in range(number):

    for ritem in range(number, 0, -1):
        sitem = number - ritem
        print(" " * (ritem - 1), "*" * (sitem + 1))


def pyramid(number):
    # for item in range(number):

    for ritem in range(number, 0, -1):
        item = number - ritem
        no_of_space = ritem - 1
        no_of_star = ((item + 1) * 2) - 1
        # print(" "*(ritem-1),"*"*(item+1),"*"*item)
        # print(" " * (ritem - 1), "*" * ((((item + 1))*2)-1))
        print("{}{}".format(" " * no_of_space, "*" * no_of_star))


number = 10

# half_pyramid_right(number)
# half_pyramid_left(number)
pyramid(number)
