# Last updated: 2/5/2026, 6:38:30 PM
class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)           # 数组长度
        res = [0] * n           # 初始化结果数组
        
        # 遍历原数组中的每个元素
        for i, num in enumerate(nums):
            if num > 0:
                # 正数：向右移动num步，使用模运算处理循环
                res[i] = nums[(i + num) % n]
            elif num < 0:
                # 负数：向左移动abs(num)步
                # 先减去绝对值，再加n确保非负，最后取模
                res[i] = nums[(i - abs(num) + n) % n]
            else:
                # 零：直接复制
                res[i] = num
        
        return res

# 时间复杂度：O(n) - 遍历数组一次，每次操作O(1)
# 空间复杂度：O(n) - 需要额外数组存储结果