class DynamicArray:
    
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.array = [None] * self.capacity

    def get(self, i: int) -> int:
        return self.array[i]

    def set(self, i: int, n: int) -> None:
        self.array[i] = n

    def pushback(self, n: int) -> None:
        if self.getSize() == self.getCapacity():
            self.resize()
        self.array[self.getSize()] = n

    def popback(self) -> int:
        index = 0
        popped = 0
        for i in self.array:
            if i == None:
                break
            index += 1
            
        popped = self.get(index - 1)
        self.array[index - 1] = None
        return popped
            

    def resize(self) -> None:
        oldCapacity = self.capacity
        self.capacity *= 2
        TempArray = self.array
        self.array = [None] * self.capacity
        self.array[:oldCapacity] = TempArray
        

    def getSize(self) -> int:
        count = 0
        for i in self.array:
            if i == None:
                break
            count += 1
        return count
    
    def getCapacity(self) -> int:
        return self.capacity