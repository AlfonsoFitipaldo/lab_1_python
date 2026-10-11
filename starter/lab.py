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

# Step 5: replace this with an if / elif / else chain that sets the rate to
# 0.0, 0.10, or 0.20 depending on how many records there are.
discount_rate = 0.0

final_cost = base_cost - (base_cost * discount_rate)

# Step 7: compare the final cost against the budget.
is_within_budget = final_cost <= 1.00

# Step 6: these already use :.2f so the money always shows two decimals.
print(f"Records:       {records}")
print(f"Base cost:     ${base_cost:.2f}")
print(f"Discount:      {discount_rate:.0%}")
print(f"Final cost:    ${final_cost:.2f}")
print(f"Within budget: {is_within_budget}")
