import sys
input = sys.stdin.readline
print = sys.stdout.write

if __name__ == "__main__":
    x = int(input())
    dp = [0] * 1000001

    for i in range(2, x+1):
        dp[i] = dp[i - 1] + 1;
        if (i % 2 == 0): dp[i] = min(dp[i], dp[i // 2] + 1);
        if (i % 3 == 0): dp[i] = min(dp[i], dp[i // 3] + 1);

    print(str(dp[x]))