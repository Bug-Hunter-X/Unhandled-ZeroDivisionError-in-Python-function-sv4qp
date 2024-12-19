def function_with_error_handling(x):
    try:
        if x == 0:
            return 1 / x
        else:
            return x + 5
    except ZeroDivisionError:
        return float('inf')  # Or another appropriate value or action

result = function_with_error_handling(0)
print(result) 