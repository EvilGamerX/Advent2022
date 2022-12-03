def day03():
    with open('./Day03/input.txt') as f:
        total = 0
        for line in f:         
            length = len(line)
            slice1 = slice(0, length//2)
            slice2 = slice(length//2, length)
            shared = ord(''.join(set(line[slice1]).intersection(line[slice2])))
            if shared > 96:
                total += shared - 96
            else:
                total += shared - 38


    print(f'The answer for the priority is: {total}')

    with open('./Day03/input.txt', 'r') as f:
        total = 0
        lines = []
        for line in f:
            lines.append(line)
            if len(lines) >= 3:
                shared = ord((''.join((set(lines[0]).intersection(lines[1])).intersection(lines[2]))).strip())
                if shared > 96:
                    total += shared - 96
                else:
                    total += shared - 38
                lines = []

    print(f'The answer for the priority is: {total}')

    
    