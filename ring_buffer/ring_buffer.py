class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.index = 0
        self.list = []

    def append(self, item):
        if self.capacity > 0:                           # If list not empty
            self.list.insert(self.index, item)          # insert new item into list @ index
            if len(self.list) > self.index+1:           # if we are replacing an item
                self.list.pop(self.index+1)             # pop it from the list @ index+1 since it has been bumped over by the insert()
            self.index = (self.index+1) % self.capacity # one-liner to increment or reset self.index

    def get(self):
        return self.list
