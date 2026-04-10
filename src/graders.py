import subprocess
import tempfile

def grade_code(submitted_code: str, test_cases: list) -> float:
    """
    test_cases: list of dicts with "input" and "expected_output"
    Returns score 0.0 to 1.0 based on fraction of tests passed.
    """
    # Wrap submitted code in a function that we can call
    # We'll assume the code defines a function `solution(*args)`.
    # For simplicity, we'll just exec and then call solution with test inputs.
    try:
        namespace = {}
        exec(submitted_code, namespace)
        if "solution" not in namespace:
            return 0.0
        solution = namespace["solution"]
    except Exception:
        return 0.0

    passed = 0
    for case in test_cases:
        try:
            inp = case["input"]
            expected = case["expected_output"]
            # If input is a tuple/list, unpack; else single argument
            if isinstance(inp, (list, tuple)):
                result = solution(*inp)
            else:
                result = solution(inp)
            if result == expected:
                passed += 1
        except Exception:
            continue
    return passed / len(test_cases) if test_cases else 1.0