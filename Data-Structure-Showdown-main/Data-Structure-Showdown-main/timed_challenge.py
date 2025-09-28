# Pick one question from timed_challenge.txt
# Paste the question as a comment below
# Set a timer for 30 minutes and complete the question!

# Question chosen: Symmetric Difference

def symmetric_difference(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    return (set1 - set2) | (set2 - set1)

print(symmetric_difference([3,9,4,6,1], [6,2,8,1,3]))

# 1. What structure you chose and why?
# - I decided to use sets because they are helpful to find unique elemnts in two lists and eliminate the duplicates.

# 2. How the time limit shaped your decision?
# - The time limit didn't really affect my decision, I think that 30 minutes was more than enough time to complete this problem.

# 3. What trade-offs or compromises you made under time pressure?
# - As I really wasn't under time pressure, I didn't have any trade-offs or compromises to make.