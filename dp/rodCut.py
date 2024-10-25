# %%
INT_MIN = -32767

# Returns the best obtainable price for a rod of length n and
# price[] as prices of different pieces
def cutRod(price, n):
    val = [0 for x in range(n+1)]
    val[0] = 0

    # Build the table val[] in bottom up manner and return
    # the last entry from the table
    for i in range(1, n+1):
        max_val = INT_MIN
        for j in range(i):
             max_val = max(max_val, price[j] + val[i-j-1])
        val[i] = max_val

    return val

# Driver program to test above functions
arr = [2, 3, 4, 6, 9, 15, 16, 19, 24, 25]
size = len(arr)
result = cutRod(arr, size)
print("Maximum Obtainable Value is " + str(result[size]))
print("The whole array of maximum values is " + str(result))

# %%