# Activity 1: Making Decisions with Conditional Statements

# Task 1: Define a Discount Function
def send_discount(books_purchased, discount_threshold):
    if books_purchased >= discount_threshold:
        print("Discount applied!")
    else:
        print("No discount.")

# Test cases
send_discount(3, 5)  # Output: No discount.
send_discount(7, 5)  # Output: Discount applied!


# Task 2: Add Logical Branching for Multiple Discount Levels
def send_discount(books_purchased, discount_threshold, bonus_threshold):
    if books_purchased >= bonus_threshold:
        print("Big discount applied!")
    elif books_purchased >= discount_threshold:
        print("Discount applied!")
    else:
        print("No discount.")

# Test cases
send_discount(3, 5, 10)   # Output: No discount.
send_discount(7, 5, 10)   # Output: Discount applied!
send_discount(12, 5, 10)  # Output: Big discount applied!
