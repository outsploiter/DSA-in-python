def pattern_1(n):
    for row in range(0, n):
        for col in range(0, n):
            print("*", end="")
        print()
    pass

def pattern_2(n):
    for row in range(0, n):
        for col in range(0, row+1):  # col = 0; col<row+1; col++
            print("*", end="")
        print()
    pass

def pattern_3(n):
    for row in range(0, n):
        for col in range(0, n-row):  # col = 0; col<n-row; col++
            print(col+1, end="")
        print()
    pass


pattern_3(5)