class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        graph = [[] for i in range(n)]
        
        for u, v, w in edges:
            graph[u].append((v, w))

        dist = [float("inf")] * n
        dist[src] = 0
        visited = [False] * n

        for i in range(n):
            u = -1
            for x in range(n):
                if not visited[x]:
                    if u == -1 or dist[x] < dist[u]:
                        u = x

            if u == -1 or dist[u] == float("inf"):
                break
            visited[u] = True
            for v, weight in graph[u]:
                newDist = dist[u] + weight
                if newDist < dist[v]:
                    dist[v] = newDist

        output_dict = {}
        for i in range(n):
            if dist[i] == float("inf"):
                output_dict[i] = -1
            else:
                output_dict[i] = dist[i]

        return output_dict