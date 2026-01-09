# Activity 2: Using Loops for Repetitive Tasks

def categorize_ratings(rating_list):
    low = medium = high = 0

    for rating in rating_list:
        if 1 <= rating <= 4:
            low += 1
        elif 5 <= rating <= 7:
            medium += 1
        elif 8 <= rating <= 10:
            high += 1

    print(f"Low: {low}")
    print(f"Medium: {medium}")
    print(f"High: {high}")


# Test the function
categorize_ratings([1, 3, 5, 7, 8, 9])
# Expected Output:
# Low: 2
# Medium: 2
# High: 2
