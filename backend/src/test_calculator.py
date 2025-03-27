import unittest
from src.calculator import Calculator 
from typing import Tuple, List, Callable, Any

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_number_addition(self):
        tests = [
            ([1, 2], 3),
            ([1, -1], 0),
            ([0, 1], 1),
            ([5.5, 10.75], 16.25),
            ([-1, -5.5], -6.5),
            ([-1.5665, 3.5005], 1.934)
        ]

        run_table_test(self, self.calculator.addition, tests)

    def test_addition_error_if_input_is_not_a_number(self):
        tests = [
            (["hello", "string"], TypeError),
            (["hello", 1], TypeError),
            ([1, "hello"], TypeError),
            ([(1, 1), 1], TypeError),
            ([1, (2, 3)], TypeError)
        ]

        run_table_test_raises(self, self.calculator.addition, tests)

    def test_number_multiplication(self):
        tests = [
            ([1, 1], 1),
            ([1, -1], -1),
            ([1, 0], 0),
            ([1.5, 2], 3),
            ([-1.5, -2.257], 3.3855),
            ([-25, -64], 1600)
        ]

        run_table_test(self, self.calculator.multiplication, tests)

    def test_multiplication_error_if_input_is_not_a_number(self):
        tests = [
            (["hello", "string"], TypeError),
            (["hello", 1], TypeError),
            ([1, "hello"], TypeError),
            ([(1, 1), 1], TypeError),
            ([1, (2, 3)], TypeError)
        ]

        run_table_test_raises(self, self.calculator.multiplication, tests)


    def test_number_substraction(self):
        tests = [
            ([1, 1], 0),
            ([1, -1], 2),
            ([1, 0], 1),
            ([20.654, 18.153], 2.501),
            ([-1, -5.5], 4.5),
            ([-1.5665, 3.5005], -5.067)
        ]

        run_table_test(self, self.calculator.subtraction, tests)

    def test_substraction_error_if_input_is_not_a_number(self):
        tests = [
            (["hello", "string"], TypeError),
            (["hello", 1], TypeError),
            ([1, "hello"], TypeError),
            ([(1, 1), 1], TypeError),
            ([1, (2, 3)], TypeError)
        ]

        run_table_test_raises(self, self.calculator.subtraction, tests)

    def test_number_division(self):
        tests = [
            ([1, -1], -1),
            ([5.55, 5], 1.11),
            ([5, 0.5], 10),
            ([1.44, 1.2], 1.2),
        ]

        run_table_test(self, self.calculator.division, tests)

    def test_error_if_division_by_zero(self):
        tests = [
            ([-2231.0034, 0], ZeroDivisionError),
        ]

        run_table_test_raises(self, self.calculator.division, tests)

    def test_division_error_if_input_is_not_a_number(self):
        tests = [
            (["hello", "string"], TypeError),
            (["hello", 1], TypeError),
            ([1, "hello"], TypeError),
            ([(1, 1), 1], TypeError),
            ([1, (2, 3)], TypeError)
        ]

        run_table_test_raises(self, self.calculator.division, tests)


    def test_number_absolute_value(self):
        tests = [
            ([-1], 1),
            ([-0], 0),
            ([1.2313], 1.2313),
            ([100020202], 100020202)
        ]

        run_table_test(self, self.calculator.absolute, tests)

    def test_absolute_value_error_if_input_is_not_a_number(self):
        tests = [
            (["hello"], TypeError),
            ([(1, 2)], TypeError),
            ([[]], TypeError),
        ]

        run_table_test_raises(self, self.calculator.absolute, tests)

    def test_degree(self):
        tests = [
            ([1, 1], 1),
            ([0, 3883], 0),
            ([11, 2], 121),
            ([5.56, 5], 5313.417697178),
            ([-1, 3], -1),
        ]

        run_table_test(self, self.calculator.degree, tests)

    def test_degree_error_if_input_is_not_a_number(self):
        tests = [
            (["hello", "string"], TypeError),
            (["hello", 1], TypeError),
            ([1, "hello"], TypeError),
            ([(1, 1), 1], TypeError),
            ([1, (2, 3)], TypeError)
        ]

        run_table_test_raises(self, self.calculator.degree, tests)

    def test_degree_error_if_base_is_negative_and_degree_is_fractional(self):
        tests = [
            ([-1.3123, 1.23], ValueError),
        ]

        run_table_test_raises(self, self.calculator.degree, tests)

    def test_degree_error_when_zero_to_zero_power(self):
        tests = [
            ([0, 0], ValueError)
        ]

        run_table_test_raises(self, self.calculator.degree, tests)

    def test_degree_error_when_zero_to_negative_power(self):
        tests = [
            ([0, -1], ZeroDivisionError),
        ]

        run_table_test_raises(self, self.calculator.degree, tests)

    def test_natural_log_of_numbers(self):
        tests = [
            ([1], 0),
            ([2], 0.693147181),
            ([200.543], 5.301028688),
            ([401235], 12.90230257),
            ([0.231233], -1.46432919),
        ]

        run_table_test(self, self.calculator.ln, tests)

    def test_natural_log_error_if_input_is_not_a_number(self):
        tests = [
            (["hello"], TypeError),
            ([(1, 2)], TypeError),
            ([[]], TypeError),
        ]

        run_table_test_raises(self, self.calculator.ln, tests)

    def test_natural_log_error_if_input_is_not_a_positive(self):
        tests = [
            ([-1], ValueError),
            ([-858.158], ValueError),
            ([0], ValueError),
        ]

        run_table_test_raises(self, self.calculator.ln, tests)

    def test_log_of_numbers(self):
        tests = [
            ([1, 3], 0),
            ([2.33, 1.55], 1.930082716),
            ([1.334345, 300055], 0.02287083),
            ([2, 0.4], -0.756470797)
        ]

        run_table_test(self, self.calculator.log, tests)

    def test_log_error_if_input_is_not_a_number(self):
        tests = [
            (["hello", "string"], TypeError),
            (["hello", 1], TypeError),
            ([1, "hello"], TypeError),
            ([(1, 1), 1], TypeError),
            ([1, (2, 3)], TypeError)
        ]

        run_table_test_raises(self, self.calculator.log, tests)

    def test_log_error_if_input_is_not_positive(self):
        tests = [
            ([-2, 2], ValueError),
            ([2, -2], ValueError),
            ([2.090132, -12332], ValueError),
            ([-5743.231100, 1102332], ValueError),
            ([-5743.231100, -12332], ValueError),
        ]

        run_table_test_raises(self, self.calculator.log, tests)

    def test_log_error_if_base_is_one(self):
        tests = [
            ([2.00504, 1], ValueError),
        ]

        run_table_test_raises(self, self.calculator.log, tests)

    def test_square_root_of_number(self):
        tests = [
            ([2], 1.414213562),
            ([2.25], 1.5),
            ([12344433212344], 3513464.559710828),
            ([0], 0)
        ]

        run_table_test(self, self.calculator.sqrt, tests)

    def test_square_root_error_if_input_is_not_a_number(self):
        tests = [
            (["hello"], TypeError),
            ([(1, 2)], TypeError),
            ([[]], TypeError),
        ]

        run_table_test_raises(self, self.calculator.sqrt, tests)

    def test_sqrt_error_if_input_is_negative(self):
        tests = [
            ([-1], ValueError),
            ([-1.300], ValueError),
            ([-3348348], ValueError)
        ]

        run_table_test_raises(self, self.calculator.sqrt, tests)

    def test_nth_root_of_numbers(self):
        tests = [
            ([1, 6], 1),
            ([2, 2], 1.414213562),
            ([0.027, 3], 0.3),
            ([128, 7], 2),
            ([12341234, 984.303], 1.0167272108),
        ]

        run_table_test(self, self.calculator.nth_root, tests)

    def test_nth_root_error_if_argument_is_negative_and_degree_is_fraction(self):
        tests = [
            ([-2, 0.2344], ValueError)
        ]

        run_table_test_raises(self, self.calculator.nth_root, tests)

    def test_nth_root_error_when_degree_is_zero(self):
        tests = [
            ([-1, 0], ValueError),
            ([1, 0], ValueError),
            ([0, 0], ValueError),
            ([1.320392, 0], ValueError),
        ]

        run_table_test_raises(self, self.calculator.nth_root, tests)

    def test_nth_root_error_if_base_is_even_and_argument_is_negative(self):
        tests = [
            ([-1, 2], ValueError),
            ([-1.383, 6], ValueError),
        ]

        run_table_test_raises(self, self.calculator.nth_root, tests)

    def test_nth_root_error_if_input_is_not_a_number(self):
        tests = [
            (["hello", "string"], TypeError),
            (["hello", 1], TypeError),
            ([1, "hello"], TypeError),
            ([(1, 1), 1], TypeError),
            ([1, (2, 3)], TypeError)
        ]

        run_table_test_raises(self, self.calculator.nth_root, tests)




def run_table_test(test_class: unittest.TestCase, test_func: Callable, test_cases: List[Tuple[List, Any]], delta=1e-6):
    for (args, expected) in test_cases:
        got = test_func(*args)
        test_class.assertAlmostEqual(got,
                                     expected,
                                     msg=f"failed when called with {args.__str__()}, expected {expected}, got {got}",
                                     delta=delta
                                     )

def run_table_test_raises(test_class: unittest.TestCase, test_func: Callable, test_cases: List[Tuple[List, Any]]):
    for (args, expected) in test_cases:
        with test_class.assertRaises(expected):
            test_func(*args)

if __name__ == "__main__":
    unittest.main()
