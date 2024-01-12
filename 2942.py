class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans=[]
        for i in range(0,len(words)):
            if x in words[i]:
                ans.append(i)
        return ans

///////
 current implementation looks functional, but there are a few improvements you can make for better readability and efficiency. Here's an updated version with some improvements:

```python
from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        return [i for i, word in enumerate(words) if x in word]
```

Changes made:

1. Used list comprehension for a more concise and readable code.
2. Used `enumerate` to get both the index and the word in each iteration.
3. Removed unnecessary range and indexing.

This updated code achieves the same result but is more Pythonic and easier to understand.
