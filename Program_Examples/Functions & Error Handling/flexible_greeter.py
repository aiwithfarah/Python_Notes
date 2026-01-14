# Write a function greet(name, title="Mr./Ms.") (using a default parameter).

# Calling greet("Farah") should print: "Hello Mr./Ms. Farah".

# Calling greet("Farah", "CEO") should print: "Hello CEO Farah".

def greet(name, title="Mr/Mrs"):

    print(f'Hello {title} {name}')


x = greet("Farah")
y = greet('Farah', 'CEO')
