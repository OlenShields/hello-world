#median
def median(list):
    numbers = len(list)
    if numbers == 0:
        return 0
    else:
        list.sort()
        midOne = numbers//2
        if numbers%2 == 0:
            return (list[midOne]+list[midOne-1])/2
        else:
            return list[midOne]
#mean
def mean(list):
    numbers = len(list)
    sum = 0 
    if numbers == 0:
        return 0
    else:
        for num in list:
            sum += num
        return sum/numbers

#mode
def mode(list):
    count = {}
    highestNum = 0
    for i in list:
        if i in count.keys():
            count[i] += 1
        else:
            count[i] = 1
    for i in count.keys():
        if count[i] > highestNum:
            highestNum = count[i]
            nummode = i
    return nummode
#I am sorry but I had no idea what the book meant by section 5.4 I found figure 5-4 which was a hex binary table I assumed did not apply to this question
def main():
    print("The mean of [1, 2, 3, 4, 5] is: ", mean(list(range(1, 5))))
    print("The mode of [1, 2, 3, 4, 5] is:", mode([1, 2, 3, 4, 5]))
    print("The median of [1, 2, 3, 4, 5] is:", median([1, 2, 3, 4, 5]))
main()
