def get_html_content(file_name):
    html_content = ""

    with open(file_name) as f:
        for line in f:
            html_content += line

    return html_content
