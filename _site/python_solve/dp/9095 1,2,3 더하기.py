
if __name__ == "__main__":
    memo = [0] * 12; memo[1] = 1; memo[2] = 2; memo[3] = 4
    t = int(input())
    for i in range(4, 12):
        memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
    for i in range(t):
        print(str(memo[int(input())]))

