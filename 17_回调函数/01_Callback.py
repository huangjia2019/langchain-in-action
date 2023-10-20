def compute(x, y, callback):
    result = x + y
    callback(result)

def print_result(value):
    print(f"The result is: {value}")

def square_result(value):
    print(f"The squared result is: {value**2}")

# 使用print_result作为回调
compute(3, 4, print_result)  # 输出: The result is: 7

# 使用square_result作为回调
compute(3, 4, square_result)  # 输出: The squared result is: 49
