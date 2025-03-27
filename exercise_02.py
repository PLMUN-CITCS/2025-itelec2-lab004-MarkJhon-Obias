user_integer = int(input("Enter an integer: "))
user_decimal = float(input("Enter a decimal number: "))
user_text = input("Enter a string: ")

print("Formatted Output using old-style formatting:")
print("Integer: %d" % user_integer)
print("Decimal: %.2f" % user_decimal)
print("String: %s" % user_text)

print("Formatted Output using f-strings:")
print(f"Integer: {user_integer}")
print(f"Decimal: {user_decimal:.2f}")  # Format decimal to two places
print(f"String: {user_text}")

exercise_03.py

a = 10
b = 5
c = 3

result1 = a + b * c
print("Result of a + b * c:", result1)

result2 = (a + b) * c
print("Result of (a + b) * c:", result2)

result3 = a - b
print("Result of a - b:", result3)

result4 = a / b
result5 = a // b
print("Result of a / b:", result4)
print("Result of a // b (floor division):", result5)

result6 = a % b
result7 = a ** c
print("Result of a % b (modulus):", result6)
print("Result of a ** c (exponentiation):", result7)

result8 = (a + b - c) * (a / b)
print("Result of (a + b - c) * (a / b):", result8)
