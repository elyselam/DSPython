class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        cur = self.head
        #if has a head, then iterate through til the end of the list
        if self.head:
            while cur.next:
                cur = cur.next
            #set next for the end of the list to be the new_element
            cur.next = new_element
        else:
            #if no head, make head new_element
            self.head = new_element


