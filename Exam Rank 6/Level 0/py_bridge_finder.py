def bridge_finder(graph: dict[int, list[int]]) -> list[tuple[int, int]]:
    disc = {}          # discovery time de cada no
    low = {}           # menor discovery alcancavel via <=1 back edge
    bridges = []
    timer = [0]        # contador em lista para mutar dentro do dfs

    def dfs(u: int, parent: int) -> None:
        disc[u] = low[u] = timer[0]
        timer[0] += 1
        for v in graph.get(u, []):
            if v not in disc:                 # tree edge
                dfs(v, u)
                low[u] = min(low[u], low[v])
                if low[v] > disc[u]:          # nada em v alcanca u ou acima
                    bridges.append((min(u, v), max(u, v)))
            elif v != parent:                 # back edge
                low[u] = min(low[u], disc[v])

    for node in graph:                        # cobre grafos desconexos
        if node not in disc:
            dfs(node, None)

    return sorted(bridges)