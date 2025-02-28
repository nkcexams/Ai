def alphabeta(depth, nodeIndex, isMax, values, alpha, beta):
    if depth == 0:
        return values[nodeIndex]

    best = float('-inf') if isMax else float('inf')
    for i in range(2):  # Loop through child nodes
        val = alphabeta(depth - 1, nodeIndex * 2 + i, not isMax, values, alpha, beta)
        best = max(best, val) if isMax else min(best, val)
        if isMax:
            alpha = max(alpha, best)
        else:
            beta = min(beta, best)
        if beta <= alpha:
            break 
    return best
# Example usage
values = [3, 4, 7, 8, 1, 2, 0, -1]
print("The optimal value is:", alphabeta(3, 0, True, values, float('-inf'), float('inf')))

'''
from math import inf

def mm(st, d, mx):
    if d == 0 or term(st): return eval(st)
    fn = max if mx else min
    return fn(mm(mv(st, a), d-1, not mx) for a in acts(st))

def term(st): return not st  
def eval(st): return sum(st)  
def acts(st): return [st[:-1], st[1:]]  
def mv(st, a): return a  

gs = [3, 5, 2, 9]  
print("Best:", mm(gs, 3, 1))
'''
