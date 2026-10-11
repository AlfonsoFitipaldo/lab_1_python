# Lab 01: Cost Estimator

A small Python script that estimates the cost of processing a batch of prompt
records, applies the volume discount tier, and checks the result against a
$1.00 budget.

## How to run

```
python starter/lab.py
```

The script asks for the number of records and the price per thousand records.

## Example output

```
How many records? 4000
Price per thousand records? 0.18

Records:       4000
Base cost:     $0.72
Discount:      10%
Final cost:    $0.65
Within budget: True
```
