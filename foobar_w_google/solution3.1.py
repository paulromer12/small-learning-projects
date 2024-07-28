def solution(M, F):
    target_M = int(M)
    target_F = int(F)
    generation = 0

    while target_M != 1 or target_F != 1:
        if target_M < 1 or target_F < 1:
            # If either target_M or target_F is less than 1, we can't proceed, return "impossible."
            return "impossible"

        if target_M == target_F:
            # If target_M and target_F are equal, we can't proceed, return "impossible."
            return "impossible"

        if target_M > target_F:
            # If target_M is greater than target_F, we check if target_M is a multiple of target_F.
            # If it is, we can't proceed, return "impossible."
            generations_needed = (target_M - 1) // target_F
            if generations_needed == 0:
                return "impossible"
            generation += generations_needed
            target_M -= generations_needed * target_F
        else:
            # If target_F is greater than target_M, we check if target_F is a multiple of target_M.
            # If it is, we can't proceed, return "impossible."
            generations_needed = (target_F - 1) // target_M
            if generations_needed == 0:
                return "impossible"
            generation += generations_needed
            target_F -= generations_needed * target_M

    return str(generation)

# Test cases
print(solution("2", "1"))  # Output: "1"
print(solution("2", "4"))  # Output: "impossible"


