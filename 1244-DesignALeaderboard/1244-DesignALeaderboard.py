# Last updated: 1/12/2026, 9:38:32 PM
1from sortedcontainers import SortedList
2
3class Leaderboard:
4
5    def __init__(self):
6        # 字典：玩家ID → 当前总分
7        self.player_scores = {}
8        
9        # 有序列表：存储所有分数（自动升序排列）
10        self.sorted_scores = SortedList()
11
12    def addScore(self, playerId: int, score: int) -> None:
13        if playerId in self.player_scores: 
14            # 1. 从有序列表中删除旧分数
15            self.sorted_scores.remove(self.player_scores[playerId])
16            
17            # 2. 更新玩家总分
18            self.player_scores[playerId] += score 
19        else: 
20            # 新玩家：直接记录分数
21            self.player_scores[playerId] = score
22        
23        # 3. 将新分数插入有序列表（自动保持排序）
24        self.sorted_scores.add(self.player_scores[playerId])
25
26    def top(self, K: int) -> int:
27        # 取最后 K 个分数（最大的 K 个）并求和
28        return sum(self.sorted_scores[-K:])
29
30    def reset(self, playerId: int) -> None:
31        # 1. 从有序列表中删除该玩家的分数
32        self.sorted_scores.remove(self.player_scores[playerId])
33        
34        # 2. 从字典中删除该玩家
35        self.player_scores.pop(playerId)