filename = input('Enter file name: ')
text = []
with open(filename, 'r') as f:
    for line in f:
        text.append(line.strip())

while True:
    print("The file has", len(text), "lines.")
    if len(text) == 0:
        break
    lineNumber = int(input("Enter a line number [0 to quit]: "))
    if lineNumber == 0:
        break
    elif lineNumber > len(text):
        print("ERROR: line number must be less than or equal to", len(text))
    else:
        print(lineNumber, ": ", text[lineNumber - 1])
