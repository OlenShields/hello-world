def printAll(seq):
    if seq: print("sequence:",seq)
    print(seq[0])
    printAll(seq[1:])
printAll("Olen Shields")
printAll((1,2,3,4,5))
printAll([1,2,3,4,5])
