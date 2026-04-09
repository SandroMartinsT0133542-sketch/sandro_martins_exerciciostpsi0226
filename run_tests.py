import sys
import importlib.util
import unittest
from pathlib import Path


def load_tests_by_path() -> unittest.TestSuite:
    suite = unittest.TestSuite()
    loader = unittest.defaultTestLoader

    for index, test_file in enumerate(sorted(Path("Exercicios").rglob("test*.py")), start=1):
        if "-" not in test_file.relative_to("Exercicios").as_posix():
            continue

        module_name = f"dynamic_test_module_{index}"
        spec = importlib.util.spec_from_file_location(module_name, test_file)
        if spec is None or spec.loader is None:
            continue

        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        suite.addTests(loader.loadTestsFromModule(module))

    return suite


def main():
    try:
        suite = unittest.defaultTestLoader.discover(
            start_dir="Exercicios",
            pattern="test*.py",
            top_level_dir=".",
        )
    except Exception:
        suite = unittest.TestSuite()

    suite.addTests(load_tests_by_path())

    result = unittest.TextTestRunner(verbosity=2).run(suite)
    sys.exit(0 if result.wasSuccessful() else 1)


if __name__ == "__main__":
    main()
