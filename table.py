"""
dinamic way to creat a table for any number
"""


def print_table(table_for, loop):
    for item in range(loop):
        print("{0} * {1} = {2}".format(table_for, (item + 1), table_for * (item + 1)))


table_for = 15
loop = 20
print_table(table_for, loop)
