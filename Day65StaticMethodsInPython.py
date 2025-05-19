class MathOperations:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def multiply(a, b):
        return a * b

# Using static methods without creating an instance of the class
result_add = MathOperations.add(5, 3)
result_multiply = MathOperations.multiply(4, 6)

print(f"Addition: {result_add}")
print(f"Multiplication: {result_multiply}")