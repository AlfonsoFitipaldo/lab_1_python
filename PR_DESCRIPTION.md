# Lab 01: Cost Estimator

## Approach

The script reads the record count with `int()` and the price per thousand with `float()`, then computes the base cost as `records / 1000 * price_per_thousand`. A single `if` / `elif` / `else` chain picks the discount tier, checking the largest tier first because the chain stops at the first match. The final cost applies that discount, and a `<= 1.00` comparison gives the `bool` used for the budget check.

## Test runs

All runs use a price of 0.18 per thousand records.

| Records | Base cost | Discount | Final cost | Within budget | Notes |
|---|---|---|---|---|---|
| 500 | $0.09 | 0% | $0.09 | True | |
| 999 | $0.18 | 0% | $0.18 | True | edge |
| 1000 | $0.18 | 10% | $0.16 | True | edge |
| 4000 | $0.72 | 10% | $0.65 | True | matches the example run |
| 9999 | $1.80 | 10% | $1.62 | False | edge |
| 10000 | $1.80 | 20% | $1.44 | False | edge |
| 20000 | $3.60 | 20% | $2.88 | False | |
| 0 | $0.00 | 0% | $0.00 | True | no crash |
| 250 | $0.04 | 0% | $0.04 | True | step 4 hand check |

For 250 records the exact cost is 0.045, but it prints `$0.04`: the float stored for 0.045 is actually 0.04499999..., so `:.2f` rounds it down.

## Question for the reviewer

Right now I only format the money with `:.2f` when printing, while the budget check compares the unrounded float. Should I round the final cost (for example with `round(final_cost, 2)`) before comparing it to the budget, so the check always agrees with what is displayed in borderline cases like 0.045?

## AI assistance

This lab was implemented with the assistance of Claude Code (Anthropic). I reviewed the code and can explain every line.
