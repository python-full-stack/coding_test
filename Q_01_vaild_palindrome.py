# 준영
import re
def isPalindrome(s):
    s = s.lower()

    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]

input_data = " A man, a plan, a canal : Panama"

result = isPalindrome(input_data)
print(result)
# 영보 - start!

# 승범
def isPalindrome(input) :
    strList = []
    for i in input:
        if i.isalnum() :
            strList.append(i.lower())
    if strList != strList[::-1] :
            return False
    return True

input = "A man, a plan, a canal: Panama"

print(isPalindrome(input))
