import sys
sys.setrecursionlimit(10 ** 6)

def dfs(graph, v, visited):
    global cnt
    visited[v] = cnt
    # print(v)
    for i in graph[v]:
        if visited[i] == 0:
            cnt += 1
            dfs(graph, i, visited)

n,m,r = map(int,sys.stdin.readline().split())
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)
cnt = 1

for i in range(m):
    a, b = map(int,sys.stdin.readline().split())
    graph[a].append(b)  
    graph[b].append(a)
    
for edge in graph:
    edge.sort(reverse=True)
    
dfs(graph, r, visited)
# print(d)
for i in range(1, n+1):
    print(visited[i])
# print(visited)