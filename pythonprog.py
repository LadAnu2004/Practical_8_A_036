symbol = input("Enter symbol: ")
rows = int(input("Enter number of rows: "))

print("\nReverse Pattern:\n")
for i in range(rows, 0, -1):
    print((symbol + " ") * i)

print("\nFull Pyramid:\n")
for i in range(1, rows + 1):
    print(" " * (rows - i) + (symbol + " ") * i)