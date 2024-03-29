class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        这道题主要用到思路是：滑动窗口
        什么是滑动窗口？其实就是一个队列,比如例题中的 abcabcbb，进入这个队列（窗口）为 abc 满足题目要求，当再进入 a，队列
    变成了 abca，这时候不满足要求。所以，我们要移动这个队列！
        如何移动？我们只要把队列的左边的元素移出就行了，直到满足题目要求！一直维持这样的队列，找出队列出现最长的长度时候，
    求出解！
        时间复杂度：O(n)
        """
        res = ''
        maxlen = 0
        for ch in s:
            if ch not in res:
                res += ch
            else:
                maxlen = max(maxlen, len(res))
                index = res.index(ch)
                res = res[index + 1:] + ch
        return max(maxlen, len(res))


if __name__ == '__main__':
    solution = Solution()
    # print(solution.lengthOfLongestSubstring('abdcagt'))
    print(solution.lengthOfLongestSubstring('abcabcbb'))
    print(solution.lengthOfLongestSubstring('bbbb'))
    print(solution.lengthOfLongestSubstring('pwwkew'))