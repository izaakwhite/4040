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