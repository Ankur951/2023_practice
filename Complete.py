Name = input("Plies inter name=")


def Complete(string):
    string = string.split(" ")
    for i in range(len(string)):
        if string[i][0].islower():
            string[i] = string[i].replace(string[i][0], string[i][0].upper(), 1)

    string = " ".join(string)

    print(string)


Complete(Name)
