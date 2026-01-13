// Last updated: 1/12/2026, 10:13:59 PM
1class Leaderboard {
2    private Map<Integer, Integer> playerScores;
3    private TreeMap<Integer, Integer> sortedScores;
4
5    public Leaderboard() {
6        playerScores = new HashMap<>();
7        sortedScores = new TreeMap<>();
8    }
9
10    public void addScore(int playerId, int score) {
11        if (playerScores.containsKey(playerId)) {
12            removeScore(playerScores.get(playerId));
13        }
14        int newScore = playerScores.getOrDefault(playerId, 0) + score;
15        playerScores.put(playerId, newScore);
16
17        sortedScores.put(newScore, sortedScores.getOrDefault(newScore, 0) + 1);
18    }
19
20    public int top(int K) {
21        int sum = 0;
22        int count = 0;
23
24        for (int score : sortedScores.descendingKeySet()) {
25            int times = sortedScores.get(score);
26
27            int take = Math.min(times, K - count);
28            sum += take * score;
29            count += take;
30
31            if (count == K)
32                break;
33        }
34        return sum;
35    }
36
37    public void reset(int playerId) {
38        int score = playerScores.get(playerId);
39        removeScore(score);
40        playerScores.remove(playerId);
41    }
42
43    private void removeScore(int score) {
44        sortedScores.put(score, sortedScores.get(score) - 1);
45        if (sortedScores.get(score) == 0) {
46            sortedScores.remove(score);
47        }
48    }
49}
50
51/**
52 * Your Leaderboard object will be instantiated and called as such:
53 * Leaderboard obj = new Leaderboard();
54 * obj.addScore(playerId,score);
55 * int param_2 = obj.top(K);
56 * obj.reset(playerId);
57 */