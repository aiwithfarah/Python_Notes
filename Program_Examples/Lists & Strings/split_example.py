# Your task is to write your own function, which behaves almost exactly like the original split() method, i.e.:

# it should accept exactly one argument – a string;
# it should return a list of words created from the string, divided in the places where the string contains whitespaces;
# if the string is empty, the function should return an empty list;
# its name should be mysplit()

def mysplit(str1):

    lst = []
    word = ""

    if str1 == " ":
        return lst
    else:
        for ch in str1:
            if ch != " ":
                word += ch
            else:
                if word != "":
                    lst.append(word)
                    word = ""

        if word != "":
            lst.append(word)
    return lst


x = mysplit("To be or not to be, that is the question")
print(x)
