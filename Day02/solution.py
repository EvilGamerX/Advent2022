def day02():
    with open('./Day02/input.txt') as f:
        score = 0
        for line in f:         
            if line[2] == 'X': #You chose Rock
                score += 1
                if line[0] == 'C':
                    score += 6
                elif line[0] == 'A':
                    score += 3
            elif line[2] == 'Y': #You chose Paper
                score += 2
                if line[0] == 'A':
                    score += 6
                elif line[0] == 'B':
                    score += 3
            elif line[2] == 'Z': #You chose Scisors
                score += 3
                if line[0] == 'B':
                    score += 6
                elif line[0] == 'C':
                    score += 3


    print(f'The answer for the max score is: {score}')

    with open('./Day02/input.txt') as f:
        score = 0
        for line in f:         
            if line[2] == 'X': #You must lose
                score += 1
                if line[0] == 'A':
                    score += 2
                elif line[0] == 'C':
                    score += 1
            elif line[2] == 'Y': #You must draw
                score += 4
                if line[0] == 'C':
                    score += 2
                elif line[0] == 'B':
                    score += 1
            elif line[2] == 'Z': #You must win
                score += 7
                if line[0] == 'B':
                    score += 2
                elif line[0] == 'A':
                    score += 1

    print(f'The answer for the max score is: {score}')
    