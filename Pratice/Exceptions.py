import sys
for integer in [3,4,"S"]:
    try:
        print(int(integer))
    except (RuntimeError, TypeError, NameError, SyntaxError):
        print("Entervalues error")
    except(ValueError):
        print("You did not enter an integer.")

class B(Exception):
    pass
class C(B):
    pass
class D(C):
    pass

for cls in [B,C,D]:
    try:
        raise cls()
    except B:
        print("B")
    except C:
        print("C")
    except D:
        print("D")


try:
    f = open("myfile.txt")
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OSError : {}".format(err))
except ValueError:
    print("Could not convert data to integer")
except:
    print("Unrecognised error", sys.exc_info()[0])
    raise

if type(3) != str:
    raise ValueError("Not an integer")

try:
    int("S")
except Exception as e:
    print(e)


#linked

class Node:
    def __init__(self, data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head = Node()

    def append(self, data):
        cur = self.head
        new_node = Node(data)
        while cur.next != None:
            cur = cur.next
        cur.next = new_node #this is where the magic happens - here you set the next

    def length(self):
        cur = self.head
        total = 0
        while cur.next != None:
            cur = cur.next
            total += 1
        return total

class Solution:
    def display(self, head):
        current = head
        while current:
            print(current.data, end=" ")
            current = current.next

    def insert(self, head, data):
        # Complete this method    def insert(self,head,data):
        current = head
        if head == None:
            head = Node(data)
        else:
            while current.next != None:
                current = current.next
            current.next = Node(data)
        return head

data = 2
mylist=Solution()
mylist.display(None)




