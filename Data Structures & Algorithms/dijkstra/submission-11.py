import heapq
class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src: int) -> Dict[int, int]:
        result = {src:0}
        for i in range(n):
            if(src == i):
                continue
            else:
                result[i] = -1
        adj = {}
        for v,u,w in edges:
            if(adj.get(v)):
                old = adj[v]
                old.append([w,u])
                adj[v] = old
            else:
                adj[v] = [list((w,u))]
        min_heap = [(0,src,frozenset())]
        while min_heap:
            x,y,visited = heapq.heappop(min_heap)
            if result[y] == -1 or result[y] >= x:
                result[y] = x
            visited = visited | {y}
            if(result[y] != -1 and result[y] < x and result != 0):
                cost_so_far = result[y]
                continue
            else:
                cost_so_far = x
            if(adj.get(y)):
                for cost, neighbor in adj[y]:
                    if neighbor in visited:
                        continue
                    else:
                        if result[y] == -1 or result.get(y) >= x:
                            result[y] = x
                        heapq.heappush(min_heap, (cost_so_far + cost, neighbor, visited))
        return result

