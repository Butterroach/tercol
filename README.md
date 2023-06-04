# **[TerCol](https://pypi.org/project/tercol/)**

TerCol is a small, pure Python library that allows you to color and style text output. TerCol has no dependencies and only requires Python 3.6 or newer. It also supports true color. (i think please tell me if it doesn't)

## Usage

```python
import tercol

print(tercol.red('Red text'))
print(tercol.blue('Blue text'))
print(tercol.rgb(255, 215, 0, 'Gold text using RGB'))
print(tercol.hexa(0xffd700, 'Gold text using HEX'))
print(tercol.hsv(51, 100, 100, 'Gold text using HSV'))
print(tercol.rainbowtext('Rainbow text'))
```

## Requirements

TerCol only requires Python 3.6 or newer. No additional dependencies are needed.

## Pros

- Small size
- Pure Python
- No dependencies
- Simple automatic reset handling
- IDE-autocomplete friendly
- True color support

## Cons

- Limited support of nested styles
- Only supports Python 3.6+

## License

TerCol is licensed under the MIT license.
