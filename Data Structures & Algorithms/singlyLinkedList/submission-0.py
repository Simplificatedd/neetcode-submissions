class LinkedList:
    
    def __init__(self):
        self.linkedlist = []
    
    def get(self, index: int) -> int:
        count = 0
        for i in self.linkedlist:
            if index == count:
                return i
            count += 1
        return -1

    def insertHead(self, val: int) -> None:
        self.linkedlist.insert(0,val)

    def insertTail(self, val: int) -> None:
        self.linkedlist.append(val)

    def remove(self, index: int) -> bool:
        count = 0
        for i in self.linkedlist:
            if index == count:
                self.linkedlist.pop(index)
                return True
            count += 1
        return False

    def getValues(self) -> List[int]:
        return self.linkedlist
