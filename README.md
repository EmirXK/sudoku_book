# Sudoku Book Generator

This project generates a custom Sudoku book in PDF format. The generator creates Sudoku puzzles of varying difficulty levels, compiles them into a book, and provides the solutions in a separate section. It uses HTML and CSS for layout, and Python scripts handle puzzle generation and PDF conversion.

## Features

- **Multiple Difficulty Levels**: Generates puzzles ranging from easy to expert.
- **PDF Output**: Compiles puzzles into a formatted PDF.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/EmirXK/sudoku_book.git
    cd sudoku_book
    ```
2. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
3. (Optional) Ensure `wkhtmltopdf` is installed and added to your system path.

## Usage

1. Generate puzzles and create the Sudoku book:
    ```bash
    python book_creator.py
    ```
2. The resulting PDF will be saved in the `puzzles/output` directory.
3. You can find the solutions at the `solutions/output` directory.

## Contributing

Feel free to submit issues or pull requests if you'd like to contribute to the project.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.
