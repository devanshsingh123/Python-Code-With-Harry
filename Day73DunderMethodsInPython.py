# ✅ Common Magic Methods (with short examples)
# 1. __init__ – Constructor

# class Dog:
#     def __init__(self, name):
#         self.name = name
# 2. __str__ – Readable string

# def __str__(self):
#     return f"Dog named {self.name}"
# 3. __repr__ – Developer-friendly string

# def __repr__(self):
#     return f"Dog('{self.name}')"
# 4. __len__ – Used by len()

# def __len__(self):
#     return len(self.name)
# 5. __eq__, __lt__, etc. – Comparisons

# def __eq__(self, other):
#     return self.name == other.name
# 6. __add__, __mul__, etc. – Math operators

# def __add__(self, other):
#     return self.name + other.name


class BankAccount:
    def __init__(self, owner: str, balance: float = 0):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return f"BankAccount({self.owner}, ₹{self.balance:.2f})"

    def __repr__(self):
        return f"BankAccount(owner='{self.owner}', balance={self.balance})"

    def __add__(self, other):
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        raise TypeError("Operands must be BankAccount instances")

    def __eq__(self, other):
        return self.balance == other.balance

    def __lt__(self, other):
        return self.balance < other.balance

    def __len__(self):
        return int(self.balance)

    def __call__(self, amount):
        print(f"{self.owner} is depositing ₹{amount}")
        self.balance += amount