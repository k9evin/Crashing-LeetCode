// Last updated: 1/12/2026, 10:16:06 PM
1class Leaderboard {
2    /**
3     * 整体空间复杂度: O(n) - n 为玩家数量
4     * playerScores 存储 n 个玩家，sortedScores 最多存储 n 个不同分数
5     */
6    
7    // 玩家ID → 当前总分
8    private Map<Integer, Integer> playerScores;
9    
10    // 分数 → 该分数的玩家数量（TreeMap 自动按 key 升序排列）
11    private TreeMap<Integer, Integer> sortedScores;
12
13    /**
14     * 构造函数
15     * 时间复杂度: O(1)
16     * 空间复杂度: O(1)
17     */
18    public Leaderboard() {
19        playerScores = new HashMap<>();
20        sortedScores = new TreeMap<>();
21    }
22
23    /**
24     * 给玩家增加分数
25     * 时间复杂度: O(log n) - TreeMap 的删除和插入操作都是 O(log n)
26     * 空间复杂度: O(1) - 只更新现有数据结构
27     */
28    public void addScore(int playerId, int score) {
29        // 如果玩家已存在，先从 sortedScores 中减少旧分数的计数 - O(log n)
30        if (playerScores.containsKey(playerId)) {
31            removeScore(playerScores.get(playerId));
32        }
33        
34        // 计算新的总分 - O(1)
35        int newScore = playerScores.getOrDefault(playerId, 0) + score;
36        playerScores.put(playerId, newScore);  // 更新玩家分数 - O(1)
37
38        // 在 sortedScores 中增加新分数的计数 - O(log n)
39        sortedScores.put(newScore, sortedScores.getOrDefault(newScore, 0) + 1);
40    }
41
42    /**
43     * 获取前 K 名玩家的总分
44     * 时间复杂度: O(K) - 最多遍历 K 个玩家，实际可能更少（如果多人同分）
45     * 空间复杂度: O(1) - 只使用常数额外空间
46     */
47    public int top(int K) {
48        int sum = 0;      // 累计分数和
49        int count = 0;    // 已统计的玩家数
50
51        // descendingKeySet() 返回降序的分数集合 - O(K) 遍历
52        for (int score : sortedScores.descendingKeySet()) {
53            int times = sortedScores.get(score);  // 该分数有多少个玩家 - O(log n)
54
55            // 计算本轮要取多少个玩家（避免超过 K）
56            int take = Math.min(times, K - count);
57            sum += take * score;  // 累加分数
58            count += take;        // 更新已统计人数
59
60            // 如果已经统计了 K 个玩家，提前退出
61            if (count == K)
62                break;
63        }
64        return sum;
65    }
66
67    /**
68     * 重置玩家分数（从排行榜中移除）
69     * 时间复杂度: O(log n) - TreeMap 的删除操作
70     * 空间复杂度: O(1) - 只删除现有数据
71     */
72    public void reset(int playerId) {
73        int score = playerScores.get(playerId);  // 获取玩家分数 - O(1)
74        removeScore(score);                       // 从 sortedScores 中移除 - O(log n)
75        playerScores.remove(playerId);            // 从 playerScores 中移除 - O(1)
76    }
77
78    /**
79     * 辅助方法：从 sortedScores 中减少某个分数的计数
80     * 时间复杂度: O(log n) - TreeMap 的 put/remove 操作
81     * 
82     * 为什么不能直接 remove？
83     * 因为多个玩家可能有相同分数，只能减少计数，当计数为 0 时才删除该分数键
84     */
85    private void removeScore(int score) {
86        // 将该分数的计数减 1 - O(log n)
87        sortedScores.put(score, sortedScores.get(score) - 1);
88        
89        // 如果计数变为 0，从 TreeMap 中移除该分数键 - O(log n)
90        if (sortedScores.get(score) == 0) {
91            sortedScores.remove(score);
92        }
93    }
94}
95
96/**
97 * 使用示例:
98 * Leaderboard obj = new Leaderboard();
99 * obj.addScore(playerId, score);
100 * int param_2 = obj.top(K);
101 * obj.reset(playerId);
102 */