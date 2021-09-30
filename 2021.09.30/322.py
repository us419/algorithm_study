class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = [-1] * (amount+1)
        cache[0] = 0
        for idx in range(1, amount+1):
            min_val = 1e9
            for coin in coins:
                if idx >= coin and cache[idx-coin] != -1 and cache[idx-coin] < min_val:
                    min_val = cache[idx-coin] + 1
                    
            if min_val != 1e9:
                cache[idx] = min_val
            
        return cache[amount]