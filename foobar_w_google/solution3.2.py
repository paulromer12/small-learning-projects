def solution(l):
    n = len(l)
    count = 0

    # Count the number of multiples for each element on the right
    multiples_count = [0] * n
    for i in range(n - 1):
        for j in range(i + 1, n):
            if l[j] % l[i] == 0:
                multiples_count[i] += 1

    # Accumulate the count of lucky triples
    for i in range(n - 2):
        for j in range(i + 1, n - 1):
            if l[j] % l[i] == 0:
                count += multiples_count[j]

    return count

# Test example
l = [1, 1, 1]
print(solution(l))  # Output: 3
