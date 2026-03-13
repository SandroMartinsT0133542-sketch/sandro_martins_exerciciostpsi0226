import unittest
from unittest import mock
from io import StringIO
from contextlib import redirect_stdout

try:
  from Exercicios.exec_loop import exec1, exec13
except ImportError:
  from exec_loop import exec1, exec13

class TestLoop(unittest.TestCase):
  
  def test_exec1(self):
    buffer = StringIO()
    with redirect_stdout(buffer):
      exec1()

    output = buffer.getvalue()
    self.assertIn("-------------------------------- Numeros pares e impares --------------------------------", output)
    self.assertIn("1 e impar", output)
    self.assertIn("30 e par", output)

  def test_exec2(self):
    buffer = StringIO()
    with mock.patch("builtins.input", side_effect=["5"]):
      with redirect_stdout(buffer):
        exec13()

    output = buffer.getvalue()
    self.assertIn("-------------------------------- Tabuada --------------------------------", output)
    self.assertIn("Tabuada do 5:", output)
    self.assertIn("5 x 1 = 5", output)
    self.assertIn("5 x 10 = 50", output)

    
if __name__ == "__main__":
  unittest.main()
