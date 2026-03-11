#
# Sylvia, 2026/3/11
# Sylvia_W3.py
# Practice Lists
#

sales_regions = ["North", "South", "East", "West", "Central"]

print("First region:", sales_regions[0])
print("Last region:", sales_regions[-1])

# print West, Central
print("Region 3-5:", sales_regions[3:5])


# Sorting lists
scores = [88, 72, 95, 61, 84, 99, 77]
scores_sorted = sorted(scores, reverse=True)
print("Ranked scores:", scores_sorted)

# Sorting list (False)
cores = [88, 72, 95, 61, 84, 99, 77]
scores_sorted = sorted(scores, reverse=False)
print("Ranked scores:", scores_sorted)


# A list of dictionaries — mimics a simple database table
customers = [
    {"name": "Apex Corp",    "region": "East",  "purchases": 34_000},
    {"name": "BlueSky LLC",  "region": "West",  "purchases": 87_500},
    {"name": "CoreTech",     "region": "East",  "purchases": 12_200},
    {"name": "Delta Group",  "region": "West",  "purchases": 56_000},
    {"name": "Edge Systems", "region": "East",  "purchases": 29_800},
]

# 3. Add customer
customers

# Filter: Sales department only
east_customers = [e for e in customers if e["region"] == "East"]
# avg_sales_salary = sum(e["salary"] for e in sales_team) / len(sales_team)

# Calculate and print the total purchases for West region.
west_customers = [e for e in customers if e["region"] == "West"]
total_purchases = sum(e["purchases"] for e in west_customers)

print(f"Total purchases for West region: ${total_purchases}")

#for c in east_customers:
    #print(f"East customers: {c["name"]} ${c["purchases"]:,.2f}")




