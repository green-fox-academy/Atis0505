class Counter(object):
    def __init__(self, number = 0):
        self.count_number = number

    def add(self, number = None):
        if number != None:
            self.count_number += number
        else:
            self.count_number +=1

    def get(self):
        return self.count_number
    
    def reset(self):
        self.__init__()