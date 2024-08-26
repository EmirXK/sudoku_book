from page_creator import generate_page
import os
from PyPDF2 import PdfMerger
import re
from tqdm import tqdm

def generate_separate_pages():
    difficulties = ['easy'] * 4 + ['medium'] * 4 + ['hard'] * 4 + ['expert'] * 4
    for i in tqdm(range(1, 17), desc="Generating Sudoku Pages", unit="page"):
        difficulty = difficulties[i - 1]
        generate_page(page_num=i, difficulty=difficulty)


def extract_number(filename):
    match = re.search(r'\d+', filename)
    if match:
        return int(match.group())
    else:
        raise ValueError("No number found in the filename.")
    

def sort_properly(my_files):
    for i in range(len(my_files)-1):
        smallest = i
        for j in range(i, len(my_files)):
            if extract_number(my_files[j]) < extract_number(my_files[smallest]):
                smallest = j
        my_files[smallest], my_files[i] = my_files[i], my_files[smallest]

    return my_files


def merge_pdfs(directory_path, output_filename):
    # Create the output directory if it doesn't exist
    output_dir = os.path.join(directory_path, 'output')
    os.makedirs(output_dir, exist_ok=True)

    # Create a PdfMerger object
    merger = PdfMerger()

    # List all files in the directory
    files = [f for f in os.listdir(directory_path) if f.endswith('.pdf')]
    files = sort_properly(files)

    for pdf_file in files:
        pdf_path = os.path.join(directory_path, pdf_file)

        # Append each PDF to the merger
        merger.append(pdf_path)

    # Define the output path
    output_path = os.path.join(output_dir, output_filename)

    # Write out the merged PDF
    with open(output_path, 'wb') as output_file:
        merger.write(output_file)

    print(f'Merged {len(files)} PDF files into {output_path}')


# generate the pages
generate_separate_pages()


# merge the pages into a pdf
puzzles_directory_path = './puzzles'  # Replace with your directory path
puzzles_output_path = 'puzzles_book.pdf'  # Replace with your desired output file path
merge_pdfs(puzzles_directory_path, puzzles_output_path)


# merge the solutions into a pdf
solutions_directory_path = './solutions'  # Replace with your directory path
solutions_output_path = 'solutions_book.pdf'  # Replace with your desired output file path
merge_pdfs(solutions_directory_path, solutions_output_path)
