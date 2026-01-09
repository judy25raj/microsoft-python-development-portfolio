# Activity 3: Sorting Test Scores with Error Handling

# Step 1: Create the list of students
students = ["John", "Lisa", "Mary", "Chris", "Linda", "Matt"]

# Step 2: Create a dictionary of test scores
test_scores = {
    "John": 88,
    "Lisa": 92,
    "Mary": 76,
    "Chris": 85,
    "Linda": 95,
    "Matt": 79
}

# Step 3: Extract scores from the dictionary
scores = []
for student in students:
    if student in test_scores:
        scores.append(test_scores[student])
    else:
        print(f"Warning: No score found for {student}")

# Step 4: Sorting the scores with a custom function
def bubble_sort(score_list):
    n = len(score_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if score_list[j] > score_list[j + 1]:
                score_list[j], score_list[j + 1] = score_list[j + 1], score_list[j]
    return score_list

# Step 5: Assign the sorted scores
sorted_scores = bubble_sort(scores)
print("Sorted Scores:", sorted_scores)

# Step 6: Calculate highest and lowest scores
highest_score = sorted_scores[-1]
lowest_score = sorted_scores[0]

# Step 7: Define a function to calculate the class average
def average_class_score(students_list, scores_list):
    if not students_list or not scores_list:
        print("Error: Student list or score list is empty.")
        return None
    if len(students_list) != len(scores_list):
        print("Error: The number of students and scores do not match.")
        return None
    total = sum(scores_list)
    avg = total / len(scores_list)
    return avg

# Step 8: Calculate the average score
average_score = average_class_score(students, scores)

# Step 9: Handle empty class case
empty_class = []
empty_scores = []
error_average = average_class_score(empty_class, empty_scores)
if error_average is None:
    print("No average available due to empty data.")
else:
    print(f"Average Score: {error_average}")

# Step 10: Print final results
print(f"Highest Score: {highest_score}")
print(f"Lowest Score: {lowest_score}")
print(f"Average Score: {average_score}")
