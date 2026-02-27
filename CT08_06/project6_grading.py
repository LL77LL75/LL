# Predefined data
answer_key = ["A", "B", "B", "D"]  # Correct answers for the quiz
student_answers = {
    "john": ["A", "C", "B", "D"],
    "jane": ["A", "B", "B", "D"],
    "alice": ["A", "C", "C", "D"],
    "bob": ["A", "B", "B", "D"]
}
avg_lst = []
e = 0.0
for i in student_answers:
    score = 0
    for j in range(len(answer_key)):
        if student_answers[i][j] == answer_key[j]:
            score += 1
            total = len(answer_key)
            percent = (score / total) * 100
            avg_lst.append(percent)
    print(f"{i} scored {percent}% on the quiz.")
for i in avg_lst:
    e += i
total_avg = e / len(avg_lst)
print(e)
print(f"The average score for the quiz is {total_avg}%.") 