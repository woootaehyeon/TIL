def DFS(graph, v, visited):
    visited[v] = True
    print(v, end = ' ')
    for k in graph[v]:
        if not visited[k]:
            DFS(graph, k, visited)

# 정점의 개수(N), 간선의 개수(M), 시작정점 (V)
N,M,V = map(int,input().split())

# 그래프 초기화
graph = [[] for _ in range(N + 1)]

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 그래프의 인접 리스트를 정렬 (문제에서 작은 번호부터 방문하라고 함)
for i in range(1, N + 1):
    graph[i].sort()

print(graph)

# DFS와 BFS를 위한 visited 리스트 초기화
visited_dfs = [False] * (N + 1)

# DFS 호출
DFS(graph, V, visited_dfs)

