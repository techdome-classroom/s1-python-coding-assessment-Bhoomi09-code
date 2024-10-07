def decode_message( s: str, p: str) -> bool:

# write your code here
  
       def is_match(message, pattern):
    m, n = len(message), len(pattern)
    
    # DP table with size (m+1) x (n+1)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    # Empty pattern matches empty message
    dp[0][0] = True
 
    # Fill the DP table
    for i in range(1, n + 1):
        if pattern[i - 1] == '*':
            dp[i][0] = dp[i - 1][0]  # '*' can match empty sequence
 
    # Iterate over the pattern and message
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if pattern[i - 1] == message[j - 1] or pattern[i - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]  # Exact match or '?' matches one character
            elif pattern[i - 1] == '*':
                # '*' can either match nothing (dp[i-1][j]) or match one or more characters (dp[i][j-1])
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
 
    # The result is whether the entire pattern matches the entire message
    return dp[n][m]
