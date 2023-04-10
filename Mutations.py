string = input("plies enter string=")
position = int(input("plies enter position="))
character = input("plies enter character=")


def mutate_string(word, index, char):
    string_list = list(word)
    string_list[index - 1] = char
    word = "".join(string_list)
    print(word)


mutate_string(string, position, character)
