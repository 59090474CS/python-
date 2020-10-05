def isEmpty (self):
    return self.head == None
def add(self,item):
    tmp = Node (item)
    tmp.setNext(self.head)
    self.head =tmp
def size(self):  
    cur =self.head
    count = 0 
    while cur != Node:
        count += 1
        cur = cur.getNext()
    return count
def search(self,time):
    cur = self.head
    found = False
    while  cur != None and not found:
        if cur.getData() == itme:
            found =True
        else:
            cur = cur.getNext()
    return found
def remove(self,item):
  cur = self.head
        pvs  = None
        while True:
            if cur.value == item:
                break
            pvs, cur = cur, cur.next
        if pvs is None:
            self.head = cur.next
        else:
            pvs.next = cur.next
def append(self, item):
    cur = self.head
    tmp = Node(item)
    while cur != None:
      cur = cur.getNext()  
    cur.setNext(temp)
def index(self,head):
    ind = 0
    cur =self.head
    found =False
    while not found:
        if cur.getData()==item:
            found = True
            return ind
        else:
            cur = cur.getNext()
            ind+=1
def insert(self,time,pos):
    ind = 0
    temp = Node(item)
    pvs = Node
    cur =self.head
    if pos == 0:
        tmp.setNext(self.head)
        self.head =tmp
    else:
        while ind < pos:
            ind += 1
            pvs = cur
            cur =cur.getNext()
        tmp.setNext(cur)
        pvs.setNext(tmp)
    
 
