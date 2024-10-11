class Node:
    def __init__(self, position):
        self.position = position
        self.g = 0  
        self.h = 0  
        self.f = 0  
        self.parent = None  

def heuristic(a, b):
   
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(start, goal, grid):
    open_list = []  
    closed_list = []  

    start_node = Node(start)
    goal_node = Node(goal)

    open_list.append(start_node)

    while open_list:
        
        current_node = min(open_list, key=lambda node: node.f)

        if current_node.position == goal_node.position:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  

        open_list.remove(current_node)
        closed_list.append(current_node)

        
        for new_position in [(0, 1), (1, 0), (0, -1), (-1, 0)]:  
            node_position = (current_node.position[0] + new_position[0], current_node.position[1] + new_position[1])

         
            if (0 <= node_position[0] < len(grid)) and (0 <= node_position[1] < len(grid[0])):
                
                if grid[node_position[0]][node_position[1]] != 1:  
                    new_node = Node(node_position)
                    if new_node in closed_list:
                        continue

                   
                    new_node.g = current_node.g + 1
                    new_node.h = heuristic(new_node.position, goal_node.position)
                    new_node.f = new_node.g + new_node.h
                    new_node.parent = current_node

                    
                    if add_to_open(open_list, new_node):
                        open_list.append(new_node)

    return []  

def add_to_open(open_list, new_node):
    for node in open_list:
        if new_node.position == node.position and new_node.g >= node.g:
            return False
    return True


grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0],
]

start = (0, 0) 
goal = (4, 4)   

path = a_star(start, goal, grid)
print("Path found:", path)
