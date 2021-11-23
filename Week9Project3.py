def main():
    fname = input("Enter the name of your .txt file: ")
    total =  0
    count = 0
    with open(fname, 'r') as f:
        for line in f:
            for num in line.strip().split():
                total += float(num)
                count += 1
    print("\nThe average is: " + str(total / count))

main()
