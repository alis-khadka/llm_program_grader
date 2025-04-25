def calc(N, B):
    A = {i:[] for i in range(N)}
    
    for edge in B:
        A[edge[0]-1].append(edge[1]-1)
    
    longest_path = [-1] * N #longest_path starting at i+1
    
    for current in range(N):
        calc_path(N, A, longest_path, current)
    return max(longest_path) - 1
    
    

def calc_path(N, A, longest_path, current):
    if longest_path[current] != -1:
        return
    current_max = 0
    for v_next in A[current]:
        #v_next is any vertex that can be reached with 1 edge by current
        
        calc_path(N, A, longest_path, v_next)
        current_max = max(current_max, longest_path[v_next])
    longest_path[current] = current_max + 1