# NumWordConverter

NumWordConverter is a Python package that provides functionality to convert numbers to words and words to numbers.

## Features
- Convert integer and float numbers to English words
- Convert English words of numbers back to integer or float
- Error handling for non-numeric and complex inputs

## Usage
```python
from NumWordConverter import num_to_word, word_to_num

print(num_to_word(123))
# one hundred and twenty-three

print(word_to_num("one hundred and twenty-three"))
# 123
```

### Running the tests
To run the tests, navigate to the test directory and run the test file using a 
test runner such as unittest or pytest:

```bash
python -m unittest discover -s tests
```