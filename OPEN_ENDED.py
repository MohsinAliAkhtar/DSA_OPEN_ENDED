class Node:
    def __init__(self,data):
        self.data = data
        self.next = None


class Linked_List:
    def __init__(self):
        self.head = None

    #Append a node to the linked list.
    
    def Append(self,data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


    #Display the Linked List.

    def Display(self):
        current = self.head
        result = []
        while current:
            result.append(str(current.data))
            current = current.next
        print(result)


    #Delete N Nodes After Skipping M Nodes.

    def Delete_N_After_M(self, M, N):
        current = self.head
        while current:
            # Skip M nodes
            for _ in range(M - 1):
                if current is None:
                    return
                current = current.next

            if current is None:
                return

            # Start deleting n nodes
            temp = current.next
            for _ in range(N):
                if temp is None:
                    break
                temp = temp.next

            current.next = temp
            current = temp



# Create a Linked List
linklist = Linked_List()
for value in [9, 1, 3, 5, 9, 4, 10, 1]:
    linklist.Append(value)

print("Original Linked List:")
linklist.Display()

# Delete n nodes after skipping m nodes
m = 2
n = 1
linklist.Delete_N_After_M(m, n)

print("\nModified Linked List:")
linklist.Display()




