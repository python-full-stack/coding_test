## 준영
def reoderLogFiles(logs):
    letters, digits = [],[]
    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    # 2개의 키를 람다 표현식으로 정렬
    letters.sort(key = lambda x : (x.split()[1:], x.split()[0]))
    return letters + digits


input_data = ["dig1 8 151", "let1 art can","dig2 3 6 ","let2 own kit dig","let3 art zero"]
ans = reoderLogFiles(input_data)
print(ans)