word = input().upper()
word_list = list(set(word))

result = []

for i in word_list:
  result.append(word.count(i))
if result.count(max(result)) > 1:
  print("?")

else:
  print(word_list[result.index(max(result))])


# 참고 : https://velog.io/@goplanit/Algorithm-%EB%B0%B1%EC%A4%80-1157%EB%B2%88-%EB%8B%A8%EC%96%B4-%EA%B3%B5%EB%B6%80%ED%8C%8C%EC%9D%B4%EC%8D%AC