def find_a_string(string, sub_string):
    count = 0
    for i in range(len(string)):
        s = string[i:i + len(sub_string)]
        if s == sub_string:
            count = count + 1

    print(count)


find_a_string("ABCDCDC", "CDC")

string = input("plies enter mane string=")
sub_string = input("plies enter sub string=")


def find_a_string_find(string, sub_string):
    print(string.find(sub_string))


find_a_string_find(string, sub_string)
