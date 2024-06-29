N, k = map(int, input().split())
student = list(map(int, input().split()))
student.sort(reverse=True)
score = []

for i in range(k):
  score.append(student[i])

print(min(score))
