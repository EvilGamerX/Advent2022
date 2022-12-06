def day05():
    towers = [['S','C','V','N'],
            ['Z','M','J','H','N','S'],
            ['M','C','T','G','J','N','D'],
            ['T','D','F','J','W','R','M'],
            ['P','F','H'],
            ['C','T','Z','H','J'],
            ['D','P','R','Q','F','S','L','Z'],
            ['C','S','L','H','D','F','P','W'],
            ['D','S','M','P','F','N','G','Z']]
        
    with open('./Day05/input.txt') as f:
        for line in f:         
            splits = line.strip().split(" ")
            i = 0
            while i < int(splits[1]):
                towers[int(splits[5]) - 1].append(towers[int(splits[3]) - 1].pop())
                i += 1

    ret = ""
    for tower in towers:
        ret += tower.pop()

    print(f'The answer for the message is: {ret}')

    towers = [['S','C','V','N'],
            ['Z','M','J','H','N','S'],
            ['M','C','T','G','J','N','D'],
            ['T','D','F','J','W','R','M'],
            ['P','F','H'],
            ['C','T','Z','H','J'],
            ['D','P','R','Q','F','S','L','Z'],
            ['C','S','L','H','D','F','P','W'],
            ['D','S','M','P','F','N','G','Z']]
        
    with open('./Day05/input.txt') as f:
        for line in f:         
            splits = line.strip().split(" ")
            i = int(splits[1])
            end = towers[int(splits[3]) - 1][-i:]
            front = towers[int(splits[3]) - 1][:-i]
            towers[int(splits[5]) - 1] += end
            towers[int(splits[3]) - 1] = front

    ret = ""
    for tower in towers:
        ret += tower[-1]

    print(f'The answer for the message is: {ret}')
    