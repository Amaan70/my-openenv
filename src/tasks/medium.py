buggy_code = """
def solution(n):
    total = 0
    for i in range(n):  # should be range(1, n+1)
        total += i
    return total
"""

test_cases = [
    {"input": 5, "expected_output": 15},
    {"input": 1, "expected_output": 1},
    {"input": 10, "expected_output": 55},
]