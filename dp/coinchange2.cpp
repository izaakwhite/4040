#include <bits/stdc++.h>

using namespace std;

    int change(int amount, vector<int>& coins) {
        vector<int> dp(amount + 1, 0);
        dp[0] = 0;

        if (amount == 0) return 1;

        for (int coin : coins) {
            for (int currentAmount = coin; currentAmount <= amount; ++currentAmount) {
                if (currentAmount == coin) {
                    dp[currentAmount] += 1;
                } else {
                    dp[currentAmount] += dp[currentAmount - coin];
                }
            }
        }

        return dp[amount];
    }

    int main() {
        int amount = 20;
        vector<int> coins = {1,4,9,16};
        cout << change(amount, coins) << endl;
        return 0;
    }
