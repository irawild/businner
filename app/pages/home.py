from fastapi.responses import HTMLResponse
import app.utils.text_reader as text_reader

def get_home_page_html():
    return HTMLResponse(content=text_reader.get_html_content("app/pages/index.html"), status_code=200)
