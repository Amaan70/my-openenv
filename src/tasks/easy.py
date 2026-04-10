buggy_code = """
def solution(a, b):
    return a - b  # bug: should be addition
"""

test_cases = [
    {"input": (2, 3), "expected_output": 5},
    {"input": (0, 0), "expected_output": 0},
    {"input": (-1, 1), "expected_output": 0},
]