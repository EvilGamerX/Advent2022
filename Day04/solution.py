def day04():
    with open('./Day04/input.txt') as f:
        total = 0
        for line in f:         
            numbers = line.strip().split(",")
            firstNums = numbers[0].split('-') 
            secondNums = numbers[1].split('-') 
            firstNums = set(range(int(firstNums[0]), int(firstNums[1]) + 1)) # need to add 1 because it goes to n-1 on the range
            secondNums = set(range(int(secondNums[0]), int(secondNums[1]) + 1))
            if (firstNums.issubset(secondNums) or secondNums.issubset(firstNums)):
                total += 1


    print(f'The answer for the complete overlap is: {total}')

    with open('./Day04/input.txt') as f:
        total = 0
        for line in f:         
            numbers = line.strip().split(",")
            firstNums = numbers[0].split('-') 
            secondNums = numbers[1].split('-') 
            firstNums = set(range(int(firstNums[0]), int(firstNums[1]) + 1))
            secondNums = set(range(int(secondNums[0]), int(secondNums[1]) + 1))
            if (firstNums.intersection(secondNums) or secondNums.intersection(firstNums)):
                total += 1


    print(f'The answer for the general overlap is: {total}')
    