class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self, new_data):
        new_node = Node(new_data) # Create a new node
        new_node.next = self.head # Next for new node becomes the current head
        self.head = new_node # Head becomes the new node

    def printList(self):
        temp = self.head # Start from the head of the list
        while temp:
            print(temp.data, end=' ') # Print the data in the current node
            temp = temp.next # Move to the next node
        print() # Ensures the output ends with a new line

    def insertAtEnd(self, new_data):
        new_node = Node(new_data) # Create a new node
        if self.head is None:
            self.head = new_node # If the list is empty, make the new node the head
            return
        last = self.head
        while last.next: # Otherwise, traverse the list to find the last node
            last = last.next
        last.next = new_node

    def deleteFromBeginning(self):
        if self.head is None:
            return "The list is empty" # If the list is empty, return this string
        self.head = self.head.next

    def deleteFromEnd(self):
        if self.head is None:
            return "The list is empty"
        if self.head.next is None:
            self.head = None # If there's only one node, remove the head by making it None
            return
        temp = self.head
        while temp.next.next: # Otherwise, go to the second-last node
            temp = temp.next
        temp.next = None

    def search(self, value):
        current = self.head # Start with the head of the list
        position = 0 # Counter to keep track of the position
        while current: # Traverse the list
            if current.data == value: # Compare the list's data to the search value
                return f"Value '{value}' found at position {position}" # Print the value if a match is found
            current = current.next
            position += 1
        return f"Value '{value}' not found in the list"

if __name__ == '__main__':
    llist = LinkedList()

    # Insert words at the beginning
    llist.insertAtBeginning('fox')
    llist.insertAtBeginning('brown')
    llist.insertAtBeginning('quick')
    llist.insertAtBeginning('the')

    # Insert a word at the end
    llist.insertAtEnd('jumps')

    # Print the list before deletion
    print("List before deletion:")
    llist.printList()

    # Deleting nodes from beginning and end
    llist.deleteFromBeginning()
    llist.deleteFromEnd()

    # Print the list after deletion
    print("List after deletion:")
    llist.printList()
    
    # Search for 'quick' and 'lazy' in the list
    print(llist.search('quick')) # Expected to find
    print(llist.search('lazy')) # Expected to not find