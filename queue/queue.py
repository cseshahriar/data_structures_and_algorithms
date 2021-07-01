""" Queue FIFO """
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        """ add item """
        self.items.append(item)

    def dequeue(self):
        """ remove first item """
        return self.items.pop(0) # first item

    def is_empty(self):
        """ check if queue is empty """
        if self.items == []:
            return True
        return False

if __name__ == '__main__':
    q = Queue()
    q.enqueue("Tahmid")
    q.enqueue("Rafi")
    q.enqueue("Tamim")

    while not q.is_empty():
        person = q.dequeue()
        print("out ", person)
