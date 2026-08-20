def package_dependency_resolver(packages: dict[str, list[str]]) -> list[str]:
    indegree = {pkg: 0 for pkg in packages}
    dependents = {pkg: [] for pkg in packages}
    for pkg, deps in packages.items():
        for dep in deps:
            if dep in packages:
                indegree[pkg] += 1
                dependents[dep].append(pkg)

    order = []
    ready = sorted(pkg for pkg in packages if indegree[pkg] == 0)
    while ready:
        order.extend(ready)
        next_ready = []
        for pkg in ready:
            for dependent in dependents[pkg]:
                indegree[dependent] -= 1
                if indegree[dependent] == 0:
                    next_ready.append(dependent)
        ready = sorted(next_ready)

    return order if len(order) == len(packages) else []