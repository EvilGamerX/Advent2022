class Node:
    def __init__(self, name):
        self.name = name
        self.children = []
        self.parent = None
    
    def __init__(self, name, parent):
        self.name = name
        self.children = []
        self.parent = parent

    def get_sum(self) -> int:
        ret = 0
        for child in self.children:
            ret += child.get_sum()
        return ret

    def list(self):
        ret = 0
        if(self.get_sum() < 100000):
            ret += self.get_sum()
        #print(f"{self.name} (dir, size={self.get_sum()})")
        for child in self.children:
            ret += child.list()
        return ret

    def listOver(self, spaceToFree: int):
        ret = []
        #print(f"{self.name} (dir, size={self.get_sum()})")
        if(self.get_sum() > spaceToFree):
            ret.append(self.get_sum())
        for child in self.children:
            ret += child.listOver(spaceToFree)
        return ret

class Leaf:    
    def __init__(self, name, parent, value: int):
        self.name = name
        self.parent = parent
        self.value = value


    def get_sum(self) -> int:
        return self.value

    def list(self):
        return 0
        
    def listOver(self, spaceToFree: int):
        ret = []
        return ret

def day07():
    root = Node("superRoot", None)
    current = root
    with open('./Day07/input.txt') as f:
         for line in f:
            split = line.strip().split(" ")
            if(split[0] == "$"): #command
                if(split[1] == "cd"): #change directory
                    if(split[2] == ".."):
                        current = current.parent
                    else:
                        nw = Node(split[2], current)
                        current.children.append(nw)
                        current = nw
            elif (split[0] != "dir"): #size and file
                current.children.append(Leaf(split[1], current, int(split[0])))

    
    print(f"The total should be: {root.list()}")

    spaceToFree = 30000000 - (70000000 - root.get_sum())
    tmp = root.listOver(spaceToFree)
    small = tmp[0]
    for t in tmp:
        if(t < small):
            small = t

    print(f"The smallest directory to delete is this big: {small}")


