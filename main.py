# contact class
class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


# node for linked list
class Node:
    def __init__(self, contact):
        self.contact = contact
        self.prev = None
        self.next = None


# doubly linked list
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, contact):
        node = Node(contact)

        if self.head == None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def show_forward(self):
        cur = self.head
        while cur:
            print(cur.contact.name, "-", cur.contact.phone)
            cur = cur.next

    def show_backward(self):
        cur = self.tail
        while cur:
            print(cur.contact.name, "-", cur.contact.phone)
            cur = cur.prev


# simple substring check
def match(name, key):
    return key.lower() in name.lower()


# data storage
contacts = DoublyLinkedList()
table = {}   # hash table


def add_contact():
    name = input("Name: ")
    phone = input("Phone: ")

    c = Contact(name, phone)

    contacts.add(c)
    table[name] = c

    print("added")


def search_keyword():
    key = input("keyword: ")
    cur = contacts.head
    found = False

    while cur:
        if match(cur.contact.name, key):
            print(cur.contact.name, "-", cur.contact.phone)
            found = True
        cur = cur.next

    if not found:
        print("no result")


def search_name():
    name = input("name: ")

    if name in table:
        c = table[name]
        print(c.name, "-", c.phone)
    else:
        print("not found")


def menu():
    while True:
        print("\n1 add")
        print("2 search keyword")
        print("3 search name")
        print("4 show forward")
        print("5 show backward")
        print("6 exit")

        ch = input("choice: ")

        if ch == "1":
            add_contact()
        elif ch == "2":
            search_keyword()
        elif ch == "3":
            search_name()
        elif ch == "4":
            contacts.show_forward()
        elif ch == "5":
            contacts.show_backward()
        elif ch == "6":
            break
        else:
            print("wrong choice")


menu()