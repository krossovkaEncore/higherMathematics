def greedy_coins(coins, s):
    count = 0

    for coin in sorted(coins, reverse=True):
        count += s // coin
        s %= coin

    return count


def dp_coins(coins, S):
    INF = float("inf")
    dp = [0] + [INF] * S

    for x in range(1, S + 1):
        for coin in coins:
            if coin <= x:
                dp[x] = min(dp[x], dp[x - coin] + 1)

    return dp


coins = [1, 3, 4]
dp = dp_coins(coins, 20)

for s in range(1, 21):
    greedy = greedy_coins(coins, s)

    if greedy != dp[s]:
        print(s, "Жадный:", greedy, "Оптимальный:", dp[s])
