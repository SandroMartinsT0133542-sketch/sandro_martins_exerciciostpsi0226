import sys
import unittest


def main():
    suite = unittest.defaultTestLoader.discover(
        start_dir="Exercicios",
        pattern="test*.py",
        top_level_dir=".",
    )
    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)


if __name__ == "__main__":
    main()
