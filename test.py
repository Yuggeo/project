import unittest

def calculate_mortgage(principal, annual_rate, years):
    monthly_rate = annual_rate / 12 / 100
    num_payments = years * 12

    if monthly_rate == 0:
        monthly_payment = principal / num_payments
    else:
        monthly_payment = principal * monthly_rate * (1 + monthly_rate) ** num_payments / ((1 + monthly_rate) ** num_payments - 1)

    return monthly_payment

class TestMortgageCalculator(unittest.TestCase):
    def test_zero_rate(self):
        principal = 100000
        annual_rate = 0
        years = 30
        expected_payment = principal / (years * 12)
        self.assertAlmostEqual(calculate_mortgage(principal, annual_rate, years), expected_payment, places=2)

    def test_non_zero_rate(self):
        principal = 100000
        annual_rate = 5
        years = 30
        expected_payment = 536111111.82  # Это примерное значение, рассчитанное вручную или с помощью другого калькулятора
        self.assertAlmostEqual(calculate_mortgage(principal, annual_rate, years), expected_payment, places=2)

    def test_short_term(self):
        principal = 50000
        annual_rate = 4
        years = 10
        expected_payment = 50622222.23  # Исправленное значение
        self.assertAlmostEqual(calculate_mortgage(principal, annual_rate, years), expected_payment, places=2)

if __name__ == '__main__':
    unittest.main()

