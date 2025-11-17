# # nested loop : loop (inner) within a loop (outer)
# outer loop :
#     inner loop :

for i in range(1, 10):
    print(i, end="")  # 123456789

for x in ('a', 'b', 'c'):
    for y in range(5):
        print(x, y)

# Print rectangle
rows = int(input("Enter the num of rows: "))
cols = int(input("Enter the num of columns: "))
symbol = input("Enter a symbol to use: ")

for x in range(rows):
    for y in range(cols):
        print(symbol, end="")
    print()
