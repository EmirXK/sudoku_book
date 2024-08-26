import pdfkit
from generate_html import generate_sudoku_board_html
from puzzle_generation import generate_human_solvable_puzzle
import os

def generate_and_save_sudoku_pdf(board1, board2, board3, board4, page, difficulty, directory, filename):
    # Ensure the directory exists
    if not os.path.exists(directory):
        os.makedirs(directory)
    
    # Generate HTML content for the Sudoku board
    html_content = generate_sudoku_board_html(board1, board2, board3, board4, page, difficulty)
    
    # Define path to wkhtmltopdf
    path_wkhtmltopdf = 'wkhtmltopdf.exe'
    
    # Configure pdfkit
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)
    
    # Convert the HTML to a PDF
    pdf_file_path = os.path.join(directory, filename)
    pdfkit.from_string(html_content, pdf_file_path, configuration=config)
    
    #print(f"Sudoku puzzle saved as {pdf_file_path}")



def generate_page(page_num, difficulty):
    # Board data
    board1, solution1 = generate_human_solvable_puzzle(difficulty)
    board2, solution2 = generate_human_solvable_puzzle(difficulty)
    board3, solution3 = generate_human_solvable_puzzle(difficulty)
    board4, solution4 = generate_human_solvable_puzzle(difficulty)

    # Define directories
    puzzle_directory = 'puzzles'
    solution_directory = 'solutions'

    # Generate and save the Sudoku puzzle PDF
    puzzle_file_name = f"puzzle_page{page_num}.pdf"
    generate_and_save_sudoku_pdf(board1, board2, board3, board4, page_num, difficulty, puzzle_directory, puzzle_file_name)

    # Generate and save the solution page PDF
    solution_file_name = f"solution_page{page_num}.pdf"
    generate_and_save_sudoku_pdf(solution1, solution2, solution3, solution4, page_num, difficulty, solution_directory, solution_file_name)
