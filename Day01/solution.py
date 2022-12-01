def day01():
    with open('./Day01/input.txt') as f:
        current = 0
        max = 0
        for line in f:            
            if line not in ['\n', '\r\n']:
                current += int(line)
            elif current > max:
                max = current
                current = 0
            else:
                current = 0
        if current > max:
            max = current

    print(f'The answer for the max calories is: {max}')

    with open('./Day01/input.txt') as f:
        current = 0
        max1 = 0
        max2 = 0
        max3 = 0
        for line in f:            
            if line not in ['\n', '\r\n']:
                current += int(line)
            else:
                if current > max1: 
                    tmp = max1               
                    max1 = current
                    current = tmp
                if current > max2:
                    tmp = max2
                    max2 = current
                    current = tmp
                if current > max3:
                    max3 = current
                print(f'{max1} | {max2} | {max3}')
                current = 0
            
        if current > max1:                
            max1 = current
            current = max1
        if current > max2:
            max2 = current
            current = max2
        if current > max3:
            max3 = current
        
        print(f'{max1} | {max2} | {max3}')

        print(f'The answer for the top three max calories is: {max1 + max2 + max3}')
    