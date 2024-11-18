import time

# %% Problem 1 a - Sparse Price Rod Cutting Algorithm
def cutRod(price_dict, n):
    INT_MIN = -9999999 # Negative infinity
    val = [0 for x in range(n+1)] # Initialize the array of maximum values
    val[0] = 0 # Base case
    for i in range(1, n+1): # Iterate through all possible rod lengths
        max_val = INT_MIN # Initialize the maximum value for the current rod price
        for length, price in price_dict.items(): # Iterate through all possible prices
            if length <= i: # If the current length is less than or equal to the current rod length
                max_val = max(max_val, price + val[i-length]) # Update the maximum value
        val[i] = max_val if max_val != INT_MIN else 0 # Update the maximum value for the current rod length

    return val # Return the array of maximum values

# %% Test Cases
price_dict = {1: 1, 2: 5, 4: 9, 6: 17, 8: 20, 10: 30, 12: 36, 16: 48}
rod_length = 16
result = cutRod(price_dict, rod_length)
print("Maximum Obtainable Value is " + str(result[rod_length]))
print("The whole array of maximum values is " + str(result))


# %% Visualization for 0-16 Rod Lengths
import matplotlib.pyplot as plt
lengths = list(range(rod_length + 1))
values = result

plt.figure(figsize=(10, 6))
plt.plot(lengths, values, marker='o', linestyle='-', color='b')
plt.title('Maximum Obtainable Values for Different Rod Lengths')
plt.xlabel('Rod Length')
plt.ylabel('Maximum Obtainable Value')
plt.grid(True)
plt.xticks(lengths)
plt.show()
# %% - 1. b - Sparse Price Rod Cutting Algorithm w/ compatibility rod lengths above 16
def cutRodPlus(price_dict, n):
    INT_MIN = -9999999  # Negative infinity
    val = [0 for x in range(n + 1)]  # Initialize the array of maximum values
    val[0] = 0  # Base case

    for i in range(1, n + 1):  # Iterate through all possible rod lengths
        max_val = INT_MIN  # Initialize the maximum value for the current rod price
        for length, price in price_dict.items():  # Iterate through all possible prices
            if length <= i:  # If the current length is less than or equal to the current rod length
                max_val = max(max_val, price + val[i - length])  # Update the maximum value
        val[i] = max_val if max_val != INT_MIN else val[i - 1]  # Handle lengths beyond available prices

    return val  # Return the array of maximum values

# %%
import matplotlib.pyplot as plt
import time

lengths = [4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
values = []
times = []

for n in lengths:
    start_time = time.time()
    result = cutRod(price_dict, n)
    end_time = time.time()
    times.append(end_time - start_time)
    values.append(result[n])

# Plot Execution Time
plt.figure(figsize=(10, 6))
plt.plot(lengths, times, marker='o')
plt.title('Execution Time of cutRod Function')
plt.xlabel('Rod Length')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()

# Output the results in a table
print(f"{'Length':>10} {'Max Value':>15} {'Time (s)':>15}")
for length, value, t in zip(lengths, values, times):
    print(f"{length:>10} {value:>15} {t:>15.6f}")


"""
In the cutRodPlus function, when no valid price can be applied 
(i.e., when max_val remains INT_MIN),
the algorithm now assigns the maximum value for the current 
rod length i to the maximum value from 
the previous length, val[i - 1], instead of setting it to 0.
"""

# %% Problem 2 - Coin Change Problem
def coinChange(amount, coins):
    ways = [0] * (amount+1)
    ways[0] = 1

    for val in coins:
        for i in range(val, amount+1):
            ways[i] += ways[i-val]
        
    return ways[amount]
# %%

def coinChangePlus(amount, coins):
    ways = [0] * (amount + 1)  # Initialize list to store number of ways to make each amount
    combinations = [[] for _ in range(amount + 1)]  # Initialize list to store combinations for each amount
    ways[0] = 1  # Base case: one way to make amount 0
    combinations[0] = [[]]  # Base case: one combination (empty list) for amount 0
        
    for coin in coins:
        for i in range(coin, amount + 1):
            if ways[i - coin] > 0:
                ways[i] += ways[i - coin]  # Update number of ways by adding ways to make (i - coin)
                for prev_comb in combinations[i - coin]:
                    new_comb = prev_comb + [coin]  # Create new combination by adding current coin
                    new_comb.sort()  # Sort to ensure unique combinations
                    if new_comb not in combinations[i]:
                        combinations[i].append(new_comb)  # Add new combination if not already present
        
    return ways[amount], combinations[amount]  # Return number of ways and the combinations
# %%
import time
import matplotlib.pyplot as plt

# Part a: US Currency
coins_us = [1, 5, 10, 25, 50, 100, 200, 500, 1000, 2000]
amounts = [10, 50, 100, 500, 1000, 1500, 2000, 3000, 5000]
times_us = []

for amount in amounts:
    start_time = time.time()
    ways = coinChange(amount, coins_us)
    end_time = time.time()
    times_us.append(end_time - start_time)
    print(f"Amount: {amount}, Ways: {ways}, Time: {end_time - start_time:.6f} seconds")

# Plot Execution Time for US Currency
plt.figure(figsize=(10, 6))
plt.plot(amounts, times_us, marker='o')
plt.title('Execution Time of coinChange Function (US Currency)')
plt.xlabel('Amount')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()

# Part b: Wizard Currency
coins_wizard = [1, 29, 493]
times_wizard = []

for amount in amounts:
    start_time = time.time()
    ways = coinChange(amount, coins_wizard)
    end_time = time.time()
    times_wizard.append(end_time - start_time)
    print(f"Amount: {amount}, Ways: {ways}, Time: {end_time - start_time:.6f} seconds")

# Plot Execution Time for Wizard Currency
plt.figure(figsize=(10, 6))
plt.plot(amounts, times_wizard, marker='o')
plt.title('Execution Time of coinChange Function (Wizard Currency)')
plt.xlabel('Amount')
plt.ylabel('Time (seconds)')
plt.grid(True)
plt.show()
# %% 2. c - Coin Change Problem with Combinations
import matplotlib.pyplot as plt
import time
# Test amounts for both US and Wizard currency
test_amounts = [10, 25, 50, 100]
coins_us = [1, 5, 10, 25, 50, 100, 200, 500, 1000, 2000]
coins_wizard = [1, 29, 493]

# Lists to store timing results
times_us = []
times_wizard = []

# US Currency experiments
print("\nUS Currency Results:")
for amount in test_amounts:
    start_time = time.time()
    ways, combinations = coinChangePlus(amount, coins_us)
    end_time = time.time()
    execution_time = end_time - start_time
    times_us.append(execution_time)
    print(f"Amount: {amount}, Ways: {ways}, Time: {execution_time:.6f} seconds")
    print(f"Combinations: {combinations}\n")

# Wizard Currency experiments
print("\nWizard Currency Results:")
for amount in test_amounts:
    start_time = time.time()
    ways, combinations = coinChangePlus(amount, coins_wizard)
    end_time = time.time()
    execution_time = end_time - start_time
    times_wizard.append(execution_time)
    print(f"Amount: {amount}, Ways: {ways}, Time: {execution_time:.6f} seconds")
    print(f"Combinations: {combinations}\n")

# Plot results
plt.figure(figsize=(10, 6))
plt.plot(test_amounts, times_us, marker='o', label='US Currency')
plt.plot(test_amounts, times_wizard, marker='s', label='Wizard Currency')
plt.title('Execution Time of coinChangePlus Function')
plt.xlabel('Amount')
plt.ylabel('Time (seconds)')
plt.legend()
plt.grid(True)
plt.show()
# %%
