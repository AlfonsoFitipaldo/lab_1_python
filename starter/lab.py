"""Starter for Lab 01: Cost Estimator.

Read the README first, then work through it step by step. Run this file after
every change you make.

Everything you need is from lessons 01 to 03. No functions, no tests, no
extra tools. This is one script, top to bottom.
"""

# Step 2 and 3: replace these two hardcoded values with input(),
# converting the record count with int() and the price with float().
# Records are a whole count, so int(); the price has decimals, so float().
records = int(input("How many records? "))
price_per_thousand = float(input("Price per thousand records? "))

# Step 4: the rate is per THOUSAND records, so divide before you multiply.
base_cost = records / 1000 * price_per_thousand

# Discount tier. Order matters: the chain stops at the first true condition,
# so the largest tier is checked first (20000 would also pass >= 1000).
if records >= 10000:
    discount_rate = 0.20
elif records >= 1000:
    discount_rate = 0.10
else:
    discount_rate = 0.0

final_cost = base_cost * (1 - discount_rate)

# A comparison gives a bool (True / False), not a number.
within_budget = final_cost <= 1.00

# Money uses :.2f so it always shows two decimals; the discount uses :.0%.
print()
print(f"Records:       {records}")
print(f"Base cost:     ${base_cost:.2f}")
print(f"Discount:      {discount_rate:.0%}")
print(f"Final cost:    ${final_cost:.2f}")
print(f"Within budget: {within_budget}")
