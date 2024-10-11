def minimax(depth, node_index, maximizing_player, values, alpha, beta):
   
    if depth == 0 or node_index >= len(values):
        return values[node_index]

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(2):  
            eval = minimax(depth - 1, node_index * 2 + i + 1, False, values, alpha, beta)
            max_eval = max(max_eval, eval)
            alpha = max(alpha, eval)
            if beta <= alpha:
                break 
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(2):  
            eval = minimax(depth - 1, node_index * 2 + i + 1, True, values, alpha, beta)
            min_eval = min(min_eval, eval)
            beta = min(beta, eval)
            if beta <= alpha:
                break  
        return min_eval


values = [3, 5, 2, 9, 12, 5, 23, 15] 
depth = 3  
optimal_value = minimax(depth, 0, True, values, float('-inf'), float('inf'))

print("Optimal value:", optimal_value)
