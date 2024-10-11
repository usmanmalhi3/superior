
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5],
    3: [1],
    4: [1],
    5: [2]
}

def bfs_without_queue(graph, start):
    visited = set()  
    bfs_list = []    
    bfs_list.append(start)  
    visited.add(start)
    
    index = 0  
    while index < len(bfs_list):
        current_node = bfs_list[index]
        print(current_node) 
        
      
        for neighbor in graph[current_node]:
            if neighbor not in visited:
                visited.add(neighbor)
                bfs_list.append(neighbor)  
        
        index += 1  


bfs_without_queue(graph, 0)
