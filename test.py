def printBox(symbol, height, width):
    if len(symbol) != 1:
        raise Exception("symbol must be 1 character")
    
    if (height < 2) or (width < 2):
        raise Exception("Height or width cannot be less than 2.")

    print (symbol * width)
    for i in range(height-2):
        print(symbol + (' ' * (width -2)) + symbol)
    print (symbol * width)

printBox("*", 5, 6)
printBox("#", 2, 3)
printBox("$", 2, 1)