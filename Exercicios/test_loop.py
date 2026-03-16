import unittest
from unittest import mock
from io import StringIO
from contextlib import redirect_stdout

try:
  from Exercicios.exec_loop import *
except ImportError:
  from exec_loop import *

try:
  from Exercicios.test_output_constants import *
except ImportError:
  from test_output_constants import *


class TestLoopExercises(unittest.TestCase):
  def _run_and_capture(self, func, inputs=None):
    buffer = StringIO()
    if inputs is None:
      with redirect_stdout(buffer):
        func()
    else:
      with mock.patch("builtins.input", side_effect=inputs):
        with redirect_stdout(buffer):
          func()
    return buffer.getvalue()

  def test_exec1_prints_even_and_odd_numbers(self):
    output = self._run_and_capture(exec1)
    self.assertIn(HEADER_EVEN_ODD, output)
    self.assertIn("1 e impar", output)
    self.assertIn("2 e par", output)
    self.assertIn("30 e par", output)

  def test_exec2_classifies_ten_input_numbers(self):
    output = self._run_and_capture(exec2, ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
    self.assertIn("1 e impar", output)
    self.assertIn("2 e par", output)
    self.assertIn("10 e par", output)

  def test_exec3_calculates_average_grade(self):
    output = self._run_and_capture(exec3, ["10", "10", "10", "10", "10", "10", "10", "10", "10", "10"])
    self.assertIn("A media das notas e: 10.0", output)

  def test_exec4_reports_prime_number(self):
    output = self._run_and_capture(exec4, ["7"])
    self.assertIn("7 e um numero primo.", output)

  def test_exec4_reports_non_prime_number(self):
    output = self._run_and_capture(exec4, ["8"])
    self.assertIn("8 nao e um numero primo.", output)

  def test_exec5_prints_integer_sequence(self):
    output = self._run_and_capture(exec5)
    self.assertIn(HEADER_INTEGERS, output)
    self.assertIn("1", output)
    self.assertIn("10000", output)

  def test_exec6_prints_first_prime_numbers(self):
    output = self._run_and_capture(exec6)
    self.assertIn("2", output)
    self.assertIn("29", output)

  def test_exec7_prints_tens_series(self):
    output = self._run_and_capture(exec7)
    self.assertIn("10", output)
    self.assertIn("1000", output)

  def test_exec8_prints_both_number_series(self):
    output = self._run_and_capture(exec8)
    self.assertIn(HEADER_SERIES_TENS, output)
    self.assertIn(HEADER_SERIES_FIFTEENS, output)
    self.assertIn("15", output)
    self.assertIn("995", output)

  def test_exec9_accepts_number_between_1_and_100(self):
    output = self._run_and_capture(exec9, ["0", "101", "50"])
    self.assertIn("O numero 50, que inseriu, esta entre 1 e 100.", output)

  def test_exec10_counts_divisors(self):
    output = self._run_and_capture(exec10, ["6"])
    self.assertIn("O numero 6 possui 4 divisores.", output)

  def test_exec11_prints_repeated_digit_pattern(self):
    output = self._run_and_capture(exec11)
    self.assertIn("1", output)
    self.assertIn("22", output)
    self.assertIn("333", output)
    self.assertIn("4444", output)
    self.assertIn("55555", output)

  def test_exec12_prints_aggregated_operations(self):
    output = self._run_and_capture(exec12, ["3"])
    self.assertIn("Soma: 15", output)
    self.assertIn("Subtracao: 3", output)
    self.assertIn("Divisao: 5.5", output)
    self.assertIn("Multiplicacao: 18", output)
    self.assertIn("Total de operacoes efetuadas: 12", output)

  def test_exec13_prints_single_multiplication_table(self):
    output = self._run_and_capture(exec13, ["5"])
    self.assertIn(HEADER_TABLE, output)
    self.assertIn("Tabuada do 5:", output)
    self.assertIn("5 x 1 = 5", output)
    self.assertIn("5 x 10 = 50", output)

  def test_exec14_prints_tables_from_1_to_100(self):
    output = self._run_and_capture(exec14)
    self.assertIn(HEADER_TABLE_1_TO_100, output)
    self.assertIn("Tabuada do 1:", output)
    self.assertIn("Tabuada do 100:", output)

  def test_exec15_prints_ascii_blocks(self):
    output = self._run_and_capture(exec15, ["n"])
    self.assertIn(HEADER_ASCII, output)
    self.assertIn("19:", output)

  def test_exec16_calculates_even_numbers_average(self):
    output = self._run_and_capture(exec16, ["2"] * 30)
    self.assertIn("A media dos numeros pares e: 2.0", output)

  def test_exec17_filters_multiples_of_5_not_3(self):
    output = self._run_and_capture(exec17)
    lines = output.splitlines()
    self.assertIn("5", lines)
    self.assertIn("10", lines)
    self.assertNotIn("15", lines)

  def test_exec18_lists_perfect_numbers_up_to_limit(self):
    output = self._run_and_capture(exec18, ["28"])
    self.assertIn("Numeros perfeitos ate 28: [6, 28]", output)

  def test_exec19_prints_fibonacci_sequence(self):
    output = self._run_and_capture(exec19)
    lines = output.splitlines()
    self.assertIn("1", lines)
    self.assertIn("2", lines)
    self.assertIn("3", lines)

  def test_exec20_prints_number_analysis(self):
    output = self._run_and_capture(exec20, ["10", "n"])
    self.assertIn("10 possui 4 divisores.", output)

  def test_exec21_runs_simple_calculator_flow(self):
    output = self._run_and_capture(exec21, ["1", "2", "3", "6"])
    self.assertIn("Resultado da soma: 5.0", output)
    self.assertIn(EXIT_MESSAGE, output)

  def test_exec22_manages_client_database_flow(self):
    output = self._run_and_capture(
      exec22,
      ["1", "Ana", "Rua A", "123", "111111111",  "100", "2", "3", "1", "4"],
    )
    self.assertIn("Cliente 1", output)
    self.assertIn("Nome: Ana", output)
    self.assertIn(EXIT_MESSAGE, output)

if __name__ == "__main__":
  unittest.main()
