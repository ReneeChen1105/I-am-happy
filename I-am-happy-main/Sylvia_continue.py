#
# Sylvia, 2026/3/4
# Sylvia_continue.py
# Test continue command to skip negative numbers
#

# continue - skip the current iteration
transactions = [200, -50, 450, -30, 1200, 80]

print("Positive transactions only:")
for t in transactions:
    if t < 0:
        continue
    print(f"  ${t:,}")