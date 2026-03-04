#
# Sylvia, 2026/3/4
# Sylvia_for_2.py
# To test for loop with range function
#


# range () generates a sequence of numbers
# range(start, stop, step)  - stop is exclusive
print("Sales Report - Q1 Weeks")
for week in range(1, 13):
    weekly_target = 50_000
    print(f"  Week {week:>2}: Target = ${weekly_target:,}")