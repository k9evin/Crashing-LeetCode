class Solution {
    public String longestPalindrome(String s) {
        if (s.length() < 2) {
            return s;
        } 
        
        String result = "";
        
        for (int i = 0; i < s.length(); i++) {
            // 寻找长度为奇数的回文串
            String odd = palindrome(s, i, i);
            // 寻找长度为偶数的回文串
            String even = palindrome(s, i, i + 1);
            // 得到最长的回文串
            result = result.length() > odd.length() ? result : odd;
            result = result.length() > even.length() ? result : even;
        }
        return result;
    }
    
    // 在 s 中寻找以 s[l] 和 s[r] 为中心的最长回文串
    String palindrome(String s, int l, int r) {
        // 防止索引越界
        while (l >= 0 && r < s.length()
                && s.charAt(l) == s.charAt(r)) {
            // 双指针，向两边展开
            l--; r++;
        }
        // 返回以 s[l] 和 s[r] 为中心的最长回文串
        return s.substring(l + 1, r);
    }
}