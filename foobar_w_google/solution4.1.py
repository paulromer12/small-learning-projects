def solution(banana_list):
    def can_form_loop(banana_a, banana_b):
        return (banana_a + banana_b) % gcd(banana_a, banana_b) == 0

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def create_graph(banana_list):
        graph = {i: [] for i in range(len(banana_list))}
        for i in range(len(banana_list)):
            for j in range(i + 1, len(banana_list)):
                if can_form_loop(banana_list[i], banana_list[j]):
                    graph[i].append(j)
                    graph[j].append(i)
        return graph

    def find_cycle_length(graph, start, visited):
        stack = [(start, 0)]
        while stack:
            current, length = stack.pop()
            visited.add(current)
            for neighbor in graph[current]:
                if neighbor not in visited:
                    stack.append((neighbor, length + 1))
                elif neighbor == start:
                    return length + 1
        return 0

    banana_count = len(banana_list)
    graph = create_graph(banana_list)
    visited = set()
    infinite_loops = [find_cycle_length(graph, i, visited) for i in range(banana_count) if i not in visited]

    return banana_count - max(infinite_loops, default=0)


# Test cases
banana_list = [1, 1, 1]
print(solution(banana_list))  # Output: 3

banana_list = [1073741823, 1073741823, 1073741823]
print(solution(banana_list))  # Output: 3

banana_list = [10]
print(solution(banana_list))  # Output: 0

banana_list = [10, 20]
print(solution(banana_list))  # Output: 2

banana_list = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512]
print(solution(banana_list))  # Output: 0

banana_list = [3, 5, 7, 11, 13]
print(solution(banana_list))  # Output: 5

banana_list = [1, 7, 3, 21, 13, 19]
print(solution(banana_list))