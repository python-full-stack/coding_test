# 준영
import re
def isPalindrome(s):
    s = s.lower()

    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]

input_data = " A man, a plan, a canal : Panama"

result = isPalindrome(input_data)
print(result)
# 영보 - start

# 승범

print("git push test")
