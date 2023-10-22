"""
Alex Chaban
Prof. Ionut Cardei
COP4045
Midterm Question 6
"""

sales_data = [('iPhone X', 10, 1000, 950), ('Samsung Galaxy X', 25, 970, 850), ('Google Pixel 2', 7, 650, 600)]

"""
Part A: Profit calculation
Algorithm:
loop through the list, take the elements and calculate profit
append to sales_prod as a tuple of (name, profit)
"""

sales_prod = []

for i in sales_data:
    profit = i[1] * (i[2] - i[3])
    sales_prod.append((i[0], profit))

print(f'Part A: {sales_prod}')

"""
Part B: Total Profit calculation
Requirements: MUST USE sum() + list comprehension
Algorithm:
specifically target the profit calculator, should probably do in one line
"""

total_profit = sum(i[1] * ((i[2] - i[3])) for i in sales_data)

print(f'Part B: {total_profit}')