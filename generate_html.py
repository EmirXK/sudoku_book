def generate_sudoku_board_html(board1, board2, board3, board4, page, difficulty):
    # Load the HTML template
    with open("sudoku_template.html", "r") as file:
        html_template = file.read()

    # Load the CSS content
    with open("styles.css", "r") as file:
        css_content = file.read()

    # Generate HTML for each board
    boards_html = []
    for board in [board1, board2, board3, board4]:
        board_html = ""
        for i in range(9):
            board_html += "<tr class=\"inner_tr\">"
            for j in range(9):
                cell_value = board[i][j]
                board_html += f"<td class=\"inner_td\">{cell_value if cell_value != 0 else ''}</td>"
            board_html += "</tr>"
        boards_html.append(board_html)
    
    css_content = "<style>" + css_content + "</style>"

    table_number = (page - 1) * 4 + 1
    table_names = []
    for _ in range(4):
        table_names.append("<h3>Puzzle " + str(table_number) + "</h3>")
        table_number += 1

    header = f"""
    <div class="header-container">
        <div class="header-left">Page: {page}</div>
        <div class="header-right">Difficulty: {difficulty.title()}</div>
    </div>
    """
    
    # Replace placeholders with actual board HTML
    html_content = html_template.format(
        board1=boards_html[0],
        board2=boards_html[1],
        board3=boards_html[2],
        board4=boards_html[3],
        css_content=css_content,
        table_1_name=table_names[0],
        table_2_name=table_names[1],
        table_3_name=table_names[2],
        table_4_name=table_names[3],
        header=header,
        pageinfo="Page " + str(page) + " of " + str(64//4)
    )

    return html_content
