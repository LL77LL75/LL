import os
with open("reviews.txt", "r") as file:
    content = file.read()
    length = len(content)
    words = content.split()
    good_reviews = 0
    bad_reviews = 0
    for i in words:
        if i == "good":
            good_reviews +=1
        elif i == "bad":
            bad_reviews += 1
    total_reviews = good_reviews + bad_reviews
    good_percent = good_reviews/total_reviews
with open("review_results.txt", "w")as file:
    if good_percent>=.7:
        file.write("Positive")
    elif good_percent>=40:
        file.write("Mixed")
    else:
        file.write("Negative")
