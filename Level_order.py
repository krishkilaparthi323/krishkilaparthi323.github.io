class Node:
    def __init__(self,key):
        self.left=None
        self.right=None
        self.data=key
    def Level_order(self,root):
        if root is  None:
            return
        q=[]
        q.append(root)
        while len(q) is not 0:
            element = q.pop(0)
            print(element.data)
            if element.left is not None:
                q.append(element.left)
            if element.right is not None:
                q.append(element.right)

root=Node(10)
root.left=Node(20)
root.right=Node(30)
root.left.left=Node(40)
root.right.right=Node(50)
root.Level_order(root)


