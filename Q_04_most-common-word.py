## 준영
import collections
import re
from typing import List

class Solution:
    def mostCommonWord(self, paragraph:str, banned : List[str]) ->str:
        words = [word for word in re.sub(r'[^\w]', ' ', paragraph).lower().split() if word not in banned]

        counts = collections.Counter(words)

        return counts.most_common(1)[0][0]

input_data = "bob hit a ball, the hit BALL flew far after it was hit."
# banned = ["hit","ball"]
banned = [""]
solution  = Solution()
ans = solution.mostCommonWord(input_data, banned)
print(ans)