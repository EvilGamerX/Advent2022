def day06():        
    with open('./Day06/input.txt') as f:
        line = f.readline()      
        i = 4
        while i < len(line):
            marker = set(line[i - 4: i])            
            if len(marker) == 4:
                break
            i += 1
    
    print(f"The first character is at index {i}")

    with open('./Day06/input.txt') as f:
        line = f.readline()           
        i = 14
        while i < len(line):
            marker = set(line[i - 14: i])            
            if len(marker) == 14:
                break
            i += 1
    
    print(f"The first character is at index {i}")
                