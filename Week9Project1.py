def isSorted(nList):
    if len(nList) == 0 or len(nList) == 1:
        return True
    else:
        for index in range(len(nList) - 1):
            if nList[index] > nList[index + 1]:
                return False
def main():
        nList = []
        print(isSorted(nList))
        nList = [1]
        print(isSorted(nList))
        nList = list(range(10))
        print(isSorted(nList))
        nList[9] = 3
        print(isSorted(nList))
        
if __name__ == "__main__":
    main()
        
