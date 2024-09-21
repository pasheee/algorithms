def naive_realization(sequence):
    sequence_len = len(sequence)
    dp = [1] * sequence_len
    for i in range(1, sequence_len):
        for j in range(i):
            if sequence[j] < sequence[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

