class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def getNext(self):
        return self.next
    def setData(self,newdata):
        self.data = newdata
    def setNext(self,newnext):
        self.next = newnext
class UnorderedList:
    def __init__(self):
        self.head = None
    def printNode(self):
        current = self.head
        print('List contains : ',end = '')
        while current != None:
            print(current.getData(),end=' ')
            current = current.getNext()
    def isEmpty(self):
        if self.head == None :
            return True
        else :
            return False
    def add(self,item):
        tmp = Node(item)
        if self.head == None :
            self.head = tmp
        else :
            tmp.setNext(self.head)
            self.head = tmp
    def size(self): 
        cur =self.head
        count = 0
        while cur != Node:
            count = count + 1
            cur =cur.getNext()
        return count
    def search(self,item):
        cur = self.head
        found = False
        while cur != None and not found:
         if cur.getData() == item:
            found = True
        else:
            cur = cur.getNext()
        return found
    def remove(self, item):
        cur = self.head
        previous = None
        while True:
            if cur.value == item:
                break
            previous, cur = cur, cur.next
        if previous is None:
            self.head = cur.next
        else:
            previous.next = cur.next
    def append(self,item):
        temp = Node(item)
        if self.head == Node:
            self.head = temp
        else:
            cur = self.head
            while cur.getNext() != None:
                cur = cur.getNext()
            cur.setNext(temp)
    def index(self,item):
        pos = 0
        cur = self.head
        found = False
        while cur is not None and not found:
            if cur.getData() == item:
                found = True
            else:
                cur = cur.getNext()
                pos += 1
        if not found:
            raise ValueError('Value not present in the List')
        return pos
    def insert(self, item, pos):
            ind = 0
            temp = Node(item)
            previous = None
            current = self.head
            if pos == 0:
                temp.setNext(self.head)
                self.head = temp
            else:
                while ind < pos:
                    ind += 1
                    previous = current
                    current = current.getNext()
                temp.setNext(current)
                previous.setNext(temp)