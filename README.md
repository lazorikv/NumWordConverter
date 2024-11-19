# num-word-converter

num-word-converter is a Python package that provides functionality to convert numbers to words and words to numbers.

## Features
- Convert integer and float numbers to English words
- Convert English words of numbers back to integer or float
- Error handling for non-numeric and complex inputs

## Usage
```python
from num_word_converter import num_to_word, word_to_num

print(num_to_word(123))
# one hundred and twenty-three

print(word_to_num("one hundred and twenty-three"))
# 123
```

### Running the tests
Tests are run using tox, which also builds a coverage report.

If you haven't installed tox, install it using pip:

```bash
pip install tox
```
Then to run the tests, simply run tox from the project root:

```bash
tox
```

This will run the tests in each environment specified in tox.ini, and generate a coverage report.
Note that tox handles setting up the virtual environments and installing dependencies, so it's not necessary 
to activate a virtual environment or install dependencies manually.