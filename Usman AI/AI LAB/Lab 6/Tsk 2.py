class Node:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

def bfs_with_queue(start):
    visited = set()
    queue = [start]  
    
    while queue:
        current_node = queue.pop(0)  
        if current_node.value not in visited:
            print(current_node.value)  
            visited.add(current_node.value)
            
           
            for neighbor in current_node.neighbors:
                if neighbor.value not in visited:
                    queue.append(neighbor)


node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)


node0.neighbors = [node1, node2]
node1.neighbors = [node0, node3, node4]
node2.neighbors = [node0, node5]
node3.neighbors = [node1]
node4.neighbors = [node1]
node5.neighbors = [node2]

bfs_with_queue(node0)
