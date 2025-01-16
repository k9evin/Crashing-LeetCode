class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Uses BFS to find the shortest transformation sequence from `beginWord` to `endWord`.

        Algorithm:
        - Create a graph using word patterns where each pattern is formed by replacing one
          character with '*'. For example, "hot" -> "*ot", "h*t", "ho*".
        - Perform BFS starting from `beginWord`. For each word, explore its neighbors (words
          that match the current pattern).
        - Keep track of visited words to avoid cycles and redundant processing.
        - Return the level of BFS when `endWord` is found. If `endWord` is not reachable,
          return 0.

        Time Complexity:
        - O(M^2 * N), where N is the number of words in the wordList, and M is the average
          length of the words.
          - Building the adjacency list takes O(M^2 * N) since for each of N words, we generate M patterns
            (O(M)), and each pattern may need O(M) comparisons.
          - BFS traverses all nodes and edges, which is also O(M^2 * N).

        Space Complexity:
        - O(M^2 * N) for the adjacency list and queue storage.
        """
        if endWord not in wordList:
            return 0  # If the endWord is not in the wordList, transformation is impossible.

        # Add beginWord to the wordList and create an adjacency list of patterns.
        wordList.append(beginWord)
        adj_list = defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                pattern = (
                    word[:i] + "*" + word[i + 1:]
                )  # Create a pattern for the word.
                adj_list[pattern].append(word)

        # BFS setup
        visited = set([beginWord])  # Keep track of visited words.
        q = deque([beginWord])  # Queue for BFS.
        res = 1  # Initialize transformation length.

        while q:
            n = len(q)
            for i in range(n):
                word = q.popleft()  # Process the current word.
                if word == endWord:  # If we reach the endWord, return the level of BFS.
                    return res
                # Check all patterns for the current word.
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j + 1:]
                    for neighbor_word in adj_list[pattern]:
                        if neighbor_word not in visited:
                            q.append(neighbor_word)  # Add the neighbor to the queue.
                            visited.add(neighbor_word)  # Mark it as visited.
            res += 1  # Increment the level of BFS.

        return 0  # If BFS completes without finding endWord, return 0.
