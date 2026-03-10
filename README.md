# Python Exercises

This repository contains beginner Python exercises focused on conditionals, loops, and utility functions.

## Project Structure

- `Exercicios/exec_if.py`: conditionals exercises.
- `Exercicios/exec_loop.py`: loops exercises (interactive).
- `Exercicios/exec_match.py`: match/case exercises.
- `Exercicios/utils.py`: shared helper functions.
- `Exercicios/test_utils.py`: unit tests for helper functions.

## Requirements

- Python 3.10+ installed.
- Windows PowerShell (commands below are written for PowerShell).

## Run Exercises

From the project root, move into the `Exercicios` folder first:

```powershell
Set-Location Exercicios
```

Run each script with Python:

```powershell
python exec_if.py
python exec_loop.py
python exec_match.py
```

If your machine does not map `python` to Python 3, use one of these alternatives:

```powershell
py exec_if.py
py exec_loop.py
py exec_match.py
```

or (example absolute interpreter path):

```powershell
& C:/Python313/python.exe exec_loop.py
```

## Run Tests

Tests are in `Exercicios/test_utils.py` and import `utils.py` from the same folder.
To avoid import path conflicts, run tests from inside `Exercicios`:

```powershell
Set-Location Exercicios
python -m unittest test_utils.py
```
