# helps with readibility | order of arguments doesn't matter

def hello(greeting, title, first, last):
    print(f"{greeting} {title} {first} {last}")


# positional arguments placed before keywprd arguments
hello('Hello', last='rube', first='farah', title='Ms')
# hello Ms farah rube
