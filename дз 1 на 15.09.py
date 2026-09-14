import numpy as np
from numpy.typing import NDArray


class deque:
    def __init__(self, arraySize: int) -> None:
        self.myArray: NDArray[np.int32] = np.empty(arraySize, dtype=np.int32)

        self.capacity = arraySize
        self.size = 0
        self.head = 0
        self.tail = 0

    def accessByIndex(self, index: np.int32) -> np.int32:
        if index < 0 or index >= self.size:
            raise IndexError("Индекс выходит за границы deque")

        real_index = (self.head + index) % self.capacity

        return self.myArray[real_index]

    def addToTail(self, num: np.int32) -> np.int32:
        if self.size == self.capacity:
            raise OverflowError("Deque заполнена")

        self.myArray[self.tail] = num

        self.tail = (self.tail + 1) % self.capacity
        self.size += 1

        return num

    def addToHead(self, num: np.int32) -> np.int32:
        if self.size == self.capacity:
            raise OverflowError("Deque заполнена")

        self.head = (self.head - 1) % self.capacity

        self.myArray[self.head] = num

        self.size += 1

        return num

d = deque(5)

d.addToTail(np.int32(1))
d.addToTail(np.int32(2))
d.addToTail(np.int32(3))

d.addToHead(np.int32(4))

print(d.accessByIndex(np.int32(0)))  
print(d.accessByIndex(np.int32(1)))  
print(d.accessByIndex(np.int32(2)))  
print(d.accessByIndex(np.int32(3)))  
