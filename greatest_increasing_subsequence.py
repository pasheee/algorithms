def naive_realization(sequence):
    sequence_len = len(sequence)
    dp = [1] * sequence_len
    for i in range(1, sequence_len):
        for j in range(i):
            if sequence[j] < sequence[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)




def lbs(mass, elem):
    l = -1
    r = len(mass)-1
    while l+1 < r:
        median = (r+l)//2
        if mass[median] < elem:
            l = median
        else:
            r = median

    return r

def fast_realization(sequence):
    n = len(sequence)
    result_length = 0
    dp = [float('inf')] * (n+1)
    dp[0] = -float('inf')

    for i in range(n):
        j = lbs(dp, sequence[i])
        print(j)
        print(dp)
        if dp[j-1] < sequence[i] and sequence[i] < dp[j]:
            dp[j] = sequence[i]
            result_length = max(result_length, j)
    print(dp)
    return result_length
