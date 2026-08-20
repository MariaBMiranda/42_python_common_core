def graph_cycle_detector(graph: dict[int, list[int]]) -> bool:
    visit, done = set(), set()

    def bfs(key):
        visit.add(key)
        for arg in graph.get(key, []):
            if arg in visit:
                return True
            if arg not in done and bfs(arg):
                return True
        visit.discard(key)
        done.add(key)
        return False
    
    return any(key not in done and bfs(key) for key in graph)