class Solution(object):
    def maxLength(self, arr):

        def is_unique(s):
            return len(s) == len(set(s))

        def backtrack(index, current, max_length):
            max_length[0] = max(max_length[0], len(current))

            for i in range(index, len(arr)):
                if is_unique(current + arr[i]):
                    backtrack(i + 1, current + arr[i], max_length)

        max_length = [0]
        backtrack(0, "", max_length)
        return max_length[0]
