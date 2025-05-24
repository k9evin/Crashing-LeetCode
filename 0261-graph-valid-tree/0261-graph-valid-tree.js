/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {boolean}
 */
var validTree = function (n, edges) {
    // A valid tree must have exactly n - 1 edges.
    if (edges.length > n - 1) {
        return false;
    }

    const adj = Array.from({ length: n }, () => []);
    for (const [u, v] of edges) {
        adj[u].push(v);
        adj[v].push(u);
    }

    const visited = new Set();
    const dfs = (node, parent) => {
        if (visited.has(node)) {
            return false;
        }
        visited.add(node);
        for (const neighbor of adj[node]) {
            // Undirected graph, skip parent to prevent false positive cycle
            if (neighbor === parent) {
                continue;
            }
            if (!dfs(neighbor, node)) {
                return false;
            }
        }
        return true;
    }

    // Check len(visited) == n to detect loop
    return dfs(0, -1) && visited.size === n;
};