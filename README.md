# Color Manipulation

This Python script provides a simple console application for interactively lightening or darkening colors and printing colored text to the terminal.

## Usage

1. **Run the Program:**
   - Execute the script by running `python color_manipulation.py` in your terminal.

2. **Input Color and Percentage:**
   - Enter the color (in hexadecimal format #RRGGBB) and the percentage by which to lighten or darken the color.

3. **Choose Operation:**
   - Select whether to darken or lighten the color.

4. **Exit the Program:**
   - To exit the program, enter `#000000 0` when prompted.

## Functions

### lighten(color: str, percent: int) -> str

Lightens the given color by a specified percentage.

- **Parameters:**
  - `color` (str): The input color in hexadecimal format (#RRGGBB).
  - `percent` (int): The percentage by which to lighten the color.

- **Returns:**
  - str: The new color in hexadecimal format (#RRGGBB) after lightening.

### darken(color: str, percent: int) -> str

Darkens the given color by a specified percentage.

- **Parameters:**
  - `color` (str): The input color in hexadecimal format (#RRGGBB).
  - `percent` (int): The percentage by which to darken the color.

- **Returns:**
  - str: The new color in hexadecimal format (#RRGGBB) after darkening.

### print_colored_text(text: str, color: str) -> None

Prints colored text to the terminal.

- **Parameters:**
  - `text` (str): The text to be printed.
  - `color` (str): The color in hexadecimal format (#RRGGBB) for the text.

- **Returns:**
  - None

### main()

Main function to interactively lighten or darken colors in the terminal.

- **Usage:**
  - To exit the program, input `#000000 0`.
  - Input color and percentage values as prompted to modify text color.
  - Choose between darkening or lightening the text.

- **Returns:**
  - None

## Example

```bash
$ python color_manipulation.py

Чтобы выйти из программы, пропишите - #000000 0
Пример: #112233 100
Введите нужные значения через пробел: #336699 25
Что нужно сделать?
(1) Затемнить текст
(2) Осветлить текст
Ваш выбор: 2
