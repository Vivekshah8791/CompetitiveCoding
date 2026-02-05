t = int(input())

for _ in range(t):
    n = int(input())
    s = list(input())
    
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    
    maximum = s[0]
    for ch in freq:
        if freq[ch] > freq[maximum]:
            maximum = ch
    
    minimum = None
    for ch in freq:
        if ch != maximum:
            if minimum is None or freq[ch] < freq[minimum]:
                minimum = ch
    
    if minimum is not None:
        for i in range(len(s)):
            if s[i] == minimum:
                s[i] = maximum
                break
    
    print("".join(s))
