# Python3 program to find the 
# longest path in the DAG 
	
# Function to traverse the DAG 
# and apply Dynamic Programming 
# to find the longest path 
def dfs(node, adj, dp, vis): 

	# Mark as visited 
	vis[node] = True
	
	# Traverse for all its children 
	for i in range(0, len(adj[node])): 
	
		# If not visited 
		if not vis[adj[node][i]]: 
			dfs(adj[node][i], adj, dp, vis) 
	
		# Store the max of the paths 
		dp[node] = max(dp[node], 1 + dp[adj[node][i]]) 
	
# Function to add an edge 
def addEdge(adj, u, v): 

	adj[u].append(v) 
	
# Function that returns the longest path 
def findLongestPath(adj, n): 

	# Dp array 
	dp = [0] * (n + 1) 
	
	# Visited array to know if the node 
	# has been visited previously or not 
	vis = [False] * (n + 1) 
	
	# Call DFS for every unvisited vertex 
	for i in range(1, n + 1): 
		if not vis[i]: 
			dfs(i, adj, dp, vis) 
	
	return max(dp)

def calc(N,A):
    adj = [[] for i in range(N + 1)] 
    for i in range(len(A)):
        addEdge(adj,A[i][0],A[i][1])
    return findLongestPath(adj, N)