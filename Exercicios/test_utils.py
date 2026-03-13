import unittest
from unittest import mock
from io import StringIO
from contextlib import redirect_stdout
from utils import print_client, print_tabuada, calc_operation

class TestUtils(unittest.TestCase):
    def test_print_client(self):
        cliente = {
            'id': 1,
            'nome': 'João Silva',
            'morada': 'Rua das Flores, 123',
            'tel': '912345678',
            'nif': '123456789',
            'compra': 150.75,
            'divfin': 50.25
        }
        
        expected = (
            "-------------------------------- Cliente 1  --------------------------------\n"
            "Nome: João Silva\n"
            "Morada: Rua das Flores, 123\n"
            "Telefone: 912345678\n"
            "NIF: 123456789\n"
            "Compra: 150.75\n"
            "Divida Final: 50.25\n"
            "-----------------------------------------------------------------------\n"
        )
        
        buf = StringIO()
        with redirect_stdout(buf):
            print_client(cliente)
        
        output = buf.getvalue()
        self.assertEqual(output, expected)

    def test_print_tabuada(self):
        expected = (
            "Tabuada do 5:\n"
            "5 x 1 = 5\n"
            "5 x 2 = 10\n"
            "5 x 3 = 15\n"
            "5 x 4 = 20\n"
            "5 x 5 = 25\n"
            "5 x 6 = 30\n"
            "5 x 7 = 35\n"
            "5 x 8 = 40\n"
            "5 x 9 = 45\n"
            "5 x 10 = 50\n"
        )
        
        buf = StringIO()
        with redirect_stdout(buf):
            print_tabuada(5)
        
        output = buf.getvalue()
        self.assertEqual(output.strip(), expected.strip())

    def test_calc_operation(self):
        with mock.patch('builtins.input', side_effect=['10', '5']):
            result = calc_operation("add")
            self.assertEqual(result, 15)

        with mock.patch('builtins.input', side_effect=['10', '5']):
            result = calc_operation("sub")
            self.assertEqual(result, 5)

        with mock.patch('builtins.input', side_effect=['10', '5']):
            result = calc_operation("mult")
            self.assertEqual(result, 50)

        with mock.patch('builtins.input', side_effect=['10', '5']):
            result = calc_operation("div")
            self.assertEqual(result, 2)

        with mock.patch('builtins.input', side_effect=['10', '0']):
            result = calc_operation("div")
            self.assertEqual(result, "Divisão por zero não é permitida")

if __name__ == '__main__':
    unittest.main()