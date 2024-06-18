class Poly:
    def __init__(self, coefficients):
        self.coefficients = coefficients

    def add(self, other):
        max_length = max(len(self.coefficients), len(other.coefficients))
        coeffs1 = self.coefficients + (0,) * (max_length - len(self.coefficients))
        coeffs2 = other.coefficients + (0,) * (max_length - len(other.coefficients))
        result_coeffs = tuple(a + b for a, b in zip(coeffs1, coeffs2))
        return Poly(result_coeffs)

    def scalar_multiply(self, scalar):
        result_coeffs = tuple(coef * scalar for coef in self.coefficients)
        return Poly(result_coeffs)

    def multiply(self, poly1, poly2):
        max_length = len(poly1) + len(poly2) - 1
        result_coeffs = [0] * max_length
        for i in range(len(poly1)):
            for j in range(len(poly2)):
                result_coeffs[i + j] += poly1[i] * poly2[j]
        return tuple(result_coeffs)

    def power(self, exponent):
        if exponent < 0:
            raise ValueError("Invalid input")

        result_coeffs = self.coefficients
        for _ in range(exponent - 1):
            result_coeffs = self.multiply(result_coeffs, self.coefficients)
        return Poly(result_coeffs)

    def diff(self):
        result_coeffs = [0] * max(0, len(self.coefficients) - 1)
        for i in range(1, len(self.coefficients)):
            result_coeffs[i - 1] = i * self.coefficients[i]
        return Poly(result_coeffs)

    def integral(self):
        result_coeffs = [0]
        for i in range(len(self.coefficients)):
            result_coeffs.append(self.coefficients[i] / (i + 1))
        return Poly(result_coeffs)

    def eval(self, x):
        result = 0
        for i in range(len(self.coefficients)):
            result += self.coefficients[i] * (x ** i)
        print(f"{result}")

    def print(self):
        terms = []
        for i, coef in enumerate(self.coefficients):
            if coef != 0:
                sign = ""
                if coef < 0:
                    sign += "- "
                elif i > 0:
                    sign += "+ "
                if abs(coef) != 1 or i == 0:
                    sign += str(abs(coef))
                if i > 0:
                    sign += "x"
                if i > 1:
                    sign += f"^{i}"
                terms.append(sign)

        print(" ".join(terms).lstrip("+"))

p = Poly((1, 0, -2))
p2 = Poly((14, 7, -5, 0, 0, 18))
p.print()
q = p.power(2)
q.print()
p.eval(3)
r = p.add(q)
r.print()
r.diff().print()
