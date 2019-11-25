class Node:
    def __init__(self,new_data):
        self.data=new_data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def PrintNthNode(self,n):
        temp=self.head
        length=0
        while temp is not None:
            temp=temp.next
            length+=1
        if n>length:
            print('Location is greater than the' +'length of LinkedList')
            return
        temp=self.head
        for i in range(0,length-n):
            temp=temp.next
        print(temp.data)
Llist=LinkedList()
Llist.push(20)
Llist.push(3)
Llist.push(15)
Llist.push(35)
Llist.PrintNthNode(4)



