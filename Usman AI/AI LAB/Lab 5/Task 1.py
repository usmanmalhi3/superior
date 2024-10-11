class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def dfs_with_stack(root):
    if not root:
        return
    
    stack = [root]
    
    while stack:
        node = stack.pop()
        print(node.value) 
        
       
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

dfs_with_stack(root)
