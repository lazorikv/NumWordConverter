# Number Word Converter

A Python library for converting numbers to words and vice versa. Supports both integers and decimal numbers.

## Features

- Convert numbers to English words
- Convert English words to numbers
- Support for:
  - Integers
  - Decimal numbers
  - Negative numbers
  - Large numbers (up to trillion)

## Installation

### For Users
```bash
pip install num-word-converter
```

### For Developers
```bash
git clone https://github.com/username/num-word-converter.git
cd num-word-converter
pip install -e ".[dev]"
```

## Usage

### Number to Words
```python
from num_word_converter import num_to_word
# Integer conversion
print(num_to_word(42)) # Output: "forty-two"
# Decimal conversion
print(num_to_word(3.14)) # Output: "three point one four"
# Negative numbers
print(num_to_word(-7)) # Output: "negative seven"
# Large numbers
print(num_to_word(1000000)) # Output: "one million"
```

### Words to Number
```python
from num_word_converter import word_to_num
# Integer words
print(word_to_num("forty-two")) # Output: 42
# Decimal words
print(word_to_num("three point one four")) # Output: 3.14
# Negative numbers
print(word_to_num("negative seven")) # Output: -7
# Large numbers
print(word_to_num("one million")) # Output: 1000000
```

## Error Handling

The library includes several error types for proper error handling:

- `NonNumberInputError`: Input is not a number
- `ComplexNumberInputError`: Input is a complex number
- `FractionTooLongError`: Fractional part is too long
- `ScaleOutOfOrderError`: Scale words are in wrong order
- `NoConversionForWordError`: Word cannot be converted

## Limitations

- Supports numbers up to trillion
- Maximum 10 decimal places for floating point numbers
- English language only


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.